import unittest

from unittest.mock import patch, Mock
from src.tracks import get_tracks_of, Track, Artist, Album


class TestPlayer(unittest.TestCase):

    @patch('src.tracks._fetch_tracks_of')
    def test_get_tracks_of__failure__return_empty_list(self, _fetch_tracks_of_mock: Mock):
        """Test get_tracks_of - error while fetching - return empty list"""
        _fetch_tracks_of_mock.return_value = None
        tracks = get_tracks_of(["1", "2", "3"], "session-id")
        self.assertEqual([], tracks)

    @patch('src.tracks._fetch_tracks_of')
    def test_get_tracks_of__success__return_list_of_tracks(self, _fetch_tracks_of_mock: Mock):
        """Test get_tracks_of - success - return list of tracks"""
        _fetch_tracks_of_mock.return_value = fetched_tracks
        track_ids = ["03DIX9HAyBasSRLvSZIkrN", "0AgIlcYIsGSJXO66r1vw6r", "0oayy8OHHzuT1URyldeu9P"]
        tracks = get_tracks_of(track_ids, "session-id")
        self.assertEqual(expected_players, tracks)


expected_players = [
    Track("03DIX9HAyBasSRLvSZIkrN", "Hey!", [Artist("Die Fantastischen Vier")], Album("Viel - Jubiläums-Edition")),
    Track("0AgIlcYIsGSJXO66r1vw6r", "Just a Day", [Artist("Feeder")], Album("Seven Days in the Sun")),
    Track("0oayy8OHHzuT1URyldeu9P", "I Know", [Artist("Drake Bell")], Album("It's Only Time")),
]

fetched_tracks = {
    "tracks": [
        {
            "isrc": "DEE860400681",
            "uri": "spotify:track:03DIX9HAyBasSRLvSZIkrN",
            "url": "https://open.spotify.com/track/03DIX9HAyBasSRLvSZIkrN",
            "name": "Hey!",
            "album": {
                "uri": "spotify:album:265fpziPcNNDSBYhwOE5YY",
                "name": "Viel - Jubiläums-Edition",
                "imageUrl": "https://i.scdn.co/image/ab67616d00001e029e6501acda7e7fdb914a6d99",
                "images": [
                    {
                        "url": "https://i.scdn.co/image/ab67616d0000b2739e6501acda7e7fdb914a6d99"
                    },
                    {
                        "url": "https://i.scdn.co/image/ab67616d00001e029e6501acda7e7fdb914a6d99"
                    },
                    {
                        "url": "https://i.scdn.co/image/ab67616d000048519e6501acda7e7fdb914a6d99"
                    }
                ]
            },
            "artists": [
                {
                    "uri": "spotify:artist:748dDObrUoBetes0pLj788",
                    "name": "Die Fantastischen Vier"
                }
            ],
            "external_urls": {
                "spotify": "https://open.spotify.com/track/03DIX9HAyBasSRLvSZIkrN"
            }
        },
        {
            "isrc": "GBBND0000767",
            "uri": "spotify:track:0AgIlcYIsGSJXO66r1vw6r",
            "url": "https://open.spotify.com/track/0AgIlcYIsGSJXO66r1vw6r",
            "name": "Just a Day",
            "album": {
                "uri": "spotify:album:2vvGQrzGWDELlfjKYK2dgw",
                "name": "Seven Days in the Sun",
                "imageUrl": "https://i.scdn.co/image/ab67616d00001e020d7c83e69494360f6af9eef9",
                "images": [
                    {
                        "url": "https://i.scdn.co/image/ab67616d0000b2730d7c83e69494360f6af9eef9"
                    },
                    {
                        "url": "https://i.scdn.co/image/ab67616d00001e020d7c83e69494360f6af9eef9"
                    },
                    {
                        "url": "https://i.scdn.co/image/ab67616d000048510d7c83e69494360f6af9eef9"
                    }
                ]
            },
            "artists": [
                {
                    "uri": "spotify:artist:0ZZr6Y49NZWRJc0uCwqpMR",
                    "name": "Feeder"
                }
            ],
            "external_urls": {
                "spotify": "https://open.spotify.com/track/0AgIlcYIsGSJXO66r1vw6r"
            }
        },
        {
            "isrc": "USUM70615212",
            "uri": "spotify:track:0oayy8OHHzuT1URyldeu9P",
            "url": "https://open.spotify.com/track/0oayy8OHHzuT1URyldeu9P",
            "name": "I Know",
            "album": {
                "uri": "spotify:album:6OI8uy6Azo79fLZe1lweKc",
                "name": "It's Only Time",
                "imageUrl": "https://i.scdn.co/image/ab67616d00001e027d05e6840f9be074ac5711f5",
                "images": [
                    {
                        "url": "https://i.scdn.co/image/ab67616d0000b2737d05e6840f9be074ac5711f5"
                    },
                    {
                        "url": "https://i.scdn.co/image/ab67616d00001e027d05e6840f9be074ac5711f5"
                    },
                    {
                        "url": "https://i.scdn.co/image/ab67616d000048517d05e6840f9be074ac5711f5"
                    }
                ]
            },
            "artists": [
                {
                    "uri": "spotify:artist:03ilIKH0i08IxmjKcn63ne",
                    "name": "Drake Bell"
                }
            ],
            "external_urls": {
                "spotify": "https://open.spotify.com/track/0oayy8OHHzuT1URyldeu9P"
            }
        }
    ]
}
