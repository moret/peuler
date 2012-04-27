class Problem(object):
    def __init__(self):
        self.triangle = []
        f = open('p67-triangle.txt')
        for line in f:
            self.triangle.append(line.split())
        self.tree_height = len(self.triangle)

    def run(self):
        sum_triangle = []

        for line in range(self.tree_height):
            sum_line = []
            for column in range(line + 1):
                current = int(self.triangle[line][column])
                if line == 0:
                    # first line, just copy
                    sum_line.append(current)
                else:
                    # yeah, I like expressive variables...
                    left_sum = 0
                    right_sum = 0
                    left_column = column - 1
                    right_column = column
                    leftmost_column = (column == 0)
                    rightmost_column = (column == line)
                    previous_line = line - 1

                    if not leftmost_column:
                        left_sum = sum_triangle[previous_line][left_column]
                    if not rightmost_column:
                        right_sum = sum_triangle[previous_line][right_column]

                    if left_sum > right_sum:
                        sum_line.append(current + left_sum)
                    else:
                        sum_line.append(current + right_sum)
            sum_triangle.append(sum_line)

        largest_sum = 0
        for column in range(self.tree_height):
            if sum_triangle[self.tree_height - 1][column] > largest_sum:
                largest_sum = sum_triangle[self.tree_height - 1][column]

        return largest_sum

problem = Problem()

if __name__ == '__main__':
    print problem.run()
