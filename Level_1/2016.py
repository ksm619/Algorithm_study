# 2016년

def solution(a, b):
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    day = 0
    for month in range(1, a):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
            day += 31
        if month == 2:
            day += 29
        if month == 4 or month == 6 or month == 9 or month == 11:
            day += 30
    day += (b - 1)
    answer = week[(5 + (day % 7)) % 7]
    return answer