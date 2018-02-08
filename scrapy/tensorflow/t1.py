import tensorflow as tf
import numpy as np

#1
x_data = np.random.rand(100).astype(np.float32)
y_data = 0.7*x_data+0.7
# print(x_data)
#2
Weigh = tf.Variable(tf.random_uniform([1],-1.0,1.0))
bia = tf.Variable(tf.zeros([1]))
y=Weigh*x_data+bia
loss= tf.reduce_mean(tf.square(y-y_data))
opm=tf.train.GradientDescentOptimizer(0.1)
train=opm.minimize(loss)
# print(t)
#3

init = tf.initialize_all_variables()
with tf.Session() as sess:
	sess.run(init)
	for i in range(2000):
		sess.run(train)
		if i %20 ==0:
			print(i,sess.run(Weigh),sess.run(bia))
