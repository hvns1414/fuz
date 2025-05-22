import socket
import sys
from time import sleep
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--int", dest="repeat_count", type="int",
                  help="Number of times to repeat the second string")
parser.add_option("-s", "--string", dest="string1",
                  help="First part of the string to send")
parser.add_option("-t", "--text", dest="string2",
                  help="Second string to multiply and append")
parser.add_option("-a", "--address", dest="ip",
                  help="Target IP address")
parser.add_option("-p", "--port", dest="port", type="int",
                  help="Target port")
parser.add_option("-w", "--wizard", action="store_true", dest="wizard",
                  help="Run the script in interactive mode")

(options, args) = parser.parse_args()

if options.wizard:
    i = int(input("int>>> "))
    str2 = input("string send text>>> ")
    a = input("string to send >>> ")
    ip = input("ip>>> ")
    port = int(input("port>>> "))
else:
    if not (options.repeat_count and options.string1 and options.string2 and options.ip and options.port):
        parser.error("Missing required options. Use --help for more information.")
    i = options.repeat_count
    str2 = options.string2
    a = options.string1
    ip = options.ip
    port = options.port

string_ts = a + "/.:/" + str2 * i
o = 0

while True:
    o += 1
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        bytes_data = string_ts.encode(encoding="latin1")
        s.send(bytes_data)

        print(f"sending {bytes_data} {o}")
        s.close()
        string_ts += str2 * i
        sleep(1)

    except KeyboardInterrupt:
        print("crashed at:" + str(len(string_ts)))
        sys.exit()

    except Exception as e:
        print("crash at:" + str(len(string_ts)))
        print("sorry bro")
        print(e)
        sys.exit()
