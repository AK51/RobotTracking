#!/usr/bin/python3
#
# Copyright (c) 2020, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#
import jetson.inference
import jetson.utils

import argparse
import sys

#import cv2
#import numpy as np
import time
from adafruit_servokit import ServoKit

kit=ServoKit(channels=16)

pan1=90
tilt1=160
pan_max = 180
pan_min = 0
tilt_max = 180
tilt_min = 70

kit.servo[2].angle=pan1
kit.servo[3].angle=tilt1
#width=720
#height=480
#work a little
#width=1024
#height=768
width=1280
height=720
flip=2
Area = 0
error_tolerance = 100
objX = width/2
objY = height/2
# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
    opt = parser.parse_known_args()[0]
except:
    print("")
    parser.print_help()
    sys.exit(0)

# load the object detection network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)

# create video sources & outputs
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)

# process frames until the user exits
while True:
    # capture the next image
    img = input.Capture()

    # detect objects in the image (with overlay)
    detections = net.Detect(img, overlay=opt.overlay)

    # print the detections
#	print("detected {:d} objects in image".format(len(detections)))
    objX = width/2
    objY = height/2
    Area = 0
    for detection in detections:
        print(detection)
#        print("detection.Center = "),
#        print(detection.Center)
#        print("width = "),
#        print(width),
#        print(" height = "),
#        print(height)
        print("Center_x = "),
        print(detection.Center[0]),
        print(" Center_y = "),
        print(detection.Center[1])
        print("detection.Area = "),
        print(detection.Area)
		
        if(int(detection.Area) > Area):
            Area = int(detection.Area)
            objX= detection.Center[0]
            objY= detection.Center[1]
#        objY= 90
#        objX= 90

    errorPan1= objX - (width/2)
    errorTilt1= objY - (height/2)
    print("errorPan1 = "),
    print(errorPan1),
    print(" errorTilt1 = "),
    print(errorTilt1)
    if abs(errorPan1)>error_tolerance:
        pan1=pan1-errorPan1/100
#reverse
#        pan1=pan1+errorPan1/40
    if abs(errorTilt1)>error_tolerance:
        tilt1=tilt1+errorTilt1/100
#reverse
#        tilt1=tilt1-errorTilt1/40
    if pan1>pan_max:
        pan1=pan_max
    if pan1<pan_min:
        pan1=pan_min
    if tilt1>tilt_max:
        tilt1=tilt_max
    if tilt1<tilt_min:
        tilt1=tilt_min
    print("pan1 = "),
    print(pan1),
    print("tilt1 = "),
    print(tilt1)
    kit.servo[2].angle=pan1
    kit.servo[3].angle=tilt1
#    kit.servo[0].angle=90
#    kit.servo[1].angle=90



    # render the image
    output.Render(img)

    # update the title bar
    output.SetStatus("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))

    # print out performance info
#	net.PrintProfilerTimes()

    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break



