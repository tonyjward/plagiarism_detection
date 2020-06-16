#!/bin/sh
# Example usage: ./check_plagiarism.sh '[random forest, xgboost]' data
# See https://stackoverflow.com/a/32763171 for explanation

python -m src.containment "$1" "$2"
python -m src.lcs "$1" "$2"
python -m src.feature_matrix "$1" "$2"


