import RPi.GPIO as GPIO
import time

class vlc_tx(object):
	"""docstring for vlc_tx"""
	def __init__(self):
		super(vlc_tx, self).__init__()
		#self.arg = arg

		self.txDelay = 1
		self.ledPin = 3
		self.fecFactor = 3
		self.enableManchester = True

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.ledPin,GPIO.OUT)


	def fec_bit(self,bit):
		
		opList = []
		bitVal = int(bit)
		for x in range(self.fecFactor):
			opList.append(bitVal)
		
		return opList

	def send_data(self,bit_stream,enableManchester=None):
		if enableManchester == None:
			enableManchester = self.enableManchester
		for bit in bit_stream:
			op = self.fec_bit(bit)
			print op
			for bitVal in op:
				self.send_bit(bitVal,enableManchester)

	def send_bit(self,bit,enableManchester=None):
		if enableManchester == None:
			enableManchester = self.enableManchester
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

	def cleanuo(self):
		GPIO.cleanup()