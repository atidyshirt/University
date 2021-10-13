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
