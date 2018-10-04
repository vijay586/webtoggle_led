import RPi.GPIO as GPIO 
import time 
import http.client 
import json 

pin = 7 
GPIO.setmode(GPIO.BOARD) 
# Board mode is safer option to use with pin numbers matching between older and 
# newer versions of Raspberry Pi, hence no confusion 
GPIO.setup(pin, GPIO.OUT) 
while True: 
  client = http.client.HTTPSConnection('<< firebase URL>>')
  client.request('GET','/LED.json') 
  httpResponse = client.getresponse() 
  dataStream = httpResponse.read() 
  dataString = str(dataStream, 'utf-8') 
  switchLedOn = json.loads(dataString) 
  print(switchLedOn) 
  # switchLedOn holds true/false as user toggles the switch 
  # with a button on the web page. 
  
  if (switchLedOn): 
     print('Switching ON...') 
     GPIO.output(pin, GPIO.HIGH) 
 else: 
     print('Switching OFF...') 
     GPIO.output(pin, GPIO.LOW) 

 time.sleep(2) 
 #retry after 2 seconds. 

GPIO.cleanup()
