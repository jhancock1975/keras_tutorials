# Use this template to copy/paste examples in
# sets up logging and tensorboard config
import logging
import configure_logging
import os
import matplotlib.pyplot as plt
import constants as const
import plot_history as ph
import keras
from keras.models import Sequential
from keras import layers

# set up tensorboard
tbCallBack = keras.callbacks.TensorBoard(log_dir=const.tb_log_dir,
                                         histogram_freq=0, write_graph=True, write_images=True)
