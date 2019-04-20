#!/bin/bash
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
	-files mapper3.py,reducer3.py \
	-mapper mapper3.py \
	-reducer reducer3.py \
	-input /common_step2/part* \
	-output /common_step3

