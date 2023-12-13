from functools import reduce

class matrix:    

    # only 2-dimensional matrices
    def __init__(self, matrix):
        self.matrix = matrix
        if type(matrix) is not list:
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