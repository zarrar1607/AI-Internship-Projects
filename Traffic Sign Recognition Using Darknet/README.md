# _Traffic Sign Recognition System_

- _Rameet Sekhon_
- _rameet.sekhon@uoit.net_
- _Thagshan Mohanarathnam_
- _thagshan.mohanarathnam@uoit.net_

## About the system

> _This system run on the darknet framework with YOLO. It has a fully annotated dataset with the relevant weights file. It is trained on 10 classes found in obj.names. It can take a live feed and detect road signs._


## How to run
> You are required to download and install darknet from: https://github.com/AlexeyAB/darknet/releases

> Replace the folders in the path with the folders in the repository

> Follow this link to download the demo video used to test the program. Store this video on the root folder along with yoloDetect. Alternatively you can proved your own video as a parameter: https://drive.google.com/file/d/1HkhFqIpk8i3TBouuawpNGPeMpEhRsTOe/view?usp=sharing

> The program takes multiple parameters to run. Simply running the program as such will initialize the webcam and begin detection over the signs dataset

```
python .\yoloDetect.py
```
> To run it with the video supply this command

```
python .\yoloDetect.py -v .\demo1.mp4
```
