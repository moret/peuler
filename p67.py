# load triangle
triangle = []

f = open('triangle.txt')

for line in f:
    triangle.append(line.split())

tree_height = len(triangle)

print 'read %d lines' % tree_height

# change the number of passes if you want to run it
# several times to measure performance
passes = 1
for run in range(passes):

    sum_triangle = []

    for line in range(tree_height):
        sum_line = []
        for column in range(line + 1):
            current = int(triangle[line][column])
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
    for column in range(tree_height):
        if sum_triangle[tree_height - 1][column] > largest_sum:
            largest_sum = sum_triangle[tree_height - 1][column]

    print 'the maximum path sum is %d' %  largest_sum
