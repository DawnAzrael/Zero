#!/bin/bash
hadoop fs -rm /common/*
hadoop fs -rmdir /common
hadoop fs -rm /common_step2/*
hadoop fs -rmdir /common_step2
hadoop fs -rm /common_step3/*
hadoop fs -rmdir /common_step3
./step1.sh
./step2.sh
./step3.sh
