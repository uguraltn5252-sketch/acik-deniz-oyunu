"""Reproducible v2.7 observation adapter over the hash-verified historical engine.

This is a heuristic stress model, not an implementation of every card timing or
human conversation. Unchanged approximations are listed in editorial_report.md.
The locked ZIP is read, verified and extracted only into a temporary directory.
"""
from pathlib import Path
import hashlib
import importlib
import importlib.util
import inspect
import json
import statistics
import sys
import tempfile
import textwrap
from route_ballot import choose as choose_observed_route

QA = Path(__file__).resolve().parent
ROOT = QA.parents[3]


def load_engine(package):
    source = QA.parent / 'sea_rock_preflight/FOULWAKE_SEA_ROCK_AB_PREFLIGHT_v2.7.py'
    spec = importlib.util.spec_from_file_location('locked_preflight_loader', source)
    loader = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loader)
    manifest = json.loads((ROOT / 'releases/v2.6/V26_RELEASE_MANIFEST.json').read_text())
    files, evidence = loader.load_package(Path(package), manifest)
    temporary = tempfile.TemporaryDirectory(prefix='foulwake_editorial_')
    for name, data in files.items():
        (Path(temporary.name) / name).write_bytes(data)
    sys.path.insert(0, temporary.name)
    module = importlib.import_module('tam_sistem_sim_v2_5')
    return module, temporary, evidence


def patched(module, method, replacements):
    """Exact, reviewable deltas to verified source; fail on unexpected upstream text."""
    source = textwrap.dedent(inspect.getsource(method))
    for before, after in replacements:
        assert before in source, (method.__name__, before)
        source = source.replace(before, after)
    namespace = dict(module.__dict__)
    exec(compile(source, '<editorial-adapter:' + method.__name__ + '>', 'exec'), namespace)
    return namespace[method.__name__]


