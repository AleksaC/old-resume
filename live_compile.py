#!/usr/bin/env python

import os
from subprocess import Popen, DEVNULL
import sys
import time


file_path = "resume.tex"
command = ["pdflatex", "-interaction=nonstopmode", "resume.tex"]


def run_command(command, verbose=True):
    output = None if verbose else DEVNULL
    process = Popen(command, stdout=output, stderr=output)
    process.communicate()


if __name__ == "__main__":
    verbose = len(sys.argv) == 2 and sys.argv[1] == "--verbose"
    try:
        print(f"Watching for changes in {file_path}")
        run_command(command, verbose=verbose)
        prev_mod = os.path.getmtime(file_path)
        while True:
            time.sleep(0.2)
            curr_mod = os.path.getmtime(file_path)
            if prev_mod != curr_mod:
                run_command(command, verbose=False)
                prev_mod = curr_mod
    except KeyboardInterrupt:
        print("\nStopping the watcher...")
