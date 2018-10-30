

# #Getting all the actions:
# f = open(r'C:\MONAST\logs\test.log','r')
# fout = open(r'C:\MONAST\logs\action.log','w')
# line = f.readline()
#
# while line:
#     if 'MSG OUT: {\'action\'' in line:
#         fout.write(line)
#     line = f.readline()
#
# f.close()
# fout.close()


#Getting all actions from ListCommand

f = open(r'C:\MONAST\files\all_actions.txt','r')
fout = open(r'C:\MONAST\files\all_commands.txt','w')

line = f.readline()

while line:
    if '\'' in line:
        data = line.split('\'')[1]+ '\n'
        fout.write(data)
    line = f.readline()


f.close()
fout.close()