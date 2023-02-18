import unittest

from parameterized import parameterized
from src.spotify import extract_id_from


class TestStatus(unittest.TestCase):

    @parameterized.expand([
        ["spotify:track:0AgIlcYIsGSJXO66r1vw6r", "0AgIlcYIsGSJXO66r1vw6r"],
        ["spotify:track:03DIX9HAyBasSRLvSZIkrN", "03DIX9HAyBasSRLvSZIkrN"],
        ["spotify:track:0oayy8OHHzuT1URyldeu9P", "0oayy8OHHzuT1URyldeu9P"],
    ])
    def test__extract_id_from__success__return_id(self, url: str, expected_id: str):
        """Test extract_id_from - valid url - return song id"""
        spotify_id = extract_id_from(url)
        self.assertEqual(expected_id, spotify_id)

    @parameterized.expand([
        ["sspotify:track:0AgIlcYIsGSJXO66r1vw6r"],
        ["spotify:track:03DIX9HAyBasSRLvSZIkrNA"],
        ["spotify:track:0*ayy8OHHzuT1URyldeu9P"],
    ])
    def test__extract_id_from__malformed_string__return_none(self, malformed_url: str):
        """Test extract_id_from - malformed url - return None"""
        spotify_id = extract_id_from(malformed_url)
        self.assertEqual(None, spotify_id)


if __name__ == '__main__':
    unittest.main()
