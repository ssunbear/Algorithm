
def solution(numbers):
    answer = ''
    answer=[str(x) for x in numbers]
    answer.sort(key=lambda x:x*4, reverse=True)
    
    if answer.count('0')==len(answer):
        return '0'
    
    return ''.join(answer)