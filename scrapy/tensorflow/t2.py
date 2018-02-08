import tensorflow as tf
import numpy as np

def add_layer(input,in_size,out_size,activation_function=None):
	with tf.name_scope('layer'):
		with tf.name_scope('weigh'):
			Weigh = tf.Variable(tf.random_normal([in_size,out_size],name='W'))
		# print(Weigh)
		with tf.name_scope('Bia'):
			bia = tf.Variable(tf.zeros([out_size])+0.1,name='B')
		trans = tf.matmul(input,Weigh)+bia
		if activation_function is None:
			out = trans
		else:
			out=activation_function(trans)
		return out

x_data = np.linspace(-1,1,300)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data)-0.5 + noise
with tf.name_scope('inputs'):
	xs = tf.placeholder(tf.float32,[None,1],name='x_input')
	ys = tf.placeholder(tf.float32,[None,1],name='y_input')

l1 = add_layer(xs,1,10,activation_function=tf.nn.relu)
prediction = add_layer(l1,10,1)
with tf.name_scope('Loss'):
	loss= tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
with tf.name_scope('Train'):
	train = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

init = tf.initialize_all_variables()
with tf.Session() as sess:
	sess.run(init)

	# write = tf.write_file('log/',sess.graph)
	for i in range(200):
		sess.run(train,feed_dict={xs:x_data,ys:y_data})
		print(sess.run(train),feed_dict={xs:x_data,ys:y_data})
