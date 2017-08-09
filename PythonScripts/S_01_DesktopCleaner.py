import os
import shutil
import time
import datetime


# now = time.strftime("%c")
i = datetime.datetime.now()
j=2

foldername='Cleanup '+time.strftime("%s-%s-%s" % (i.month, i.day, i.year))
destinationdir=('C:\\Users\\Ryu\\Desktop\\{0}'.format(foldername))
destinationdir2=destinationdir

while os.path.exists(destinationdir2):
    destinationdir2=destinationdir+" ("+str(j)+")"
    if j < 11:
        j+=1
    else:
        exit()
os.makedirs(destinationdir2)

lis=os.listdir('C:\\Users\\Ryu\\Desktop')  #os.path.abspath(__file__)
for x in lis:
    print(x)
    if x == __file__ and x != "DesktopCleaner.pyw":
        continue
    shutil.move(x,destinationdir2)