
from pathlib import Path
import pandas as pd

URL = (
    "https://deepchemdata.s3-us-west-1.amazonaws.com/"
    "datasets/delaney-processed.csv"
)

# Locate the project root
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Create raw data directory
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = RAW_DATA_DIR / "esol.csv"


def download_esol():
    print("Downloading ESOL dataset...")

    df = pd.read_csv(URL)

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nDownload successful!")
    print(f"Saved to: {OUTPUT_FILE}")
    print(f"Dataset shape: {df.shape}")
    print(f"\nColumns:\n{df.columns.tolist()}")


if __name__ == "__main__":
    download_esol()
