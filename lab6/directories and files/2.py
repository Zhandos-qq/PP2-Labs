import os
path=r"C:\Users\ATYRAU\OneDrive\Документы\KBTU PP2 Codes\lab6"
allDirs = os.listdir(path)
for item in allDirs:
    if  os.path.isfile(os.path.join(path,item)):
        print(f"only file= {item}")