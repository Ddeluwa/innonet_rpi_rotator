import serial
import serial.rs485
import time

# ===================================================== # 
#                    Pelco-D Protocol                   #
# ===================================================== # 
#           No parity / 8 Data bits / 1 Stop bit        #
# ===================================================== # 
#                   7 hexadecimal bytes                 #
#     Byte 1 : STX-Start of Text, fixed to FF           #
#     Byte 2 : Camera Address(1 is 01)                  #
#     Byte 3 : Command 1                                #
#     Byte 4 : Command 2                                #
#     Byte 5 : Data 1                                   #
#     Byte 6 : Data 2                                   #
#     Byte 7 : Checksum - sum of Bytes then modulo 100  #
# ===================================================== #
#     Ex : FF 01 00 04 20 00 25 - pan Left              #
#     Ex : FF 01 00 02 20 00 23 - pan Right             #
# ===================================================== # 
try:
    ser = serial.Serial(
        port = '/dev/ttyUSB0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    panLeft = [0xFF, 0x02, 0x00, 0x04, 0x01, 0x00, 0x07]
    panRight = [0xFF, 0x02, 0x00, 0x02, 0x40, 0x00, 0x44]
    allStop = [0xFF, 0x02, 0x00, 0x00, 0x00, 0x00, 0x02]
    tiltUp = [0xFF, 0x02, 0x00, 0x08, 0x00, 0x3F, 0x49]
    tiltDown = [0xFF, 0x02, 0x00, 0x10, 0x00, 0x3F, 0x51]

    
    left = 0
    right = 0
    while 1:
        # serial.write()는 Byte 형태로 전달한다.
        actionCommand = input("Command : ")
        ser.write(allStop)
        if actionCommand == "L" :
            ser.write(panLeft)
            time.sleep(1.6)
            left = left + 1
            print(left)
        elif actionCommand == "R" :
            ser.write(panRight)
            time.sleep(1.6)
            right = right + 1
            print(right)
        elif actionCommand == "I" :
            ser.write(panRight)
            time.sleep(55)
        elif actionCommand == "0" :
            left = 0
            right = 0
        ser.write(allStop)
        
except KeyboardInterrupt:
    print("KeyboardInterrupt : Ctrl + C")
    ser.write(allStop)
    ser.close()
