import RPi.GPIO as GPIO
import time


txDelay = 1
ledPin = 3
fecFactor = 3
enableManchester = True
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin,GPIO.OUT)


def fec_bit(bit):
	
	opList = []
	bitVal = int(bit)
	for x in range(fecFactor):
		opList.append(bitVal)
	
	return opList

def send_data(bit_stream,enableManchester=True):
	for bit in bit_stream:
		op = fec_bit(bit)
		for bitVal in op:
			send_bit(bitVal,enableManchester)

def send_bit(bit,enableManchester=True):
	if enableManchester == True:
		if bit == 1:
			GPIO.output(ledPin,GPIO.HIGH)
			time.sleep(txDelay)
			GPIO.output(ledPin,GPIO.LOW)
			time.sleep(txDelay)	
		elif bit == 0:
			GPIO.output(ledPin,GPIO.LOW)
			time.sleep(txDelay)
			GPIO.output(ledPin,GPIO.HIGH)
			time.sleep(txDelay)
	else:
		if bit == 1:
			GPIO.output(ledPin,GPIO.HIGH)
			time.sleep(txDelay)
		elif bit == 0:
			GPIO.output(ledPin,GPIO.LOW)
			time.sleep(txDelay)

GPIO.cleanup()