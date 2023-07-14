Automation Framework - Trello API Automation

This framework focuses on automating various Trello APIs. It offers an efficient way to interact with Trello, automate tasks, and perform seamless testing. Below are the details regarding the framework setup, execution, and the specific Trello APIs that have been automated.

Trello APIs Automated:

- test_1_Board_Create_Board
- test_2_Board_Create_ToDoList
- test_3_Board_Create_DoneList
- test_4_Board_Create_CardinToDoList
- test_5_Board_Move_Card_in_DoneList
- test_6_Board_Delete_Board
- test_7_Board_Retrieve_Deleted_Board

Setup Instructions:

1. Ensure that Python is installed on your system.
2. Set up PyCharm IDE on your Windows machine.
3. Open PyCharm, click on "File" > "Open Projects from File System," and navigate to the framework directory.
4. Import the framework into PyCharm and run the following command in your terminal:
   ```
   pip install -r requirements.txt
   ```
5. Verify that the required libraries are installed after running the command:
   - requests==2.28.2
   - pytest==7.2.2
   - request_oauthlib==1.3.1
   - pytest-html==3.2.0

Running the Framework:

To execute the framework and run the Trello API automated test cases, use the following command:
```
pytest -k Production --html=report.html
```

Framework Highlights:

- JSON Files: Consider storing all relevant values, such as Todo list ID, done list ID, and other values, in a single file for improved readability.
- RAR File: Extract the provided RAR file and save the project on your system.
- Assertions: Assertions have been implemented throughout the framework, primarily focusing on validating the received status codes, as no specific requirements were mentioned.
- Naming Convention: Method names are chosen to be descriptive, enhancing the code's readability.
- Comments: Comments are strategically placed throughout the project to improve code comprehension and maintainability.
