import os, sys
import shutil
import time
import datetime

# now = time.strftime("%c")
i = datetime.datetime.now()
j=2
lis = []

foldername='Cleanup '+time.strftime("%s-%s-%s" % (i.month, i.day, i.year))
destinationdir=('F:\\INbox\\{0}'.format(foldername))
destinationdir2=destinationdir

while os.path.exists(destinationdir2):
    destinationdir2=destinationdir+" ("+str(j)+")"
    if j < 11:
        j+=1
    else:
        exit()
os.makedirs(destinationdir2)

lis=os.listdir('C:\\Users\\Ryu\\Desktop')  # os.path.abspath(__file__)
for x in lis:                                  #[filename for filename in files if not filename.startswith("doc")]
    # if not x.startswith("DesktopCleaner"):
        # print(x)
    # if x == __file__:   # name of app   and x != "DesktopCleaner.pyw"    and (not x.startswith("DesktopCleaner"))
    #     continue
    if x.startswith("Desktop"):
        continue
    print(x)
    shutil.move(x, destinationdir2)

    def menu_background_activate_cb(self, menu, file):
        os.system("xte 'keydown F5' 'keyup F5'")

    # 'C:\\Users\\Ryu\\Desktop\\aaa'

# for file in lis:     # vypis
#    print (file)
