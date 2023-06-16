Automation Framework

Trello Api’s

JSON Files
    1.  Current each value like Todo list ID, done list id and other values are stored in each different files but they can also be stored in a single file. Just wanted to increase Readability.


RAR File
    2.  Extract the rar file and store the project in your system.

Setup

    1. Make sure Python is installed in your System.
    2. Setup Pycharm IDE in your Windows Machine.
    3. Now click on File > Open Projects from File System Then navigate to your framework and open it in your ID.
    4. After importing the Project, run the provided command in your terminal.
                                           pip install -r requirements.txt
    5. Make sure the following libraries are installed after you have run the command.
	requests==2.28.2
	pytest==7.2.2
	request_oauthlib==1.3.1
	pytest-html==3.2.0

Assertions

Assertions is applied throughout the framework. Mostly on the status code received as there were no requirement mentioned.


Which Language and Tool used?

Python is used. Along with the implementation of Pytest, request,etc libraries


How to Run framework?

The framework should be run using the command:-

	pytest -k Production –html=report.html




Naming Convention

Method Names are detailed hence improving readability of the code.


Comments

Throughout the project Comments have been placed to increase code readability.

Automated Test Cases
Following are the test cases that have been automated:

1. test_1_Board_Create_Board
2. test_2_Board_Create_ToDoList
3. test_3_Board_Create_DoneList
4. test_4_Board_Create_CardinToDoList
5. test_5_Board_Move_Card_in_DoneList
6. test_6_Board_Delete_Board
7. test_7_Board_Retrieve_Deleted_Board
