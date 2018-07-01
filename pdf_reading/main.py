#!/usr/bin/python3

import PyPDF2

#open the pdf
pdf_object = open('Harry_Potter_and_the_Sorcerers_Stone.pdf','rb')

pdfreader = PyPDF2.PdfFileReader(pdf_object)
count = pdfreader.numPages

# print no of pages
print(count)


for i in range(40,60):
	page = pdfreader.getPage(i)
	print(page.extractText())

