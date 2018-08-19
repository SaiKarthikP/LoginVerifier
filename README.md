Windows Login Verifier using Face recognition module and OpenCV

Descrition
----
This python script verifies if the user is indeed the person in 'IDs/p1.jpg' within seconds via face recognition using the attached webcam. If not, the user will be locked out of the system. A 3 second video of the intruder will also be saved in the 'intruders' directory.

How to setup and run the python script in Anaconda
----
1. Insert a picture of you under IDs and name the file 'p1.jpg'. Enter your name in 'people.txt' (This step is not required and can be 'user' as default.)
2. Open Anaconda Prompt and cd to directory containing 'LoginVerifier.py'
3. compile and run using command 'python LoginVerifier.py'
4. Alternatively this script can be run on any Python IDE

How to setup script on Task Scheduler to start on system login in Windows 10
----
1. Open 'Task Scheduler' under Control Panel\System and Security\Administrative Tools on Windows PC
2. Click on 'Task Scheduler Library' in the left panel. 
3. Click on 'Create Task...' on right panel and enter a Name for the task. 
4. In the Triggers tab, click 'New...', choose 'On workstation unlock' and click 'OK;.
5. In the Actions tab, click 'New...', choose 'Start a program' and do the following: 
	a. Program/script: insert path to python.exe
	b. Add argument: LoginVerifier.py
	c. Start in: insert path to directory where script is saved
	d. Click 'OK'

Required Libraries
----
face_recognition - facial recognition api for Python built using Dlib 
https://github.com/ageitgey/face_recognition

OpenCV - Computer Vision library implemented in C++
https://opencv.org/


Notes
----
Dlib - modern C++ toolkit containing machine learning algorithms 
https://github.com/davisking/dlib