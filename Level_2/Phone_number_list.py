# 전화번호 목록

def solution(phone_book):
    config = 0
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if len(phone_book[i]) <= len(phone_book[j]) and phone_book[i] in phone_book[j][:len(phone_book[i])] and i != j:
                answer = False
                config = 1
                break
            elif len(phone_book[j]) < len(phone_book[i]) and phone_book[j] in phone_book[i][:len(phone_book[j])] and i != j:
                answer = False
                config = 1
                break
        if config == 1:
            break
    return answer