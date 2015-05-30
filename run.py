import socket
import fcntl
import struct
import os

ip_used = ""

def get_ip_address(ifname):
	if (not ifname): ifname = "eth0"
	
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(
		fcntl.ioctl(s.fileno(),
			    0x8915,
		            struct.pack('256s',ifname[:15])
                           )[20:24])


try:
   ip_used = str(get_ip_address("eth0")) + ":8050"
except:
   try:
      ip_used = str(get_ip_address("wlan0")) + ":8050"
   except:
       try:
           ip_used = str(get_ip_address("wlan1")) + ":8050"
       except:
           print("Not Connected to Internet")

if (ip_used != ""):
   print("Address: " + ip_used) 
   try:
	os.system("python manage.py runserver " + ip_used)
        #subprocess.popen([sys.executable,"python manage.py runserver " + ip_used],shell=True)
	print("Server Started")
	#try:
           #os.system("python serialMonitorSetup.py")
	   #print("Listening...")
	#except:
           #print ("Failed to Listen")
   except:
	print ("Failed to start server")





