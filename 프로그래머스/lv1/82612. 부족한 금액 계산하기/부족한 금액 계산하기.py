def solution(price, money, count):
    total = (count + 1) * count // 2 * price
    answer = 0
    if money < total:
        answer = total - money
    else:
        answer = 0

    return answer