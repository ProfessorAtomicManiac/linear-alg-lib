class matrix:    

    # only 2-dimensional matrices
    def __init__(self, matrix):
        if not (type(matrix) is list):
            raise TypeError('matrix only accepts list type')
        if (self.__get_dim(matrix) != 2):
            raise TypeError('matrix must have 2 dimensions. It has {} dimension(s)'.format(self.__get_dim(matrix)))
        if (not self.__is_valid_matrix(matrix)):
            raise TypeError('invalid matrix')
        self.matrix = matrix
        self.print()

    # get dimension of matrix
    def __get_dim(self, matrix):
        if not (type(matrix) is list):
            return 0
        max_inner_dim = 0
        for ele in matrix:
            max_inner_dim = max(max_inner_dim, self.__get_dim(ele))
        return 1 + max_inner_dim
    
    def __is_valid_matrix(self, matrix):
        cols = -1
        for ele in matrix:
            if (cols == -1):
                cols = len(ele)
            elif (len(ele) != cols):
                return False
        return True
    
    def print(self):
        print('[', end='')
        for i in range(len(self.matrix)):
            row = self.matrix[i]
            if (i > 0):
                print(' ', end='')
            print('[', end='')
            for j in range(len(row)):
                if (j == len(row) - 1 and i == len(self.matrix) - 1):
                    print(str(row[j]) + "]]", end='')
                elif (j == len(row) - 1):
                    print(str(row[j]) + "]")
                else: 
                    print(str(row[j]) + ", ", end='')