import tensorflow as tf
import os
import joblib
import logging
from src.utils.all_utils import get_timestamp



def create_and_save_tensorboard_callback(callbacks_dir, tensorboard_log_dir):
    unique_name = get_timestamp("tb_logs")

    tb_running_log_dir = os.path.join(tensorboard_log_dir, unique_name)
    tensorflow_callbacks = tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    tb_callback_flepath = os.path.join(callbacks_dir, "tensorboard_cb.cb")
    joblib.dump(tensorflow_callbacks, tb_callback_flepath)
    logging.info(f"Tensorboard callback is being saved at {tb_callback_flepath}")

def create_and_save_checkpoint_callback(callbacks_dir, checkpoint_dir):
    pass
