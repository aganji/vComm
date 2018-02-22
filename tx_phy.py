import RPi.GPIO as GPIO
import time

class vlc_tx(object):
	"""docstring for vlc_tx"""
	def __init__(self, arg):
		super(vlc_tx, self).__init__()
		#self.arg = arg

		self.txDelay = 1
		self.ledPin = 3
		self.fecFactor = 3
		self.enableManchester = True

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(ledPin,GPIO.OUT)


	def fec_bit(bit):
		
		opList = []
		bitVal = int(bit)
		for x in range(self.fecFactor):
			opList.append(bitVal)
		
		return opList

	def send_data(bit_stream,enableManchester=self.enableManchester):
		for bit in bit_stream:
			op = fec_bit(bit)
			for bitVal in op:
				send_bit(bitVal,enableManchester)

	def send_bit(bit,enableManchester=self.enableManchester):
		if enableManchester == True:
			if bit == 1:
				GPIO.output(self.ledPin,GPIO.HIGH)
				time.sleep(self.txDelay)
				GPIO.output(self.ledPin,GPIO.LOW)
				time.sleep(self.txDelay)	
			elif bit == 0:
				GPIO.output(self.ledPin,GPIO.LOW)
				time.sleep(self.txDelay)
				GPIO.output(self.ledPin,GPIO.HIGH)
				time.sleep(self.txDelay)
		else:
			if bit == 1:
				GPIO.output(self.ledPin,GPIO.HIGH)
				time.sleep(self.txDelay)
			elif bit == 0:
				GPIO.output(self.ledPin,GPIO.LOW)
				time.sleep(self.txDelay)

	def cleanuo():
		GPIO.cleanup()