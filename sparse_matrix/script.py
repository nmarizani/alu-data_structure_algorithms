class SparseMatrix:
    def __init__(self, file_path=None, num_rows=None, num_cols=None):
        self.elements = {}
        if file_path:
            self._from_file(file_path)
        elif num_rows is not None and num_cols is not None:
            self.num_rows = num_rows
            self.num_cols = num_cols
        else:
            raise ValueError("Provide either a file path or dimensions for the matrix.")

    def _from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.num_rows = self._parse_value(file.readline().strip())
                self.num_cols = self._parse_value(file.readline().strip())
                for line in file:
                    line = line.strip()
                    if line:
                        if not (line.startswith('(') and line.endswith(')')):
                            raise ValueError("Input file has wrong format")
                        row, col, value = self._parse_entry(line)
                        self.elements[(row, col)] = value
        except Exception as e:
            raise ValueError(f"Error reading file: {str(e)}")

    def _parse_value(self, line):
        key, value = self._split(line, '=')
        return int(value)

    def _parse_entry(self, line):
        entry = line[1:-1]
        row, col, value = self._split(entry, ',')
        return int(row), int(col), int(value)

    def _split(self, s, delimiter):
        parts = []
        current = ''
        for char in s:
            if char == delimiter:
                parts.append(current)
                current = ''
            else:
                current += char
        parts.append(current)
        return parts

    def get_element(self, row, col):
        return self.elements.get((row, col), 0)

    def set_element(self, row, col, value):
        if value != 0:
            self.elements[(row, col)] = value
        else:
            self.elements.pop((row, col), None)

    def _elementwise_operation(self, other, op):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for operation")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        keys = set(self.elements.keys()).union(other.elements.keys())
        for key in keys:
            result.set_element(*key, op(self.get_element(*key), other.get_element(*key)))
        return result

    def add(self, other):
        return self._elementwise_operation(other, lambda x, y: x + y)

    def subtract(self, other):
        return self._elementwise_operation(other, lambda x, y: x - y)

    def multiply(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrices dimensions do not match for multiplication")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for (i, k), val in self.elements.items():
            for j in range(other.num_cols):
                if (k, j) in other.elements:
                    result.set_element(i, j, result.get_element(i, j) + val * other.get_element(k, j))
        return result

    def __str__(self):
        result = f"Rows={self.num_rows}, Cols={self.num_cols}\n"
        for (row, col), value in sorted(self.elements.items()):
            result += f"({row}, {col}, {value})\n"
        return result


def get_matrix_input(prompt):
    file_path = input(prompt)
    return SparseMatrix(file_path=file_path)

def perform_operation(matrix1, matrix2, operation):
    if operation == '1':
        return matrix1.add(matrix2)
    elif operation == '2':
        return matrix1.subtract(matrix2)
    elif operation == '3':
        return matrix1.multiply(matrix2)
    else:
        raise ValueError("Invalid operation selected")

def main():
    print("Sparse Matrix Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    
    operation = input("Select an operation (1/2/3): ")
    
    if operation not in {'1', '2', '3'}:
        print("Invalid selection. Exiting.")
        return

    matrix1 = get_matrix_input("Enter the path for the first matrix file: ")
    matrix2 = get_matrix_input("Enter the path for the second matrix file: ")

    try:
        result = perform_operation(matrix1, matrix2, operation)
        print("Result:")
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


