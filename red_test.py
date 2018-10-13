import os
import RPi.GPIO as GPIO
from google.cloud import firestore
from firebase import firebase

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

firebase = firebase.FirebaseApplication('https://cloud-parking-69.firebaseio.com/', None)

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
        Presence="Present"
    else:
        data1=1
        Presence="Absent"
    if(GPIO.input(s2)==True): #no car found in slot 1
        data2=0
        Presence_2="Present"
    else:
        data2=1
        Presence_2="Absent"
    
    print("Received: %s" % data1)
    data_1 = {"Car": Presence, "bin": data1}
    firebase.post('/sensor/dht', data_1)
    data_2 = {"Car":Presence_2 , "bin": data2}
    firebase.post('/sensor/dht', data_2)
    
