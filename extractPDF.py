import PyPDF2

fhandle = open('input.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(fhandle)
pagehandle = pdfReader.getPage(0)
print(pagehandle.extractText())