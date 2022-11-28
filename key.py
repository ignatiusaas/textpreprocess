import os
import glob
#import sastrawi as stw
import extractPDF as pdf
import tokenPDF as tkn

#Get key path
def getKey():
    path = os.getcwd()+'\\key\*.pdf'
    return(path)

def processKey(path):
#Main code
    for filepath in glob.glob(path):

        #Open key path
        print(filepath)
        fp= open(filepath, 'rb')
        
        #Get PDF
        ePDF = pdf.extractPDF(fp)

        #Tokenize
        ePDF = tkn.tokenPDF(ePDF, fn = 'Ligma')

        #Lemmatizing
        ePDF = tkn.ligma(ePDF)

        #Stemming
        #ePDF = [stw.stemmer.stem(tokens) for tokens in ePDF]

        #Export output
        ouput = open(os.getcwd()+'\\key\key'+'.txt', "w")
        ouput.write(' '.join(ePDF))
        ouput.close