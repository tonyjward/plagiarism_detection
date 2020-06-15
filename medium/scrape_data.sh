#!/bin/sh
# Example usage: ./scrape_data.sh '[random forest, xgboost]' data
# See https://stackoverflow.com/a/32763171 for explanation

python -m src.scrape "$1" "$2"
python -m src.clean_data "$1" "$2"
python -m src.manipulate_data "$1" "$2"

