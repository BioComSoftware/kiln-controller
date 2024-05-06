#! /usr/bin/env python3
import RPi.GPIO as GPIO
import time
from multiprocessing import Process

# List of GPIO pins to monitor
pinlist = [
3,
5,
7,
11,
13,
15,
19,
##27,
31,
33,
35,
37,
8,
10,
12,
##16,
18,
22,
##24,
##26,
##28,
32,
36,
38,
40
]  # Example pins

def edge_detected(channel):
    print(f"Edge detected on channel {channel}")

def monitor_pin(pin):
    print(f"Starting monitoring for pin {pin}")
    try: 
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN)
        GPIO.add_event_detect(pin, GPIO.BOTH, callback=edge_detected)
        # Keep the process running to monitor the pin
        try:
            while True:
                time.sleep(1)
        finally:
            GPIO.cleanup(pin)
    
    except Exception as e:
        print(f"ERROR: Halting thread for {pin} due to {e}")
                
if __name__ == "__main__":
    # Create and start a separate process for each pin to be monitored
    processes = []
    for pin in pinlist:
        p = Process(target=monitor_pin, args=(pin,))
        processes.append(p)
        p.start()

    # Join all processes to ensure they keep running
    for process in processes:
        process.join()
