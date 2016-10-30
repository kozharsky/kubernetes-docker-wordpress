import subprocess
import os

keyhome = "/home/dima/tocopy/Andrey/semigaylo.pem"
ip = "52.57.229.220"

prog = subprocess.Popen(["ssh", "-o", "StrictHostKeyChecking=no", "-i", keyhome, "ec2-user@"+ip, "docker info | grep Running"], stdout=subprocess.PIPE)
res = prog.stdout.readline()
res = res.split()

if(res[1] == '2'):
    print ('Running: ' + res[1])
    exit(0)
else:
    print ('Running: ' + res[1])
    exit(1)




