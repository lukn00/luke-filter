import pandas as pd
import csv
import datetime
# import winsound


current_date = datetime.datetime.now()
date = str(current_date.month)+ '_' + str(current_date.day) + '_' + str(current_date.year)


pro2=pd.read_csv("_pros.csv")
pro=pro2[pro2.columns[0]]

con2=pd.read_csv("_cons.csv")
con=con2[con2.columns[0]]

bad2=pd.read_csv("_bads.csv")
bad=bad2[bad2.columns[0]]



my_file = "PURPS.csv"

df = pd.read_csv(my_file)

local = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New.Hampshire','New.Jersey','New.Mexico','New.York','North.Carolina','North.Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode.Island','South.Carolina','South.Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West.Virginia','Wisconsin','Wyoming','AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']


df['Pro Name'] = df['(Required)'].str.count('|'.join(pro))
#df['Pro Count'] = df['Comments'].str.count('|'.join(pro))
df['Con Name'] = df['(Required)'].str.count('|'.join(con))
#df['Con Count'] = df['Comments'].str.count('|'.join(con))
df['Bad Name'] = df['(Required)'].str.count('|'.join(bad))
#df['Bad Count'] = df['Comments'].str.count('|'.join(bad))
#df['Local Count'] = df['Comments'].str.count('|'.join(local))

df['Score'] = 0 + (df['Pro Name']*3) - (df['Con Name']*2) - (df['Bad Name']*13)

#df['Score2'] = (df['Pro Name']*3) + (df['Pro Count']*3) - (df['Con Name']*2) - (df['Con Count']*2) - (df['Bad Name']*13) - (df['Bad Count']*13)



purped_csv = df

purped_csv.sort_values("Pro Name", inplace = True)

purped_csv.sort_values("Con Name", inplace = True)

purped_csv.sort_values("Bad Name", inplace = True)

purped_csv.sort_values("Score", inplace = True)

purped_csv.to_csv ("PURPED_" + date + ".csv", index=False, encoding='utf-8-sig')

###.version.3 Scoring System fully applied.  01.31.22
print('done')
##sound to play when done
# duration = 100  # milliseconds
# freq = 700  # Hz
# winsound.Beep(freq, duration)
