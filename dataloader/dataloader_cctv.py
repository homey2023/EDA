import pandas as pd
import csv



df = pd.DataFrame(columns = ['district', 'address', 'latitude','longitude', 'count','update_date'])

with open("서울시 안심이 CCTV 연계 현황.csv", "r") as f_in:
    reader = csv.reader(f_in, delimiter=",", quotechar='"')
    for line in reader:
       
        if line[0] == '관악구':
            
            row = {
            'district': line[0], 
            'address': line[1], 
            'latitude': float(line[2]), 
            'longitude': float(line[3]), 
            'count' : int(line[4]), 
            'update_year': int(line[5].split("-")[0]),
            'update_month': int(line[5].split("-")[1]),
            'update_date': int(line[5].split("-")[2])
            }
            
            df = pd.concat([df, pd.DataFrame.from_dict([row])], ignore_index=True)

print(df)
df.to_csv("---path----", sep = ',', index = False)
