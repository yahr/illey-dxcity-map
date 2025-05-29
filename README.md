# Naver Map Viewer

A Streamlit application that displays coordinates from a CSV file on a map.

## Setup

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

## CSV File Format

The CSV file should contain the following columns:
- `latitude`: Latitude coordinates
- `longitude`: Longitude coordinates

Example CSV format:
```csv
latitude,longitude
37.5665,126.9780
37.5714,126.9760
37.5796,126.9770
```

## Features

- Upload CSV files containing coordinate data
- Preview the uploaded data
- Display coordinates on an interactive map
- Click markers to see location information 