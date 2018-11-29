import serial
import time # Optional (if using time.sleep() below)

# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

MORSE_INV = {v: k for k, v in MORSE_CODE_DICT.iteritems()}
def morseToText(arr):
    result = ''
    for item in arr:
        result += MORSE_INV[item]
    print(result)

port = '/dev/ttyUSB0' #READLINE  
baud = 9600
serial_port = serial.Serial(port, baud, timeout=3)

cnt = 0
space = 0
res = []
temp = []
tempStr = ''

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
        #print('decoding MORSE', cnt, space)
        if(cnt >= 3 and space < 10):
            tempStr += '-'
            space = 0
        elif( cnt < 3 and cnt > 0 and space < 10 ):
            tempStr += '.'
            space = 0
        elif(space > 10):
            if(len(tempStr)):
                res.append(tempStr)
                tempStr = ''
                space = 0

        cnt = 0
        space +=1

        #print(res)
        morseToText(res)
        time.sleep(0.1) 