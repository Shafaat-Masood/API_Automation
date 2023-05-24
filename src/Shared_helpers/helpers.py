import json
import os
import logging as logger


def get_data_from_json(param, file=None):
    if not file:
        json_file_location = os.path.abspath(__file__).replace("Shared_helpers\\helpers.py", "configs") + "\\plan.json"
    else:
        json_file_location = os.path.abspath(__file__).replace("Shared_helpers\\helpers.py", "configs") + "\\" + file
    f = open(json_file_location, )
    data = json.load(f)
    return data[param]


def assign_data_to_json_file(param, value, file=None):
    if file:
        json_file_location = os.path.abspath(__file__).replace("Shared_helpers\\helpers.py",
                                                               "configs") + "\\" + file
        logger.critical("File name specified")
    else:
        json_file_location = os.path.abspath(__file__).replace("Shared_helpers\\helpers.py",
                                                               "configs") + "\\AuthToken.json"

        logger.critical("File name not specified")
    # f = open(json_file_location, )
    # data = json.load(f)
    kaido = {param: value}
    with open(json_file_location, 'w') as fp:
        json.dump(kaido, fp)
    pass
