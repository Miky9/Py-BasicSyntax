# otevře csv s hodnotami, udělá 2 nové csv

csvpath = 'C:\\Users\\Miky\\Desktop\\Sheet1.csv'
#print(csvpath, csvpath, sep='')
f = open (csvpath, 'r', encoding='utf8')
matice = []
muzi = []
zeny = []
#text = f.read()

for line in f:
    line = line.rstrip()
    # print (line.split(','))
    # matice.append (line.split(','))
    # print(matice)
    values = line.split(',')
    if values[1] == 'muž':
        muzi.append(values)
    if values[1] == 'žena':
        zeny.append(values)


f.close()

def klic(radek):
    return radek[1]

muzi.sort(key=klic)
zeny.sort(key=klic)

muzicsv = open ('C:\\Users\\Miky\\Desktop\\novecsv.csv', 'w+', encoding='utf8')
zenycsv = open ('C:\\Users\\Miky\\Desktop\\novecsv.csv', 'w+', encoding='utf8')

# matice.sort(key=klic)
# print (matice)

# f = open ('C:\\Users\\Miky\\Desktop\\novecsv.csv', 'w+', encoding='utf8') #w+ =vytvořit nový soubor

# for line in matice:
#     f.write (','.join(line))
#     f.write('\n')
#
# f.close()

def ulozcsv(matice,cesta):
    f = open (cesta, 'w+', encoding = 'utf8')

    for line in matice:
        f.write (','.join(line))
        f.write('\n')


    f.close()

ulozcsv(zeny, 'C:\\Users\\Miky\\Desktop\\zeny.csv')
ulozcsv(muzi, 'C:\\Users\\Miky\\Desktop\\muzi.csv')