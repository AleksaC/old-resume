#!/usr/bin/env python

import os
import time


file_path = "resume.tex"
command = "pdflatex resume.tex"


if __name__ == '__main__':
    print(f"Watching {file_path} for changes")
    prev_mod = os.path.getmtime(file_path)
    while True:
        time.sleep(0.2)
        curr_mod = os.path.getmtime(file_path)
        if prev_mod != curr_mod:
            os.system(command)
            prev_mod = curr_mod
