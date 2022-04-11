import pandas as pd
import numpy as np
import csv
import datetime
import glob2
from tqdm import tqdm
import winsound
import os
import time
import re

#    start_epoch_sec = int(time.time())
#    #df['result'] = df.apply(lambda row: divide(row['A'], row['B']), axis=1)
#    end_epoch_sec = int(time.time())
#    result_apply = end_epoch_sec - start_epoch_sec


current_date = datetime.datetime.now()
date = str(current_date.month)+ '_' + str(current_date.day) + '_' + str(current_date.year)


def scorefind(c):   #(this one will be scoring)
    start_epoch_sec = int(time.time())
    #df['result'] = df.apply(lambda row: divide(row['A'], row['B']), axis=1)
    
    data = {'first_column':  [str(c)],
            }

    dfs = pd.DataFrame(data)

    firstcolumn = dfs.columns[0]
        
    pro2=pd.read_csv("G:\My Drive\Git\luke-filter\_pros.csv")
    pro=pro2[pro2.columns[0]]

    con2=pd.read_csv("G:\My Drive\Git\luke-filter\_cons.csv")
    con=con2[con2.columns[0]]

    bad2=pd.read_csv("G:\My Drive\Git\luke-filter\_bads.csv")
    bad=bad2[bad2.columns[0]]

    #dfs['Pro Name'] = str(dfs['Pro Name'])
    #dfs['Con Name'] = str(dfs['Con Name'])
    #dfs['Bad Name'] = str(dfs['Bad Name'])
    
    dfs['Pro Name'] = dfs[firstcolumn].str.count('|'.join(pro))
    dfs['Con Name'] = dfs[firstcolumn].str.count('|'.join(con))
    dfs['Bad Name'] = dfs[firstcolumn].str.count('|'.join(bad))
    
    #df['Pro Count'] = df[secondcolumn].str.count('|'.join(pro))
    #df['Con Count'] = df[secondcolumn].str.count('|'.join(con))
    #df['Bad Count'] = df[secondcolumn].str.count('|'.join(bad))
    #df['Local Count'] = df[secondcolumn].str.count('|'.join(local))

    dfs['Score'] = (dfs['Pro Name']*3) - (dfs['Con Name']*2) - (dfs['Bad Name']*13)
    dfs['Score'] = dfs['Score'].replace('Name: Score, dtype: int64','')
    
    #df['Score2'] = (df['Pro Name']*3) + (df['Pro Count']*3) - (df['Con Name']*2) - (df['Con Count']*2) - (df['Bad Name']*13) - (df['Bad Count']*13)

    
    #score = str(df['Score'])
    return(dfs['Score'])
    end_epoch_sec = int(time.time())
    result_apply = end_epoch_sec - start_epoch_sec
    print("ScoreFind Results in " + str(result_apply))
    
def pwcfind(p):   #(this one will be pwc
    p = str(p)


    #df['result'] = df.apply(lambda row: divide(row['A'], row['B']), axis=1)
    
    data = {'first_column':  [str(p)],
            }
    dfp = pd.DataFrame(data)

    pwc_filter = pd.read_csv(os.path.join('G:\\My Drive\\Git\\filters\\','pwc_filter.csv'))

    dfp['pwclist'] = '0'
            # print('Filtering Pwc ...')
    for row in pwc_filter.itertuples(index=False):
        term = row[0]
        pwc = row[1]
        if term is not None:
            if term in p:
                dfp['pwclist'] = pwc
                break
    
    return(dfp['pwclist'])

def zipfind(z):    #(this one will be zip
    
    start_epoch_sec = int(time.time())
    
    ziplist = pd.read_csv(os.path.join('G:\\My Drive\\Git\\filters\\','area_to_zip.csv'))

    zipdict = {row[0] : row[1] for _, row in pd.read_csv(ziplist).iterrows(index=False)}

    data = {'first_column':  [str(z)],
            }
    dfz = pd.DataFrame(data)
    dfz['second_column'] = ''
    

    for zs in z:
        search = zs
        values = [value for value in zipdict.values() if search in value]
        dfz['second_column'] = value
        
    #if z in zipdict[0]
    
    
    
    #df['Z'] = df.apply(lambda x: x. in x.B, axis=1)
    
    ziplist = pd.read_csv(os.path.join('G:\\My Drive\\Git\\filters\\','area_to_zip.csv'))

    dfz['ziplist'] = ''
    
    #found_zip = '#N/A'
    for row in ziplist.itertuples(index=False):
        area_code = str(row[0])
        zip_code = str(row[1])
                # print(area_code, zip_code)
    dfzz = dfz.columns[0]
    for z in dfzz:
        if z in area_code:
            dfz['ziplist'] = zip_code
                    # print(found_zip)
            if '0' in found_zip[0]:
                dfz['ziplist'] = '`'+dfz['ziplist']
                    #     print(found_zip)
          
    end_epoch_sec = int(time.time())
    result_apply = end_epoch_sec - start_epoch_sec
    print("ZipFind Results in " + str(result_apply))
    

