import pickle
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "models" / "malaria_model.pkl"

def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

malaria_model = load_model()