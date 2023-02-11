a = open("file a.txt","x")

b = open("file a.txt", "r")
print(b.read())

c = open("file a.txt", "w")
c.write("ini adalah file a.txt")
c.close()

d = open("file a.txt", "r")
print(d.read())

e = open("file a.txt", "a")
e.write("\n Ini adalah teks yang dibuat dengan append")
e.close()

f = open("file a.txt", "r")
print(f.read())