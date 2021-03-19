# RobotTracking

Youtube Demo video
https://youtu.be/5mjPr2e_6sY

![github5](https://user-images.githubusercontent.com/8468724/111451478-6fed0280-874c-11eb-9dc3-e802d50127a3.jpg)
![github6](https://user-images.githubusercontent.com/8468724/111451600-914dee80-874c-11eb-971f-988e421e25d9.jpg)


I am still cleaning up the code. For the model, you can train your own as mine is for Robomaster competition. https://www.robomaster.com/en-US
The code is tested in my Nvidia Xiaver NX, and it will work on nano too. The fps can go up to 200.

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
Copy my code into the same ssd folder (github has 25Mb limit...)
https://drive.google.com/drive/folders/13qB9RhnMC-AKEtlUMmfBfmPJEQiczuAM?usp=sharing
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



Happy coding with Jetson
![IMG_20210317_182500](https://user-images.githubusercontent.com/8468724/111453213-49c86200-874e-11eb-8c4d-fc011bbab895.jpg)

Designing a new onmi-wheel robot using Nvidia Nano for an undergrad. class. Coming Soon!
![IMG_20210127_161254](https://user-images.githubusercontent.com/8468724/111727588-20bae500-88a6-11eb-8a4e-ff7a0e559338.jpg)
![IMG_20210126_143021](https://user-images.githubusercontent.com/8468724/111727689-5790fb00-88a6-11eb-8712-a4d181fab605.jpg)
Upgaded with arms and fingers
![IMG_20210319_122314](https://user-images.githubusercontent.com/8468724/111731304-21577980-88ae-11eb-85ac-a5001ccab36f.jpg)
![IMG_20210319_122245](https://user-images.githubusercontent.com/8468724/111731309-23b9d380-88ae-11eb-8d71-a73574f8ad66.jpg)
![IMG_20210319_122250](https://user-images.githubusercontent.com/8468724/111731310-23b9d380-88ae-11eb-98e0-62f4e8b81fdd.jpg)



