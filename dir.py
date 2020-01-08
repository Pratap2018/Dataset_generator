import os
string=os.getcwd()
string=string+'/pratap'
try:
    os.rmdir(string)
except:
    print(string)
if string:
    os.rmdir(os.getcwd() +'/pratap2')