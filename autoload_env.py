from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(__file__).parent / ".env"

if env_path.exists():
    load_dotenv(env_path)
    print(f"[OK] Loaded .env from {env_path}")
    # Show which keys are present
    for key in ["RASA_PRO_LICENSE", "OPENAI_API_KEY"]:
        val = os.getenv(key)
        print(f"  {key} = {'SET' if val else 'MISSING'}")
else:
    print(f"[FAIL] No .env file found at {env_path}")