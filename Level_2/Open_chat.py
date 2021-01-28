record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

record = [x.split(" ") for x in record]

online = []
result = ""
for i in range(len(record)):
    if "Enter" in record[i]:
        result += "%s님이 들어왔습니다. %s \n" % (record[i][2], record[i][1])
        online.append([record[i][1], record[i][2]])
    elif "Leave" in record[i]:
        for j in range(len(online)):
            if record[i][1] in online[j]:
                result += "%s님이 나갔습니다. %s \n" % (online[j][1], online[j][0])
                break
        del online[j]

    elif "Change" in record[i]:
        result += "%s님이 변경하였습니다. %s \n" % (record[i][2], record[i][1])
        for j in range(len(result)):
        
            if record[i][1] in result[j]:
                result[j] = result[j].replace(record[j][2], record[i][2])

    # print('online', online)
    # print(result)
print(result)




# Muzi님이 들어왔습니다.     Muzi님이 들어왔습니다.     Prodo님이 들어왔습니다.         Prodo님이 들어왔습니다.
# Prodo님이 들어왔습니다     Prodo님이 들어왔습니다.    Prodo님이 들어왔습니다.         Ryan님이 들어왔습니다.
#                           Muzi님이 나갔습니다.       Prodo님이 나갔습니다.           Prodo님이 나갔습니다.
#                                                     Prodo님이 들어왔습니다.         Prodo님이 들어왔습니다