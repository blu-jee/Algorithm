'''
핵심포인트,구명보트에는 2명만 탈 수 있다.
2명 => 제일 무거운 사람 + 가장 가벼운 사람

시간초과 해결)
1. 큐로 접근하였을때, pop()으로 시간초과.
2. index로 이용할것.
'''


def solution(people, limit):
    people.sort()
    count = 0
    heavy = len(people)-1
    light = 0
    while light<=heavy:
        print(light, heavy)
        if limit-people[heavy] >= people[light]:
            light += 1
        heavy-=1
        count+=1

    return count
