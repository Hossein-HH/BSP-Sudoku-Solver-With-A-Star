# BSP Sudoku Solver with A* Algorithm

This Python project is a Sudoku solver using the A* search algorithm. It was developed as part of an Artificial Intelligence and Expert Systems course at Jahrom University, under the guidance of Dr. Mohammad Javad Parseh.

## Project Structure

- **input.txt**: Input file containing the initial Sudoku puzzle. Use '0' for empty cells, like this:

  ```
  8 0 0 0 0 0 0 0 0
  0 0 3 6 0 0 0 0 0
  0 7 0 0 9 0 2 0 0
  0 5 0 0 0 7 0 0 0
  0 0 0 0 4 5 7 0 0
  0 0 0 1 0 0 0 3 0
  0 0 1 0 0 0 0 6 8
  0 0 8 5 0 0 0 1 0
  0 9 0 0 0 0 4 0 0
  ```

- **output.txt**: Output file where the solved Sudoku will be written in the following format:

  ```
  8 1 2 7 5 3 6 4 9
  9 4 3 6 8 2 1 7 5
  6 7 5 4 9 1 2 8 3
  1 5 4 2 3 7 8 9 6
  3 6 9 8 4 5 7 2 1
  2 8 7 1 6 9 5 3 4
  5 2 1 9 7 4 3 6 8
  4 3 8 5 2 6 9 1 7
  7 9 6 3 1 8 4 5 2
  ```

- **main.py**: The main Python file containing the Sudoku-solving code.

## Usage

1. Ensure you have Python installed on your system.
2. Put your Sudoku puzzle in the `input.txt` file as described above.
3. Run `main.py`.
4. The solved Sudoku will be generated and saved in the `output.txt` file.

## Acknowledgments

- Dr. Mohammad Javad Parseh for the guidance and inspiration.
