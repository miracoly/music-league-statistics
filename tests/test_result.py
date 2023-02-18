import unittest

from unittest.mock import patch, Mock
from src.result import get_submissions_of, Submission


class TestPlayer(unittest.TestCase):

    @patch('src.result._fetch_results_of')
    def test_get_submissions_of__failure__return_empty_list(self, _fetch_results_of_mock: Mock):
        """Test get_submissions_of - error while fetching - return empty list"""
        _fetch_results_of_mock.return_value = None
        submissions = get_submissions_of("round-id", "league-id", "session-id")
        self.assertEqual([], submissions)

    @patch('src.result._fetch_results_of')
    def test_get_submission_of__success__return_list_of_submissions(self, _fetch_results_of_mock: Mock):
        """Test get_submissions_of - success - return list of submissions"""
        _fetch_results_of_mock.return_value = fetched_standings
        submissions = get_submissions_of("round-id", "league-id", "session-id")
        self.assertEqual(expected_submissions, submissions)


expected_submissions = [
    Submission(round_id='round-id', player_id='1', spotify_song_id='03DIX9HAyBasSRLvSZIkrN'),
    Submission(round_id='round-id', player_id='2', spotify_song_id='0AgIlcYIsGSJXO66r1vw6r'),
    Submission(round_id='round-id', player_id='3', spotify_song_id='0oayy8OHHzuT1URyldeu9P'),
    Submission(round_id='round-id', player_id='4', spotify_song_id='18lR4BzEs7e3qzc0KVkTpU'),
    Submission(round_id='round-id', player_id='5', spotify_song_id='1qgBWVUAPvtlvSuQMZEEkS'),
]

fetched_standings = {
  "standings": [
    {
      "pointsActual": 0,
      "pointsPossible": 0,
      "rank": 1,
      "submission": {
        "created": "2023-01-25T10:50:28.9132Z",
        "submitterId": "1",
        "spotifyUri": "spotify:track:03DIX9HAyBasSRLvSZIkrN",
        "comment": "",
        "commentVisibility": ""
      },
      "submitterVoted": True,
      "tieBreaker": "",
      "votes": []
    },
    {
      "pointsActual": 0,
      "pointsPossible": 0,
      "rank": 1,
      "submission": {
        "created": "2023-01-30T07:50:51.328248Z",
        "submitterId": "2",
        "spotifyUri": "spotify:track:0AgIlcYIsGSJXO66r1vw6r",
        "comment": "",
        "commentVisibility": ""
      },
      "submitterVoted": True,
      "tieBreaker": "",
      "votes": []
    },
    {
      "pointsActual": 0,
      "pointsPossible": 0,
      "rank": 1,
      "submission": {
        "created": "2023-01-30T07:48:15.627225Z",
        "submitterId": "3",
        "spotifyUri": "spotify:track:0oayy8OHHzuT1URyldeu9P",
        "comment": "Mein celebrity crush mit 14 als die Twilight-Phase anfing :D :D ",
        "commentVisibility": ""
      },
      "submitterVoted": True,
      "tieBreaker": "",
      "votes": []
    },
    {
      "pointsActual": 0,
      "pointsPossible": 0,
      "rank": 1,
      "submission": {
        "created": "2023-01-26T20:14:10.366271Z",
        "submitterId": "4",
        "spotifyUri": "spotify:track:18lR4BzEs7e3qzc0KVkTpU",
        "comment": "",
        "commentVisibility": ""
      },
      "submitterVoted": True,
      "tieBreaker": "",
      "votes": []
    },
    {
      "pointsActual": 0,
      "pointsPossible": 0,
      "rank": 1,
      "submission": {
        "created": "2023-01-25T08:41:54.635219Z",
        "submitterId": "5",
        "spotifyUri": "spotify:track:1qgBWVUAPvtlvSuQMZEEkS",
        "comment": "",
        "commentVisibility": ""
      },
      "submitterVoted": True,
      "tieBreaker": "",
      "votes": []
    }
  ]
}

if __name__ == '__main__':
    unittest.main()
