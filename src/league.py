import logging
import requests

from dataclasses import dataclass
from dacite import from_dict
from typing import List, Dict, TypeVar, Type, Optional
from functional import seq
from requests import RequestException


@dataclass
class _LeagueDto:
    created: str
    currentRound: Optional[Dict]
    description: str
    id: str
    images: Dict
    members: List[Dict]
    name: str
    nextRound: Optional[Dict]
    numMembers: int
    numRounds: int
    ownerId: str
    preferences: Dict
    spaceId: str
    status: str
    tier: str
    visibility: str


@dataclass
class League:
    id: str
    name: str
    description: str

    T = TypeVar('T', bound='League')

    @classmethod
    def new_from(cls: Type[T], dto: _LeagueDto) -> T:
        return League(dto.id, dto.name, dto.description)


def get_leagues_of(user_id: str, session_id: str) -> List[League]:
    json = _fetch_leagues_of(user_id, session_id)
    return seq(json) \
        .map(lambda entry: from_dict(_LeagueDto, entry)) \
        .map(League.new_from)\
        .list()


def _fetch_leagues_of(user_id: str, session_id: str) -> List[Dict]:
    url = f'https://app.musicleague.com/api/v1/users/{user_id}/leagues'
    headers = {'cookie': f'session={session_id}'}
    try:
        return requests.get(url, headers=headers).json()
    except RequestException:
        logging.error("Could not fetch leagues of user from url %s", url)
        return []
