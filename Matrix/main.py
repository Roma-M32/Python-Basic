
class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('The matrices must have the same dimensions for addition')

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('The matrices must have the same dimensions for subtraction.')

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError(
                'The number of columns in the first matrix should be equal to the number of rows in the second matrix.')

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result


# Creating instances of the Matrix class
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]


# Testing operations
print('Matrix 1:')
print(m1)

print('Matrix 2:')
print(m2)

print('Matrix addition:')
print(m1.add(m2))

print('Matrix subtraction:')
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print('Matrix multiplication:')
print(m1.multiply(m3))

print('Matrix transposition 1:')
print(m1.transpose())