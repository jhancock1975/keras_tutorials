#!/bin/bash
if [ $# -lt 1 ]; then
    echo usage $(basename $0) "[ script name ]"
    exit 1
fi


source utils.sh
source constants.py

log "starting up"

log "log_dir = "${log_dir}

killall -HUP tensorboard
rm -rf ${log_dir} 
mkdir -p ${log_dir}
    
tensorboard --logdir=${log_dir} --port=8888 &
python $1 2>&1 | tee addition_rnn.log
