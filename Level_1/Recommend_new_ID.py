# 신규 아이디 추천

def solution(new_id):
    new_id = new_id.lower()

    temp = ''
    for i in new_id:
        if i == '-' or i == '_' or i == '.' or i.isalpha() or i.isdigit():
            temp += i
    new_id = temp

    for i in range(len(new_id)//2):
        new_id = new_id.replace("..", ".")

    if new_id[0] == ".":
        new_id = new_id[1:]
    if new_id[-1:] == ".":
        new_id = new_id[:-1]
    if new_id == "":
        new_id += "a"

    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1:] == ".":
            new_id = new_id[:-1]

    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id