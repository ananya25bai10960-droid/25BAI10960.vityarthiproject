def spiral(size):
    matrix = [[" " for _ in range(size)] for _ in range(size)]
    left, right = 0, size - 1
    top, bottom = 0, size - 1
    ch = "*"
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = ch
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = ch
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = ch
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = ch
            left += 1
    for row in matrix:
        print(" ".join(row))
