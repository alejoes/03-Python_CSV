import os
import csv
from datetime import date

path_Budget=open("/Users/marian/desktop/budget_data.csv","r")
csvF_Budget=csv.reader(path_Budget,delimiter=",")
csvF_Budget=[one for one in csvF_Budget]

column_count=len(csvF_Budget[0])
row_count=sum(1 for row in csvF_Budget)

month=[]
month.append(csvF_Budget[1][0].split())


