import subprocess
import os
import psutil


def run_aria2():
    cwd = os.getcwd()
    relative_path = 'Binaries/aria2/aria2c.exe'
    # Combine the current working directory with the relative path
    path_to_aria2c = os.path.join(cwd, relative_path)

    # Check if aria2c.exe is already running
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'aria2c.exe':

                return
        except (psutil.NoSuchProcess, psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    # Start aria2c.exe if it's not already running
    subprocess.Popen(
        [path_to_aria2c, "--enable-rpc=true", "--rpc-listen-all=true"],
        shell=True,
        creationflags=subprocess.CREATE_NO_WINDOW)
