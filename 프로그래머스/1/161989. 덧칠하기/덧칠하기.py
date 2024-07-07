def solution(n, m, section):
    answer = 0
    while section:
        if len(section) > 0:
            next_pos = section[0] + m
            while section and section[0] < next_pos:
                section.pop(0) # O(N)
            answer += 1
    return answer

