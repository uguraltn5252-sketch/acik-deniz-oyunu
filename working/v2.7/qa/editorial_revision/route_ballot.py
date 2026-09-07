"""Exact route counting and a transparent heuristic voter, separate concerns.

Counting is deterministic. Choice, willingness to spend powers and speech remain
heuristic; this module does not claim to model a human table.
"""
from collections import Counter


def tally(votes, captain, reduced=False, hat=None, commitments=None, crow=None):
    counts=Counter()
    for pid, route in votes.items():
        if pid in (commitments or {}) and commitments[pid] != route:
            continue  # A zero vote cannot be resurrected by the hat.
        counts[route] += (2 if pid == captain and not reduced else 1) + int(pid == hat)
    if crow is not None and counts[crow] > 0:
        counts[crow] += 1
    return counts


def winners(counts):
    if not counts or max(counts.values()) <= 0:
        raise ValueError('No positive route vote')
    return [c for c,v in counts.items() if v == max(counts.values())]


def can_recount(counts, already_repeated=False):
    values=sorted(counts.values(),reverse=True)
    return not already_repeated and len(values)>1 and values[0]-values[1]==1


def choose(game, module, candidates):
    if not candidates:
        raise RuntimeError('Rota secenegi yok')
    game.maybe_use_wet_map(candidates)
    coords={(r,c):(r,c,dc) for r,c,dc in candidates}
    voters=game.active(include_cabin=False)
    claims=game._make_claims(candidates) if len(coords)>1 else []
    commitments={}; rom_pid=None; hat_pid=None; crow=None; reduced=False

    def spend(key, probability=1):
        holder,power=game.holder_for_power({key},helpful=True)
        if holder and power and game.rng.random()<probability:
            holder.powers.remove(power);game.record_power_effect(power)
            return holder

    def preferred(player, noise=True):
        def score(coord):
            value=game._score_with_claims(player,coord,claims)
            if player.traitor:
                value=-game.perceived_value(player,coord)
            return value + (game.rng.gauss(0,game.persona.route_noise) if noise else 0)
        return max(coords,key=lambda c:(score(c),game.rng.random()))

    if len(coords)>1:
        holder=spend('papagan',.38)
        if holder:
            target=max(voters,key=lambda p:game.enemy_probability(holder,p))
            commitments[target.pid]=preferred(target,False)
            game.metrics_count['public_commitments']+=1
        holder=spend('kacak_rom',.32)
        if holder:
            rom_pid=max(voters,key=lambda p:game.enemy_probability(holder,p)).pid
            game.metrics_count['last_open_votes']+=1
        cups=[p for p in voters if 'catlak_kupa' in p.powers
              and game.enemy_probability(p,game.player(game.captain))>=.46]
        if cups:
            holder=game.rng.choice(cups);holder.powers.remove('catlak_kupa')
            game.record_power_effect('catlak_kupa');reduced=True
        holder=spend('eski_sapka',.30)
        if holder:hat_pid=holder.pid
        karga=game.find_role('karga_yuvasi',helpful=True)
        if karga and game.rng.random()<.45:
            crow=preferred(karga,False)  # Mark BEFORE any vote is revealed.
            game.mark_character_used(karga)

    ordered=[p for p in voters if p.pid!=rom_pid]+[p for p in voters if p.pid==rom_pid]
    def ballot():
        votes={p.pid:preferred(p) for p in ordered}
        counts=tally(votes,game.captain,reduced,hat_pid,commitments,crow)
        game.metrics_count['ballots_cast']+=len(votes)
        game.metrics_count['broken_commitments']+=sum(votes[p]!=c for p,c in commitments.items())
        return votes,counts

    votes,counts=ballot()
    if can_recount(counts):
        holder=spend('bir_daha_say',.55)
        if holder:
            votes,counts=ballot()  # Everyone votes again; active modifiers persist.
            game.metrics_count['route_recounts']+=1
    tied=winners(counts)
    if len(tied)>1:
        game.metrics_count['route_ties']+=1
        holder=spend('muhurlu_emir')
        chooser=holder or game.player(game.captain)
        picked=max(tied,key=lambda c:((-1 if chooser.traitor else 1)*game.perceived_value(chooser,c),game.rng.random()))
    else:picked=tied[0]
    game.vote_entropy_total+=module.entropy_normalized(list(counts.values()))
    game.vote_rounds+=1;game.metrics_count['route_votes']+=1
    game.metrics_count['contested_routes']+=int(len([v for v in counts.values() if v>0])>1)
    game.last_claims=claims;game.last_votes=votes;game.last_choice=picked
    game.last_choice_voters=[pid for pid,c in votes.items() if c==picked]
    game.last_route_weights=dict(counts)
    return coords[picked]
