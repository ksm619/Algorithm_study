record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

record = [x.split(" ") for x in record]

online = []
result = ""
for i in range(len(record)):
    if "Enter" in record[i]:
        result += "%s님이 들어왔습니다. %s " % (record[i][2], record[i][1])
        online.append([record[i][1], record[i][2]])
        print("online", online)
    elif "Leave" in record[i]:
        for j in range(len(online)):
            if record[i][1] in online[j]:
                result += "%s님이 나갔습니다. %s " % (online[j][1], online[j][0])
        # online = online.replace()
    elif "Change" in record[i]:
        result += "%s님이 변경하였습니다. %s " % (record[i][2], record[i][1])
        for k in range(i):
            if record[i][1] in


print(result)
