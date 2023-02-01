words = input()
answer = ''
for word in words:
    if word.isupper():
        answer += word.lower()
    else:
        answer += word.upper()
print(answer)