import queue

def is_goal_state(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False

    for i in range(9):
        if len(set(sudoku[i])) != 9:
            return False
        if len(set([sudoku[j][i] for j in range(9)])) != 9:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if len(set([sudoku[x][y] for x in range(i, i+3) for y in range(j, j+3)])) != 9:
                return False

    return True


def solve_sudoku(input_file, output_file):
    with open(input_file, 'r') as f:
        sudoku = []
        for line in f:
            row = [int(x) for x in line.strip().split()]
            sudoku.append(row)

    def heuristic(sudoku):
        count = 0
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    count += 1
        return count

    q = queue.PriorityQueue()
    q.put((heuristic(sudoku), sudoku))

    while not q.empty():
        current_state = q.get()[1]

        if is_goal_state(current_state):
            with open(output_file, 'w') as f:
                for row in current_state:
                    f.write(' '.join(str(x) for x in row) + '\n')
            return True

        row, col = None, None
        for i in range(9):
            for j in range(9):
                if current_state[i][j] == 0:
                    row, col = i, j
                    break
            if row is not None:
                break

        possible_values = set(range(1, 10)) - \
            set(current_state[row]) - \
            set([current_state[i][col] for i in range(9)]) - \
            set([current_state[i][j] for i in range(row//3*3, (row//3+1)*3)
                for j in range(col//3*3, (col//3+1)*3)])

        for value in possible_values:
            new_state = [row[:] for row in current_state]
            new_state[row][col] = value

            new_cost = heuristic(new_state) + 1

            q.put((new_cost, new_state))


solve_sudoku('input.txt', 'output.txt')
