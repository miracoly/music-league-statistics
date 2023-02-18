import logging
import requests

from dataclasses import dataclass
from dacite import from_dict
from typing import List, Dict
from functional import seq
from requests import RequestException


@dataclass
class Player:
    id: str
    name: str


@dataclass
class _UserDto:
    id: str
    name: str
    profileImage: str


@dataclass
class _PlayerDto:
    created: str
    isAdmin: bool
    isPlayer: bool
    user: _UserDto


def get_members_of(league_id: str, session_id: str) -> List[Player]:
    json = _fetch_members_of(league_id, session_id)
    return seq(json) \
        .map(lambda entry: from_dict(_PlayerDto, entry)) \
        .map(lambda dto: Player(dto.user.id, dto.user.name))\
        .list()


def _fetch_members_of(league_id: str, session_id: str) -> List[Dict]:
    url = f'https://app.musicleague.com/api/v1/leagues/{league_id}/members'
    headers = {'cookie': f'session={session_id}'}
    try:
        return requests.get(url, headers=headers).json()
    except RequestException:
        logging.error("Could not fetch members of league from url %s", url)
        return []
