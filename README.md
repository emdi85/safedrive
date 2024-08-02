# Car Alert System

## Description
This project is a car alert system that uses GPS data and integrates with vegvesenet.no to provide real-time alerts for speed cameras, traffic conditions, and more.

## Setup

### Prerequisites
- Python 3.x
- A virtual environment tool (e.g., `venv`)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/car_alert_system.git
    cd car_alert_system
    ```

2. Create a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
1. Navigate to the `app` directory:
    ```bash
    cd app
    ```

2. Run the Flask application:
    ```bash
    python main.py
    ```

3. Open a web browser and navigate to `http://localhost:5000` to view the interface.

## Files

- `app/` - Contains the application code.
- `app/static/` - Contains static files like CSS.
- `app/templates/` - Contains HTML templates.
- `app/main.py` - The main Flask application file.
- `app/gps_reader.py` - Reads GPS data.
- `app/alert_system.py` - Handles alert generation.
- `app/data_fetcher.py` - Fetches data from vegvesenet.no.
- `app/utils.py` - Utility functions.
