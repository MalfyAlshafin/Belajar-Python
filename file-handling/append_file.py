Motor = ["Ducati","Kawasaki"]

with open("intermediate.txt","a") as file:
    for Motor in Motor:
        file.write(Motor)
        file.write("\n")