###    return(dfz['ziplist'])
    return(dfz['secondcolumn'])
  

def get_info(path_to_directory,output_path):
    
    start_epoch_sec = int(time.time())
    
    files = []
    path = path_to_directory + '/*.csv'
    files = glob2.glob(path)
    
    my_file = "scrub.csv" ##OG
    df = pd.read_csv(my_file, low_memory=False) ##

    df.columns = ['Company','First','Last','Phone','Business Fax','CellPhone','Website URL','Email','Address 1','Address 2','City','Zip','PWC','Source','Comments']#company=(Required) #phone = (RequiredifnoEmail) #email = (Required if no Business Phone) #pwc = (ID or Description)    

    df['Phone'] = df['Phone'].replace('(','')
    df['Phone'] = df['Phone'].replace(')','')
    df['Phone'] = df['Phone'].replace('-','')
    df['Phone'] = df['Phone'].replace('+','')
    df['Phone'] = df['Phone'].replace('"','')
    df['Phone'] = df['Phone'].replace('\/','')
    df['Phone'] = df['Phone'].replace('\\','')
    df['Phone'] = df['Phone'].replace(' ','')
    
    pwcc = np.vectorize(pwcfind, otypes=[object])
    
    #npstr = np.array(milstr, dtype=np.string_)
    
    scorer = np.vectorize(scorefind, otypes=[object])

    zipp = np.vectorize(zipfind, otypes=[object])

    
    end_epoch_sec = int(time.time())
    result_apply = end_epoch_sec - start_epoch_sec
    print("End of initial get_info and vectorize.  Results in " + str(result_apply))
    
    
    print("Starting PWC Finder for Company")
    start_epoch_secpwcc = int(time.time())
    df['companypwc'] = pwcc(df['Company'])
    end_epoch_secpwcc = int(time.time())
    result_applypwcc = end_epoch_secpwcc - start_epoch_secpwcc
    print("PWC Finder (Company) Results in ")
    print(result_applypwcc)
    
    print("Starting PWC Finder for PWC")
    start_epoch_secpwcp = int(time.time())
    df['pwcfinder'] = pwcc(df['PWC'])
    df['pwcfinder'] = df['pwcfinder'].replace('0    ','')
    df['pwcfinder'] = df['pwcfinder'].replace('Name: Score, dtype: int64','')
    df['pwcfinder'] = df['pwcfinder'].replace('/n','')
    
    end_epoch_secpwcp = int(time.time())
    result_applypwcp = end_epoch_secpwcp - start_epoch_secpwcp
    print("PWC Finder (PWC) Results in ")
    print(result_applypwcp)

    print("Starting ScoreFindCompany")
    start_epoch_secsc = int(time.time())
    df['scorefindercompany'] = scorer(df['Company'])
    end_epoch_secsc = int(time.time())
    result_applysc = end_epoch_secsc - start_epoch_secsc
    print("ScoreFindCompany Results in ")
    print(result_applysc)

    print("Starting ScoreFindPWC")
    start_epoch_secsp = int(time.time())
    df['scorefinderpwc'] = scorer(df['PWC'])
    end_epoch_secsp = int(time.time())
    result_applysp = end_epoch_secsp - start_epoch_secsp
    print("ScoreFindPWC Results in ")
    print(result_applysp)

    print("Starting ScoreFindComments")
    start_epoch_secsco = int(time.time())
    df['scorefindercomments'] = scorer(df['Comments'])
    end_epoch_secsco = int(time.time())
    result_applysco = end_epoch_secsco - start_epoch_secsco
    print("ScoreFindComments Results in ")
    print(result_applysco)

    print("Starting ScoreFindZip")
    #start_epoch_secz = int(time.time())
    #df['zipfind'] = zipp(df['Phone'])
    #end_epoch_secsz = int(time.time())
    #result_applyz = end_epoch_secz - start_epoch_secz
    #print("ZipFind Results in ")
    #print(result_applyz)

    
    
   # for row in tqdm(cdf.itertuples(index=False), total=cdf.shape[0]):
   #     if phone is not None:
    #        phone = str(phone).strip()
    #        phone = phone.replace('(','')
   #         phone = phone.replace(')','')
    #        phone = phone.replace('-','')
   #         phone = phone.replace('+','')
   ##         phone = phone.replace('"','')
    #        phone = phone.replace('\/','')
    #        phone = phone.replace('\\','')
    #        phone = phone.replace(' ','')
   #     if zipcode != [5]:
   #         cdf['zipcodecodecheck'] = "if zipcode != [4,5] this is a yes"
   #         cdf['zipcoderesult'] = zipfind(phone)
   #     if companyname is not None:
  #          cdf['companynamecheck'] = scorefind(companyname)
   #         cdf['companynamepwccheck'] = pwcfind(companyname)
    



 #   local = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New.Hampshire','New.Jersey','New.Mexico','New.York','North.Carolina','North.Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode.Island','South.Carolina','South.Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West.Virginia','Wisconsin','Wyoming','AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']


  #  df['Pro Name'] = df[companyname].str.count('|'.join(pro))
   # df['Pro Count'] = df[comments].str.count('|'.join(pro))
