# alert_system.py

import os
import sys
import time

# Ensure that the `mock_modules` directory is correctly added to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
mock_modules_path = os.path.join(current_dir, '..', 'mock_modules')
sys.path.insert(0, mock_modules_path)

import RPi.GPIO as GPIO
from utils import is_nearby, calculate_distance

# GPIO Pin Definitions
LED_PIN = 18
SPEAKER_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SPEAKER_PIN, GPIO.OUT)

def generate_alerts(current_location, data):
    alerts = []
    for alert in data['alerts']:
        if is_nearby(current_location, alert['location']):
            alerts.append({
                'type': alert['type'],
                'location': alert['location'],
                'distance': calculate_distance(current_location, alert['location'])
            })
            trigger_alert(alert)
    return alerts

def trigger_alert(alert):
    print(f"Alert: {alert['type']} at {alert['location']}")
    # Simulate blinking LED and sounding speaker
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.output(SPEAKER_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(SPEAKER_PIN, GPIO.LOW)
    time.sleep(0.5)

def cleanup():
    GPIO.cleanup()
