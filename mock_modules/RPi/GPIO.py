# mock_modules/RPi/GPIO.py

BCM = 'BCM'
OUT = 'OUT'
HIGH = True
LOW = False

def setmode(mode):
    print(f"Mock GPIO: Set mode to {mode}")

def setup(pin, mode):
    print(f"Mock GPIO: Setup pin {pin} to mode {mode}")

def output(pin, state):
    print(f"Mock GPIO: Set pin {pin} to state {state}")

def cleanup():
    print("Mock GPIO: Cleanup")
