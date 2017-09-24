#!/usr/bin/env python3
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
hi = tf.constant("hello tensflow")
sess = tf.Session()
print(sess.run(hi))
print("hello world")