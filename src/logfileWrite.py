

DEFULT_FILE = "/var/log/apache2/"
NEW_FILE = "/home/kali/Desktop/project/ThreatWatch-Log-Analysis-Automation-Tool/logs/"
def writeLog(FILE):

    accessFile = DEFULT_FILE + "access.log"
    errorFile = DEFULT_FILE + "error.log"   

    newAccessFile = NEW_FILE + "access.log"
    newErrorFile = NEW_FILE + "error.log"

    with open(accessFile, 'r') as readfile:
        for line in readfile:
            with open(newAccessFile, 'a') as writefile:
                writefile.write(line)
    print("Done writing access log")

    with open(errorFile, 'r') as readfile:
        for line in readfile:
            with open(newErrorFile, 'a') as writefile:
                writefile.write(line)
    print("Done writing error log")

    



writeLog(DEFULT_FILE)