#    df['Con Name'] = df[companyname].str.count('|'.join(con))
 #   df['Con Count'] = df[comments].str.count('|'.join(con))
  #  df['Bad Name'] = df[companyname].str.count('|'.join(bad))
   # df['Bad Count'] = df[comments].str.count('|'.join(bad))
    #df['Local Count'] = df[comments].str.count('|'.join(local))

#    df['Score'] = 0 + (df['Pro Name']*3) - (df['Con Name']*2) - (df['Bad Name']*13)

#    df['Score2'] = (df['Pro Name']*3) + (df['Pro Count']*3) - (df['Con Name']*2) - (df['Con Count']*2) - (df['Bad Name']*13) - (df['Bad Count']*13)

#    df['Combo'] = 0 + (df['Pro Name']*3) - (df['Con Name']*2) - (df['Bad Name']*13) + (df['Pro Name']*3) + (df['Pro Count']*3) - (df['Con Name']*2) - (df['Con Count']*2) - (df['Bad Name']*13) - (df['Bad Count']*13) + (df['Local Count'])

#pure = int(df['Combo'])
#if pure <= 0 and pure >= -3:
#    df['InSum'] = "Sketchy"
#    
#if pure <= -4:
#    df['InSum'] = "Bad"
#
#if pure >= 1 and pure<= 4:
#    df['InSum'] = "Good"#
#
#if pure >= 5 and pure <= 15:
#    df['InSum'] = "Better"
#
#if pure >= 16:
#    df['InSum'] = "Best"

#if df['Score'] <= -1:
#    df['InSum'] = "Bad"
    

#if df['Bad Name'] >= 1:
#    df['InSum'] = "Baddie"

#if df['Pro Name'] >= 2:
#    df['InSum'] = "Reedeem"



#purped_csv.sort_values("Pro Name", inplace = True)

#purped_csv.sort_values("Con Name", inplace = True)

#purped_csv.sort_values("Bad Name", inplace = True)

#    purped_csv.sort_values("Score", inplace = True)
    purped_csv = df

    purped_csv.to_csv ("SCRUBBED_" + date + ".csv", index=False, encoding='utf-8-sig')
    print('done')
                            
    duration = 100  # milliseconds
    freq = 700  # Hz
    winsound.Beep(freq, duration)

###.version.3 Scoring System fully applied.  01.31.22
##sound to play when done



def main():
    path_to_directory = "G:\\My Drive\\Git\\luke-filter"
    output_path  = "G:\\My Drive\\Git\\luke-filter\\filtered"

    #parser = argparse.ArgumentParser()
    #parser.add_argument('-i', '--input', dest='input_path', help='specify directory of csv files you wish to filter', action='store', required=True)
    #parser.add_argument('-o', '--output', dest='output_path', help='specify where you want output to be saved. default is in current working directory', action='store')
    
    #args = parser.parse_args()

    input_directory = path_to_directory
    if output_path:
        output=output_path
    else:
        output=''
    
    get_info(input_directory,output)

if __name__ == '__main__':
    main()