def make_engine(m):
    class ObservedGame(m.V25AuditGame):
        def __init__(self, rng, config, variant='B'):
            assert variant in ('A', 'B')
            self.variant = variant
            self.met_hains = {}
            self.boat_trip = None
            super().__init__(rng, config)
            pool = [e for e in self.map_pool if e.category in (m.SEA, m.ROCK)]
            self.shared_mean = statistics.mean(e.score for e in pool)
            self.shared_damage = statistics.mean(m.event_is_damage(e) for e in pool)

        def observed_back(self, coord):
            category = self.grid[coord].category
            return 'sea_rock' if self.variant == 'B' and category in (m.SEA, m.ROCK) else category

        def prior(self, coord):
            token = self.observed_back(coord)
            if token == 'sea_rock':
                return self.shared_mean, self.shared_damage
            return self.category_mean[token], self.category_damage_rate[token]

        def known(self, player, coord):
            return coord in self.public_known or coord in player.knowledge

        def perceived_value(self, player, coord):
            if self.known(player, coord):
                return self.true_route_value(coord)
            value, risk = self.prior(coord)
            if coord in player.damage_signals:
                value = -2.5 if player.damage_signals[coord] else max(-.15, value + .45)
            elif self.hull == 1:
                value -= 5 * risk
            if self.scurvy_active and self.observed_back(coord) == m.ISLAND:
                value += 6.0  # crew utility; traitors minimize it, avoiding the mandatory cure.
            return value

        def enemy_probability(self, actor, target):
            if actor.pid == target.pid:
                return 0.0
            if actor.traitor and actor.pid in self.met_hains:
                return float(target.pid not in self.met_hains[actor.pid])
            suspicion = self.suspicion[target.pid]
            return 1 - suspicion if actor.traitor else suspicion

        def horizon_coords(self, far=False):
            near = self.valid_candidates()
            if not far:
                return [(r, c) for r, c, _ in near]
            rr = self.row + 2
            if rr >= self.voyage.height:
                return []
            return [(rr, c) for c in range(max(0, self.col-1), min(self.voyage.width, self.col+2))
                    if (rr, c) not in self.public_blocked
                    and abs(c-self.port_col) <= self.voyage.height-1-rr
                    and any(abs(c-nc) <= 1 for _, nc, _ in near)
                    and self._can_reach_port(rr, c, frozenset(self.public_blocked), {})]

        def look_for_player(self, player, coords):
            coords = [c for c in coords if c in self.grid and not self.known(player, c)]
            if coords:
                worst = min(self.prior(c)[0] for c in coords)
                player.knowledge.add(self.rng.choice([c for c in coords if self.prior(c)[0] == worst]))

        def look_for_hains(self, coords, amount):
            coords = [c for c in coords if c in self.grid and c not in self.hain_team_known and c not in self.public_known]
            for _ in range(min(amount, len(coords))):
                worst = min(self.prior(c)[0] for c in coords)
                chosen = self.rng.choice([c for c in coords if self.prior(c)[0] == worst])
                self.hain_team_known.add(chosen)
                for player in self.active(traitor=True, include_cabin=False):
                    player.knowledge.add(chosen)
                coords.remove(chosen)
                self.metrics_count['hain_peeks'] += 1

        def _make_claims(self, candidates):
            coords = [(r, c) for r, c, _ in candidates]
            claims = []
            for p in self.active(include_cabin=False):
                known = [c for c in coords if self.known(p, c)]
                if not p.traitor:
                    if not known or self.rng.random() > self.persona.share_rate:
                        continue
                    target = max(known, key=lambda c: abs(self.perceived_value(p, c)))
                    signal = 1 if self.perceived_value(p, target) >= 0 else -1
                elif self.rng.random() < self.persona.hain_truth_build and known:
                    target = max(known, key=lambda c: self.perceived_value(p, c))
                    signal = 1 if self.perceived_value(p, target) >= 0 else -1
                elif coords and self.rng.random() < self.persona.share_rate + .18:
                    target = min(coords, key=lambda c: (self.perceived_value(p, c), self.rng.random()))
                    signal = 1
                else:
                    continue
                # Truth used for AFTER-THE-FACT metrics only; no policy reads this flag.
                truth = (self.true_route_value(target) >= 0) == (signal > 0)
                claims.append(m.Claim(p.pid, target, signal, truth, target in known))
            self.metrics_count['claims'] += len(claims)
            self.metrics_count['true_claims'] += sum(c.truthful for c in claims)
            self.metrics_count['false_claims'] += sum(not c.truthful for c in claims)
            self.metrics_count['informed_claims'] += sum(c.informed for c in claims)
            return claims

        def maybe_use_wet_map(self, candidates):
            if self.row < 0 and self.day <= 1:
                return
            return super().maybe_use_wet_map(candidates)

        def use_day_information(self, candidates, fog_expected=False):
            # Opening restriction is about information, not all day powers.
            if self.day > 1:
                m.AuditGame.use_day_information(self, candidates, fog_expected)
                holder, power = self.holder_for_power({'pusula'}, helpful=True)
                unseen = [(r, c) for r, c, _ in candidates if (r, c) not in self.public_known]
                if holder and unseen and self.rng.random() < .22:
                    choose = min if holder.traitor else max
                    coord = choose(unseen, key=lambda c: self.perceived_value(holder, c))
                    holder.powers.remove(power); self.record_power_effect(power)
                    self.public_known.add(coord)
                    if self.grid[coord].kind == 'impassable_reef': self.public_blocked.add(coord)
            holders = [p for p in self.active(include_cabin=False) if 'guverte_aramasi' in p.powers]
            targets = [p for p in self.active(include_cabin=False) if len(p.powers) >= 2]
            if holders and targets and self.rng.random() < .22:
                h = self.rng.choice(holders)
                target = max(targets, key=lambda p: self.enemy_probability(h, p))
                h.powers.remove('guverte_aramasi'); self.record_power_effect('guverte_aramasi')
                drop = min(target.powers, key=lambda x: m.POWER_KEEP_PRIORITY.get(x, 1))
                target.powers.remove(drop); self._discard_power(drop)
                self.metrics_count['deck_search_discards'] += 1

        def public_reveal(self, coords):
            unseen = [c for c in coords if c in self.grid and c not in self.public_known]
            if unseen:
                captain = self.player(self.captain)
                choose = min if captain.traitor else max
                coord = choose(unseen, key=lambda c: self.perceived_value(captain, c))
                self.public_known.add(coord)
                if self.grid[coord].kind == 'impassable_reef': self.public_blocked.add(coord)
                self.metrics_count['public_info'] += 1

        def gain_powers(self, amount, source_category=None):
            recipients = self.active(include_cabin=False)
            if not recipients: return
            # Receiver selected by Captain BEFORE any card face is drawn.
            captain = self.player(self.captain)
            ordered = sorted(recipients, key=lambda p: self.enemy_probability(captain, p))
            chosen_recipients = ordered[:min(amount, len(ordered))]
            distributor = self.find_role('iskele_sicani', helpful=True) if source_category in (m.ISLAND, m.LIGHT) else None
            if distributor and chosen_recipients:
                first = min(recipients, key=lambda p: self.enemy_probability(distributor, p))
                chosen_recipients = [first] + [p for p in ordered if p != first][:amount-1]
                self.mark_character_used(distributor)
            for target in chosen_recipients:
                if not self.power_deck and self.power_discard:
                    self.rng.shuffle(self.power_discard)
                    self.power_deck = self.power_discard; self.power_discard = []
                    self.metrics_count['power_deck_reshuffles'] += 1
                if not self.power_deck: break
                power = self.power_deck.pop()
                thief, sock = self.holder_for_power({'islak_corap'}, helpful=False)
                if thief and thief != target:
                    thief.powers.remove(sock)
                    target.powers.append(sock)
                    while len(target.powers) > 2:
                        drop = min(target.powers, key=lambda x: m.POWER_KEEP_PRIORITY.get(x, 1))
                        target.powers.remove(drop); self._discard_power(drop)
                    self.power_used_seen.add(sock); self.power_effect_used_seen.add(sock)
                    self.metrics_count['powers_used'] += 1
                    target = thief
                self.add_power(target, power)

        def add_power(self, player, power):
            player.powers.append(power); self.metrics_count['powers_drawn'] += 1
            while len(player.powers) > 2:
                drop = min(player.powers, key=lambda x: m.POWER_KEEP_PRIORITY.get(x, 1))
                player.powers.remove(drop); self._discard_power(drop)
                self.metrics_count['powers_lost'] += 1

        def random_targets(self, amount):
            candidates = self.active(include_cabin=False)
            if getattr(self, 'require_power_target', False):
                candidates = [p for p in candidates if p.powers]
            if not candidates:
                self.marked_marti_pid = None  # The next target event consumes a stale mark.
                return []
            amount = min(amount, len(candidates))
            if self.marked_marti_pid is not None:
                marked = [p for p in candidates if p.pid == self.marked_marti_pid]
                self.marked_marti_pid = None
                if marked:
                    first = marked[0]
                    self.metrics_count['marti_targets'] += 1
                    return [first] + self.rng.sample([p for p in candidates if p != first], amount-1)
            out = self.rng.sample(candidates, amount)
            # A complete d12 re-selection can select the SAME target again.
            holders = [p for p in candidates if 'ugurlu_altin' in p.powers]
            willing = [p for p in holders if any(self.enemy_probability(p, t) < .3 for t in out)]
            if willing:
                holder = self.rng.choice(willing)
                holder.powers.remove('ugurlu_altin'); self.record_power_effect('ugurlu_altin')
                out = self.rng.sample(candidates, amount)
                self.metrics_count['lucky_rerolls'] += 1
            return out

        def prepare_suspicious_seagull(self):
            if self.marked_marti_pid is not None: return
            holders = [p for p in self.active(include_cabin=False) if 'supheli_marti' in p.powers]
            if not holders: return
            holder = self.rng.choice(holders)
            targets = [p for p in self.active(include_cabin=False) if p != holder]
            if not targets: return
            target = max(targets, key=lambda p: self.enemy_probability(holder, p))
            if self.enemy_probability(holder, target) < .46: return
            holder.powers.remove('supheli_marti'); self.record_power_effect('supheli_marti')
            self.marked_marti_pid = target.pid
            self.metrics_count['marti_placed'] += 1

        def prepare_flare_for_island(self):
            stranded = [p for p in self.players if p.status == 'stranded']
            if not stranded or self.boat_trip: return
            boatman = self.find_role('kirik_kurek', helpful=True)
            holders = [p for p in self.players if p.status in ('ship', 'stranded') and not p.cabin and 'pusula' in p.powers]
            if not boatman or not holders: return
            holder = self.rng.choice(holders)
            holder.powers.remove('pusula'); self.record_power_effect('pusula')
            target = self.rng.choice(stranded)
            self.mark_character_used(boatman)
            boatman.status = 'boat_trip'
            self.boat_trip = (boatman.pid, target.pid, self.day+1)
            self.elect_if_needed()

        def clear_cabins(self):
            if self.boat_trip and self.day >= self.boat_trip[2]:
                for pid in self.boat_trip[:2]:
                    p = self.player(pid); p.status = 'ship'; p.stranded_at = None
                self.boat_trip = None
                self.metrics_count['kayikci_rescues'] += 1
            return super().clear_cabins()

        def rescue_stranded_after_move(self):
            # Boat rescue now takes a full watch, never an instantaneous chain.
            return None

        def night_phase(self, fog, first_night):
            awake = {p.pid for p in self.active(traitor=True, include_cabin=False)}
            for pid in awake:
                self.met_hains.setdefault(pid, set()).update(awake)
            return super().night_phase(fog, first_night)

        def role_information(self, fog):
            # Anahtar Deliği is a DAY card, not a night-phase shortcut.
            temporarily = []
            for p in self.players:
                if p.cabin and 'anahtar_deligi' in p.powers:
                    p.powers.remove('anahtar_deligi'); temporarily.append(p)
            super().role_information(fog)
            for p in temporarily: p.powers.append('anahtar_deligi')

        def cabin_day_window(self):
            # Called after the day's event/political action, BEFORE night begins.
            for player in self.players:
                if player.status == 'ship' and player.cabin and 'anahtar_deligi' in player.powers:
                    coords = [c for c in self.horizon_coords() if not self.known(player,c)]
                    if coords:
                        self.look_for_player(player,coords)
                        player.powers.remove('anahtar_deligi')
                        self.record_power_effect('anahtar_deligi')
                        self.metrics_count['cabin_day_peeks'] += 1

        def resolve_event(self, event):
            # v2.7 card text follows locked v2.6 rules over stale legacy policies.
            if event.category == m.ISLAND and self.scurvy_active:
                self.scurvy_active = False; self.scurvy_cleared = True
                self.metrics_count['scurvy_cleared'] += 1
            if event.kind == 'hostage':
                self.metrics_count['events'] += 1; self.reached_map_names[event.name] += 1
                if len(self.active(include_cabin=False)) > 1:
                    target = self.random_targets(1)
                    if target: self.strand_on_island(target[0])
                return False, False
            if event.kind == 'everyone_keep_one':
                self.metrics_count['events'] += 1; self.reached_map_names[event.name] += 1
                for p in self.active(include_cabin=False):
                    while len(p.powers) > 1: self.lose_one_concealed(p)
                return False, False
            self.require_power_target = event.kind in ('lose_random', 'two_lose_all')
            try:
                return super().resolve_event(event)
            finally:
                self.require_power_target = False

        def move_once(self, first_move=False, forced=False):
            if forced and not self.valid_candidates():
                return False, False
            if not self.valid_candidates() and self.emergency_reverse():
                return False, False
            result = base_move(self, first_move=False, forced=forced)
            coord = (self.row, self.col)
            if coord in self.opened_cards:
                self.public_known.add(coord)
            return result

    base_move = patched(m, m.AuditGame.move_once, [
        ('self.public_known.add(coord)\n        self.opened_cards.add(coord)\n        self.update_suspicion_after_route(event)', 'self.public_known.add(coord)\n        self.update_suspicion_after_route(event)'),
    ])
    ObservedGame._vote_accusation = patched(m, m.AuditGame._vote_accusation, [
        ('if target.traitor:', 'if self.enemy_probability(p, target) < .5:'),
    ])
    ObservedGame.choose_route = lambda self, candidates, first_move=False: choose_observed_route(self, m, candidates)
    ObservedGame.update_suspicion_after_route = patched(m, m.AuditGame.update_suspicion_after_route, [
        ('if self.player(pid).traitor and delta > 0:', 'if delta > 0:'),
        ('if self.player(claim.pid).traitor and delta > 0:', 'if delta > 0:'),
    ])
    ObservedGame.political_action = patched(m, m.AuditGame.political_action, [
        ('if self.config.politics_rule == "none" or self.day <= 1:', 'if self.port_approach or self.config.politics_rule == "none" or self.day <= 1:'),
        ('((not p.traitor and captain.traitor) or (p.traitor and not captain.traitor))', '(self.enemy_probability(p, captain) >= .54)'),
    ])
    ObservedGame.run = patched(m, m.V25AuditGame.run, [
        ('self.category_mean[self.grid[(r,c)].category]', 'self.prior((r,c))[0]'),
        ('self.political_action()', 'self.political_action();self.cabin_day_window()'),
    ])
    return ObservedGame
