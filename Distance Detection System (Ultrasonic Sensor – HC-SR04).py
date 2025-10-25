import RPi.GPIO as GPIO
import time

# --- GPIO Pin Setup ---
TRIG = 23  # Trigger pin
ECHO = 24  # Echo pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("Starting Distance Detection System...")
time.sleep(2)

def get_distance():
    # Send trigger pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10 microseconds
    GPIO.output(TRIG, False)

    # Wait for echo start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # Wait for echo end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate distance
    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 34300) / 2  # speed of sound 34300 cm/s

    return round(distance, 2)

try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist} cm")

        # Example alert conditions
        if dist < 10:
            print("🚨 WARNING! Object too close!")
        elif dist < 30:
            print("⚠️ Approaching obstacle...")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nStopping Distance Detection...")
    GPIO.cleanup()
