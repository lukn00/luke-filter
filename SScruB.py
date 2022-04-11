import os
import glob
import pandas as pd
import datetime
import re
import winsound
import csv
import sys
import time



# get date for export files
current_date = datetime.datetime.now()
date = str(current_date.month)+"_"+str(current_date.day)+"_"+str(current_date.year)
##

#initial directory loads
tic = time.perf_counter()

filters = 'g:/my drive/git/luke-filter/' #### location of ZIP LIST directory
extension = 'csv' ### extension of files to join - keep as csv
scrubs = ['/My Drive/Git/luke-filter/scrub/*.{}'.format(extension)] ### location of FILES TO JOIN AND FILTER

pwcfile = '/My Drive/Git/luke-filter/pwc_filter_mod.csv' ### location of 'modded' pwc_filter csv for dictionary import
pwcvfile = '/My Drive/Git/luke-filter/pwc_verify.csv' ### location of 'modded' pwc_filter csv for dictionary import


toc = time.perf_counter()
print(f" Directory Loads in {toc - tic:0.2f} seconds")


###rawtimer save to copy paste
#tic = time.perf_counter()  # nanoseconds: time.perf_counter_ns()
#toc = time.perf_counter()

#print(f" THREAD IN {toc - tic:0.4f} seconds")
###


#prep glob
tic = time.perf_counter()
files = glob.glob('/My Drive/Git/luke-filter/scrub/*.{}'.format(extension))
df2 = pd.DataFrame()

for f in files:
    df2 = df2.append(pd.read_csv(f))


df = df2.iloc[: , [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]].copy()

df.columns=['CompanyName','First','Last','Phone','Fax','CellPhone','Website URL','Email','Address 1','Address 2','City','Zip','PWC','Source','Comments']#company=(Required) #phone = (RequiredifnoEmail) #email = (Required if no Business Phone) #pwc = (ID or Description)    
#df = df3.rename( columns={0 :'CompanyName',1 :'First',2 :'Last',3 : 'Phone',4 : 'Business Fax',5 : 'CellPhone',6 : 'Website URL',7 : 'Email',8 : 'Address 1',9 : 'Address 2',10 : 'City',11 : 'Zip',12 : 'PWC',13 : 'Source',14 : 'Comments'}, inplace=True )
print(df)
toc = time.perf_counter()

print(f" Globbed in {toc - tic:0.2f} seconds")
## end glob

#prep pwc dictionary
tic = time.perf_counter()
pwcmaster = dict()
f = open(pwcfile)
for line in f:
    line = line.strip('\n')
    (key, val) = line.split(",")
    pwcmaster[key] = val

pwcverify = dict()
f2 = open(pwcvfile)
for line in f2:
    line = line.strip('\n')
    (key, val) = line.split(",")
    pwcverify[key] = val
    
#apply pwc mod
df['CompanyNamePWC'] = df['CompanyName'].replace('[0-9]','', inplace=False, regex=True)
df['PWC1'] = df['CompanyNamePWC'].replace(pwcmaster, inplace=True, regex=True)
df['PWC1'] = df['CompanyNamePWC'].replace('^.*tndodntint', '', inplace=True, regex=True)
df['PWC1'] = df['CompanyNamePWC'].replace('dnmitaodbyatagwk.*$', '', inplace=True, regex=True)
df['PWC1'] = df['CompanyNamePWC'].replace('[^0-9]','', inplace=True, regex=True)
df['PWC1'] = df['CompanyNamePWC'].replace('','No PWC Found', inplace=True, regex=True)

df['PWC1'] = df['CompanyNamePWC'].replace(pwcverify, regex=True)

