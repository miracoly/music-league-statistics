from dataclasses import dataclass
from typing import Tuple, List, Callable
from functional import seq

from src.player import Player
from src.round import Round
from src.result import get_submissions_of
from src.tracks import Track, get_tracks_of


@dataclass
class RoundStatistic:
    player_name: str
    round_name: str
    artist: str
    track: str


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
        return [RoundStatistic(player_name, round_name, track.artists[0].name, track.name)]
    return f



def write_to_csv(rounds: List[RoundStatistic], out_file_name="statistics.csv"):
    header = ["Player", "Round", "Artist", "Track"]
    rows = seq(rounds).map(lambda r: [r.player_name, r.round_name, r.artist, r.track]).list()
    seq([header] + rows).to_csv(out_file_name)
