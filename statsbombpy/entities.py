def competitions(competitions: list) -> dict:
    competitions_ = {}
    for c in competitions:
        competitions_[
            (
                c["country_name"],
                c["competition_name"],
                c["season_name"],
                c["competition_gender"],
            )
        ] = c
    return competitions_


def matches(matches: list) -> dict:
    matches_ = {
        m["match_id"]: m
        for m in matches
        if m["match_status"] == "available"
    }
    return matches_


def lineups(lineups: list) -> dict:
    lineups_ = {l["team_id"]: l for l in lineups}
    return lineups_


def events(events: list, match_id: int) -> dict:
    events_ = {}
    for e in events:
        e["match_id"] = match_id
        events_[e["id"]] = e
    return events_