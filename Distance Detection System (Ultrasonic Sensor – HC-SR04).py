import RPi.GPIO as GPIO
import time

# --- GPIO pin configuration ---
TRIG = 23      # Trigger pin of HC-SR04
ECHO = 24      # Echo pin of HC-SR04
BUZZER = 18    # Buzzer pin
LED_RED = 17   # Red LED (danger)
LED_YELLOW = 27 # Yellow LED (warning)

# --- Setup ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)

# Make sure all outputs are off initially
GPIO.output(TRIG, False)
GPIO.output(BUZZER, False)
GPIO.output(LED_RED, False)
GPIO.output(LED_YELLOW, False)

print("🚗 Vehicle Distance Detection System Starting...")
time.sleep(2)

def measure_distance():
    """Measure distance using ultrasonic sensor."""
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 34300) / 2
    return round(distance, 2)

def alert(distance):
    """Control LEDs and buzzer based on distance."""
    # Reset outputs
    GPIO.output(BUZZER, False)
    GPIO.output(LED_RED, False)
    GPIO.output(LED_YELLOW, False)

    if distance < 10:
        # Too close — red light + continuous buzzer
        GPIO.output(LED_RED, True)
        GPIO.output(BUZZER, True)
        print(f"🚨 DANGER! Object {distance} cm away!")
    elif distance < 30:
        # Medium — yellow light + short buzzer beeps
        GPIO.output(LED_YELLOW, True)
        GPIO.output(BUZZER, True)
        time.sleep(0.1)
        GPIO.output(BUZZER, False)
        print(f"⚠️ Warning: Object {distance} cm away.")
    else:
        print(f"✅ Clear: Object {distance} cm away.")

try:
    while True:
        dist = measure_distance()
        alert(dist)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n🛑 System Stopped by User")

finally:
    GPIO.cleanup()
    print("GPIO Cleaned Up. Bye!")
