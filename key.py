import os
import glob
import sastrawi as stw
import extractPDF as pdf
import tokenPDF as tkn

#Get key path
def getKey():
    path = os.getcwd()+'\\key\*'
    return(path)

def processKey(path):
#Main code
    for filepath in glob.glob(path):

        #Open key path
        print(filepath)
        fp= open(filepath, 'rb')
        
        #Get PDF
        ePDF = pdf.convert_pdf_to_txt(fp)

        #Tokenize
        ePDF = tkn.tokenPDF(ePDF)

        #Stemming
        ePDF = [stw.stemmer.stem(tokens) for tokens in ePDF]

        #Print test
        #print(ePDF)

        #Export output
        ouput = open(os.getcwd()+'\\key\key'+'.txt', "w")
        ouput.write(' '.join(ePDF))
        ouput.close