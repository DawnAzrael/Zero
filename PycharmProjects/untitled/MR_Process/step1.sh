#!/bin/bash
hadoop fs -rm /common/*
hadoop fs -rmdir /common
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
	-files mapper1.py,reducer1.py \
	-mapper mapper1.py \
	-reducer reducer1.py \
	-input /subUnionsData.txt \
	-output /common
