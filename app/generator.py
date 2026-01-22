from data.history import save_pitch

def generate_pitch(idea: str):
    names = [
        f"{idea.title()} Labs",
        f"{idea.title()}ify",
        f"Neo{idea.title()}",
        f"{idea.title()}Works"
    ]

    slogans = [
        f"Reimagining {idea}",
        f"The future of {idea}",
        f"Built to transform {idea}",
        f"Where {idea} meets innovation"
    ]

    save_pitch(idea, names, slogans)

    return {
        "names": names,
        "slogans": slogans
    }
