from .check_platform import detect_platform
from pathlib import Path

class UnsupportedOSException(Exception):
    """Exception raised when the current OS is not supported."""
    pass

def get_driver_path():
    """
    Returns the chrome driver system path based on the current operating system.

    Returns:
        str: The absolute path to the web driver executable.
    """
    
    system = detect_platform()
    if system == "unknown":
        raise UnsupportedOSException("Unsupported platform detected. Please check your system configuration.")
    elif system == "win32":  # Windows 32-bit
        raise UnsupportedOSException("Win-32 detected, which is not supported for now.")
    elif system == "linux32": # Linux 32-bit
        raise UnsupportedOSException("Linux-32 detected, which is not supported for now.")
    elif system == "win64":  # Windows 64-bit
        return str(Path(Path(__file__).parent.parent / "chromedriver/win64/chromedriver.exe").resolve())
    elif system == "linux64":  # Linux 64-bit
        return str(Path(Path(__file__).parent.parent / "chromedriver/linux64/chromedriver").resolve())
    elif system == "macx64":
        raise UnsupportedOSException("MacOSX64 detected, which is not supported for now.")
    elif system == "macarm64":
        raise UnsupportedOSException("MacOSARM64 detected, which is not supported for now.")

    
if __name__ == "__main__":
    try:
        print(f"chrome driver path: {get_driver_path()}")
    except UnsupportedOSException as e:
        print(f"OS Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
