import time
import serial
import select
import sys

def input_with_timeout(prompt, timeout):
	sys.stdout.write(prompt)
	sys.stdout.flush()
	ready, _, _ = select.select([sys.stdin], [], [], timeout)
	if ready:
		return sys.stdin.readline().rstrip('\n')
	return None


try:
	ser = serial.Serial(
		port='/dev/ttyAMA0',
		baudrate=9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
	)

	
	

	while True:
		file = open("data.txt", 'a')
		dataString = "55"
		i = 0
		if ser.read().hex() == "55":
			while i < 10 :
				s_rcv = ser.read().hex()
				dataString = dataString + " " + s_rcv
				i = i + 1
			print(dataString)
			file.write(dataString+"\n")
			file.close()
		else :
			print("No Data")
		s_snd = input_with_timeout('',2)

except KeyboardInterrupt:
	print("Ctrl + C")
	ser.close()
except (OSError, serial.SerialException):
	print("Serial port check")
	ser.close()

