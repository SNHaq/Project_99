import time, os, shutil

dayNumber = input("Please enter how frequently would you like to clear your files (in days): ")
time.time(dayNumber)

while True: 
    os.walk(path)

os.path.join()
cTime = os.stat(path).st_cTime

if cTime > dayNumber:
    if path == file:
        os.remove(path)
    elif path == folder: 
        shutil.rmtree()
else: 
    print("ERROR! File not found.")
