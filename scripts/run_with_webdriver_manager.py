#!/usr/bin/env python3
"""
Example helper showing how to use webdriver-manager to auto-manage ChromeDriver
and then run Robot Framework tests using that driver.

Two usage modes:
1) Use webdriver-manager to download the driver and add its path to PATH.
2) Import this in a custom Robot library if you need programmatic control.

This script is a simple example; Robot Framework SeleniumLibrary can work
...\n

if __name__ == "__main__":
    main()
"""

from webdriver_manager.chrome import ChromeDriverManager
from shutil import which
import os
import subprocess
import sys

def ensure_chromedriver_on_path():
    # Download driver and return its path
    path = ChromeDriverManager().install()
    # ChromeDriverManager returns a path to the binary; ensure directory is in PATH
    bin_dir = os.path.dirname(path)
    if bin_dir not in os.environ.get("PATH", ""):
        os.environ["PATH"] = bin_dir + os.pathsep + os.environ.get("PATH", "")
    return path

def main():
    # Install driver (if necessary) and run a Robot test
    try:
        driver_path = ensure_chromedriver_on_path()
        print(f"ChromeDriver is available at: {driver_path}")
    except Exception as e:
        print("Failed to ensure chromedriver:", e)
        sys.exit(1)

    # Example: run the login test
    cmd = ["robot", "tests/login.robot"]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
