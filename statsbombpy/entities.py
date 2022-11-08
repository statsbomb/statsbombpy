def competitions(competitions: list) -> dict:
    competitions_ = {}
    for comp in competitions:
        competitions_[
            (
                comp["country_name"],
                comp["competition_name"],
                comp["season_name"],
                comp["competition_gender"],
            )
        ] = comp
    return competitions_


def matches(matches: list) -> dict:
    matches_ = {match["match_id"]: match for match in matches}
    return matches_


def lineups(lineups: list) -> dict:
    lineups_ = {lineup["team_id"]: lineup for lineup in lineups}
    return lineups_


def events(events: list, match_id: int) -> dict:
    events_ = {}
    for ev in events:
        ev["match_id"] = match_id
        events_[ev["id"]] = ev
    return events_


def frames(frames: list, match_id: int) -> list:
    for fr in frames:
        fr["match_id"] = match_id
    return frames
