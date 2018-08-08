#  Connects to POP3 Port on the specified ip and send test as username and password
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    
    ip = raw_input('Enter the ip: ')  
    print "\nConnecting to " + ip + " on port 110..."
    s.connect((ip,110)) 
    
    # receive and print banner
    data = s.recv(1024) 
    print data # print banner
    
    # send username "test" and print reply
    s.send('USER test' +'\r\n') 
    data = s.recv(1024) 
    print data 
    
    # send password "test" and print reply
    s.send('PASS test\r\n') 
    data = s.recv(1024) 
    print data 
    
    # close socket
    s.close() 
    print "\nDone!"
except:
    print "Could not connect to POP3!"