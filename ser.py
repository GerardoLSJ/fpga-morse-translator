import serial
import time


serial_port = serial.Serial('/dev/ttyUSB0')
print(serial_port.inWaiting())
data_str = serial_port.read(1)
print(data_str)
serial_port.close()

# while(True):
#     for i in range(65,90):
#         port = serial.Serial('/dev/ttyUSB0')
#         port.write(chr(i))
#         time.sleep(1)

