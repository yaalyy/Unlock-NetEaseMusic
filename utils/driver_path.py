from .check_platform import detect_platform
from pathlib import Path

def get_driver_path():
    """
    Returns the chrome driver system path based on the current operating system.

    Returns:
        str: The absolute path to the web driver executable.
    """
    
    system = detect_platform()
    if system == "unknown":
        raise Exception("Unsupported platform detected. Please check your system configuration.")
    elif system == "win32":  # Windows 32-bit
        raise Exception("Win-32 detected, which is not supported for now.")
    elif system == "linux32": # Linux 32-bit
        raise Exception("Linux-32 detected, which is not supported for now.")
    elif system == "win64":  # Windows 64-bit
        return str(Path("chromedriver/win64/chromedriver.exe"))
    elif system == "linux64":  # Linux 64-bit
        return str(Path("chromedriver/linux64/chromedriver"))
    elif system == "macx64":
        raise Exception("MacOSX64 detected, which is not supported for now.")
    elif system == "macarm64":
        raise Exception("MacOSARM64 detected, which is not supported for now.")

    
if __name__ == "__main__":
    try:
        print(f"chrome driver path: {get_driver_path()}")
    except Exception as e:
        print(f"Error: {e}")
    