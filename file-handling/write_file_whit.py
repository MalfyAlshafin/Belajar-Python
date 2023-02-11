Motor = ["Honda","Suzuki","Yamaha",]

with open("intermediate.txt", "w") as file:
    file.write("Nama merek motor terkenal")
    file.write("\n")
    file.write("===========================")
    file.write("\n")
    file.write("\n")
    for Motor in Motor:
        file.write(Motor)
        file.write("\n")