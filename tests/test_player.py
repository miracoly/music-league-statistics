import unittest

from unittest.mock import patch, Mock
from src.player import get_members_of, Player, get_me, Me


class TestPlayer(unittest.TestCase):

    @patch('src.player._fetch_me')
    def test_get_me__failure__return_none(self, _fetch_me_mock: Mock):
        """Test get_me - error while fetching - return None"""
        _fetch_me_mock.return_value = None
        me = get_me("session-id")
        self.assertEqual(None, me)

    @patch('src.player._fetch_me')
    def test_get_me__success__return_me(self, _fetch_me_mock: Mock):
        """Test get_me - success - return me"""
        _fetch_me_mock.return_value = fetched_me
        me = get_me("session-id")
        self.assertEqual(expected_me, me)

    @patch('src.player._fetch_members_of')
    def test_get_members_of__failure__return_empty_list(self, _fetch_members_of_mock: Mock):
        """Test get_members_of - error while fetching - return empty list"""
        _fetch_members_of_mock.return_value = []
        players = get_members_of("league-id", "session-id")
        self.assertEqual([], players)

    @patch('src.player._fetch_members_of')
    def test_get_members_of__success__return_list_of_players(self, _fetch_members_of_mock: Mock):
        """Test get_members_of - success - return list of players"""
        _fetch_members_of_mock.return_value = fetched_members
        players = get_members_of("league-id", "session-id")
        self.assertEqual(expected_players, players)


expected_me = Me(id='5', name='Miracoly')

fetched_me = {
    "id": "5",
    "name": "Miracoly",
    "email": "bla@keks.com",
    "images": {
        "profile": "url-to-profile-picture"
    },
    "chatToken": "secret",
    "meta": {
        "adSegment": 4,
        "isAdmin": False,
        "patronTier": 0
    },
    "stats": {
        "numLeagues": 5,
        "numPlacedFirst": 1,
        "numPlacedSecond": 0,
        "numPlacedThird": 0
    }
}

expected_players = [
    Player(id='1', name='rahel'),
    Player(id='2', name='fabian'),
    Player(id='3', name='1ɴɢ0ʟꜰ'),
    Player(id='4', name='phil'),
    Player(id='5', name='Miracoly'),
    Player(id='6', name='Nils'),
    Player(id='7', name='Seb')
]

fetched_members = [
    {
        "created": "2022-06-07T06:18:16.594798Z",
        "isAdmin": True,
        "isPlayer": True,
        "user": {
            "id": "1",
            "name": "rahel",
            "profileImage": "url-to-profile-picture"
        }
    },
    {
        "created": "2022-06-07T06:21:21.368052Z",
        "isAdmin": False,
        "isPlayer": True,
        "user": {
            "id": "2",
            "name": "fabian",
            "profileImage": "url-to-profile-picture"
        }
    },
    {
        "created": "2022-06-07T06:24:02.572755Z",
        "isAdmin": False,
        "isPlayer": True,
        "user": {
            "id": "3",
            "name": "1ɴɢ0ʟꜰ",
            "profileImage": "url-to-profile-picture"
        }
    },
    {
        "created": "2022-06-07T06:35:24.583997Z",
        "isAdmin": False,
        "isPlayer": True,
        "user": {
            "id": "4",
            "name": "phil",
            "profileImage": "url-to-profile-picture"
        }
    },
    {
        "created": "2022-06-07T07:07:33.892625Z",
        "isAdmin": False,
        "isPlayer": True,
        "user": {
            "id": "5",
            "name": "Miracoly",
            "profileImage": "url-to-profile-picture"
        }
    },
    {
        "created": "2022-06-07T07:21:45.33194Z",
        "isAdmin": False,
        "isPlayer": True,
        "user": {
            "id": "6",
            "name": "Nils",
            "profileImage": "url-to-profile-picture"
        }
    },
    {
        "created": "2022-06-07T07:48:34.627437Z",
        "isAdmin": False,
        "isPlayer": True,
        "user": {
            "id": "7",
            "name": "Seb",
            "profileImage": "url-to-profile-picture"
        }
    }
]

if __name__ == '__main__':
    unittest.main()
