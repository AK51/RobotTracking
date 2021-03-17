# RobotTracking

![github5](https://user-images.githubusercontent.com/8468724/111451478-6fed0280-874c-11eb-9dc3-e802d50127a3.jpg)
![github6](https://user-images.githubusercontent.com/8468724/111451600-914dee80-874c-11eb-971f-988e421e25d9.jpg)



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
And I've combined the code with Paul McWhorter code (He has a great jetson nano video playlist)
https://youtu.be/8YKAtpPSEOk?list=PLGs0VKk2DiYxP-ElZ7-QXIERFFPkOuP4_

The whole idea is to get the center point of the largest object and use the servo to track it. The trick is that the servo should be sensitve but not vibrating. The tuning of the control parameter can takes up to an hour.


Here are some pictures of the wiring
![github1](https://user-images.githubusercontent.com/8468724/111451654-9f9c0a80-874c-11eb-97bf-467656d42689.jpg)
![github2](https://user-images.githubusercontent.com/8468724/111451656-a165ce00-874c-11eb-9e31-57d56eecc5a5.jpg)
![github3](https://user-images.githubusercontent.com/8468724/111451661-a1fe6480-874c-11eb-9063-137ab58a6988.jpg)
![github4](https://user-images.githubusercontent.com/8468724/111451663-a296fb00-874c-11eb-9255-3270694aacd4.jpg)



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