df['PWCPWC'] = df['PWC'].replace('[0-9]','', inplace=False, regex=True)
df['PWC2'] = df['PWCPWC'].replace(pwcmaster, inplace=True, regex=True)
df['PWC2'] = df['PWCPWC'].replace('^.*tndodntint', '', inplace=True, regex=True)
df['PWC2'] = df['PWCPWC'].replace('dnmitaodbyatagwk.*$', '', inplace=True, regex=True)
df['PWC2'] = df['PWCPWC'].replace('[^0-9]','', inplace=True, regex=True)
df['PWC2'] = df['PWCPWC'].replace('','No PWC Found', inplace=True, regex=True)


df['PWC2'] = df['PWCPWC'].replace(pwcverify, regex=True)

#df['CommentsPWC'] = df['Comments'].replace('[0-9]','', inplace=False, regex=True)
#df['PWC3'] = df['CommentsPWC'].replace(pwcmaster, inplace=True, regex=True)
#df['PWC3'] = df['CommentsPWC'].replace('^.+?tndodntint', '', inplace=True, regex=True)
#df['PWC3'] = df['CommentsPWC'].replace('dnmitaodbyatagwk.+?$', '', inplace=True, regex=True)
#df['PWC3'] = df['CommentsPWC'].replace('[^0-9]','', inplace=True, regex=True)
#df['PWC3'] = df['CommentsPWC'].replace('','No PWC Found', inplace=True, regex=True)


#df['PWC3'] = df['CommentsPWC'].replace(pwcverify, regex=True)

## ye old ones not regex friendly
####df['PWCCompany'] = df['CompanyName'].map(pwc_map)
####df['PWCPWC'] = df['PWC'].map(pwc_map)
####df['PWCComments'] = df['Comments'].map(pwc_map)
toc = time.perf_counter()
print(f" PWC Applied in {toc - tic:0.2f} seconds")
## end of PWC


#start of scoring
tic = time.perf_counter()

firstcolumn = df.columns[0]
secondcolumn =  df.columns[14]

pro2=pd.read_csv("G:\My Drive\Git\luke-filter\_pros.csv")
pro=pro2[pro2.columns[0]]

con2=pd.read_csv("G:\My Drive\Git\luke-filter\_cons.csv")
con=con2[con2.columns[0]]

bad2=pd.read_csv("G:\My Drive\Git\luke-filter\_bads.csv")
bad=bad2[bad2.columns[0]]

    #dfs['Pro Name'] = str(dfs['Pro Name'])
    #dfs['Con Name'] = str(dfs['Con Name'])
    #dfs['Bad Name'] = str(dfs['Bad Name'])
    
df['Pro Name'] = df[firstcolumn].str.count('|'.join(pro))
df['Con Name'] = df[firstcolumn].str.count('|'.join(con))
df['Bad Name'] = df[firstcolumn].str.count('|'.join(bad))
    
df['Pro Count'] = df[secondcolumn].str.count('|'.join(pro))
df['Con Count'] = df[secondcolumn].str.count('|'.join(con))
df['Bad Count'] = df[secondcolumn].str.count('|'.join(bad))
#df['Local Count'] = df[secondcolumn].str.count('|'.join(local))

df['Score'] = (df['Pro Name']*3) - (df['Con Name']*2) - (df['Bad Name']*13)
df['Score2'] = (df['Pro Count']*3) - (df['Con Count']*2) - (df['Bad Count']*13)
df['Score3'] = 0 + (df['Pro Name']*3) - (df['Con Name']*2) - (df['Bad Name']*13) + (df['Pro Count']*3) - (df['Con Count']*2) - (df['Bad Count']*13)

toc = time.perf_counter()
print(f" Scoring done in {toc - tic:0.2f} seconds")
## end of scoring

## start of zip applicator
tic = time.perf_counter()

