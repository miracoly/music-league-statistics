from dataclasses import dataclass
from typing import Tuple, List, Callable

from functional import seq

from src.league import get_leagues_of
from src.player import Player, get_members_of, get_me
from src.result import get_submissions_of
from src.round import Round, get_rounds_of, Status
from src.tracks import Track, get_tracks_of


@dataclass
class RoundStatistic:
    player_name: str
    round_name: str
    artist: str
    track: str


def get_statistic_of_all_leagues(session_id: str) -> List[RoundStatistic]:
    me = get_me(session_id)
    leagues = get_leagues_of(me.id, session_id)
    return seq(leagues) \
        .flat_map(lambda league: get_statistic_of_league(league.id, session_id)) \
        .list()


def get_statistic_of_league(league_id: str, session_id: str) -> List[RoundStatistic]:
    rounds = get_rounds_of(league_id, session_id)
    members = get_members_of(league_id, session_id)
    return seq(rounds) \
        .filter(lambda r: r.status == Status.COMPLETE) \
        .flat_map(lambda r: get_statistic_of_round(r, members, session_id)) \
        .list()


def get_statistic_of_round(r: Round, members: List[Player], session_id: str) -> List[RoundStatistic]:
    submissions = get_submissions_of(r.id, r.league_id, session_id)

    track_ids = seq(submissions) \
        .map(lambda sub: sub.spotify_song_id) \
        .list()

    player_names = seq(submissions) \
        .map(lambda sub: sub.player_id) \
        .map(lambda player_id: seq(members).find(lambda m: m.id == player_id)) \
        .map(lambda player: player.name) \
        .list()

    return seq(get_tracks_of(track_ids, session_id)) \
        .zip(player_names) \
        .flat_map(_to_statistic(r.name)) \
        .list()


def _to_statistic(round_name: str) -> Callable[[Tuple[Track, str]], List[RoundStatistic]]:
    def f(track_player: Tuple[Track, str]) -> List[RoundStatistic]:
        track, player_name = track_player
        return seq(track.artists) \
            .map(lambda artist: RoundStatistic(player_name, round_name, artist.name, track.name)) \
            .list()
    return f


def write_to_csv(rounds: List[RoundStatistic], out_file_name="statistics.csv"):
    header = ["Player", "Round", "Artist", "Track"]
    rows = seq(rounds).map(lambda r: [r.player_name, r.round_name, r.artist, r.track]).list()
    seq([header] + rows).to_csv(out_file_name)
