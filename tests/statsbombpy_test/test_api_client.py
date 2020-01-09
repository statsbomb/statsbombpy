from unittest import TestCase, main

from statsbombpy.api_client import (
    get_competitions,
    get_matches,
    get_lineups,
    get_events,
)


class TestApiClient(TestCase):
    def test_get_competitions(self):
        competitions = get_competitions()
        self.assertIsInstance(competitions, dict)
    
    def test_get_matches(self):
        matches = get_matches(competition_id=43, season_id=3)
        self.assertIsInstance(matches, dict)

    def test_get_lineups(self):
        lineups = get_lineups(match_id=7562)
        self.assertIsInstance(lineups, dict)

    def test_get_events(self):
        events = get_events(match_id=7562)
        self.assertIsInstance(events, dict)


if __name__ == "__main__":
    main()
