#!/bin/sh

python -m src.scrape "$1"
python -m src.clean_data "$1"
python -m src.manipulate_data "$1"

