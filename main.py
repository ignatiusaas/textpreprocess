import extractPDF as pdf
import sastrawi as stw
from nltk.corpus import stopwords
import string

#nltk.download()

#Get PDF
ePDF = pdf.pagehandle.extract_text()

#Case Folding
ePDF = ePDF.lower()

#Tokenize
ePDF = ePDF.strip()
ePDF = ePDF.translate(str.maketrans("","",'1234567890'))
ePDF = ePDF.translate(str.maketrans("","", string.punctuation))

stop_words = set(stopwords.words('indonesian'))
from nltk.tokenize import word_tokenize
tokens = word_tokenize(ePDF)
ePDF = [i for i in tokens if not i in stop_words]

#Stemming
ePDF = [stw.stemmer.stem(tokens) for tokens in ePDF]

#Print test
#print(ePDF)

#Export output
ouput = open("output.txt", "w")
ouput.write(' '.join(ePDF))
ouput.close