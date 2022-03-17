#!/usr/bin/fish
# shellcheck disable=SC2121
# python3 sudokuVisualizer sudoku_lengal.in -input
python3 sudoku.py > sudokuClause.in
cat sudokuClause.in
echo
echo
minisat sudokuClause.in sudokuClause.out
cat sudokuClause.out
python3 sudokuVisualizer.py -clause sudokuClause.out
