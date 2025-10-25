import RPi.GPIO as GPIO
import time

BUZZER = 18
LED_RED = 17
LED_YELLOW = 27

GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)

def handle_alert(distance):
    GPIO.output(LED_RED, False)
    GPIO.output(LED_YELLOW, False)
    GPIO.output(BUZZER, False)

    if distance < 10:
        GPIO.output(LED_RED, True)
        GPIO.output(BUZZER, True)
        print("🚨 DANGER: Object too close!")
    elif distance < 30:
        GPIO.output(LED_YELLOW, True)
        GPIO.output(BUZZER, True)
        time.sleep(0.1)
        GPIO.output(BUZZER, False)
        print("⚠️ Warning: Approaching obstacle.")
