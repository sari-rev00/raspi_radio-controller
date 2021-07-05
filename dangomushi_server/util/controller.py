# -*- coding: utf-8 -*-
try:
    import RPi.GPIO as GPIO
except:
    print("module RPi.GPIO can't import")
import time


# pin configration ===
AIN1 = 6
AIN2 = 5
PWMA = 12

STBY = 16

BIN1 = 20
BIN2 = 26
PWMB = 18

LIST_PIN_OUT_BCM = [
    AIN2, AIN1, PWMA,
    BIN1, BIN2, PWMB,
    STBY
]

class Controller():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        for pin in LIST_PIN_OUT_BCM:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        return None
    
    def __del__(self):
        self.mot_A_stop()
        GPIO.cleanup()
        return None
    
    def mot_A_stop(self):
        # STBY -> H
        GPIO.output(STBY, GPIO.HIGH)
        # AIN1 -> L
        GPIO.output(AIN1, GPIO.LOW)
        # AIN2 -> L
        GPIO.output(AIN2, GPIO.LOW)
        # PWMA-> H
        GPIO.output(PWMA, GPIO.HIGH)
        return None
    
    def mot_A_ccw(self):
        # STBY -> H
        GPIO.output(STBY, GPIO.HIGH)
        # AIN1 -> L
        GPIO.output(AIN1, GPIO.LOW)
        # AIN2 -> H
        GPIO.output(AIN2, GPIO.HIGH)
        # PWMA-> H
        GPIO.output(PWMA, GPIO.HIGH)
        return None
    
    def mot_A_cw(self):
        # STBY -> H
        GPIO.output(STBY, GPIO.HIGH)
        # AIN1 -> H
        GPIO.output(AIN1, GPIO.HIGH)
        # AIN2 -> L
        GPIO.output(AIN2, GPIO.LOW)
        # PWMA-> H
        GPIO.output(PWMA, GPIO.HIGH)
        return None

    def mot_B_stop(self):
        # STBY -> H
        GPIO.output(STBY, GPIO.HIGH)
        # AIN1 -> L
        GPIO.output(BIN1, GPIO.LOW)
        # AIN2 -> L
        GPIO.output(BIN2, GPIO.LOW)
        # PWMA-> H
        GPIO.output(PWMB, GPIO.HIGH)
        return None
    
    def mot_B_ccw(self):
        # STBY -> H
        GPIO.output(STBY, GPIO.HIGH)
        # BIN1 -> L
        GPIO.output(BIN1, GPIO.LOW)
        # BIN2 -> H
        GPIO.output(BIN2, GPIO.HIGH)
        # PWMB-> H
        GPIO.output(PWMB, GPIO.HIGH)
        return None
    
    def mot_B_cw(self):
        # STBY -> H
        GPIO.output(STBY, GPIO.HIGH)
        # BIN1 -> H
        GPIO.output(BIN1, GPIO.HIGH)
        # BIN2 -> L
        GPIO.output(BIN2, GPIO.LOW)
        # PWMB-> H
        GPIO.output(PWMB, GPIO.HIGH)
        return None

    def stop(self):
        print("stop")
        self.mot_A_stop()
        self.mot_B_stop()
        return None
    
    def forward(self):
        print("forward")
        self.mot_A_ccw()
        self.mot_B_ccw()
        return None
    
    def backward(self):
        print("backward")
        self.mot_A_cw()
        self.mot_B_cw()
        return None
    
    def rotate_right(self):
        print("rotate_right")
        self.mot_A_cw()
        self.mot_B_ccw()
        return None
    
    def rotate_left(self):
        print("rotate_left")
        self.mot_A_ccw()
        self.mot_B_cw()
        return None


class TestController():
    def __init__(self):
        return None
    
    def stop(self):
        print("test: stop")
        return None
    
    def forward(self):
        print("test: forward")
        return None
    
    def backward(self):
        print("test: backward")
        return None
    
    def rotate_right(self):
        print("test: rotate_right")
        return None
    
    def rotate_left(self):
        print("test: rotate_left")
        return None