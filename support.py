def get_roots(a, b, c, d):
    answer = []
    if d > 0:
        x1 = (-b + d ** 0,5) / (2 * a)
        answer.append(x1)
        x2 = (-b - d ** 0,5) / (2 * a)
        answer.append(x2)
    elif discr == 0:
        x = -b / (2 * a)
        answer.append(x)
    return answer
