list = []

name1 = "张"
name2 = '李'
uname1 = "asdfghj"
uname2 = "qazwsxed"
phnum1 = "13404038110"
phnum2 = "13704038110"
emial1 = "pzq"
emial2 = "zwl"

for s in range(100):
    dict = {}
    print(s)
    if s%2 == 0:
        dict["name"] = name1 + 4 * str(s)
        dict["account"] = uname1 + str(s)
        if s < 10:
            dict["phnum"] = phnum1[0:10] + str(s)
        else:
            dict["phnum"] = phnum1[0:9] + str(s)
        dict["emial"] = emial1 + 4 * str(s) + "@163.com"
    else:
        dict["name"] = name2 + 4 * str(s)
        dict["account"] = uname2 + str(s)
        if s < 10:
            dict["phnum"] = phnum2[0:10] + str(s)
        if s >= 10:
            dict["phnum"] = phnum2[0:9] + str(s)
        dict["emial"] = emial2 + 4 * str(s) + "@qq.com"
    # print(dict)
    # 将数据存到list集合
    list.append(dict)
for i in range(100):
    print(list[i].get('name'))
