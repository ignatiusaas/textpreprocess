from openpyxl import load_workbook
import os
import glob
import tokenPDF as tkn
import key as anskey
import string

import time
start_time = time.time()

blacklist = ['mail', 'ugm', 'ac', 'id']

#Get answers path
path = os.getcwd()+'\\answer\*.xlsx'

#Main code
for filepath in glob.glob(path):

    file_name = os.path.basename(filepath)
    file_name = os.path.splitext(file_name)[0]

    output_path = os.getcwd()+'\\'+str(file_name)
    os.mkdir(output_path)

    wb = load_workbook(filepath)
    for sheet_title in wb.sheetnames:
        ws = wb[sheet_title]
        all_columns = list(ws.columns)
    ws_column = 9
    ws_row = 2
    fn_i = 1
    for row in range(1,ws.max_row):
        if(ws.cell(row,1).value is None):
            break
        new_answ = ''
        fn = ws.cell(ws_row,3).value
        fn = fn.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
        fn = ''.join(fn)
        fn = fn.split()
        fn = [i for i in fn if not i in blacklist]
        fn = ''.join(fn)

            #print(new_fn)
        for column in range(ws_column,ws.max_column):
            if(ws.cell(ws_row,column).value is None):
                break
            answ = ws.cell(ws_row,column).value
            new_answ = new_answ + answ
            #print(new_answ)
        ws_row += 1
        fin_ans = tkn.tokenPDF(new_answ,'')
        fin_ans = tkn.ligma(fin_ans)

        #Export output
        ouput = open(output_path + '\\' + str(fn_i).zfill(3) + '_' + str(fn)+'.txt', "w")
        ouput.write(' '.join(fin_ans))
        ouput.close
        fn_i += 1
print("--- %s seconds ---" % (time.time() - start_time))
