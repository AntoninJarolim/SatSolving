#!/usr/bin/fish
# shellcheck disable=SC2121
set N $argv[1]
clean
python3 queens.py $N > queens.in
cat queens.in
echo "Generated input $N.";
minisat queens.in queens.out
cat queens.out

python3 chessVisualizer.py
