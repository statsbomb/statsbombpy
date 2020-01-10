import pandas as pd

from unittest import TestCase, main

from statsbombpy.base import get_competitions, get_matches, get_lineups


class TestBaseGetters(TestCase):
    def test_get_competitions(self):
        competitions = get_competitions()
        self.assertIsInstance(competitions, pd.DataFrame)
        competitions = get_competitions(fmt="json")
        self.assertIsInstance(competitions, dict)

    def test_get_matches(self):
        matches = get_matches(competition_id=43, season_id=3)
        self.assertIsInstance(matches, pd.DataFrame)
        matches = get_matches(competition_id=43, season_id=3, fmt="json")
        self.assertIsInstance(matches, dict)

    def test_get_lineups(self):
        lineups = get_lineups(match_id=7562)
        self.assertIsInstance(lineups, dict)
        self.assertIsInstance([*lineups.values()][0], pd.DataFrame)
        lineups = get_lineups(match_id=7562, fmt="json")
        self.assertIsInstance(lineups, dict)


if __name__ == "__main__":
    main()
