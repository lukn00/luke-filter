import pandas as pd
import csv
import datetime
import winsound
#from tqdm import tqdm  ### no loops // not working as intended
import time

#tic = time.perf_counter()
#toc = time.perf_counter()
#print(f" Directory Loads in {toc - tic:0.2f} seconds")


#tqdm.pandas(desc="progression")

current_date = datetime.datetime.now()
date = str(current_date.month)+ '_' + str(current_date.day) + '_' + str(current_date.year)

my_file = "scrub3.csv"


df = pd.read_csv(my_file, low_memory=False)

firstcolumn = df.columns[0]  #A or Company Name
secondcolumn =  df.columns[14] #O or Comments
thirdcolumn =  df.columns[12] #M or PWC

#firstcolumn = '(Required)'
#secondcolumn = 'Comments'
#firstcolumn = 'Company Name'
#secondcolumn = 'Contact Name'

pro2=pd.read_csv("_pros.csv")
pro=pro2[pro2.columns[0]]

con2=pd.read_csv("_cons.csv")
con=con2[con2.columns[0]]

bad2=pd.read_csv("_bads.csv")
bad=bad2[bad2.columns[0]]

local = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New.Hampshire','New.Jersey','New.Mexico','New.York','North.Carolina','North.Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode.Island','South.Carolina','South.Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West.Virginia','Wisconsin','Wyoming','AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

ticc = time.perf_counter()

tic = time.perf_counter()
print("checking pros by company name...")
df['Pro Name'] = df[firstcolumn].str.count('|'.join(pro))
toc = time.perf_counter()
print(f"pro name done in {toc - tic:0.2f} seconds")

tic = time.perf_counter()
print("checking pros by comments...")
df['Pro Count'] = df[secondcolumn].str.count('|'.join(pro))
toc = time.perf_counter()
print(f"pro comments done in {toc - tic:0.2f} seconds")

tic = time.perf_counter()
print("checking pros by pwc...")
df['Pro PWC'] = df[thirdcolumn].str.count('|'.join(pro))
toc = time.perf_counter()
print(f"pro pwc done in {toc - tic:0.2f} seconds")

tic = time.perf_counter()
print("checking cons by company name...")
df['Con Name'] = df[firstcolumn].str.count('|'.join(con))
toc = time.perf_counter()
print(f"con name done in {toc - tic:0.2f} seconds")

tic = time.perf_counter()
print("checking cons by comments...")
df['Con Count'] = df[secondcolumn].str.count('|'.join(con))
toc = time.perf_counter()
print(f"con comments done in {toc - tic:0.2f} seconds")

tic = time.perf_counter()
print("checking cons by pwc...")
df['Con PWC'] = df[thirdcolumn].str.count('|'.join(con))
toc = time.perf_counter()
print(f"con pwc done in {toc - tic:0.2f} seconds")

tic = time.perf_counter()
print("checking bads by company name...")
df['Bad Name'] = df[firstcolumn].str.count('|'.join(bad))
toc = time.perf_counter()
print(f"bad name done in {toc - tic:0.2f} seconds")

tic = time.perf_counter()
print("checking bads by comments...")
df['Bad Count'] = df[secondcolumn].str.count('|'.join(bad))
toc = time.perf_counter()
print(f"bad comments done in {toc - tic:0.2f} seconds")

tic = time.perf_counter()
print("checking bads by pwc...")
df['Bad PWC'] = df[thirdcolumn].str.count('|'.join(bad))
toc = time.perf_counter()
print(f"bad pwc done in {toc - tic:0.2f} seconds")

tic = time.perf_counter()
print("checking local...")
df['Local Count'] = df[secondcolumn].str.count('|'.join(local))
toc = time.perf_counter()
print(f"local done in {toc - tic:0.2f} seconds")

tocc = time.perf_counter()
print(f"filters applied in {tocc - ticc:0.2f} seconds")


df['Score'] = 0 + (df['Pro Name']*3) - (df['Con Name']*2) - (df['Bad Name']*13)


df['ScoreAll'] = (df['Pro Name']*3) + (df['Pro Count']*3) + (df['Pro PWC']*3) - (df['Con Name']*2) - (df['Con Count']*2) - (df['Con PWC']*2) - (df['Bad Name']*13) - (df['Bad Count']*13) - (df['Bad PWC']*13)

df['ScorePWC'] = (df['Pro Name']*3) + (df['Pro PWC']*3) - (df['Con Name']*2) - (df['Con PWC']*2) - (df['Bad Name']*13) - (df['Bad PWC']*13)

df['Combo'] = 0 + (df['Pro Name']*3) - (df['Con Name']*2) - (df['Bad Name']*13) + (df['Pro Name']*3) + (df['Pro Count']*3) - (df['Con Name']*2) - (df['Con Count']*2) - (df['Bad Name']*13) - (df['Bad Count']*13) + (df['Local Count'])

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


purped_csv = df

purped_csv.sort_values("Pro Name", inplace = True)

purped_csv.sort_values("Con Name", inplace = True)

purped_csv.sort_values("Bad Name", inplace = True)

purped_csv.sort_values("Score", inplace = True)

purped_csv.to_csv ("SCRUBBED_" + date + ".csv", index=False, encoding='utf-8-sig')

###.version.3 Scoring System fully applied.  01.31.22
print(f"successfully processed {len(df['Score'])} records.  thank you for shopping with us! your invoice will be emailed shortly.")

#print('done')
##sound to play when done
duration = 100  # milliseconds
freq = 700  # Hz
#winsound.Beep(freq, duration)
