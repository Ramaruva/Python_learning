st = "Hey you are amazing"

f = open("myfile.txt","w")
f.write(st)
f.close()

f = open("file.txt")
lines = f.readlines()
print(lines,type(lines))
f.close()

with open("file.txt") as f:
    print(f.read())