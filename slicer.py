import subprocess


def slice_to_gcode(gcode_name, model, config):
    return subprocess.run(["./prusa-slicer.AppImage", "-g", "-o", f"{gcode_name}", "--load", f"{config}", f"{model}"])
