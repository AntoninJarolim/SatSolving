#!/usr/bin/fish
# shellcheck disable=SC2121
python3 sudoku/sudoku.py > sudoku/sudokuClause.in
cat sudoku/sudokuClause.in
echo
echo
minisat sudoku/sudokuClause.in sudoku/sudokuClause.out
cat sudoku/sudokuClause.out