echo "creating virtual environment"
python3 -m venv venv
source venv/bin/activate
echo "installing flask"
pip install flask gunicorn
echo "installing prusa-slicer"
if uname -m | grep '64'; then
  curl  https://github.com/davidk/PrusaSlicer-ARM.AppImage/releases/download/version_2.7.4/PrusaSlicer-version_2.7.4-aarch64.AppImage -L -o prusa-slicer.AppImage
else
    curl  https://github.com/prusa3d/PrusaSlicer/releases/download/version_2.7.3/PrusaSlicer-2.7.3+linux-armv7l-GTK2-202403280945.AppImage -L -o prusa-slicer.AppImage
fi

chmod +x prusa-slicer.AppImage



cat > EDITME.py <<- "EOF"
EXPORT_PATH = '/home/$USER/printer_data/gcodes'
EOF

cat << EOF | sudo tee /etc/systemd/system/slicedBread.service
[Unit]
Description=Slicer Web App
After=network.target

[Service]
WorkingDirectory=$PWD
Environment=$PWD/venv/bin
ExecStart=$PWD/venv/bin/gunicorn -w 1 -b 0.0.0.0:5050 'server:app'
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target

EOF

sudo systemctl enable slicedBread
sudo systemctl start slicedBread

echo "The default config is for the Ender 3 V3 SE with PLA, you can export a new config from PrusaSlicer and replace the config.ini file (configs/config.ini)"
