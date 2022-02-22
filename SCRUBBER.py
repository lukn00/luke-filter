import pandas as pd
import csv
import datetime
# import winsound


current_date = datetime.datetime.now()
date = str(current_date.month)+ '_' + str(current_date.day) + '_' + str(current_date.year)

my_file = "scrub.csv"


df = pd.read_csv(my_file, low_memory=False)

firstcolumn = df.columns[0]
secondcolumn =  df.columns[14]

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


df['Pro Name'] = df[firstcolumn].str.count('|'.join(pro))
df['Pro Count'] = df[secondcolumn].str.count('|'.join(pro))
df['Con Name'] = df[firstcolumn].str.count('|'.join(con))
df['Con Count'] = df[secondcolumn].str.count('|'.join(con))
df['Bad Name'] = df[firstcolumn].str.count('|'.join(bad))
df['Bad Count'] = df[secondcolumn].str.count('|'.join(bad))
df['Local Count'] = df[secondcolumn].str.count('|'.join(local))

df['Score'] = 0 + (df['Pro Name']*3) - (df['Con Name']*2) - (df['Bad Name']*13)

df['Score2'] = (df['Pro Name']*3) + (df['Pro Count']*3) - (df['Con Name']*2) - (df['Con Count']*2) - (df['Bad Name']*13) - (df['Bad Count']*13)

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
print('done')
##sound to play when done
# duration = 100  # milliseconds
# freq = 700  # Hz
# winsound.Beep(freq, duration)
