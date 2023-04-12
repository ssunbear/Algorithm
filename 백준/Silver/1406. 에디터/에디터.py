import sys
#(참신한 풀이) 커서를 기준으로 문자열을 스택두개에 나눠 담는 방법
st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
            
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':
        if st1:
            st1.pop()
            
    else:
        st1.append(command[1])
        
st1.extend(reversed(st2))
print(''.join(st1))