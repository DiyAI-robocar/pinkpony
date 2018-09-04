"""
CAR CONFIG

This file is read by your car application's manage.py script to change the car
performance.

EXMAPLE
-----------
import dk
cfg = dk.load_config(config_path='~/mycar/config.py')
print(cfg.CAMERA_RESOLUTION)

"""


import os

#PATHS
CAR_PATH = PACKAGE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(CAR_PATH, 'data')
MODELS_PATH = os.path.join(CAR_PATH, 'models')

#VEHICLE
DRIVE_LOOP_HZ = 20
MAX_LOOPS = 100000

#CAMERA
CAMERA_RESOLUTION = (120, 160) #(height, width)
CAMERA_FRAMERATE = DRIVE_LOOP_HZ

#STEERING
STEERING_CHANNEL = 0
STEERING_LEFT_PWM = 450
STEERING_RIGHT_PWM = 270

#THROTTLE
THROTTLE_CHANNEL = 1
THROTTLE_FORWARD_PWM = 413 # min forward 
THROTTLE_STOPPED_PWM = 410
THROTTLE_REVERSE_PWM = 381 # min backward

#TRAINING
BATCH_SIZE = 128
TRAIN_TEST_SPLIT = 0.8


#JOYSTICK
USE_JOYSTICK_AS_DEFAULT = False
JOYSTICK_STEERING_AXIS = 'x'
JOYSTICK_STEERING_SCALE = 1.0
JOYSTICK_THROTTLE_AXIS = 'ry'
JOYSTICK_MAX_THROTTLE = 1.0
JOYSTICK_THROTTLE_SCALE = -1.0
#AUTO_RECORD_ON_THROTTLE = True
AUTO_RECORD_ON_THROTTLE = False


TUB_PATH = os.path.join(CAR_PATH, 'tub') # if using a single tub

#ROPE.DONKEYCAR.COM
ROPE_TOKEN="GET A TOKEN AT ROPE.DONKEYCAR.COM"
