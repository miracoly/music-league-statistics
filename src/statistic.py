from dataclasses import dataclass
from typing import Tuple, List, Callable

from functional import seq
from tqdm import tqdm

from src.console import BColors
from src.league import League
from src.player import Player, get_members_of
from src.result import get_submissions_of
from src.round import Round, get_rounds_of, Status
from src.tracks import Track, get_tracks_of


@dataclass
class RoundStatistic:
    player_name: str
    round_name: str
    artist: str
    track: str


def get_statistic_of_league(league: League, session: str) -> List[RoundStatistic]:
    members = get_members_of(league.id, session)
    rounds = get_rounds_of(league.id, session)
    completed_rounds = seq(rounds).filter(lambda r: r.status == Status.COMPLETE).list()
    progress_bar = tqdm(range(0, len(completed_rounds)), desc=f' {BColors.OKBLUE}{league.name}')
    return seq(progress_bar) \
        .flat_map(lambda i: get_statistic_of_round(completed_rounds[i], members, session)) \
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


def write_to_csv(rounds: List[RoundStatistic], out_file_name: str):
    header = ["Player", "Round", "Artist", "Track"]
    rows = seq(rounds).map(lambda r: [r.player_name, r.round_name, r.artist, r.track]).list()
    seq([header] + rows).to_csv(out_file_name)
