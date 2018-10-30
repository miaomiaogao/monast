#1. copy the file which you want to run
#2. paste it here
#3. run test.py
#4. OK, done


f = open(r'C:\MONAST\logs\test.log','r')
fout = open(r'C:\MONAST\files\all_Hangup.txt','w')

line = f.readline()

while line:
    if 'Incoming Message' in line:
        if 'Hangup' in line:
            fout.write(line)
    line = f.readline()


f.close()
fout.close()
