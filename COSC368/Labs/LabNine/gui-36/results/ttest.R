#!/usr/bin/env Rscript
data <- read.table("ttest-data.txt", header=TRUE)
t.test(data$four, data$thirtysix, paired=TRUE)
