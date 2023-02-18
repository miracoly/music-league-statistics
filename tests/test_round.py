import unittest

from unittest.mock import patch, Mock
from src.round import get_rounds_of, Status, Round


class TestStatus(unittest.TestCase):

    def test_new_from__valid_value__return_instance_of_status(self):
        """Test new_from - value exists in Enum - return instance of Status"""
        status = Status.new_from("NOT_STARTED")
        self.assertEqual(status, Status.NOT_STARTED)

    def test_new_from__invalid__return_none(self):
        """Test new_from - value exists in Enum - return None"""
        status = Status.new_from("DOES_NOT_EXIST")
        self.assertEqual(status, None)


class TestRound(unittest.TestCase):

    @patch('src.round._fetch_rounds_of')
    def test_get_members_of__failure__return_empty_list(self, _fetch_rounds_of_mock: Mock):
        """Test get_rounds_of - error while fetching - return empty list"""
        _fetch_rounds_of_mock.return_value = []
        rounds = get_rounds_of("league-id", "session-id")
        self.assertEqual(rounds, [])

    @patch('src.round._fetch_rounds_of')
    def test_get_members_of__success__return_list_of_players(self, _fetch_rounds_of_mock: Mock):
        """Test get_rounds_of - success - return list of rounds"""
        _fetch_rounds_of_mock.return_value = fetched_rounds
        rounds = get_rounds_of("league-id", "session-id")
        self.assertEqual(rounds, expected_rounds)


expected_rounds = [
    Round(id='1', league_id='league-id', name='Is this a language?', status=Status.COMPLETE),
    Round(id='2', league_id='league-id', name='Verkehr', status=Status.COMPLETE),
    Round(id='3', league_id='league-id', name='Songs die man nicht laut im Büro hören sollte', status=Status.COMPLETE),
    Round(id='4', league_id='league-id', name='Gegensätze', status=Status.COMPLETE),
    Round(id='5', league_id='league-id', name='Lullabies to use if you want your baby to never sleep again', status=Status.COMPLETE)
]

fetched_rounds = [{'id': '1', 'name': 'Is this a language?', 'completed': '2022-06-13T11:01:13.061308Z',
                   'description': 'Eine Reise in fremde Kulturen', 'downvotesPerUser': 0, 'highStakes': False, 'leagueId': 'league-id',
                   'maxDownvotesPerSong': 0, 'maxUpvotesPerSong': 1, 'playlistUrl': 'url-to-spotify-playlist', 'sequence': 1,
                   'songsPerUser': 1, 'startDate': '2022-06-07T06:18:17.169392Z', 'status': 'COMPLETE', 'submissionsDue': '2022-06-09T11:00:00Z',
                   'upvotesPerUser': 1, 'votesDue': '2022-06-13T11:00:00Z', 'templateId': ''},
                  {'id': '2', 'name': 'Verkehr', 'completed': '2022-06-16T11:01:10.013501Z', 'description': '',
                   'downvotesPerUser': 0, 'highStakes': False, 'leagueId': 'league-id', 'maxDownvotesPerSong': 0, 'maxUpvotesPerSong': 1,
                   'playlistUrl': 'url-to-spotify-playlist', 'sequence': 2, 'songsPerUser': 1,
                   'startDate': '2022-06-13T11:00:00Z', 'status': 'COMPLETE', 'submissionsDue': '2022-06-14T11:00:00Z', 'upvotesPerUser': 1,
                   'votesDue': '2022-06-16T11:00:00Z', 'templateId': ''},
                  {'id': '3', 'name': 'Songs die man nicht laut im Büro hören sollte',
                   'completed': '2022-06-22T09:43:53.425053Z', 'description': '', 'downvotesPerUser': 0, 'highStakes': False,
                   'leagueId': 'league-id', 'maxDownvotesPerSong': 0, 'maxUpvotesPerSong': 1,
                   'playlistUrl': 'url-to-spotify-playlist', 'sequence': 3, 'songsPerUser': 1,
                   'startDate': '2022-06-16T11:00:00Z', 'status': 'COMPLETE', 'submissionsDue': '2022-06-20T11:00:00Z', 'upvotesPerUser': 1,
                   'votesDue': '2022-06-22T10:00:00Z', 'templateId': ''},
                  {'id': '4', 'name': 'Gegensätze', 'completed': '2022-06-27T10:01:14.807436Z', 'description': '',
                   'downvotesPerUser': 0, 'highStakes': False, 'leagueId': 'league-id', 'maxDownvotesPerSong': 0, 'maxUpvotesPerSong': 1,
                   'playlistUrl': 'url-to-spotify-playlist', 'sequence': 4, 'songsPerUser': 1,
                   'startDate': '2022-06-22T10:00:00Z', 'status': 'COMPLETE', 'submissionsDue': '2022-06-23T11:00:00Z', 'upvotesPerUser': 1,
                   'votesDue': '2022-06-27T10:00:00Z', 'templateId': ''},
                  {'id': '5', 'name': 'Lullabies to use if you want your baby to never sleep again',
                   'completed': '2022-07-01T11:01:09.601221Z', 'description': '', 'downvotesPerUser': 0, 'highStakes': False,
                   'leagueId': 'league-id', 'maxDownvotesPerSong': 0, 'maxUpvotesPerSong': 1,
                   'playlistUrl': 'url-to-spotify-playlist', 'sequence': 5, 'songsPerUser': 1,
                   'startDate': '2022-06-27T10:00:00Z', 'status': 'COMPLETE', 'submissionsDue': '2022-06-29T11:00:00Z', 'upvotesPerUser': 1,
                   'votesDue': '2022-07-01T11:00:00Z', 'templateId': ''}]

if __name__ == '__main__':
    unittest.main()
