fp = open("harry potter.txt","r")
fp2= open("Game of Thornes.txt","w")
list = []
fp_contents = fp.read()
punt = [".","?","!",";",":",",", "-","/"]
line= " "
for p in fp_contents:
    if p  not in punt:
        line = line + p
line = line.split ()

for x in line:
    if x not in list:
        list.append(x)
        fp2.write(str(x) + "\n")

print("There are",len(list),"words")

