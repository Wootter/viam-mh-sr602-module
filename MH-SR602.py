from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(17)  # GPIO17 (Pin 11)

print("PIR sensor warming up... (about 1 minute)")
pir.wait_for_inactive()  # <-- newer method name
print("Ready! Waiting for motion...")

def on_motion():
    print("Motion detected!")

def on_no_motion():
    print("No motion detected.")

pir.when_activated = on_motion
pir.when_deactivated = on_no_motion

pause()
