import pandas as pd
from glob import glob

data_files=sorted(glob('Tweets\data*.csv'))
data_files

mergeddata = pd.concat(pd.read_csv(datafile).assign(sourcefilename= datafile)
                for datafile in data_files)
#after the merge all data and save it a newfile as merged.csv
mergeddata.to_csv('Tweets\merged.csv')