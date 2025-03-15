# IoT Anomaly Detection and Forecasting System

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Datasets](#datasets)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Project Overview
This project focuses on developing an anomaly detection and forecasting system for Industrial IoT (IIoT) applications. By leveraging the MIMII dataset, which contains audio recordings of industrial machines under various conditions, and integrating with the ThingSpeak IoT platform, the system simulates real-time data streams to detect anomalies and predict future machine behavior.

---

## Features
- **Anomaly Detection**: Utilizes machine learning models to identify deviations from normal operational patterns in industrial machines.
- **Forecasting**: Implements time-series forecasting techniques to predict future sensor readings and potential anomalies.
- **Real-Time Data Simulation**: Employs ThingSpeak to emulate live data streaming from industrial sensors.
- **Interactive Dashboard**: Provides a user-friendly interface for monitoring real-time data, detected anomalies, and forecasts.

---

## Architecture
The system architecture comprises the following components:
1. **Data Source**: MIMII dataset serving as the historical data foundation.
2. **Data Simulation**: ThingSpeak platform simulating real-time data streams.
3. **Anomaly Detection Module**: Machine learning models analyzing data for anomalies.
4. **Forecasting Module**: Time-series models predicting future sensor behavior.
5. **Dashboard**: Interactive visualization of data, anomalies, and forecasts.

*For a visual representation of the architecture, refer to the Architecture Diagram.*

---

## Datasets
- **MIMII Dataset**: Contains audio recordings of industrial machines (valves, pumps, fans, and slide rails) under normal and anomalous conditions.
- **Access**: [MIMII Dataset on Zenodo](https://zenodo.org/)
- **Documentation**: [MIMII Dataset Documentation](https://zenodo.org/doc)

---

## Installation

### Prerequisites
- Conda (Anaconda or Miniconda)
- ThingSpeak account

### Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/iot-anomaly-detection.git
    cd iot-anomaly-detection
    ```

2. **Create a Conda Environment**:
    ```bash
    conda create --name iot_env python=3.8
    ```

3. **Activate the Environment**:
    ```bash
    conda activate iot_env
    ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up ThingSpeak Channel**:
    - Create a new channel on ThingSpeak with appropriate fields for your data.
    - Note the Channel ID and Write API Key.

6. **Configure Environment Variables**:
    - Rename `.env.example` to `.env`.
    - Update the `.env` file with your ThingSpeak credentials:
        ```env
        THINGSPEAK_CHANNEL_ID=your_channel_id
        THINGSPEAK_WRITE_API_KEY=your_write_api_key
        ```

---

## Usage

### Data Simulation

1. **Extract Features from MIMII Dataset**:
    Use the provided `feature_extraction.py` script to process audio files and extract features.
    ```bash
    python feature_extraction.py --data_dir path_to_mimii_data --output_dir path_to_features
    ```

2. **Simulate Real-Time Data Streaming**:
    Run the `data_simulation.py` script to upload extracted features to ThingSpeak at regular intervals.
    ```bash
    python data_simulation.py --features_dir path_to_features
    ```

### Anomaly Detection and Forecasting

1. **Train Anomaly Detection Model**:
    Execute the `train_anomaly_model.py` script to train the model on normal condition data.
    ```bash
    python train_anomaly_model.py --features_dir path_to_normal_features
    ```

2. **Train Forecasting Model**:
    Use the `train_forecasting_model.py` script to develop a time-series forecasting model.
    ```bash
    python train_forecasting_model.py --features_dir path_to_historical_features
    ```

### Dashboard

1. **Launch Dashboard**:
    Start the Dash application to visualize real-time data, anomalies, and forecasts.
    ```bash
    python app.py
    ```

2. **Access Dashboard**:
    Navigate to [http://127.0.0.1:8050/](http://127.0.0.1:8050/) in your web browser to interact with the dashboard.

---

## Project Structure

```plaintext
iot-anomaly-detection/
│
├── data/
│   ├── raw/                   # Raw MIMII dataset files
│   └── processed/             # Processed feature files
│
├── notebooks/
│   └── exploratory_analysis.ipynb  # Jupyter notebook for data exploration
│
├── src/
│   ├── feature_extraction.py  # Script for extracting features from audio
│   ├── data_simulation.py     # Script for real-time data simulation
│   ├── train_anomaly_model.py # Script for training anomaly detection model
│   ├── train_forecasting_model.py # Script for time-series forecasting
│   └── app.py                 # Dashboard application
│
├── environment.yml            # Python dependencies
├── .env                       # Environment variable configuration example
└── README.md                  # Project documentation
```

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements
- [MIMII Dataset](https://zenodo.org/)
- ThingSpeak IoT Platform
- Dash Framework for Python