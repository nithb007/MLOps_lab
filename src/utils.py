import os
import sys


def check_python_version():
    """Return current Python version."""
    return sys.version


def current_working_directory():
    """Return current working directory."""
    return os.getcwd()


def list_files(path="."):
    """List files in a directory."""
    return os.listdir(path)


if __name__ == "__main__":
    print("Python Version:", check_python_version())
    print("Working Directory:", current_working_directory())
    print("Files:", list_files())