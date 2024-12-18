
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
    
    def get_all_combinations(self):
        """
        Returns a list of all rows, columns and diagonals.
        """
        return self.get_all_rows() + self.get_all_columns() + self.get_all_diagonals()

    def get_all_rows(self):
        """
        Returns a list of all rows.
        """
        return self.matrix

    def get_all_columns(self):
        """
        Returns a list of all columns.
        """

        columns = []
        for i in range(len(self.matrix)):
            columns.append([row[i] for row in self.matrix])
        return columns

    def get_all_diagonals(self):
        """
        Returns a list of all diagonals.

        Example:
        get_all_diagonals(Matrix([[1,2,3]
         [4,5,6]
         [7,8,9]]) returns [['7'], ['4', '8'], ['1', '5', '9'], ['2', '6'], ['3'], ['1'], ['2', '4'], ['3', '5', '7'], ['6', '8'], ['9']]

        """
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        diagonals = []

        for d in range(-(rows - 1), cols): 
            diag = []
            for i in range(rows):
                j = i + d
                if 0 <= j < cols:
                    diag.append(self.matrix[i][j])
            if diag:
                diagonals.append(diag)

        for d in range(rows + cols - 1):
            anti_diag = []
            for i in range(rows):
                j = d - i
                if 0 <= j < cols:
                    anti_diag.append(self.matrix[i][j])
            if anti_diag:
                diagonals.append(anti_diag)

        return diagonals
    
    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])