import socket
import threading

import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((b'127.0.0.1',9090))
s.listen(5)
print(b'Waiting for connection ------->>>>')
while True:
	sock,addr = s.accept()
	# th =threading.Thread(target=tcplink,args=(sock,addr))
	# th.start()
	while True:

		sock.send(b'Hello welcome ------<<<>>>>')
		time.sleep(1)
		data=sock.recv(1024)
		if data:
			print(data)
		if data=='exit' or not data:
			pass

		sock.send(b'Bye ------==')

	sock.close()
	print('Connection closed !!!')
