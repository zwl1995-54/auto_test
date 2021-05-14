import yaml

with open("C:\\Users/Administrator/PycharmProjects/auto_test/parameterize/data_y1.yaml", "r", encoding="utf-8") as f:
    data = yaml.load(f)
    print(data)
# data2 = {"add": {"del": {"exe": {"value": "hello"}, "values": "走啊"}}}
# with open("C:\\Users/Administrator/PycharmProjects/auto_test/parameterize/data_y2.yaml", "w") as f:
#     yaml.dump(data2, f, encoding="utf-8", allow_unicode=True)
