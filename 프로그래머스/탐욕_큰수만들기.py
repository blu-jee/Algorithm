def solution(number, k):
    stack = [number[0]]
    for n in number[1:]:
        while stack and n > stack[-1] and k>0:
                stack.pop()
                k -= 1

        stack.append(n)
    if k!=0:
        stack = stack[:-k]

    return ''.join(stack)


