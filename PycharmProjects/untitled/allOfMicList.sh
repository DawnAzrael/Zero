#!/bin/bash
python /home/hadoop/PycharmProjects/untitled/micList.py
python /home/hadoop/PycharmProjects/untitled/MR_Process/prepare.py
hadoop fs -rm /subUnionsData.txt
hadoop fs -copyFromLocal subUnionsData.txt /
