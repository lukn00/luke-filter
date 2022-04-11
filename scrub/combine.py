import os
import glob
import pandas as pd
#os.chdir("/Users/luke.nielson/OneDrive - HomeAdvisor/fresh/combine")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

combined_csv.to_excel( "combined_csv_excel.xlsx", index=False, encoding = 'utf-8-sig')
