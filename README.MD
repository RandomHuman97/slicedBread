# slicedBread
A self-hosted g-code slicer for 3D printers. This project is a work in progress and is not yet ready for use.

## Installation
1. Clone the repository
2. `chmod +x install.sh
3. `./install.sh` (Make sure you have `libfuse2`, `python3` and `pip3` installed) *Keep in mind that I've only tested this with KIAUH installed klipper, custom installs may need some file editing*
4. The server should now be running on `printer-ip:5050`, via the systemd service `slicedBread.service`
5. Edit the `configs/config.ini` file to match your printer's settings (can be exported from PrusaSlicer)

## Features
- [X] Slice 3D models

## TO-DO
- [ ] Add preview of sliced model
- [ ] Add setting overrides for model-specific features (infill, layer height, etc.)
- [ ] Add support for multiple models in a single print