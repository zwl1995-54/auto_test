import os

import yaml


def analyze_file(file_name, data_key):
    # with open("C:\\Users\\Administrator\\PycharmProjects\\auto_test\\auto_pytest\\PO\data/" + file_name, "r",
    with open("C:\\Users\\Administrator\\PycharmProjects\\auto_test\\auto_pytest\\PO" + os.sep + "data" + os.sep + file_name, "r", encoding="utf-8") as f:
        data = yaml.load(f)
        data_dict = data[data_key]
        list_data = []
        for i in data_dict.values():
            list_data.append(i)
        return list_data
