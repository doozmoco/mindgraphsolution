import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv

MetaData = pd.read_csv('Metadata.csv')
Organizers= pd.read_csv('Organisers_In_Fests.csv')
Participants= pd.read_csv('Participants_In_Fests.csv')
actual_organizers_names = []
for i in Organizers.index:
    check = True
    x = -100
    actual_name = ""
    for j in MetaData.index:
        temp = fuzz.token_sort_ratio(MetaData['Name'][j], Organizers['Name'][i])
        if(x<temp):
            x = temp
            actual_name = MetaData['Name'][j]
    if(x>50):
        actual_organizers_names.append(actual_name)
    else:
        actual_organizers_names.append("")


print(len(actual_organizers_names))
print(actual_organizers_names)
Organizers["Actual_name"] = actual_organizers_names
Organizers.to_csv('Organisers_Actual_names.csv', index=False)
print("hello")
