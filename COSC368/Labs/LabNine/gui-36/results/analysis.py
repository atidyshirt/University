"""
File: analysis.py
Author: Jordan Pyott
Description: I will use a python module I wrote a while back to generate a markdown report using matplotlib and python;
             if the marker wishes to run this script, the module can be installed from the below github link
Module: https://github.com/atidyshirt/MarkdownWriter
"""

import matplotlib.pyplot as plt
from markdown_writer.markdown_writer import MarkdownWriter

md = MarkdownWriter("./analysis.md")
md.clear_file()
md.header1("COSC368 Lab 9 Results")

four_tile_res = open("../experiment_four.txt", "r")

read_results = []
times = []
block = []
tmp = []
result_time = []


figure = plt.figure()

for line in four_tile_res:
    read_results.append(line.split())
for line in read_results:
    block.append(line[3])
    times.append(line[4])

for block_num in range(0, 9):
    for b in range(0, len(block) - 1):
        if int(block[b]) == block_num:
            tmp.append(float(times[b]))
    result_time.append(sum(tmp)/len(tmp))
    tmp = []

plt.plot([b for b in range(0, 9)], result_time, "r", label="Four tiles (9 pages)")

four_tile_res.close()

thirtysix_tile_res = open("../experiment_thirtysix.txt", "r")

read_results = []
times = []
block = []
tmp = []
result_time = []

for line  in thirtysix_tile_res:
    read_results.append(line.split())
for line in read_results:
    block.append(line[3])
    times.append(line[4])

for block_num in range(0, 9):
    for b in range(0, len(block) - 1):
        if int(block[b]) == block_num:
            tmp.append(float(times[b]))
    result_time.append(sum(tmp)/len(tmp))
    tmp = []

plt.plot([b for b in range(0, 9)], result_time, "r", label="Thirty six tiles (1 page)")
thirtysix_tile_res.close()

plt.title("Four tiles vs Thirty six tiles")
plt.xlabel("Block Number")
plt.ylabel("Times")
plt.legend()

md.plot(figure, file_name='comparison.png', description='Four tiles vs Thirty six tiles')

md.paragraph("""
After spending a couple of hours trying to run the R scripts on my home machine I have not
been able to isolate the problem, in the first script:
""")

md.codeblock("""
#!/usr/bin/env Rscript

data <- read.table("ttest-data.txt", header=TRUE)
t.test(data$four, data$thirtysix, paired=TRUE)
""")

md.paragraph("""
I am not sure what I have done wrong here, but I get the output as follows:
""")

md.codeblock("""
Error in t.test.default(data$four, data$thirtysix, paired = TRUE) :
  'y' is missing for paired test
Calls: t.test -> t.test.default
Execution halted
""")

md.codeblock("""
#!/usr/bin/env Rscript

library(ez)

data <- read.table("ttest-data.txt", header=TRUE)
novice_data <- data[which(data$block == 0),]
expert_data <- data[which(data$block == 9),]

print("NOVICE ANALYSIS")
ezANOVA(data=novice_data, dv=as.numeric(time), within=condition, wid=subject)
ezStats(data=novice_data, dv=as.numeric(time), within=condition, wid=subject)

print("EXPERT ANALYSIS")
ezANOVA(data=expert_data, dv=as.numeric(time), within=condition, wid=subject)
ezStats(data=expert_data, dv=as.numeric(time), within=condition, wid=subject)
""")

md.paragraph("""The output of this script has a different error, I tried to cast the time to an integer to avoid the issue
    however this seems to be of no avail, and recieves the following error: """)

md.codeblock("""
[1] "NOVICE ANALYSIS"
Error in ezANOVA_main(data = data, dv = dv, wid = wid, within = within,  :
  "dv" must be numeric.
Calls: ezANOVA -> ezANOVA_main
Execution halted
""")

md.paragraph("""
I am not sure what to do here, any feedback would be appreciated.
""")
