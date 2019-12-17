#!/bin/bash
# 
# this script is for running examples
# from https://keras.io/examples
# it clears out tensorboard info so watch out
# it starts tensorboard and saves all console
# output to a log file
if [ $# -lt 1 ]; then
    echo usage $(basename $0) "[ script name ]"
    exit 1
fi


source utils.sh
source constants.py

log "starting up"

log "log_dir = "${tb_log_dir}

killall -HUP tensorboard
rm -rf ${tb_log_dir} 
mkdir -p ${tb_log_dir}
    
tensorboard --logdir=${tb_log_dir} --port=8888 --bind_all &
python $1 2>&1 | tee $(basename $0).log
