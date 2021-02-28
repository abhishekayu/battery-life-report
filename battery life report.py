import os
os.system('powercfg /batteryreport') # Battery life Command  run on Win shell
"By : Abhishek Patel @imdarkcoder"
import shutil
# move report file one dir to another dir // In your case dir path may be diffrent
shutil.move('C:/Users/abhishekpatel/battery-report.html', 'C:/Users/abhishekpatel/Desktop/battery-report.html')
import webbrowser
# Open report file on web
url = 'file:///C:/Users/abhishekpatel/Desktop/battery-report.html'
webbrowser.open(url, new=1)