import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

def full_connected():
    # 获取真实的数据
    mnist = input_data.read_data_sets("./data/mnist/", one_hot=True)
    