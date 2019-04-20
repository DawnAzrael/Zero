#!/bin/bash
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
	-files mapper2.py,reducer2.py \
	-mapper mapper2.py \
	-reducer reducer2.py \
	-input /common/part* \
	-output /common_step2
