#!/usr/bin/env python

import os
import time


file_path = "resume.tex"
command = "pdflatex -interaction=nonstopmode resume.tex"


if __name__ == '__main__':
    try:
        print(f"Watching for changes in {file_path}")
        prev_mod = os.path.getmtime(file_path)
        while True:
            time.sleep(0.2)
            curr_mod = os.path.getmtime(file_path)
            if prev_mod != curr_mod:
                os.system(command)
                prev_mod = curr_mod
    except KeyboardInterrupt:
        print("\nStopping the watcher")
