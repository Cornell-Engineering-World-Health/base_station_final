#!/usr/bin/env python
import serial
import MySQLdb
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basestation.settings")

from main.models import Patient

#print "before db connect"
#db = MySQLdb.connect(user="django",passwd="django-pass",host="localhost",db="basestation")
#cursor = db.cursor()
#print "after db connect"

def main():
	print "starting main"
	try :
		ser = serial.Serial('/dev/ttyACM0',115200)
	except:
		try:
			ser = serial.Serial('/dev/ttyACM1',115200)
		except:
			try:
				ser = serial.Serial('/dev/ttyAMA0',115200)
			except:
				ser = serial.Serial('/dev/ttyAMA1',115200)
			else:
				print "Serial failed"
	while 1:	
		try :
			data = ser.readline()
			execute(data)
		except:
			print "in except1"
			continue	


def execute(data):
	try: 
		data = data[data.find("<d>")+3 : data.find("</d>")]
	except: 
		print "in except2"
		return

	data = data.split("|")
	patient,bed,condition = data[0],data[1],data[2]
	print patient, bed, condition

	sql1 = "USE basestation;" 
	sql2 = "UPDATE `main_patient` SET `bed` = %s WHERE `p_id` = %s;" % (bed,patient)
	sql3 = "UPDATE `main_patient` SET `condition` = %s WHERE `p_id` = %s;" % (condition,patient)
	
	try:
		Patient.edit(patient,bed,condition)
		#print "edit worked"	
		#cursor.execute(sql1)
		#db.commit()
		#print "sql1 worked"
		#cursor.execute(sql2)
		#db.commit()
		#print "sql2 worked"
		#cursor.execute(sql3)
		#db.commit()
		#print "sql3 worked"
	except:
		print "in except3"
		db.rollback()

	
if __name__ == "__main__":

	main()