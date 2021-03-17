# RobotTracking

I am still cleaning up the code. For the model, you can train your own as mine is for Robomaster competition.

prerequisite:
I assume the detectnet is working using Dusty code
https://github.com/dusty-nv/jetson-inference

Here are the hardware requirement
- 4 servos (pan/tilt servo x 2 pairs)
- 2 camera pan/tilt structures
- 1 PCA9685 servo controller
- female to female jumper cables
- 2 rpi camera ver 2

Reference:
And I've combined the code with Paul McWhorter (He has a great jetson nano video playlist)
https://youtu.be/8YKAtpPSEOk?list=PLGs0VKk2DiYxP-ElZ7-QXIERFFPkOuP4_

Procedure
Go to jetson-inference/python/training/detection/ssd
Copy my code into the same ssd folder

Then run these two commands

cd ~
cd jetson-inference/python/training/detection/ssd
NET=models/robot
python3 detectnet_andy.py --model=$NET/ssd-mobilenet.onnx --labels=$NET/labels.txt           --input-blob=input_0 --output-cvg=scores --output-bbox=boxes             csi://0

#another terminal

cd ~
cd jetson-inference/python/training/detection/ssd
NET=models/robot
python3 detectnet_andy_2nd_cam.py --model=$NET/ssd-mobilenet.onnx --labels=$NET/labels.txt           --input-blob=input_0 --output-cvg=scores --output-bbox=boxes             csi://1

