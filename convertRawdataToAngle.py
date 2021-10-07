f = open("data.txt", 'r')
w = open("data_angle.txt", 'w')

while True:
    dataString = f.readline()
    data = dataString.split(' ')

    if not dataString: break
    if(data[1] == '54'):
        # print('Angle Data')

        rollL = int(data[2], 16)
        rollH = int(data[3], 16)
        pitchL = int(data[4], 16)
        pitchH = int(data[5], 16)
        yawL = int(data[6], 16)
        yawH = int(data[7],16)
        tl = int(data[8], 16)
        th = int(data[9], 16)
        sum = int(data[10], 16)

        # print(hex(rollL), hex(rollH), hex(pitchL), hex(pitchH), hex(yawL), hex(yawH), hex(tl), hex(th), hex(sum))

        # WE DON'T NEED THE CODES BELOW ANYMORE
        # scale = 16 ## equals to hexadecimal
        # num_of_bits = 8
        # rollLBinary = bin(int(rollL, scale))[2:].zfill(num_of_bits)
        # print(rollLBinary)
        # rollLBinaryShift = rollLBinary + '00000000'
        # print(rollLBinaryShift)

        rollX = ((rollH << 8) | rollL) / 32768 * 180
        pitchY = ((pitchH << 8 ) | pitchL) / 32768 * 180
        yawZ = ((yawH << 8 ) | yawL ) / 32768 * 180

        # print(round(rollX, 2), round(pitchY, 2), round(yawZ, 2))
        angle = str(round(rollX, 2)) + ', ' + str(round(pitchY, 2)) + ', ' + str(round(yawZ, 2)) + '\n'
        w.write(angle)