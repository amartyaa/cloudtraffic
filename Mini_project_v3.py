import os
import bluetooth
import RPi.GPIO as GPIO
from google.cloud import firestore

############Explicit Credential environment
path="/home/pi/Desktop/Cloud-Parking-f348563ba8bf.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =path

#GPIO starts
s1=14
s2=16
GPIO.setmode(GPIO.BCM)     
GPIO.setwarnings(False)
GPIO.setup(s1,GPIO.IN)
GPIO.setup(s2,GPIO.IN)



#firestore initialization
db = firestore.Client()
doc_ref_s1 = db.collection(u'sensor').document(u'Sensor1')				#node sensor1 in #node sensor
doc_ref_s2 = db.collection(u'sensor').document(u'Sensor1')
#here starts main
data1=0
data2=0
while 1:
	
	if(GPIO.input(s1)==True): #no car found in slot 1
		data1=0
	else: data1=1
        
	print("Received: %s" % data1)
	if(data1=="0"):
		(
		doc_ref_s1.update({
		u'Car': u'Absent',				#in field  , value form
		u'bin': 0
		})
		
		)
	elif(data1=="1"):
		(
		doc_ref_s1.update({
		u'Car': u'Present',	#in field  , value form
		u'bin': 1
		})
		)
	###Now starts for sensor 2
	if(GPIO.input(s2)==True): #no car found in slot 2
		data1=0
	else: data1=1
        
	print("Received: %s" % data2)
	if(data2=="0"):
		(doc_ref_s2.update({
		u'Car': u'Absent',				#in field  , value form
		u'bin': 0
		})
		
		)
	elif(data2=="1"):
		(
		doc_ref_s2.update({
		u'Car': u'Present',	#in field  , value form
		u'bin': 1
		})
		)

