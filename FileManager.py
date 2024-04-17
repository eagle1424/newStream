
fich = open("test.txt", "r")
data = fich.read()

# print(int(15) + int(data))

fich.close()

fich = open("test.txt", "w")
fich.write("moi")

fich.close()