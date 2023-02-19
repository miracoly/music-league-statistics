import logging
from dataclasses import dataclass
from typing import List, Dict, Optional, TypeVar, Type

import requests
from dacite import from_dict
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


@dataclass
class _MeDto:
    chatToken: str
    email: str
    id: str
    images: Dict
    meta: Dict
    name: str
    stats: Dict


@dataclass
class Me:
    id: str
    name: str

    T = TypeVar('T', bound='Me')

    @classmethod
    def new_from(cls: Type[T], dto: _MeDto) -> T:
        return Me(dto.id, dto.name)


def get_me(session_id: str) -> Optional[Me]:
    json = _fetch_me(session_id)
    return None if json is None else Me.new_from(from_dict(_MeDto, json))


def get_members_of(league_id: str, session_id: str) -> List[Player]:
    json = _fetch_members_of(league_id, session_id)
    return seq(json) \
        .map(lambda entry: from_dict(_PlayerDto, entry)) \
        .map(lambda dto: Player(dto.user.id, dto.user.name)) \
        .list()


def _fetch_me(session_id: str) -> Optional[Dict]:
    url = 'https://app.musicleague.com/api/v1/me'
    headers = {'cookie': f'session={session_id}'}
    try:
        return requests.get(url, headers=headers).json()
    except RequestException:
        logging.error("Could not fetch infos about me from url %s", url)
        return None


def _fetch_members_of(league_id: str, session_id: str) -> List[Dict]:
    url = f'https://app.musicleague.com/api/v1/leagues/{league_id}/members'
    headers = {'cookie': f'session={session_id}'}
    try:
        return requests.get(url, headers=headers).json()
    except RequestException:
        logging.error("Could not fetch members of league from url %s", url)
        return []
