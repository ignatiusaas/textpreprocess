from nltk.corpus import stopwords
import string

def tokenPDF(ePDF,fn):
    #Case Folding
    ePDF = ePDF.lower()
    fn = fn.lower()

    #Tokenize
    fn = fn.strip()
    fn = fn.translate(str.maketrans("","",'1234567890'))
    fn = fn.translate(str.maketrans("","", string.punctuation))

    ePDF = ePDF.strip()
    ePDF = ePDF.translate(str.maketrans("","",'1234567890'))
    ePDF = ePDF.translate(str.maketrans("","", string.punctuation))

    #Remove stopwords
    stop_words = set(stopwords.words('indonesian'))
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(ePDF)
    ePDF = [i for i in tokens if not i in stop_words]

    #Remove name
    ePDF = [i for i in ePDF if not i in fn]

    #Remove dupe clause
    ePDF = list(dict.fromkeys(ePDF))

    return(ePDF)