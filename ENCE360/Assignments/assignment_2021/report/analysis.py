"""
File: alalysis.py
Author: Jordan Pyott
Description: I will use a python module I wrote a while back to generate a markdown report using matplotlib and python
Module: https://github.com/atidyshirt/MarkdownWriter
"""

import subprocess
import matplotlib.pyplot as plt
import time
from markdown_writer.markdown_writer import MarkdownWriter

def execute(cmd: str):
    command_broken = [_ for _ in cmd.split(" ")]
    start = time.time()
    output = subprocess.run(command_broken, stdout=subprocess.PIPE, text=True)
    end = time.time()
    return output.stdout, end - start

def main():
    theirs_commands = {
        "small": [
            '../bin/downloader test_small.txt 1 download',
            '../bin/downloader test_small.txt 2 download',
            '../bin/downloader test_small.txt 3 download',
            '../bin/downloader test_small.txt 4 download',
            '../bin/downloader test_small.txt 5 download',
            '../bin/downloader test_small.txt 6 download',
            '../bin/downloader test_small.txt 7 download',
            '../bin/downloader test_small.txt 8 download',
            '../bin/downloader test_small.txt 9 download',
            '../bin/downloader test_small.txt 10 download',
            '../bin/downloader test_small.txt 11 download',
            '../bin/downloader test_small.txt 12 download',
            '../bin/downloader test_small.txt 13 download',
            '../bin/downloader test_small.txt 14 download',
            '../bin/downloader test_small.txt 15 download'
            '../bin/downloader test_small.txt 16 download'
            '../bin/downloader test_small.txt 17 download'
            '../bin/downloader test_small.txt 18 download'
            '../bin/downloader test_small.txt 19 download'
            '../bin/downloader test_small.txt 20 download'
            '../bin/downloader test_small.txt 21 download'
            '../bin/downloader test_small.txt 22 download'
            '../bin/downloader test_small.txt 23 download'
            '../bin/downloader test_small.txt 24 download'
            '../bin/downloader test_small.txt 25 download'
            '../bin/downloader test_small.txt 26 download'
            '../bin/downloader test_small.txt 27 download'
            '../bin/downloader test_small.txt 28 download'
            '../bin/downloader test_small.txt 29 download'
            '../bin/downloader test_small.txt 30 download'
            '../bin/downloader test_small.txt 31 download'
            '../bin/downloader test_small.txt 32 download'
            '../bin/downloader test_small.txt 33 download'
            '../bin/downloader test_small.txt 34 download'
            '../bin/downloader test_small.txt 35 download'
            '../bin/downloader test_small.txt 36 download'
            '../bin/downloader test_small.txt 37 download'
            '../bin/downloader test_small.txt 38 download'
            '../bin/downloader test_small.txt 39 download'
            '../bin/downloader test_small.txt 40 download'
            '../bin/downloader test_small.txt 41 download'
            '../bin/downloader test_small.txt 42 download'
            '../bin/downloader test_small.txt 43 download'
            '../bin/downloader test_small.txt 44 download'
            '../bin/downloader test_small.txt 45 download'
            '../bin/downloader test_small.txt 46 download'
            '../bin/downloader test_small.txt 47 download'
            '../bin/downloader test_small.txt 48 download'
            '../bin/downloader test_small.txt 49 download'
            '../bin/downloader test_small.txt 50 download'
        ],
        "large": [
            '../bin/downloader test_large.txt 1 download',
            '../bin/downloader test_large.txt 2 download',
            '../bin/downloader test_large.txt 3 download',
            '../bin/downloader test_large.txt 4 download',
            '../bin/downloader test_large.txt 5 download',
            '../bin/downloader test_large.txt 6 download',
            '../bin/downloader test_large.txt 7 download',
            '../bin/downloader test_large.txt 8 download',
            '../bin/downloader test_large.txt 9 download',
            '../bin/downloader test_large.txt 10 download',
            '../bin/downloader test_large.txt 11 download',
            '../bin/downloader test_large.txt 12 download',
            '../bin/downloader test_large.txt 13 download',
            '../bin/downloader test_large.txt 14 download',
            '../bin/downloader test_large.txt 15 download'
            '../bin/downloader test_large.txt 16 download',
            '../bin/downloader test_large.txt 17 download',
            '../bin/downloader test_large.txt 18 download',
            '../bin/downloader test_large.txt 19 download',
            '../bin/downloader test_large.txt 20 download',
            '../bin/downloader test_large.txt 21 download',
            '../bin/downloader test_large.txt 22 download',
            '../bin/downloader test_large.txt 23 download',
            '../bin/downloader test_large.txt 24 download',
            '../bin/downloader test_large.txt 25 download',
            '../bin/downloader test_large.txt 26 download',
            '../bin/downloader test_large.txt 27 download',
            '../bin/downloader test_large.txt 28 download',
            '../bin/downloader test_large.txt 29 download',
            '../bin/downloader test_large.txt 30 download',
            '../bin/downloader test_large.txt 31 download',
            '../bin/downloader test_large.txt 32 download',
            '../bin/downloader test_large.txt 33 download',
            '../bin/downloader test_large.txt 34 download',
            '../bin/downloader test_large.txt 35 download',
            '../bin/downloader test_large.txt 36 download',
            '../bin/downloader test_large.txt 37 download',
            '../bin/downloader test_large.txt 38 download',
            '../bin/downloader test_large.txt 39 download',
            '../bin/downloader test_large.txt 40 download',
            '../bin/downloader test_large.txt 41 download',
            '../bin/downloader test_large.txt 42 download',
            '../bin/downloader test_large.txt 43 download',
            '../bin/downloader test_large.txt 44 download',
            '../bin/downloader test_large.txt 45 download',
            '../bin/downloader test_large.txt 46 download',
            '../bin/downloader test_large.txt 47 download',
            '../bin/downloader test_large.txt 48 download',
            '../bin/downloader test_large.txt 49 download',
            '../bin/downloader test_large.txt 50 download',
    }
    commands = {
        "small": [
            '../downloader test_small.txt 1 download',
            '../downloader test_small.txt 2 download',
            '../downloader test_small.txt 3 download',
            '../downloader test_small.txt 4 download',
            '../downloader test_small.txt 5 download',
            '../downloader test_small.txt 6 download',
            '../downloader test_small.txt 7 download',
            '../downloader test_small.txt 8 download',
            '../downloader test_small.txt 9 download',
            '../downloader test_small.txt 10 download',
            '../downloader test_small.txt 11 download',
            '../downloader test_small.txt 12 download',
            '../downloader test_small.txt 13 download',
            '../downloader test_small.txt 14 download',
            '../downloader test_small.txt 15 download'
            '../downloader test_small.txt 16 download',
            '../downloader test_small.txt 17 download',
            '../downloader test_small.txt 18 download',
            '../downloader test_small.txt 19 download',
            '../downloader test_small.txt 20 download',
            '../downloader test_small.txt 21 download',
            '../downloader test_small.txt 22 download',
            '../downloader test_small.txt 23 download',
            '../downloader test_small.txt 24 download',
            '../downloader test_small.txt 25 download',
            '../downloader test_small.txt 26 download',
            '../downloader test_small.txt 27 download',
            '../downloader test_small.txt 28 download',
            '../downloader test_small.txt 29 download',
            '../downloader test_small.txt 30 download',
            '../downloader test_small.txt 31 download',
            '../downloader test_small.txt 32 download',
            '../downloader test_small.txt 33 download',
            '../downloader test_small.txt 34 download',
            '../downloader test_small.txt 35 download',
            '../downloader test_small.txt 36 download',
            '../downloader test_small.txt 37 download',
            '../downloader test_small.txt 38 download',
            '../downloader test_small.txt 39 download',
            '../downloader test_small.txt 40 download',
            '../downloader test_small.txt 41 download',
            '../downloader test_small.txt 42 download',
            '../downloader test_small.txt 43 download',
            '../downloader test_small.txt 44 download',
            '../downloader test_small.txt 45 download',
            '../downloader test_small.txt 46 download',
            '../downloader test_small.txt 47 download',
            '../downloader test_small.txt 48 download',
            '../downloader test_small.txt 49 download',
            '../downloader test_small.txt 50 download',
        ],
        "large": [
            '../downloader test_large.txt 1 download',
            '../downloader test_large.txt 2 download',
            '../downloader test_large.txt 3 download',
            '../downloader test_large.txt 4 download',
            '../downloader test_large.txt 5 download',
            '../downloader test_large.txt 6 download',
            '../downloader test_large.txt 7 download',
            '../downloader test_large.txt 8 download',
            '../downloader test_large.txt 9 download',
            '../downloader test_large.txt 10 download',
            '../downloader test_large.txt 11 download',
            '../downloader test_large.txt 12 download',
            '../downloader test_large.txt 13 download',
            '../downloader test_large.txt 14 download',
            '../downloader test_large.txt 15 download',
            '../downloader test_large.txt 16 download',
            '../downloader test_large.txt 17 download',
            '../downloader test_large.txt 18 download',
            '../downloader test_large.txt 19 download',
            '../downloader test_large.txt 20 download',
            '../downloader test_large.txt 21 download',
            '../downloader test_large.txt 22 download',
            '../downloader test_large.txt 23 download',
            '../downloader test_large.txt 24 download',
            '../downloader test_large.txt 25 download',
            '../downloader test_large.txt 26 download',
            '../downloader test_large.txt 27 download',
            '../downloader test_large.txt 28 download',
            '../downloader test_large.txt 29 download',
            '../downloader test_large.txt 30 download',
            '../downloader test_large.txt 31 download',
            '../downloader test_large.txt 32 download',
            '../downloader test_large.txt 33 download',
            '../downloader test_large.txt 34 download',
            '../downloader test_large.txt 35 download',
            '../downloader test_large.txt 36 download',
            '../downloader test_large.txt 37 download',
            '../downloader test_large.txt 38 download',
            '../downloader test_large.txt 39 download',
            '../downloader test_large.txt 40 download',
            '../downloader test_large.txt 41 download',
            '../downloader test_large.txt 42 download',
            '../downloader test_large.txt 43 download',
            '../downloader test_large.txt 44 download',
            '../downloader test_large.txt 45 download',
            '../downloader test_large.txt 46 download',
            '../downloader test_large.txt 47 download',
            '../downloader test_large.txt 48 download',
            '../downloader test_large.txt 49 download',
            '../downloader test_large.txt 50 download',
        ]
    }

    md = MarkdownWriter("./analysis.md")
    md.clear_file()
    md.header1("ENCE360 Report")
    md.header3("Algorithm analysis")
    md.header3("Performance analysis")
    md.header4("Comparison between assessment implementation and provided binary")

    threads = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    times = []
    output = []

    for command in commands['large']:
        print(command)
        out, time = execute(command)
        output.append(out)
        times.append(time)

    our_figure = plt.figure()

    plt.plot(threads, times, "r", label="Large Text")

    times = []
    output = []

    for command in commands['small']:
        print(command) # just for status
        out, time = execute(command)
        output.append(out)
        times.append(time)

    plt.plot(threads, times, "b", label="Small Text")

    plt.title("Assessment Implementation: Short vs Long text execution time")
    plt.xlabel("Number of threads")
    plt.ylabel("Execution times")
    plt.legend()

    md.plot(our_figure, file_name='ours_threads_vs_times.png', description='Assessment Implementation: Threads Vs Times')

    times = []
    output = []

    for command in theirs_commands['large']:
        print(command)
        out, time = execute(command)
        output.append(out)
        times.append(time)

    their_figure = plt.figure()

    plt.plot(threads, times, "r", label="Large Text")

    times = []
    output = []

    for command in theirs_commands['small']:
        print(command) # just for status
        out, time = execute(command)
        output.append(out)
        times.append(time)

    plt.plot(threads, times, "b", label="Small Text")

    plt.title("Provided Implementation: Short vs Long text execution time")
    plt.xlabel("Number of threads")
    plt.ylabel("Execution times")
    plt.legend()

    md.plot(their_figure, file_name='theirs_threads_vs_times.png', description='Provided Implementation: Threads Vs Times')

main()