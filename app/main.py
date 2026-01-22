from fastapi import FastAPI
from app.schemas import PitchRequest, PitchResponse
from app.generator import generate_pitch

app = FastAPI(
    title="AiPitcher API",
    description="Startup name and slogan generator",
    version="1.0"
)

@app.post("/pitch", response_model=PitchResponse)
def pitch(request: PitchRequest):
    return generate_pitch(request.idea)
