import os
import glob
import sastrawi as stw
import extractPDF as pdf
import tokenPDF as tkn
import key as anskey

import time
start_time = time.time()

i = 0

#Process key
anskey.processKey(anskey.getKey())

#Get answer path
path = os.getcwd()+'\\answer\*'

#Main code
for filepath in glob.glob(path):

    #Open input path
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
    ouput = open(os.getcwd()+'\\output\output'+str(i)+'.txt', "w")
    ouput.write(' '.join(ePDF))
    ouput.close
    i = i + 1
print("--- %s seconds ---" % (time.time() - start_time))