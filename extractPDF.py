import pdfplumber

def extractPDF(fp):
    pdf = pdfplumber.open(fp)
    page = pdf.pages[0]
    return(page.extract_text(x_tolerance = 1))