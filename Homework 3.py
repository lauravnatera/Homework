fp = open("Game of Thornes.txt","r")

punt = [".","?","!",";",":",","," "]
for liner in fp:
    for p in punt:
        liner = liner.replace(p, "")

    print(liner)