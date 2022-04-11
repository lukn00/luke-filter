import os
import glob
import pandas as pd
#os.chdir("/Users/luke.nielson/OneDrive - HomeAdvisor/fresh/combine")

extension = 'xlsx'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_xlsx = pd.concat([pd.read_excel(f) for f in all_filenames ])
#export to excel
combined_xlsx.to_excel( "combined_xlsx.xlsx", index=False, encoding='utf-8-sig')

combined_xlsx.to_csv( "combined_xlsx_tocsv.csv", index=False, encoding='utf-8-sig')
