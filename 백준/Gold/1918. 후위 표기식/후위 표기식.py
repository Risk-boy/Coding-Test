import sys
# sys.stdin = open("input.txt")

def push(item):
    return stack.append(item)

def pop():
    return stack.pop()

def is_empty():
    if not len(stack):
        return True
    else:
        return False


icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

data = input()
stack = list()
result = ''
for char in data:
    if char not in '+-*/()':    # 피연산자는 바로 result에 추가
        result += char
    else:   # 피연산자가 아니면
        if is_empty():  # 스택이 비어있다면 추가
            push(char)
        else:   # 스택에 무언가 있다면
            if char == ')': # 닫는 괄호면
                while stack[-1] != '(': # 여는 괄호 찾을때까지
                    result += pop() # 스택애들 팝해서 result에 추가
                pop()   # 여는 괄호 팝해서 날려버리기
            elif icp[char] > isp[stack[-1]]:    # 더 쎄면 추가
                push(char)
            else:   # 스택에 있는 아이보다 약하다면
                while icp[char] <= isp[stack[-1]]:  # 쎄질때까지
                    result += pop()     # 스택에 있는 애들 쫓아내서 result로
                    if is_empty():  # 스택에 있는 애들이 다 쎄서 다 쫓아버렸으면
                        break   # while 문 탈출
                push(char)  # 스택에 추가
while not is_empty():   # 스택에 아무것도 없을 때 까지
    result += pop()     # 팝해서 result 에 추가

print(result)