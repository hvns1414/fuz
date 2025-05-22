import socket
import sys  
from time import sleep
i=int(input("int>>> "))
str2=input("string send text>>> ")
a=str(input("string to send >>> "))
string_ts=a+str("/.:/")+str2 * i
ip=str(input("ip>>> "))
port=int(input("port>>> "))
o=0
while True:
    o=o+1
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        bytes=string_ts.encode(encoding="latin1")
        s.send(bytes)
        
        print(f"sending {bytes} {o}")
        s.close
        string_ts=string_ts + str2 * i
        sleep(1)
    except KeyboardInterrupt:
        print("crashed at:"+str(len(string_ts)))
        sys.exit()
        
    except Exception as e:
        print("crash at:"+str(len(string_ts)))
        print("sorry bro")
        print(e)
        sys.exit()