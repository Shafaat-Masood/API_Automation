import logging as logger
import os

import pytest

from src.Shared_helpers.helpers import assign_data_to_json_file, get_data_from_json
from src.configs.hosts_config import API_HOSTS
from src.utilities.requestsUtility import RequestsUtility

trello_url = API_HOSTS[os.environ.get('ENV', 'dev')]
trello_userKey = API_HOSTS[os.environ.get('ENV', 'key')]
trello_APIToken = API_HOSTS[os.environ.get('ENV', 'token')]

# Method to create a Board, The values are similar to the one given in the demo api's
@pytest.mark.Production
@pytest.mark.tcid1
def test_1_Board_Create_Board():
    ru = RequestsUtility()
    logger.info("Request Hit Successfully")

    endpoint = "boards/"
    name = "Kaido"
    params = {
        "name": name,
        "key": trello_userKey,
        "token": trello_APIToken,
        "defaultLists": "false"
    }
    fyp = trello_url + endpoint
    res = ru.post(endpoint=endpoint, payload=params, expected_status_code=200)
    Board_id = res['id']
    assign_data_to_json_file("BoardId", Board_id, file="plan.json")
    assert res['name'] == name
    return Board_id


@pytest.mark.Production
@pytest.mark.tcid2
def test_2_Board_create_ToDoList():
    ru = RequestsUtility()
    BoardID = get_data_from_json("BoardId", file="plan.json")
    if not BoardID:
        BoardID=test_1_Board_Create_Board()
    logger.info("Request Hit Successfully")
    endpoint = "lists/"
    name = "ToDo"
    params = {
        "name": name,
        "idBoard": BoardID,
        "key": trello_userKey,
        "token": trello_APIToken
    }
    res = ru.post(endpoint=endpoint, payload=params, expected_status_code=200)
    ToDo_id = res['id']
    assign_data_to_json_file("To_Do", ToDo_id, file="toDo.json")
    assert res['name'] == name
    return ToDo_id


@pytest.mark.Production
@pytest.mark.tcid3
def test_3_Board_create_Done_List():
    ru = RequestsUtility()
    BoardID = get_data_from_json("BoardId", file="plan.json")
    if not BoardID:
        BoardID=test_1_Board_Create_Board()
    logger.info("Request Hit Successfully")
    endpoint = "lists/"
    name = "Done"
    params = {
        "name": name,
        "idBoard": BoardID,
        "key": trello_userKey,
        "token": trello_APIToken
    }
    res = ru.post(endpoint=endpoint, payload=params, expected_status_code=200)
    Done_List_id = res['id']
    assign_data_to_json_file("Done_List", Done_List_id, file="Done.json")
    assert res['name'] == name
    return Done_List_id


@pytest.mark.Production
@pytest.mark.tcid4
def test_4_Board_create_Card_in_Todo_List():
    ru = RequestsUtility()
    ToDoList_ID = get_data_from_json("To_Do", file="toDo.json")
    endpoint = "cards/"
    name = "Learning Postman"
    params = {
        "name": name,
        "idList": ToDoList_ID,
        "key": trello_userKey,
        "token": trello_APIToken
    }
    res = ru.post(endpoint=endpoint, payload=params, expected_status_code=200)
    card = res['id']
    assign_data_to_json_file("card", card, file="card.json")
    assert res['name'] == name
    return card


@pytest.mark.Production
@pytest.mark.tcid5
def test_5_Board_Move_Card_in_Done_List():
    ru = RequestsUtility()
    card_ID = get_data_from_json("card", file="card.json")
    Done_List_ID = get_data_from_json("Done_List", file="Done.json")
    endpoint = f"cards/{card_ID}"
    params = {
        "idList": Done_List_ID,
        "key": trello_userKey,
        "token": trello_APIToken
    }
    res = ru.put(endpoint=endpoint, payload=params, expected_status_code=200)
    card = res['id']
    assign_data_to_json_file("card", card, file="card.json")
    return card


@pytest.mark.Production
@pytest.mark.tcid6
def test_6_Board_Delete_Board():
    ru = RequestsUtility()
    Board_ID = get_data_from_json("BoardId", file="plan.json")
    endpoint = f"boards/{Board_ID}"
    params = {
        "key": trello_userKey,
        "token": trello_APIToken
    }
    res = ru.delete(endpoint=endpoint, payload=params, expected_status_code=200)


@pytest.mark.Production
@pytest.mark.tcid7
def test_7_Board_retrieve_Deleted_Board():
    ru = RequestsUtility()
    Board_ID = get_data_from_json("BoardId", file="plan.json")
    endpoint = f"boards/{Board_ID}"
    params = {
        "key": trello_userKey,
        "token": trello_APIToken
    }
    res = ru.get(endpoint=endpoint, payload=params, expected_status_code=404)
    """
        In Trello there are two options with which a board can be deleted,
        1. Temporary Delete and the 2. one is permanent delete so in test case 6 
        we are deleting the board permanently so we cannot retrieve a permanently deleted board.
        So the status code for the above api would be 404, against which the epected code is also 404 given.
    """

