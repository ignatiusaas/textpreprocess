from docx2pdf import convert
import glob
import os
from win32com.client import Dispatch, constants, gencache
import shutil

def convertDOCX(fp):
    for filepath in glob.glob(fp):
        #Get input name
        file_name = os.path.basename(filepath)
        file_name = os.path.splitext(file_name)[0]

        convert(filepath,os.getcwd()+'\\answer\\')

        shutil.move(str(filepath),os.getcwd()+'\\docx\\')
