import os
import glob
import convertPDF as doc
import extractPDF as pdf
import tokenPDF as tkn
import key as anskey

import time
start_time = time.time()

#Process key
anskey.processKey(anskey.getKey())

#Get DOCX answers path
pathDOCX = os.getcwd()+'\\answer\*.docx'

#Convert Words
doc.convertDOCX(pathDOCX)

#Get PDF answers path
pathPDF = os.getcwd()+'\\answer\*.pdf'

fn_i = 1
#Main code
for filepath in glob.glob(pathPDF):

    #Get input name
    file_name = os.path.basename(filepath)
    file_name = os.path.splitext(file_name)[0]

    #Open input path
    print(filepath)
    fp= open(filepath, 'rb')

    #Get PDF
    ePDF = pdf.extractPDF(fp)

    #Tokenize
    ePDF = tkn.tokenPDF(ePDF,file_name)

    #Lemmatizing
    ePDF = tkn.ligma(ePDF)

    #Stemming
    #ePDF = [stw.stemmer.stem(tokens) for tokens in ePDF]

    #Export output
    ouput = open(os.getcwd()+'\\output\\'+ str(fn_i).zfill(3) + "_" + str(file_name)+'.txt', "w")
    ouput.write(' '.join(ePDF))
    ouput.close
    fn_i += 1

print("--- %s seconds ---" % (time.time() - start_time))