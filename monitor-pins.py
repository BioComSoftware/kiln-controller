#! /usr/bin/env python3
import RPi.GPIO as GPIO
import sys
import argparse

def edge_detected(channel):
    print(f"Edge detected on channel {channel}")


if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Monitor selected pins for activity')
    parser.add_argument('-p','--pins', nargs='+', required=True)
    args = vars(parser.parse_args())
    pinslist = args["pins"]
    print("args=", args)
    print("pinslist =", pinslist)
        
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_to_monitor, GPIO.IN)
    GPIO.add_event_detect(pin_to_monitor, GPIO.BOTH, callback=edge_detected)
    
    try:
        # Keep your program running to keep the callback active
        message = input("Press enter to quit\n\n")
    finally:
        GPIO.cleanup()
    