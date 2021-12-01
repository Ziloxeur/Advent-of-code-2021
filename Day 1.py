#First and Second stars in python

nombre = []
measurements = 0

fichier = open('C:/Users/Eddy Amani/OneDrive/Documents/Advent code/nombre.txt', "r")
for i  in fichier.readlines():
    nombre.append(int(i.replace("/n","")))

for i in range(0,1997):
    if nombre[i]+nombre[i+1]+nombre[i+2] < nombre[i+1]+nombre[i+2]+nombre[i+3]:
        measurements += 1
print(measurements) 
