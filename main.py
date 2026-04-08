import platform
import sys
import os


def get_system_report():
    info = {
        "Python Version": sys.version.split()[0],
        "Operating System": platform.system(),
        "OS Release": platform.release(),
        "Architecture": platform.machine(),
        "CWD": os.getcwd()
    }

    print("--- Environment Report ---")
    for key, value in info.items():
        print(f"{key}: {value}")
    print("--------------------------")


if __name__ == "__main__":
    get_system_report()
    if platform.system() == "Windows":
        print("Running on Windows (Laptop/Home PC)")
    else:
        print("Running on Linux (Fedora/Docker)")