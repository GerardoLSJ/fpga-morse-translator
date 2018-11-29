# import threading
# import serial
# import time
# connected = False
# port = 'COM4'
# baud = 9600

# # serial_port = serial.Serial(port, baud, timeout=0)

# def loop():
#     while(True):
#         print('wait')
#         time.sleep(1)

# def w():
#     while(True):
#         print('holi')
#         if not t1.isAlive():
#             break
#         time.sleep(0.5)

# # def handle_data(data):
# #     print(data)

# # def read_from_port(ser):
# #     while not connected:
# #         #serin = ser.read()
# #         connected = True

# #         while True:
# #            print("test")
# #            reading = ser.readline().decode()
# #            handle_data(reading)

# # thread = threading.Thread(target=read_from_port, args=(serial_port,))
# # #thread.start()
# t1 = threading.Thread(target=loop)
# t1.start()
# t2 = threading.Thread(target=w)
# t2.start()


import serial
import time # Optional (if using time.sleep() below)

port = '/dev/ttyUSB0' #READLINE  
baud = 9600
serial_port = serial.Serial(port, baud, timeout=3)

cnt = 0
space = 0
res = []
temp = []
"""
si cnt > 3 es "linea"

si cnt < 3 es "punto"

si space > 10 es fin de cadena

"""
while (True):
    if (serial_port.inWaiting()>0): 
        #print('wait',serial_port.inWaiting())  
        data_str = serial_port.read(1) 
        serial_port.reset_input_buffer()
        cnt += 1
        space = 0
        time.sleep(0.2) 

    else:
        print('decoding MORSE', cnt, space)
        if(cnt >= 3 and space < 10):
            temp.append('--')
            space = 0
        elif( cnt < 3 and cnt > 0 and space < 10 ):
            temp.append('.')
            space = 0
        elif(space > 10):
            if(len(temp)):
                res.append(temp)
                temp = []
                space = 0

        cnt = 0
        space +=1

        print(res)
        time.sleep(0.1) 