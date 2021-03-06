# Copyright 2017-2019 TensorHub, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import logging
import os
import sys

import numpy as np

import tensorflow as tf

from tensorflow import keras

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(message)s")

log = logging.getLogger()

class_names = [
    'T-shirt/top',
    'Trouser',
    'Pullover',
    'Dress',
    'Coat',
    'Sandal',
    'Shirt',
    'Sneaker',
    'Bag',
    'Ankle boot',
]

def main(argv):
    print("hello: 1.123")
    args = _init_args(argv)
    data = load_data(args.data_dir)
    model = init_model(learning_rate=args.lr)
    _init_output_dirs(args)
    _train_model(model, data, args)
    _test_model(model, data)

def _init_args(argv):
    p = argparse.ArgumentParser()
    p.add_argument(
        "-e", "--epochs",
        default=5, type=int,
        help="Number of epochs to train")
    p.add_argument(
        "-r", "--lr", default=0.04, type=float,
        help="Learning rate")
    p.add_argument(
        "-b", "--batch-size", default=100, type=int,
        help="Batch size")
    p.add_argument(
        "-d", "--data-dir",
        help=(
            "Directory containing prepare data; if not specified, "
            "downloads raw data"))
    p.add_argument(
        "-c", "--checkpoint-dir", default=".",
        help="Directory to write checkpoints")
    p.add_argument(
        "-l", "--log-dir", default=".",
        help="Directory to write logs")
    return p.parse_args(argv[1:])

def load_data(from_dir=None):
    if from_dir:
        log.info("Loading data from %s", from_dir)
        return _load_prepared_data(from_dir)
    log.info("Loading raw data")
    return _load_and_process_raw_data()

def _load_prepared_data(dir):
    return (
        (np.load(os.path.join(dir, "train-images.npy")),
         np.load(os.path.join(dir, "train-labels.npy"))),
        (np.load(os.path.join(dir, "test-images.npy")),
         np.load(os.path.join(dir, "test-labels.npy"))))

def _load_and_process_raw_data():
    fashion_mnist = keras.datasets.fashion_mnist
    return _process_data(fashion_mnist.load_data())

def _process_data(data):
    log.info("Processing data")
    (train_images, train_labels), (test_images, test_labels) = data
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    return (train_images, train_labels), (test_images, test_labels)

def init_model(**optimizer_kw):
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    model.compile(
        optimizer=tf.optimizers.Adam(**optimizer_kw),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy'])
    return model

def checkpoint_callback(checkpoint_dir):
    file_pattern = os.path.join(
        checkpoint_dir,
        "weights-{epoch:04d}-{loss:0.3f}.hdf5")
    return keras.callbacks.ModelCheckpoint(file_pattern)

def _init_output_dirs(args):
    log.info("Checkpoints will be written to %s", args.checkpoint_dir)
    tf.io.gfile.makedirs(args.checkpoint_dir)
    log.info("Logs will be written to %s", args.log_dir)
    tf.io.gfile.makedirs(args.log_dir)

def _train_model(model, data, args):
    log.info("Training model")
    (train_images, train_labels), _ = data
    model.fit(
        train_images,
        train_labels,
        batch_size=args.batch_size,
        epochs=args.epochs,
        callbacks=_train_callbacks(args))

def _train_callbacks(args):
    return [
        _tensorboard_callback(args),
        _checkpoint_callback(args),
    ]

def _tensorboard_callback(args):
    return tf.keras.callbacks.TensorBoard(log_dir=args.log_dir)

def _checkpoint_callback(args):
    _ensure_h5py()
    file_pattern = os.path.join(
        args.checkpoint_dir,
        "weights-{epoch:04d}-{loss:0.3f}.hdf5")
    return keras.callbacks.ModelCheckpoint(file_pattern)

def _ensure_h5py():
    import h5py as _

def _test_model(model, data):
    log.info("Evaluating trained model")
    _, (test_images, test_labels) = data
    _loss, test_acc = model.evaluate(test_images, test_labels)
    print("Test accuracy: %s" % test_acc)

if __name__ == "__main__":
    main(sys.argv)
