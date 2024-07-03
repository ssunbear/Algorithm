def solution(plans):
    answer=[]
    now=[]
    plans.sort(key=lambda x:x[1])
    for i in range(len(plans)):
        plans[i][1]=int(plans[i][1][0:2])*60+int(plans[i][1][3:])
        plans[i][2]=int(plans[i][2])
        
    for i in range(len(plans)-1):
        now.append(plans[i])
        diff=plans[i+1][1]-plans[i][1]
        while now and diff:
            if now[-1][2]<=diff:
                diff-=now[-1][2]
                answer.append(now[-1][0])
                now.pop()
            else: 
                now[-1][2]-=diff
                diff=0
    
    answer.append(plans[-1][0])
    while now:
        answer.append(now[-1][0])
        now.pop(-1)
    return answer