import logging
import requests

from dataclasses import dataclass
from dacite import from_dict
from typing import List, Dict, TypeVar, Type, Optional
from enum import Enum
from functional import seq
from requests import RequestException


class Status(Enum):
    COMPLETE = 1
    ACCEPTING_VOTES = 2
    NOT_STARTED = 3

    T = TypeVar('T', bound='Status')

    @classmethod
    def new_from(cls: Type[T], status: str) -> Optional[T]:
        try:
            return Status[status]
        except KeyError:
            return None


@dataclass
class Round:
    id: str
    league_id: str
    name: str
    status: Optional[Status]


@dataclass
class _RoundDto:
    id: str
    name: str
    completed: str
    description: str
    downvotesPerUser: int
    highStakes: bool
    leagueId: str
    maxDownvotesPerSong: int
    maxUpvotesPerSong: int
    playlistUrl: str
    sequence: int
    songsPerUser: int
    startDate: str
    status: str
    submissionsDue: str
    upvotesPerUser: int
    votesDue: str
    templateId: str


def get_rounds_of(league_id: str, session_id: str) -> List[Round]:
    json = _fetch_rounds_of(league_id, session_id)
    return seq(json) \
        .map(lambda entry: from_dict(_RoundDto, entry)) \
        .map(_to_model) \
        .list()


def _to_model(dto: _RoundDto) -> Round:
    return Round(dto.id, dto.leagueId, dto.name, Status.new_from(dto.status))


def _fetch_rounds_of(league_id: str, session_id: str) -> List[Dict]:
    url = f'https://app.musicleague.com/api/v1/leagues/{league_id}/rounds'
    headers = {'cookie': f'session={session_id}'}
    try:
        return requests.get(url, headers=headers).json()
    except RequestException:
        logging.error("Could not fetch rounds of league from url %s", url)
        return []
