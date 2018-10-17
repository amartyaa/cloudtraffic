import os
import RPi.GPIO as GPIO
from google.cloud import firestore
import time 

############Explicit Credential environment
path="/home/pi/Desktop/shreshthParking.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =path

#GPIO starts
s1=2
s2=21
GPIO.setmode(GPIO.BCM)     
GPIO.setwarnings(False)
GPIO.setup(s1,GPIO.IN)
GPIO.setup(s2,GPIO.IN)


#firestore initialization
db = firestore.Client()
doc_ref_s1 = db.collection(u'sensors').document(u'sensor1')			
doc_ref_s2 = db.collection(u'sensors').document(u'sensor2')
#here starts main
data1=0
data2=0
counter=0
while 1:
	
	if(GPIO.input(s1)==False): #car found in slot 1
		data1=1
		counter+=1
	else: data1=0
        
	print("Received from 1: %s" % data1)
	###Now starts for sensor 2	
	if(GPIO.input(s2)==False): #car found in slot 2
		data2=1
		counter-=1
	else: data2=0
	print("Received from 2: %s" % data2)
	if(counter>8):
		counter=8
	elif(counter<0):
		counter=0
	print("Counter= %s" % counter)
	doc_ref_s1.update({
		u'occupancy': counter
		})
	
