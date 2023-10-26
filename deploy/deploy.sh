#!/bin/bash

path="$(pwd)"
project_path="$(dirname "$path")"

python3 -m venv "$project_path"/.venv
source "$project_path"/.venv/bin/activate
python3 -m ensurepip --default-pip
pip3 install -r requirements.txt

echo "if you get an error at runtime : install espeak package"
echo "if you are on manjaro, intall it from AUR, espeak-ng from pacman not work"
