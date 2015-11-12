'''
Usage: python3 usb_eject.py
OS: Window7 and later
Eject the usb storage when the usb device plugin your PC!
'''
from time import sleep
import http.client
import subprocess

def monitorUSBStorage():
    label = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
    'T','U','V','W','X','Y','Z']
    monitorDisk = []
    for i in label:
        try:
            file = open(i+':/')
        except Exception as e:
            '''
            error = 2  =>not found
            error = 13 =>permission denied (exist!)
            '''
            if(e.errno == 13):
                print("Disk : "+i+" Exist!")
            else:
                monitorDisk.append(i)

    print("Start monitoring.....")
    while(True):
        print("Check...")
        isININ = False;
        disk = '';
        for i in monitorDisk:
            try:
                file = open(i+':/')
            except Exception as e:
                if(e.errno == 13):
                    print("Disk : "+i+" Exist!")
                    isININ = True
                    disk = i
                    break
        if(isININ):
            tmpFile = open('tmp.ps1','w')
            tmpFile.write('$driveEject = New-Object -comObject Shell.Application\n')
            tmpFile.write('$driveEject.Namespace(17).ParseName("'+disk+':").InvokeVerb("Eject")')
            tmpFile.close()
            process = subprocess.Popen(['powershell.exe', '-ExecutionPolicy','Unrestricted','./tmp.ps1'])
            process.communicate()
        #sleep for 2 seconds
        sleep(2)

if __name__ == '__main__':
    monitorUSBStorage()