df['Phone'] = df['Phone'].replace('(','')
df['Phone'] = df['Phone'].replace(')','')
df['Phone'] = df['Phone'].replace('-','')
df['Phone'] = df['Phone'].replace('+','')
df['Phone'] = df['Phone'].replace('"','')
df['Phone'] = df['Phone'].replace('\.','')
df['Phone'] = df['Phone'].replace('_','')
df['Phone'] = df['Phone'].replace('\/','')
df['Phone'] = df['Phone'].replace('\\','')
df['Phone'] = df['Phone'].replace(' ','')
#df['Phone'] = df['Phone'].replace({'^1':''}, regex=True, inplace=True)

zip_list = pd.read_csv(os.path.join(filters,'area_to_zip.csv'),header=None, dtype={0:str}).set_index(0).squeeze().to_dict()


df['Zip'] = 'NoFind'

df['Zip'] = df['Phone'].str[:6].map(zip_list)


toc = time.perf_counter()
print(f" Zip Codes done in {toc - tic:0.2f} seconds")

### FINAL TUNING SECTION

tict = time.perf_counter()
df['ScoreResults'] = ''
df['Canada'] = ''

def adjustscore(df_line):
#    for line in df_line:
#    print('adjusting score')
    if df_line['Score3'] <= 0:
        return "Bad"
    elif df_line['Score2'] <= -1:
        return "Bad"
    elif df_line['Score'] <= 0:
        return "Bad"
    else:
        return "Pass"

def adjustpwc(df_line):
#    print('adjusting pwc')
    if df_line['PWC1'] is not None:
        if df_line['PWC1'] == "No PWCV Found":
            if df_line['PWC2'] is not None:
                
                if df_line['PWC2'] == "No PWCV Found":
        #            if df_line['PWC3'] == "No PWCV Found":
                    return "No PWC Found"
                    print('No PWCV Found')
        #            else:
        #                return df_line['PWC3']
        #                print('pwc 3 found')
                else:
                    return df_line['PWC2']
                    print('pwc 2 found')
        else:
            return df_line['PWC1']
            print('pwc 1 found')

#def adjustzip(df_line): bad
#    print('adjusting zip')

#    if df_line['Zip'] is not None:
        
#        return df_line['Zip']
#    else:
#        return "No Zip Found"
    

def canadacheck(df_line):
#    print('Checking for Canadians')
    if df_line['Address 2'] != type(float):
        if len(df_line['Address 2']) >= 7:
            if "Canada" in df_line['Address 2']:
                return "Canada"
    elif df_line['Comments'] != type(float):
        if "Canada" in df_line['Comments']:
            return "Canada"
    elif df_line['Address 1'] != type(float):
        if "Canada" in df_line['Address 1']:
            return "Canada"
    elif df_line['Fax'] != type(float):
        if "Canada" in df_line['Fax']:
            return "Canada"
    else:
        return ''

#zip code second level not needed
#tic = time.perf_counter()
#df['Zippy'] = df['Zip']
#df['Zippy'] = df.apply(adjustzip, axis=1)
#toc = time.perf_counter()
#print(f" Zip Codes adjusted in {toc - tic:0.2f} seconds")

tic = time.perf_counter()
df['ScoreResults'] = df.apply(adjustscore, axis=1)
toc = time.perf_counter()
print(f" Scoring adjusted in {toc - tic:0.2f} seconds")

tic = time.perf_counter()
df['PWC'] = df.apply(adjustpwc, axis=1)
toc = time.perf_counter()
print(f" PWC adjusted in {toc - tic:0.2f} seconds")

#df['Canada'] = df.apply(canadacheck, axis=1)



toct = time.perf_counter()
print(f" Final tuning done in {toct - tict:0.2f} seconds")
##begin export
tic = time.perf_counter()

scrubbed_csv = df

scrubbed_csv.sort_values("Score", inplace = True)

scrubbed_csv.to_csv ("SCRUBBED_" + date + ".csv", index=False, encoding='utf-8-sig')


toc = time.perf_counter()
print(f" {len(df['CompanyName'])} records exported in {toc - tic:0.2f} seconds")


## end export

### end of version whatever.itis by lukenielson

