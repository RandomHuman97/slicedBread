# slicedBread
A self-hosted g-code slicer for 3D printers. This project is a work in progress and is not yet ready for use.

## Installation
1. Clone the repository
2. `chmod +x install.sh` to make the script executable if it isn't already.
3. `./install.sh` (Make sure you have `libfuse2`, `python3` and `pip3` installed) *Keep in mind that I've only tested this with KIAUH installed klipper, custom installs may need some file editing*
4. The server should now be running on `printer-ip:5050`, via the systemd service `slicedBread.service`
5. Add new configs to the `configs` folder (they can be exported from PrusaSlicer via: *File/Export/Export Config*)

## Features
- [X] Slice 3D models
- [X] Multiple printer profiles/configs
- 
## TO-DO
- [ ] Add preview of sliced model
- [ ] Add support for multiple models in a single print