from keras.models import Sequential
from keras.layers import Dense, Activation
import keras
import numpy as np

#  repeatability
np.random.seed(0)

def arr_rand_sample(arr, n=5):
    """random sample of numpy array elements
    @param arr: input array
    @param n: number of samples to return, default 5
    @return array of n elements sampled from arr
    """
    return arr[np.random.randint(np.size(arr, axis=0), size = (n))]

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
logging.debug('sample of data {}'.format(arr_rand_sample(data)))

labels = np.random.randint(10, size=(1000, 1))
logging.debug('labels.shape = {}'.format(labels.shape))
logging.debug('sample of labels {}'.format(arr_rand_sample(labels)))

# Convert labels to categorical one-hot encoding
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)
logging.debug('one_hot_labels.shape = {}'.format(one_hot_labels.shape))
logging.debug('sample of one_hot_labels {}'.format(arr_rand_sample(one_hot_labels)))

assert False

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, epochs=10, batch_size=32)
