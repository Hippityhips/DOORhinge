import RPi.GPIO as GPIO
import time

from flask import Flask

app = Flask(__name__)

servoPIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start(0) 

try:
  @app.route('/')
	def index():
		return 'Send a request with close or open!'  

	@app.route('/close')
	def close():
		global c
		try:
			c
		except:
			c = 2
    
		if c == 1:
			return 'Door already closed!'
		else:
			p.ChangeDutyCycle(7.5)
			time.sleep(1)
			p.ChangeDutyCycle(0)
			c = 1

			return 'Door closed!'

	@app.route('/open')
	def open():
		global c
		try:
			c
		except:
			c = 2
        
		if c == 0:
			return 'Door already opened!'
		else:
			p.ChangeDutyCycle(2.5)
			time.sleep(1)
			p.ChangeDutyCycle(0)
			c = 0
			
			return 'Door Opened!'

	if __name__ == '__main__':
		app.run(debug=True, host='0.0.0.0')

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
