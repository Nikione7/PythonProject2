def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        str_ = []
        matrix.append(str_)
        for j in range(m):
            str_.append(value)
    return matrix
print(get_matrix(2,3,5))
print(get_matrix(4,5,6))
print(get_matrix(5,2,9))