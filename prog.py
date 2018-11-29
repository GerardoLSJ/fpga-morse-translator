import serial
import time

port = serial.Serial('/dev/ttyUSB0')
# cmd = 'G1abcd\n'
# print(cmd)
# port.write(cmd.encode())
# time.sleep(1)

# cmd = 'G2abcd\n'
# print(cmd)
# port.write(cmd.encode())
# time.sleep(1)

# cmd = 'G3abcd\n'
# print(cmd)
# port.write(cmd.encode())
# time.sleep(1)
msj = port.read(7)
print('eco', msj)
port.close()
