data = []

file_list = ["text\\"+str(x)+".txt" for x in range(1, 11)]

for file_name in file_list:
    print(file_name)
    file = open(file_name, 'r', encoding='utf-8').readlines()
    for x in file:
        x = x.strip()
        tmp = x.split(' ')
        if "name" in tmp[0].lower():
            try:
                if tmp[1] == ":":
                    data.append({"name": " ".join(tmp[2:]).lower()})
                else:
                    data.append({"name": " ".join(tmp[1:]).lower()})
            except:
                data.append({"name": "-"})
        elif "ather" in tmp[0].lower():
            try:
                if tmp[2] == ":":
                    data[-1].update({"0f1h": "0", "relname": " ".join(tmp[3:]).lower()})
                else:
                    data[-1].update({"0f1h": "0", "relname": " ".join(tmp[2:]).lower()})
            except:
                data[-1].update({"0f1h": "0", "relname": "-"})
        elif "usband" in tmp[0].lower():
            try:
                if tmp[2] == ":":
                    data[-1].update({"0f1h": "1", "relname": " ".join(tmp[3:]).lower()})
                else:
                    data[-1].update({"0f1h": "1", "relname": " ".join(tmp[2:]).lower()})
            except:
                data[-1].update({"0f1h": "1", "relname": "-"})
        elif ("ouse" in tmp[0].lower()) and ("umber" in x.lower()):
            try:
                if tmp[2] == ":":
                    data[-1].update({"house": tmp[3]})
                else:
                    data[-1].update({"house": tmp[2]})
                try:
                    rand = int(data[-1]["house"])
                except:
                    data[-1]["house"] = "-"
            except:
                data[-1].update({"house": "-"})
        elif ("age" in tmp[0].lower()) and ("gender" in x):
            if tmp[1] == ":":
                try:
                    if tmp[4] == ":":
                        data[-1].update({"age": tmp[2].lower(), "gender": tmp[5].strip(' ').lower()})
                    else:
                        data[-1].update({"age": tmp[2].lower(), "gender": tmp[4].strip(' ').lower()})
                except:
                    data[-1].update({"age": tmp[2].lower(), "gender": "-"})
            else:
                try:
                    if tmp[3] == ":":
                        data[-1].update({"age": tmp[1].lower(), "gender": tmp[4].strip(' ').lower()})
                    else:
                        data[-1].update({"age": tmp[1].lower(), "gender": tmp[3].strip(' ').lower()})
                except:
                    data[-1].update({"age": tmp[1].lower(), "gender": "-"})

print(data)
data_file = open("data.txt", "w", encoding="utf-8")
data_file.close()
data_file = open("data.txt", "a", encoding="utf-8")
for person in data:
    for details in list(person.values()):
        data_file.write(details+'\n')
    data_file.write('\n')
data_file.close()

