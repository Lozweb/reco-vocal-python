#!/bin/bash

path="$(pwd)"
project_path="$(dirname "$path")"

python3 -m venv "$project_path"/.venv
source "$project_path"/.venv/bin/activate
python3 -m ensurepip --default-pip
pip3 install -r requirements.txt

cd ..

if [[ ! -d "model" ]]
then
  echo "mkdir -p model"
  mkdir -p "model"
fi

cd "model" || exit
pwd

if [[ ! -f "vosk-model-small-fr-0.22/README" ]];then
  echo "vosk model small required"
  wget "https://alphacephei.com/vosk/models/vosk-model-small-fr-0.22.zip"
  unzip "vosk-model-small-fr-0.22.zip"
  rm "vosk-model-small-fr-0.22.zip"
else
  echo "vosk model already satisfied"
fi

if [[ ! -f "vosk-model-fr-0.22/README" ]];then
  echo "vosk modal large optional"
  wget "https://alphacephei.com/vosk/models/vosk-model-fr-0.22.zip"
  unzip "vosk-model-fr-0.22.zip"
  rm "vosk-model-fr-0.22.zip"
else
  echo "vosk model large already satisfied"
fi

echo "if you get an error at runtime : install espeak package"
echo "if you are on manjaro, intall it from AUR, espeak-ng from pacman not work"
