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
		file_row = open("data.txt", 'a')
		
		dataString = "55"
		i = 0
		# IMU module row data save 
		if ser.read().hex() == "55":
			while i < 10 :
				s_rcv = ser.read().hex()
				dataString = dataString + " " + s_rcv
				i = i + 1

			file_row.write(dataString + '\n')	
			file_row.close()

		else :
			print("No Data")
			continue

		# '53' data 
		file_angle_write = open("data_angle.txt", 'a')

		data = dataString.split(' ')
		if data[1] == "53" :
			rollL = int(data[2], 16)
			rollH = int(data[3], 16)
			pitchL = int(data[4], 16)
			pitchH = int(data[5], 16)
			yawL = int(data[6], 16)
			yawH = int(data[7],16)
			tl = int(data[8], 16)
			th = int(data[9], 16)
			sum = int(data[10], 16)

			rollX = ((rollH << 8) | rollL) / 32768 * 180
			pitchY = ((pitchH << 8 ) | pitchL) / 32768 * 180
			yawZ = ((yawH << 8 ) | yawL ) / 32768 * 180

			# print(round(rollX, 2), round(pitchY, 2), round(yawZ, 2))
			angle = str(round(rollX, 2)) + ', ' + str(round(pitchY, 2)) + ', ' + str(round(yawZ, 2)) + '\n'

			file_angle_write.write(dataString + " " + angle)		
			print("Angle parameter is saved. Angle :" + angle)
			file_angle_write.close()
		else :
			file_angle_write.close()
	
		s_snd = input_with_timeout('',2)

except KeyboardInterrupt:
	print("Ctrl + C")
	ser.close()
except (OSError, serial.SerialException):
	print("Serial port check")
	ser.close()

