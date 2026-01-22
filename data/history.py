PITCH_HISTORY = []

def save_pitch(idea, names, slogans):
    PITCH_HISTORY.append({
        "idea": idea,
        "names": names,
        "slogans": slogans
    })
