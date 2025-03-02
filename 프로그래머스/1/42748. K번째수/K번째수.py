def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        s,e=commands[i][0]-1, commands[i][1]
        tmp=array[s:e]
        tmp.sort()
        answer.append(tmp[commands[i][2]-1])
                      
    return answer