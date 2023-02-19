import logging
import requests

from dataclasses import dataclass
from dacite import from_dict
from typing import List, Dict, Optional, Type, TypeVar
from functional import seq
from requests import RequestException

from src.spotify import extract_id_from


@dataclass
class _AlbumDto:
    name: str
    imageUrl: str
    uri: str
    images: List[Dict]


@dataclass
class _ArtistDto:
    name: str
    uri: str


@dataclass
class _TrackDto:
    isrc: str
    name: str
    uri: str
    url: str
    album: _AlbumDto
    artists: List[_ArtistDto]
    external_urls: Dict


@dataclass
class _TracksDto:
    tracks: List[_TrackDto]


@dataclass
class Artist:
    name: str

    T = TypeVar('T', bound='Artist')

    @classmethod
    def new_from(cls: Type[T], artist: _ArtistDto) -> T:
        return Artist(artist.name)


@dataclass
class Album:
    name: str

    T = TypeVar('T', bound='Album')

    @classmethod
    def new_from(cls: Type[T], album: _AlbumDto) -> T:
        return Album(album.name)


@dataclass
class Track:
    spotify_id: str
    name: str
    artists: List[Artist]
    album: Album

    T = TypeVar('T', bound='Song')

    @classmethod
    def new_from(cls: Type[T], track: _TrackDto) -> T:
        return Track(
            extract_id_from(track.uri),
            track.name,
            seq(track.artists).map(Artist.new_from).list(),
            Album.new_from(track.album)
        )


def get_tracks_of(track_ids: List[str], session_id: str) -> List[Track]:
    json = _fetch_tracks_of(track_ids, session_id)
    tracks = [] if json is None else from_dict(_TracksDto, json).tracks
    return seq(tracks) \
        .map(Track.new_from) \
        .list()


def _fetch_tracks_of(track_ids: List[str], session_id: str) -> Optional[Dict]:
    url = f"https://app.musicleague.com/api/v1/tracks"
    params = {"ids": ",".join(track_ids)}
    headers = {'cookie': f'session={session_id}'}
    try:
        return requests.get(url, params=params, headers=headers).json()
    except RequestException:
        logging.error("Could not fetch tracks from url %s", url)
        return None
