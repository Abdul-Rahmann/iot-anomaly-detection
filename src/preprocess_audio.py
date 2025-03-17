import zipfile
import os
import librosa
import pandas as pd
import logging
from sklearn.preprocessing import StandardScaler

DATA_DIR = "data/raw"
OUTPUT_DIR = "data/processed"
LOG_DIR = "logs"

# Ensure necessary directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# Set up logging
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "preprocessing.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def extract_features(zip_path):
    """Extracts MFCC features from audio files inside a ZIP archive."""
    print(f"Processing {zip_path}...")

    with zipfile.ZipFile(zip_path, 'r') as archive:
        for file in archive.namelist():
            if file.endswith(".wav"):
                with archive.open(file) as f:
                    try:
                        # Load audio
                        audio, sr = librosa.load(f, sr=16000)

                        # Extract MFCC features
                        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)

                        # Convert to DataFrame
                        df = pd.DataFrame(mfccs.T)
                        df.columns = [f"mfcc_{i}" for i in range(df.shape[1])]

                        # Check for missing values and replace with zero if any
                        if df.isnull().values.any():
                            logging.warning(f"Missing values detected in {file}, replacing with 0.")
                            df = df.fillna(0)

                        # Normalize the features using StandardScaler
                        # scaler = StandardScaler()
                        # df.iloc[:, :] = scaler.fit_transform(df)

                        # Create the output directory structure
                        subdir = os.path.dirname(file)
                        save_path = os.path.join(OUTPUT_DIR, subdir)
                        os.makedirs(save_path, exist_ok=True)

                        # Save as Parquet
                        output_file = os.path.join(save_path, f"{os.path.basename(file).replace('.wav', '.parquet')}")
                        df.to_parquet(output_file, engine="pyarrow")

                        logging.info(f"Successfully processed and saved {output_file}")
                        print(f"Saved: {output_file}")

                    except Exception as e:
                        logging.error(f"Error processing {file}: {e}")
                        print(f"Error processing {file}: {e}")


# Process all ZIP files in the dataset directory
for zip_path in os.listdir(DATA_DIR):
    extract_features(os.path.join(DATA_DIR, zip_path))

print("Feature extraction complete!")