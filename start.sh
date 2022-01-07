version=$(python3 -V 2>&1 | grep -Po '(?<=Python )(.+)')

if [[ -z "$version" ]]
then
    sudo apt-get install python3 
else
    pip install pytube
    pip install Pillow
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade Pillow
    clear
    echo Good Luck $(whoami)
    python3 main.pyw
fi
