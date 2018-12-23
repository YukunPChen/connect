#this file is used for connect the computer of my home

from subprocess import call
import webbrowser
class connecter():
    def __init__(self):
        self.name  = 'default'
        self.IP ='0.0.0.0'
        self.username = 'default_usr'
        self.passcode = 'Forcewithyou.pem'
        self.jupyter = 'off'
    def setparameter(self):
        location = input('please give me your destination:')
        if location =='home':
            self.name = 'home'
            self.IP = '72.66.111.163'
            self.username = 'peterchan'
            self.passcode = '/users/chanpc/.ssh/id_rsa'
        elif location == 'AWS':
            self.name = 'AWS'
            self.IP = 'ec2-34-226-234-77.compute-1.amazonaws.com'
            self.username = 'ubuntu'
            self.passcode = 'Forcewithyou.pem'
        elif location == 'jupyter':
            self.name = 'jupyter'
            self.IP = 'ec2-35-172-28-244.compute-1.amazonaws.com'
            self.username = 'ubuntu'
            self.passcode = 'Forcewithyou.pem'
            self.jupyter = 'on'
        elif location == 'ppt':
            self.name = 'ppt'
            self.IP = 'ec2-35-172-28-244.compute-1.amazonaws.com'
            self.username = 'ubuntu'
            self.passcode = 'Forcewithyou.pem'
        elif location == 'es':
            self.name = 'es'
            self.IP = 'ec2-54-158-210-199.compute-1.amazonaws.com'
            self.username  = 'ec2-user'
            self.passcode = 'Forcewithyou.pem'
        elif location =='ec2':
            self.name = 'ec2'
            self.IP = 'ec2-52-91-250-210.compute-1.amazonaws.com'
            self.username = 'ec2-user'
        elif location == 'a2p':
            self.name = 'a2p'
            self.IP = 'ec2-52-90-201-9.compute-1.amazonaws.com'
            self.username = 'ec2-user'
        elif location == 'test':
            self.name = 'test'
            self.IP = 'ec2-54-208-247-174.compute-1.amazonaws.com'
            self.username = 'ec2-user'     
        elif location == 'task6':
            self.name = 'task6'
            self.IP = 'ec2-3-83-215-220.compute-1.amazonaws.com'
            self.username = 'ec2-user' 
            self.passcode = 'task6keypair.pem'
        elif location == 'task62':
            self.name = 'task62'
            self.IP = 'ec2-54-172-9-61.compute-1.amazonaws.com'
            self.username = 'ec2-user'
            self.passcode = 'task6keypair.pem'          
        else:
            print('the location you input does not exist in our records, please type again.')
            self.setparameter()





    def run(self):
 #       if self.es =='yes':
 #           print('you are connecting to the ec2 instance which has the access to your es endpoint')
        if self.jupyter == 'off':
            print('you are connecting to')
            print(self.IP)
            print('as username')
            print(self.username)
            print('using key')
            print(self.passcode)
            line= self.username+'@'+runner.IP
            call(['ssh',line,'-i',self.passcode])
        else:
            print('you are connecting to')
            print(self.IP)
            print('as username')
            print(self.username)
            portnumber = input('please enter the port name of the remote jupyter server: ')
            inputnumber = input('please enter the port of the localhost: ')
            line= self.username+'@'+self.IP
            host = 'localhost:'+inputnumber+':localhost:'+portnumber
            call(['ssh','-N','-f','-L',host,line,'-i',self.passcode])
            localhostip = 'localhost:'+inputnumber
            webbrowser.open(localhostip)




if __name__ == '__main__':
    runner = connecter()
    runner.setparameter()
    runner.run()
