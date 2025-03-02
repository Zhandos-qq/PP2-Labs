file_path=r"C:\Users\ATYRAU\OneDrive\Документы\KBTU PP2 Codes\lab6"
array=["apple","banana","chery"]

with open(file_path,"w") as file:
    for item in array:
        file.write(item+" ")