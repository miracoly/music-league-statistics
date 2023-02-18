import logging
import requests

from dataclasses import dataclass
from dacite import from_dict
from typing import List, Dict, TypeVar, Type, Optional
from functional import seq
from requests import RequestException

from src.spotify import extract_id_from


@dataclass
class _SubmissionDto:
    comment: str
    commentVisibility: str
    created: str
    spotifyUri: str
    submitterId: str


@dataclass
class _ResultDto:
    pointsActual: int
    pointsPossible: int
    rank: int
    submission: _SubmissionDto
    submitterVoted: bool
    tieBreaker: str
    votes: List[Dict]


@dataclass
class _StandingsDto:
    standings: List[_ResultDto]


@dataclass
class Submission:
    round_id: str
    player_id: str
    spotify_song_id: str

    T = TypeVar('T', bound='Submission')

    @classmethod
    def new_from(cls: Type[T], round_id: str, result: _ResultDto) -> T:
        return Submission(
            round_id,
            result.submission.submitterId,
            extract_id_from(result.submission.spotifyUri)
        )


def get_submissions_of(round_id: str, league_id: str, session_id: str) -> List[Submission]:
    json = _fetch_results_of(round_id, league_id, session_id)
    results = [] if json is None else from_dict(_StandingsDto, json).standings
    return seq(results) \
        .map(lambda dto: Submission.new_from(round_id, dto)) \
        .list()


def _fetch_results_of(round_id: str, league_id: str, session_id: str) -> Optional[Dict]:
    url = f'https://app.musicleague.com/api/v1/leagues/{league_id}/rounds/{round_id}/results'
    headers = {'cookie': f'session={session_id}'}
    try:
        return requests.get(url, headers=headers).json()
    except RequestException:
        logging.error("Could not fetch results of round from url %s", url)
        return None
