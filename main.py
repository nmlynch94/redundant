import PySimpleGUI as sg
from installer import main as install_launcher
from installer import cleanup
from pathlib import Path
import os
import subprocess

sg.theme('DarkAmber')
# Window layout
layout = [  [sg.Text('Launchers:')],
            [sg.Text('Jagex Launcher'), sg.Button('Install'), sg.Button('Run')],
            [sg.Output(size=(60,15))],
            [sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Redundant', layout, icon="icons/redundant64.png")

# PySimpleGUI event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Install':
        # Create a directory to place the jagex launcher installation
        Path('jlauncher').mkdir(parents=True, exist_ok=True)
        prior_dir=os.getcwd()
        os.chdir(os.path.join(os.getcwd(), 'jlauncher'))
        install_launcher()
        cleanup()
        os.chdir(prior_dir)
    if event == 'Run':
        # Specify the Bash script path and command here
        script_path = "jlauncher.sh"
        cmd = ["bash", script_path]

        # Run the Bash script and capture its output
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        while True:
            output = process.stdout.readline()
            print(output)
            window.Refresh()
            if not output:
                break

window.close()