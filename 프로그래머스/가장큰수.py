def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)

    return str(int(''.join(numbers))) #오버플로우 방지 코드 ex.'0000'


m = solution([3, 30, 34, 5, 9])
print(type(m))