import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

i_pin = 14
o_pin = 15

gpio.setup(i_pin, gpio.IN)
gpio.setup(o_pin, gpio.OUT)

def chargeCell1():
	gpio.output(o_pin, 1)

def chargeCell2():
	gpio.output(o_pin, 0)

def fetch():
	file = open('./cell','r')
	f = file.read()
	if f == '0':
		return 0
	if f == '1':
		return 1
	file.close()
	
def set(value):
	file = open('./cell','r+w')
	file.write(value)
        file.close()
try:
 while True:
	getmode = gpio.input(i_pin)
	if getmode == 1:
		if fetch() == '1':
			set(0)
			chargeCell1()	
		if fetch() == '0':
			set(1)
			chargeCell2()
		

except KeyboardInterrupt:
	gpio.cleanup()

