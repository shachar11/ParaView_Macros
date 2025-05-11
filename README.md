# ParaView Macro: Soot Foil Visualization

This repository contains a Python macro script for ParaView, `soot_foil_macro_update.py`, designed to automate the visualization of soot foil data. The script was originally generated using ParaView's built-in trace functionality, which records user actions and converts them into a Python script. The recorded script was then generalized to work with any file name and any number of soot foil files.

## Features
- **Automated Visualization**: Automates the process of loading and visualizing multiple soot foil `.vtk` files in ParaView.
- **Generalized Input**: Works with any file name and any number of soot foil files by specifying the base file name and the total number of files.
- **Custom Scalar Coloring**: Automatically applies scalar coloring to visualize the `Max_Normalized_Pressure` field.
- **Color Map Preset**: Uses the "X Ray" color map preset for consistent visualization.
- **Batch Processing**: Loops through all specified files and applies the same visualization settings.

## Usage
1. Update the `name_of_file` variable with the base name of your soot foil files (e.g., `Epsilon_9_Q_50_G_1.2`).
2. Set the `number_of_files` variable to the total number of soot foil files.
3. Run the script in ParaView's Python Shell or as a macro.

## Requirements
- ParaView version 5.10.0 or later.
- Soot foil data files in `.vtk` format.
