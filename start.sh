version=$(python -V 2>&1 | grep -Po '(?<=Python )(.+)')

if [[ -z "$version" ]]
then
    sudo apt-get install python 
else
    pip install pytube
    pip install Pillow
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade Pillow
    clear
    python3 main.py
fi
