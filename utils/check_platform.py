import platform


def detect_platform():
    """
    Detects the platform and architecture of the current system.

    Returns:
        str: A string representing the detected platform and architecture:
            - "win64" for 64-bit Windows
            - "win32" for 32-bit Windows
            - "linux64" for 64-bit Linux
            - "linux32" for 32-bit Linux
            - "macx64" for macOS with x86_64 or amd64 architecture
            - "macarm64" for macOS with arm64 or aarch64 architecture
            - "unknown" for unsupported or unrecognised platforms
    """
    system = platform.system()
    machine = platform.machine().lower()

    if system == "Windows":
        if '64' in machine:
            return "win64"
        else:
            return "win32"
    elif system == "Linux":
        if '64' in machine:
            return "linux64"
        else:
            return "linux32"
    elif system == "Darwin":
        if machine in ['x86_64', 'amd64']:
            return "macx64"
        elif machine in ['arm64', 'aarch64']:
            return "macarm64"
    else:
        return "unknown"

if __name__ == "__main__":
    print(detect_platform())