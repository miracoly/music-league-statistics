import re

from typing import Optional


def extract_id_from(spotify_uri: str) -> Optional[str]:
    match = re.match("^spotify:track:([a-zA-Z0-9]{22})$", spotify_uri)
    return None if match is None else match.group(1)
