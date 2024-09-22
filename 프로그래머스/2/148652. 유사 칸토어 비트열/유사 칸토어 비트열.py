def get_cnt_1(n, l, r):
    if n == 1:
        return "11011"[l:r + 1].count("1")

    ranges = []

    for i in range(5):
        ranges.append(range(i * 5 ** (n - 1), (i + 1) * 5 ** (n - 1)))

    ret = 0
    for i in range(len(ranges)):
        if ranges[i].start == 2 * 5 ** (n - 1):
            continue

        # 완전 포함
        if l <= ranges[i].start and r >= ranges[i].stop:
            ret += get_cnt_1(n - 1, 0, 5 ** (n - 1) - 1)
        # 부분 포함
        elif l <= ranges[i].start and ranges[i].start <= r < ranges[i].stop:
            ret += get_cnt_1(n - 1, 0, r - ranges[i].start)
        elif ranges[i].stop >= l > ranges[i].start and r >= ranges[i].stop:
            ret += get_cnt_1(n - 1, l - ranges[i].start, 5 ** (n - 1) - 1)
        elif l > ranges[i].start and r < ranges[i].stop:
            ret += get_cnt_1(n - 1, l - ranges[i].start, r - ranges[i].start)

    return ret

def solution(n, l, r):
    ret = get_cnt_1(n, l - 1, r - 1)
    return ret