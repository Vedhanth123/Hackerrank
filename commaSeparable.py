# 1) to remove comma from entries

entry = ['10,300','2,351']

a = str(10,300)
b = str(20,300)

string = entry[0]

string = string.replace(',','')

print(string)

entry[0] = string

print(entry[0])
