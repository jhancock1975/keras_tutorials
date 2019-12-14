#!/bin/bash
source utils.sh
source constants.py

log "starting up"

log_dir=/git/tensorboard/addition_rnn_graph
log "log_dir = "${log_dir}

killall -HUP tensorboard
rm -rf ${log_dir} 
mkdir -p ${log_dir}
    
tensorboard --logdir=${log_dir} --port=8888 &
python addition_rnn.py 2>&1 | tee addition_rnn.log
