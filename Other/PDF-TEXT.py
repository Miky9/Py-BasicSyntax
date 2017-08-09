# import pyPdf
#
# pdf = pyPdf.PdfFileReader(open("C:\Users\Mikeska\Desktop\Kurz E2\idrive\IDrive-Sync\programatorska-cvicebnice-kopie.pdf", "rb"))
# for page in pdf.pages:
#     print page.extractText()
#
# import PyPDF2
# import textwrap

# pdf_file = open('C:\\Users\\Mikeska\\Desktop\\Kurz E2\\idrive\\IDrive-Sync\\programatorska-cvicebnice-kopie.pdf', 'rb')
# read_pdf = PyPDF2.PdfFileReader(pdf_file)
# number_of_pages = read_pdf.getNumPages()
# page = read_pdf.getPage(7)
# page_content = page.extractText()
# x = page_content.encode('UTF-8')
# s = str(x)

# filename = 'TEXT.txt'
# s = open(filename, 'r')


# print(textwrap.fill(str(x), width=80))

# s = s.replace('xa1', '')
# s = s.replace("xc3", "á")
# s = s.replace("xc5", "š")
# s = s.replace("áxad", "í")
# s = s.replace("áxa9", "é")
# s = s.replace("áxbd", "ý")
# s = s.replace("šxbe", "ž")
# s = s.replace("ráx8f", "ř")


# print(str(s))

# PDF-TEXT 2

# s = """1.	Pro  zadane´  cˇ´ıslo  vypocˇ´ıtejte  posloupnost  vygenerovany´ch  cˇ´ısel
# a  tuto posloupnost zobrazte graficky (podobneˇ jako na obra´zku 3.1 A).
# 2.	Pro  cˇ´ısla  od  1  do  n vypocˇ´ıtejte,  kolik  kroku˚  potrˇebujeme,  nezˇ  se  do-
# staneme do jednicˇky. Hodnoty vykreslete grafem – pro male´  n vypada´   vy´ sledny´ graf vcelku na´ hodneˇ,
# pro velke´ n se vsˇak objev´ı zaj´ımava´ struk- tura (viz obra´ zek 3.1 B).
# 3.	Podobneˇ  jako prˇedchoz´ı bod, nezobrazujte vsˇak pocˇet kroku˚ , ale maxi-
# ma´ ln´ı hodnotu, na kterou v pru˚ beˇhu vy´ pocˇtu naraz´ıme (naprˇ. pro zacˇa´ tek v cˇ´ısle 7 je touto maxima´ ln´ı hodnotou 52).
# 4.	Pro ktere´ cˇ´ıslo od 1 do 100 000 potrˇebujeme nejv´ıce kroku˚ , nezˇ dospeˇjeme
# do jednicˇky? Jake´  je maxima´ ln´ı cˇ´ıslo, ktere´  se v prˇ´ıslusˇne´  posloupnosti objev´ı?"""

s = open("INPUT.txt", "r").read()

# with open('INPUT.txt', 'r') as s:
#     ss = s.read().encode('UTF-8')
#
# s = str(ss)
# print(str(ss))

s = s.replace("a´ ", "á")
s = s.replace("a´", "á")
s = s.replace("e´", "é")
s = s.replace("´?", "í")
# s = s.replace("y´ ", "ý")
s = s.replace("y´", "ý")
s = s.replace("u?", "ů")
s = s.replace("cˇ", "č")
s = s.replace("eˇ", "ě")
s = s.replace("rˇ", "ř")
s = s.replace("zˇ", "ž")
s = s.replace("sˇ", "š")

s = str(s)


text_file = open("OUTPUT.txt", "w")
text_file.write(s)
text_file.close()

# print(s.format())