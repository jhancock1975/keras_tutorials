from keras.models import Sequential
from keras.layers import Dense, Activation
import keras
import numpy as np
import jh_util as jh

#  repeatability
np.random.seed(0)


import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.info('starting up')

# For a single-input model with 10 classes (categorical classification):

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Generate dummy data
import numpy as np
data = np.random.random((1000, 100))
logging.debug('data.shape = {}'.format(data.shape))
logging.debug('sample of data {}'.format(jh.arr_rand_sample(data)))

labels = np.random.randint(10, size=(1000, 1))
logging.debug('labels.shape = {}'.format(labels.shape))
logging.debug('sample of labels {}'.format(jh.arr_rand_sample(labels)))

# Convert labels to categorical one-hot encoding
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)
logging.debug('one_hot_labels.shape = {}'.format(one_hot_labels.shape))
logging.debug('sample of one_hot_labels {}'.format(jh.arr_rand_sample(one_hot_labels)))


# Train the model, iterating on the data in batches of 32 samples
model.fit(data, one_hot_labels, epochs=10, batch_size=32)
