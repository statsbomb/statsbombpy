import os

import pandas as pd

from unittest import TestCase, main

from statsbombpy import sb


class TestBaseGetters(TestCase):
    def test_competitions(self):
        competitions = sb.competitions()
        self.assertIsInstance(competitions, pd.DataFrame)

        competitions = sb.competitions(fmt="json")
        self.assertIsInstance(competitions, dict)

        competitions = sb.competitions(creds={})
        self.assertIsInstance(competitions, pd.DataFrame)

    def test_matches(self):
        matches = sb.matches(competition_id=43, season_id=3)
        self.assertIsInstance(matches, pd.DataFrame)

        matches = sb.matches(competition_id=43, season_id=3, fmt="json")
        self.assertIsInstance(matches, dict)

        matches = sb.matches(competition_id=43, season_id=3, creds={})
        self.assertIsInstance(matches, pd.DataFrame)

        matches = sb.matches(competition_id=2, season_id=44)
        self.assertIsInstance(matches, pd.DataFrame)

        matches = sb.matches(competition_id=2, season_id=44, fmt="json")
        self.assertIsInstance(matches, dict)

        matches = sb.matches(competition_id=2, season_id=44, creds={})
        self.assertIsInstance(matches, pd.DataFrame)

    def test_lineups(self):
        lineups = sb.lineups(match_id=7562)
        self.assertIsInstance(lineups, dict)
        self.assertIsInstance([*lineups.values()][0], pd.DataFrame)

        lineups = sb.lineups(match_id=7562, fmt="json")
        self.assertIsInstance(lineups, dict)

        lineups = sb.lineups(match_id=7562, creds={})
        self.assertIsInstance(lineups, dict)


class TestEventGetters(TestCase):
    def test_events(self):
        events = sb.events(match_id=7562)
        self.assertIsInstance(events, pd.DataFrame)

        events = sb.events(match_id=7562, split=True)
        self.assertIsInstance(events, dict)
        self.assertIsInstance(events["shots"], pd.DataFrame)

        events = sb.events(match_id=7562, fmt="json")
        self.assertIsInstance(events, dict)

        events = sb.events(match_id=7562, creds={})
        self.assertIsInstance(events, pd.DataFrame)
        self.assertTrue("shot_statsbomb_xg" in events.columns)

        events = sb.events(match_id=7562, creds={}, flatten_attrs=False)
        self.assertIsInstance(events, pd.DataFrame)
        self.assertFalse("shot_statsbomb_xg" in events.columns)
        self.assertTrue("shot" in events.columns)

    def test_competition_events(self):
        events = sb.competition_events(
            country="England", division="FA Cup", season="2019/2020", gender="male"
        )
        self.assertIsInstance(events, pd.DataFrame)

        events = sb.competition_events(
            country="England",
            division="FA Cup",
            season="2019/2020",
            split=True,
        )
        self.assertIsInstance(events["shots"], pd.DataFrame)

        events = sb.competition_events(
            country="England",
            division="FA Cup",
            season="2019/2020",
            fmt="json",
        )


if __name__ == "__main__":
    main()
