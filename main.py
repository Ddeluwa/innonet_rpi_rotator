from reference import *

import serial

if __name__ == "__main__" :
    try :
        rotator = openSerial("/dev/ttyUSB0", 9600, serial.PARITY_NONE, serial.STOPBITS_ONE, serial.EIGHTBITS, 1)
        rotatorControl = Rotator()
        
        while True :
            IMU_angleDataFile = open("IMU_angle_data.txt", 'r')

            angleData = IMU_angleDataFile.readline().split(' ')

            angleDataX = angleData[0]
            angleDataY = angleData[1]
            angleDataZ = angleData[2]
            print(angleDataX + " " + angleDataY + " "+angleDataZ)

            # 1. Rotator Stop
            rotator.write(rotatorControl.Stop())
            #time.sleep(10)
            # 2. Rotator Pan Right
            #rotator.write(rotatorControl.PanRight())
            #time.sleep(10)
            rotator.write(rotatorControl.Stop())


            # 3. Rotator Pan Light
            #rotator.write(rotatorControl.PanLeft())
            #time.sleep(10)
            rotator.write(rotatorControl.Stop())


            
            

    except KeyboardInterrupt:
        print("Ctrl + C")
        IMU_angleDataFile.close()
        rotator.write(rotatorControl.Stop())
        closeSerial(rotator)

    except (OSError, serial.SerialException):
        print("Serial port check")
        IMU_angleDataFile.close()
        rotator.write(rotatorControl.Stop())
        closeSerial(rotator)