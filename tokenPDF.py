from nltk.corpus import stopwords
import string

def tokenPDF(ePDF):
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
    return(ePDF)