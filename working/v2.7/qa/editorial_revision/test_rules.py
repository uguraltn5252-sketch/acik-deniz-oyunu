"""Targeted rules and hidden-information regressions, using the locked package."""
import copy
import os
import random
import unittest
from observation_engine import load_engine, make_engine

M, TEMP, EVIDENCE = load_engine(os.environ['FOULWAKE_SOURCE_ZIP'])
G = make_engine(M)


def game(seed=3, n=10, variant='B'):
    return G(random.Random(seed), M.canonical_config(n, length='short'), variant)


def clear(g):
    for p in g.players:
        p.knowledge.clear(); p.damage_signals.clear(); p.powers.clear()
        p.character = 'fici_bekcisi'; p.character_used = False
    g.public_known.clear(); g.hain_team_known.clear()


class RulesTests(unittest.TestCase):
    def test_initial_real_power_and_neutral_peek_all_counts(self):
        for n in range(6, 16):
            g = game(n=n)
            self.assertTrue(all(len(p.powers) == 1 for p in g.players))
            self.assertEqual(sum(len(p.knowledge) for p in g.players), 1)
            self.assertEqual(len(g.hain_team_known), 0)
            self.assertEqual(g.scurvy_active, g.scurvy_owner != g.captain)
            self.assertEqual(g.hull, 2)

    def test_no_first_route_information_power_consumption(self):
        for seed in range(20):
            g = game(seed); clear(g); g.day = 1
            p = g.player(g.captain); p.powers = ['kirik_durbun', 'seyir_defteri']
            state = g.rng.getstate(); g.use_day_information(g.valid_candidates())
            self.assertEqual(p.powers, ['kirik_durbun', 'seyir_defteri'])
            self.assertEqual(p.knowledge, set()); self.assertEqual(p.damage_signals, {})

    def test_information_power_works_after_first_day(self):
        g = game(); clear(g); g.day = 2
        for p in g.players: p.traitor = False
        p = g.players[0]; p.powers = ['kirik_durbun']
        g.use_day_information(g.valid_candidates())
        self.assertNotIn('kirik_durbun', p.powers); self.assertEqual(len(p.knowledge), 1)

    def test_first_night_characters_work_but_never_attack_even_in_fog(self):
        for fog in (False, True):
            g = game(); clear(g); g.day = 1
            near_player, far_player = [p for p in g.players if not p.traitor][:2]
            near_player.character = 'uzakgoren'; far_player.character = 'kiyicizen'
            g.night_phase(fog, True)
            self.assertEqual(g.metrics_count['attacks'], 0)
            self.assertTrue(near_player.knowledge)
            self.assertEqual(bool(far_player.knowledge), not fog)

    def test_regular_fog_allows_peek_and_attack(self):
        g = game(); clear(g); g.day = 2; g.night_phase(True, False)
        self.assertEqual(g.metrics_count['attacks'], 1)
        self.assertEqual(g.metrics_count['hain_peeks'], 1)

    def test_known_front_retains_information(self):
        g = game(); clear(g); p = g.players[0]
        coord = g.horizon_coords()[0]
        g.grid[coord] = next(e for e in g.map_pool if e.kind == 'storm_damage')
        p.knowledge.add(coord)
        self.assertEqual(g.perceived_value(p, coord), g.true_route_value(coord))
        self.assertEqual(g.observed_back(coord), 'sea_rock')

    def test_hidden_card_permutation_does_not_change_claims_votes_or_peeks(self):
        for seed in range(30):
            a = game(seed); clear(a); a.day = 2
            candidates = a.valid_candidates()[:2]
            if len(candidates) < 2: continue
            ca, cb = [(r, c) for r, c, _ in candidates]
            a.grid[ca] = next(e for e in a.map_pool if e.kind == 'storm_damage')
            a.grid[cb] = next(e for e in a.map_pool if e.kind == 'impassable_reef')
            b = copy.deepcopy(a); b.grid[ca], b.grid[cb] = b.grid[cb], b.grid[ca]
            claims_a = [(x.pid, x.coord, x.signal, x.informed) for x in a._make_claims(candidates)]
            claims_b = [(x.pid, x.coord, x.signal, x.informed) for x in b._make_claims(candidates)]
            self.assertEqual(claims_a, claims_b)
            self.assertEqual(a.choose_route(candidates), b.choose_route(candidates))
            self.assertEqual(a.last_votes, b.last_votes)
            a.look_for_player(a.players[0], [ca, cb]); b.look_for_player(b.players[0], [ca, cb])
            self.assertEqual(a.players[0].knowledge, b.players[0].knowledge)

    def test_unrevealed_other_loyalty_does_not_change_enemy_estimate(self):
        g = game(); clear(g); p = next(p for p in g.players if not p.traitor)
        target = next(t for t in g.players if t != p)
        before = g.enemy_probability(p, target); target.traitor = not target.traitor
        self.assertEqual(before, g.enemy_probability(p, target))

    def test_cabin_hain_does_not_receive_team_peek(self):
        g = game(); clear(g); hains = [p for p in g.players if p.traitor]
        hains[0].cabin = True; g.night_phase(False, True)
        self.assertFalse(hains[0].knowledge)
        self.assertTrue(hains[1].knowledge)

    def test_scurvy_clears_before_hostage_even_if_new_stranded_player(self):
        g = game(); clear(g); g.scurvy_active = True
        g.resolve_event(next(e for e in g.map_pool if e.kind == 'hostage'))
        self.assertFalse(g.scurvy_active)
        self.assertEqual(sum(p.status == 'stranded' for p in g.players), 1)

    def test_customs_does_not_discard_loyalty_or_extra_hain_power(self):
        g = game(); clear(g)
        for p in g.players: p.powers = ['yama', 'zipkin']
        g.resolve_event(next(e for e in g.map_pool if e.kind == 'everyone_keep_one'))
        self.assertTrue(all(len(p.powers) == 1 for p in g.players))
        self.assertEqual(g.metrics_count['identity_discards'], 0)

    def test_power_loss_only_targets_holders_and_consumes_stale_seagull(self):
        g = game(); clear(g)
        target = g.players[0]; target.powers = ['yama']
        g.marked_marti_pid = g.players[1].pid
        g.resolve_event(next(e for e in g.map_pool if e.kind == 'lose_random'))
        self.assertFalse(target.powers); self.assertIsNone(g.marked_marti_pid)

    def test_gains_two_distinct_recipients(self):
        g = game(); clear(g); g.power_deck = ['yama', 'zipkin']
        g.gain_powers(2)
        self.assertEqual(sum(bool(p.powers) for p in g.players), 2)

    def test_island_valued_as_cure_by_both_factions(self):
        g = game(); clear(g); g.scurvy_active = True
        coord = next(c for c, e in g.grid.items() if e.category == M.ISLAND)
        p, h = next(p for p in g.players if not p.traitor), next(p for p in g.players if p.traitor)
        self.assertEqual(g.perceived_value(p, coord), g.perceived_value(h, coord))
        self.assertGreater(g.perceived_value(p, coord), 0)  # traitor minimizes crew utility

    def test_port_skips_new_politics(self):
        g = game(); g.day = 8; g.port_approach = True
        g.suspicion = {p.pid: .99 for p in g.players}
        for _ in range(20): g.political_action()
        self.assertEqual(g.metrics_count['accusation_attempts'], 0)
        self.assertEqual(g.metrics_count['mutiny_attempts'], 0)

    def test_boat_trip_takes_whole_day_and_night(self):
        g = game(); clear(g); g.day = 3
        g.players[0].character = 'kirik_kurek'; g.players[0].traitor = False
        g.players[1].status = 'stranded'; g.players[1].powers = ['pusula']
        g.prepare_flare_for_island()
        self.assertEqual(g.players[0].status, 'boat_trip')
        self.assertEqual(g.players[1].status, 'stranded')
        g.clear_cabins(); self.assertEqual(g.players[0].status, 'boat_trip')
        g.day = 4; g.clear_cabins()
        self.assertEqual(g.players[0].status, 'ship'); self.assertEqual(g.players[1].status, 'ship')

    def test_lucky_reroll_can_return_same_target(self):
        repeated = 0
        for seed in range(100):
            g = game(seed); clear(g)
            for p in g.players: p.traitor = False; p.powers = ['ugurlu_altin']
            state = g.rng.getstate(); first = g.rng.sample(g.active(include_cabin=False), 1)[0]
            g.rng.setstate(state); second = g.random_targets(1)[0]
            repeated += first.pid == second.pid
        self.assertGreater(repeated, 0)

    def test_impassable_reveal_is_never_a_visit(self):
        g = game(); clear(g)
        before = (g.row, g.col)
        choice = g.valid_candidates()[0]; coord = choice[:2]
        g.grid[coord] = next(e for e in g.map_pool if e.kind == 'impassable_reef')
        g.choose_route = lambda *args, **kwargs: choice
        g.move_once()
        self.assertEqual((g.row, g.col), before)
        self.assertIn(coord, g.public_known)
        self.assertIn(coord, g.public_blocked)
        self.assertNotIn(coord, g.opened_cards)

    def test_forced_extra_with_no_target_does_not_reverse(self):
        g = game(); g.valid_candidates = lambda *a, **k: []
        g.emergency_reverse = lambda: self.fail('Event extra movement cannot start an emergency reverse')
        self.assertEqual(g.move_once(forced=True), (False, False))

    def test_full_model_finishes_each_player_count(self):
        for n in range(6, 16):
            g = game(n=n); r = g.run()
            self.assertIn(r['reason'], ('sunk', 'crew_extinct', 'scurvy', 'port'))
            self.assertIn(r['hull_left'], (0, 1, 2))
            self.assertFalse(r['identity_discards'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
