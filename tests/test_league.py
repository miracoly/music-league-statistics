import unittest

from unittest.mock import patch, Mock
from src.league import get_leagues_of, League


class TestPlayer(unittest.TestCase):

    @patch('src.league._fetch_leagues_of')
    def test_get_leagues_of__failure__return_empty_list(self, _fetch_leagues_of_mock: Mock):
        """Test get_leagues_of - error while fetching - return empty list"""
        _fetch_leagues_of_mock.return_value = []
        leagues = get_leagues_of("user-id", "session-id")
        self.assertEqual([], leagues)

    @patch('src.league._fetch_leagues_of')
    def test_get_leagues_of__success__return_list_of_leagues(self, _fetch_leagues_of_mock: Mock):
        """Test get_leagues_of - success - return list of leagues"""
        _fetch_leagues_of_mock.return_value = fetched_leagues
        leagues = get_leagues_of("user-id", "session-id")
        self.assertEqual(expected_leagues, leagues)


expected_leagues = [
    League(id="league-1", name="KB League - Wer hat's eingereicht?", description="description of league 1"),
    League(id="league-2", name="KB League IV", description="description of league 2"),
    League(id="league-3", name="KB League III", description="description of league 3"),
    League(id="league-4", name="KB League II", description="description of league 4"),
    League(id="league-5", name="kb League", description="description of league 5")
]

fetched_leagues = [
    {
        "created": "2023-01-23T17:10:41.419609Z",
        "description": "description of league 1",
        "id": "league-1",
        "images": {
            "cover": "url-to-cover-image"
        },
        "members": [],
        "name": "KB League - Wer hat's eingereicht?",
        "currentRound": {
            "amPlaying": True,
            "haveSubmitted": True,
            "haveVoted": False,
            "sequence": 5,
            "status": "ACCEPTING_VOTES",
            "submissionsDue": "2023-02-17T11:00:00Z",
            "votesDue": "2023-02-20T11:00:00Z"
        },
        "nextRound": {
            "sequence": 6,
            "starting": "2023-02-22T11:00:00Z"
        },
        "numMembers": 10,
        "numRounds": 9,
        "ownerId": "user-id-1",
        "preferences": {
            "id": "league-1",
            "trackCount": 1,
            "highStakes": True,
            "maxMembers": 20,
            "upvoteBankSize": 0,
            "maxUpvotesPerSong": 0,
            "downvoteBankSize": 0,
            "maxDownvotesPerSong": 0,
            "submissionCommentVisibility": "AFTER_VOTING",
            "submissionIntervalDays": 2,
            "voteIntervalDays": 3,
            "pacing": "ACCELERATED"
        },
        "spaceId": "",
        "status": "IN_PROGRESS",
        "tier": "PREMIUM_1",
        "visibility": "RESTRICTED"
    },
    {
        "completed": "2022-10-12T09:11:49.153725Z",
        "created": "2022-10-12T09:11:49.153725Z",
        "description": "description of league 2",
        "id": "league-2",
        "images": {
            "cover": "url-to-cover-image"
        },
        "members": [],
        "name": "KB League IV",
        "numMembers": 7,
        "numRounds": 6,
        "ownerId": "user-id-1",
        "preferences": {
            "id": "league-2",
            "trackCount": 1,
            "highStakes": False,
            "maxMembers": 10,
            "upvoteBankSize": 1,
            "maxUpvotesPerSong": 1,
            "downvoteBankSize": 0,
            "maxDownvotesPerSong": 0,
            "submissionCommentVisibility": "AFTER_VOTING",
            "submissionIntervalDays": 1,
            "voteIntervalDays": 2,
            "pacing": "ACCELERATED"
        },
        "spaceId": "",
        "status": "COMPLETE",
        "tier": "PREMIUM_1",
        "visibility": "RESTRICTED"
    },
    {
        "completed": "2022-06-07T06:18:16.590284Z",
        "created": "2022-06-07T06:18:16.590284Z",
        "description": "description of league 3",
        "id": "league-3",
        "images": {
            "cover": "url-to-cover-image"
        },
        "members": [],
        "name": "KB League III",
        "numMembers": 7,
        "numRounds": 5,
        "ownerId": "user-id-1",
        "preferences": {
            "id": "league-3",
            "trackCount": 1,
            "highStakes": False,
            "maxMembers": 20,
            "upvoteBankSize": 1,
            "maxUpvotesPerSong": 1,
            "downvoteBankSize": 0,
            "maxDownvotesPerSong": 0,
            "submissionCommentVisibility": "AFTER_VOTING",
            "submissionIntervalDays": 1,
            "voteIntervalDays": 2,
            "pacing": "ACCELERATED"
        },
        "spaceId": "",
        "status": "COMPLETE",
        "tier": "PREMIUM_1",
        "visibility": "RESTRICTED"
    },
    {
        "completed": "2022-04-25T12:30:43.063838Z",
        "created": "2022-04-25T12:30:43.063838Z",
        "description": "description of league 4",
        "id": "league-4",
        "images": {
            "cover": "url-to-cover-image"
        },
        "members": [],
        "name": "KB League II",
        "numMembers": 9,
        "numRounds": 9,
        "ownerId": "user-id-1",
        "preferences": {
            "id": "league-4",
            "trackCount": 2,
            "highStakes": True,
            "maxMembers": 15,
            "upvoteBankSize": 15,
            "maxUpvotesPerSong": 10,
            "downvoteBankSize": 1,
            "maxDownvotesPerSong": 1,
            "submissionCommentVisibility": "AFTER_VOTING",
            "submissionIntervalDays": 1,
            "voteIntervalDays": 2,
            "pacing": "ACCELERATED"
        },
        "spaceId": "",
        "status": "COMPLETE",
        "tier": "PREMIUM_1",
        "visibility": "RESTRICTED"
    },
    {
        "completed": "2021-11-19T18:41:30.815112Z",
        "created": "2021-11-19T18:41:30.815112Z",
        "description": "description of league 5",
        "id": "league-5",
        "images": {
            "cover": "url-to-cover-image"
        },
        "members": [],
        "name": "kb League",
        "numMembers": 11,
        "numRounds": 11,
        "ownerId": "user-id-2",
        "preferences": {
            "id": "league-5",
            "trackCount": 2,
            "highStakes": False,
            "maxMembers": 100,
            "upvoteBankSize": 10,
            "maxUpvotesPerSong": 0,
            "downvoteBankSize": 1,
            "maxDownvotesPerSong": 0,
            "submissionCommentVisibility": "AFTER_VOTING",
            "submissionIntervalDays": 2,
            "voteIntervalDays": 5,
            "pacing": "ACCELERATED"
        },
        "spaceId": "",
        "status": "COMPLETE",
        "tier": "PREMIUM_1",
        "visibility": "RESTRICTED"
    }
]

if __name__ == '__main__':
    unittest.main()
