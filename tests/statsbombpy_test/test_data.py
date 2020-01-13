import os

import pandas as pd

from unittest import TestCase, main

from statsbombpy.data import (
    get_competitions,
    get_competition_events,
    get_events,
    get_matches,
    get_lineups,
)


class TestBaseGetters(TestCase):
    def test_get_competitions(self):
        competitions = get_competitions()
        self.assertIsInstance(competitions, pd.DataFrame)
        competitions = get_competitions(fmt="json")
        self.assertIsInstance(competitions, dict)

        competitions = get_competitions(creds={})
        self.assertIsInstance(competitions, pd.DataFrame)

    def test_get_matches(self):
        matches = get_matches(competition_id=43, season_id=3)
        self.assertIsInstance(matches, pd.DataFrame)
        matches = get_matches(competition_id=43, season_id=3, fmt="json")
        self.assertIsInstance(matches, dict)

        matches = get_matches(competition_id=43, season_id=3, creds={})
        self.assertIsInstance(matches, pd.DataFrame)

    def test_get_lineups(self):
        lineups = get_lineups(match_id=7562)
        self.assertIsInstance(lineups, dict)
        self.assertIsInstance([*lineups.values()][0], pd.DataFrame)
        lineups = get_lineups(match_id=7562, fmt="json")
        self.assertIsInstance(lineups, dict)

        lineups = get_lineups(match_id=7562, creds={})
        self.assertIsInstance(lineups, dict)


class TestEventGetters(TestCase):
    def test_get_events(self):
        events = get_events(match_id=7562)
        self.assertIsInstance(events, pd.DataFrame)

        events = get_events(match_id=7562, split=True)
        self.assertIsInstance(events, dict)
        self.assertIsInstance(events["shots"], pd.DataFrame)

        events = get_events(match_id=7562, fmt="json")
        self.assertIsInstance(events["shots"], list)
        self.assertIsInstance(events["shots"][0], dict)

        shots = get_events(match_id=7562, filters={"type": "Shot"}, fmt="json")["shots"]
        self.assertSetEqual({"Shot"}, set(map(lambda s: s["type"]["name"], shots)))

        events = get_events(match_id=7562, creds={})
        self.assertIsInstance(events, pd.DataFrame)

    def test_get_competition_events(self):
        competition = {
            "country": "England",
            "division": "FA Cup",
            "season": "2019/2020",
            "gender": "male",
        }
        events = get_competition_events(competition)
        self.assertIsInstance(events, pd.DataFrame)

        events = get_competition_events(competition, split=True)
        self.assertIsInstance(events["shots"], pd.DataFrame)

        events = get_competition_events(competition, fmt="json")
        self.assertIsInstance(events["shots"], list)
        self.assertIsInstance(events["shots"][0], dict)


if __name__ == "__main__":
    main()
