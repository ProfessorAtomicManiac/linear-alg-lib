from functools import reduce

class matrix:    

    # only 2-dimensional matrices
    def __init__(self, matrix):
        self.matrix = matrix
        if not isinstance(matrix, list):
            raise TypeError('matrix only accepts list type')
        if self.__get_dim(self.matrix) != 2:
            raise TypeError('matrix must have 2 dimensions. It has {} dimension(s)'.format(self.__get_dim(matrix)))
        if not self.__is_valid_matrix():
            raise TypeError('invalid matrix')

    # get dimension of matrix
    def __get_dim(self, matrix):
        if not isinstance(matrix, list): 
            return 0
        return 1 + self.__get_dim(matrix[0]) if matrix else 0
    
    def __is_valid_matrix(self):
        if self.__get_dim(self.matrix) != 2: 
            return False
        cols = len(self.matrix[0])
        lens = [len(li) == cols for li in self.matrix]
        return all(lens)
    
    def __str__(self):
        return "\n".join(['[' + ' '.join([str(i) for i in li]) + ']' for li in self.matrix])
    
    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, index):
        return self.matrix[index]

    def __mul__(self, right):
        if type(right) in [float, int]:
            m = [[i * right for i in li] for li in self.matrix]
            return matrix(m)
        elif type(right) is matrix:
            if len(self.matrix[0]) != len(right):
                raise TypeError("Cannot multiply this matrix")
            m = []
            for row in range(len(self.matrix)):
                m.append([])
                for col in range(len(right[0])):
                    val = 0
                    for i in range(len(right)):
                        val += self.matrix[row][i] * right[i][col]
                    m[row].append(val)
            return matrix(m)
        else:
            raise TypeError('Cannot mutiply with {}'.format(str(type(right))))
    
    def __rmul__(self, left):
        if type(left) in [float, int]:
            m = [[i * left for i in li] for li in self.matrix]
            return matrix(m)
        elif type(left) is matrix:
            if len(left[0]) != len(self.matrix):
                raise TypeError("Cannot multiply this matrix")
            m = []
            for row in range(len(left)):
                m.append([])
                for col in range(len(self.matrix[0])):
                    val = 0
                    for i in range(len(left[0])):
                        val += left[row][i] * self.matrix[i][col]
                    m[row].append(val)
            return matrix(m)
        else:
            raise TypeError('Cannot mutiply with {}'.format(str(type(left))))
        