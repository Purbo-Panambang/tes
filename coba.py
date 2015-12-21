import socket
import sys

server_address = ('localhost',5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

try:
	while True:
		data=raw_input()

		namafile=data.split(' ',1)
		#print data
		for i in namafile:
			namafile1=i
		namafile1
		client_socket.send(data)
		f=open(namafile1,'wb')
		
		while (True):
			l=client_socket.recv(1024)
			while(l):
				f.write(l)
				l=client_socket.recv(1024)
	f.close()

except KeyboardInterrupt:
	client_socket.close()
	sys.exit(0)
