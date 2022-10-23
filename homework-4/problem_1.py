matrix = [[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]


def search_in_matrix(matrix, target):
    for index1, value1 in enumerate(matrix):
        for index2, value2 in enumerate(value1):
            if value2 == target:
                return [index1, index2]
    return [-1, -1]

print(search_in_matrix(matrix, 1004))
print(search_in_matrix(matrix, 44))
print(search_in_matrix(matrix, 1005))
print(search_in_matrix(matrix, 128))
print(search_in_matrix(matrix, 1056))