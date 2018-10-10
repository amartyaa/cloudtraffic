import os
import bluetooth
from google.cloud import firestore
############Explicit Credential environment
path="/home/pi/Desktop/Cloud-Parking-f348563ba8bf.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =path
##########Initialize bluetooth
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
client_socket,address = server_socket.accept()
print ("Accepted connection from ",address)

# Project ID is determined by the GCLOUD_PROJECT environment variable
#firestore initialization
db = firestore.Client()
doc_ref = db.collection(u'sensor').document(u'Sensor1')				#node sensor1 in #node sensor
while 1:
	
	d = client_socket.recv(1024)
	c=str(d)
	data=c[2]
	print("Received: %s" % data)
	if(data=="0"):
		(#print("Sent: %s" % data)
		doc_ref.update({
		u'Car': u'Absent',				#in field  , value form
		u'bin': 0
		})
		
		)
	elif(data=="1"):
		(
		#print("Sent: %s" % data)
		doc_ref.update({
		u'Car': u'Present',	#in field  , value form
		u'bin': 1
		})
		)

