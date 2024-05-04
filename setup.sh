echo "creating virtual environment"
python3 -m venv venv
source venv/bin/activate
echo "installing flask"
pip install flask
echo "installing prusa-slicer"
if uname -m | grep '64'; then
  curl  https://github.com/davidk/PrusaSlicer-ARM.AppImage/releases/download/version_2.7.4/PrusaSlicer-version_2.7.4-aarch64.AppImage -L -O prusa-slicer.AppImage
else
    curl  https://github.com/prusa3d/PrusaSlicer/releases/download/version_2.7.3/PrusaSlicer-2.7.3+linux-armv7l-GTK2-202403280945.AppImage -L -O prusa-slicer.AppImage
fi

chmod +x prusa-slicer.AppImage


echo "Installation *almost done, change EXPORT_PATH in setup.sh to the path where you want to save the gcode files"
echo "Run \"flask run --host=0.0.0.0 server\" to start the server."