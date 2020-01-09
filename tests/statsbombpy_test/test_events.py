from unittest import TestCase, main

import pandas as pd

from statsbombpy.events import get_competition_events, get_events


class TestEventGetters(TestCase):
    def test_get_events(self):
        events = get_events(match_id=7562)
        self.assertIsInstance(events, pd.DataFrame)

        events = get_events(match_id=7562, split=True)
        self.assertIsInstance(events, dict)
        self.assertIsInstance(events["Shot"], pd.DataFrame)

        events = get_events(match_id=7562, fmt="json")
        self.assertIsInstance(events["Shot"], list)
        self.assertIsInstance(events["Shot"][0], dict)

        shots = get_events(match_id=7562, filters={"type": "Shot"}, fmt="json")["Shot"]
        self.assertSetEqual(
            {"Shot"}, set(map(lambda s: s["type"]["name"], shots))
        )
    
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
        self.assertIsInstance(events["Shot"], pd.DataFrame)

        events = get_competition_events(competition, fmt="json")
        self.assertIsInstance(events["Shot"], list)
        self.assertIsInstance(events["Shot"][0], dict)


if __name__ == "__main__":
    main()
