import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import json

class my_dictionary(dict):
 
  # __init__ function
  def __init__(self):
    self = dict()
 
  # Function to add key:value
  def add(self, key, value):
    self[key] = value

Organizers= pd.read_csv("Organisers_Actual_names.csv")
Participants= pd.read_csv('Participants_In_Fests.csv')

MetaData = pd.read_csv('Metadata.csv')
Clubs_Data= pd.read_csv('Clubs_data.csv')

marked_clubs = [0 for i in range(len(Clubs_Data))]
marked_fests = [0 for i in range(len(Participants))]
new_table = []
max_clubs = 0
max_event = 0
max_fests = 0
for i in Clubs_Data.index:
    club_info = Clubs_Data["Event"][i]
    club_no = club_info[5:club_info.find("_", 5)]
    event_no = club_info[club_info.rfind("_")+1:]
    max_clubs = max(max_clubs, int(club_no))
    max_event = max(max_event, int(event_no))

listclub = [[0 for i in range(max_event+1)] for j in range(max_clubs+1)]
max_event = 0
for i in Participants.index:
    fest_info = Participants["Event"][i]
    fest_no = fest_info[5:fest_info.find("_", 5)]
    event_no = fest_info[fest_info.rfind("_")+1:]
    max_fests = max(max_fests, int(fest_no))
    max_event = max(max_event, int(event_no))
listfest = [[0 for i in range(max_event+1)] for j in range(max_fests+1)]

for i in MetaData.index:
    name = my_dictionary()
    name.add("name", MetaData["Name"][i])
    name.add("id", MetaData["ID"][i])
    club = my_dictionary()
    for j in Clubs_Data.index:
        club_i = my_dictionary()
        x = fuzz.token_sort_ratio(MetaData['Name'][i], Clubs_Data['Name'][j])
        if(x>65 and marked_clubs[j]!=1):
            marked_clubs[j]=1
            role = "" if Clubs_Data["Role"][j][0]=="P" else Clubs_Data["Role"][j]
            club_i_event_j = my_dictionary()
            club_i_event_j.add("Participated", (True if role=="" else False))
            club_i.add("isOrganiser", role)
            club_i.add(Clubs_Data["Event"][j], club_i_event_j)
            club_info = Clubs_Data["Event"][j]
            club_no = int(club_info[5:club_info.find("_", 5)])
            event_no = int(club_info[club_info.rfind("_")+1:])
            listclub[club_no][event_no] +=1

            club.add(Clubs_Data["Club_Name"][j],club_i)
    name.add("Clubs", club)
    

    fest = my_dictionary()
    for j in Participants.index:
        fest_i = my_dictionary()
        x = fuzz.token_sort_ratio(MetaData['Name'][i], Participants['Name'][j])
        if(x>65 and marked_fests[j]==0):
            marked_fests[j]=1
            role = "" # role is empty for participants
            fest_i_event_j = my_dictionary()
            for k in Organizers.index:
                if(MetaData['Name'][i]==Organizers["Actual_name"][k]):
                    role = Organizers["Role"][k]
                    break
            fest_i.add("isOrganiser", Organizers["Role"][k])
            fest_i_event_j.add("Participated", (True if role=="" else False))

            fest_i.add(Participants["Event"][j], fest_i_event_j)
            fest.add(Participants["Fest_Name"][j], fest_i)

            fest_info = Participants["Event"][j]
            fest_no = int(fest_info[5:fest_info.find("_", 5)])
            event_no = int(fest_info[fest_info.rfind("_")+1:])
            listfest[fest_no][event_no] +=1
    name.add("Fests", fest)
    new_table.append(name)

print(listclub)
print(listfest)
with open('output.json', 'w') as outfile:
    json.dump(new_table, outfile)
with open('FrequencyClubsFests.txt', 'w') as filehandle:
    filehandle.write(f'{str(len(listclub))} ')
    filehandle.write(f'{str(len(listclub[0]))}\n')
    for listitem in listclub:
        for item in listitem:
            filehandle.write(f'{str(item)} ')
        filehandle.write(f'\n')
    filehandle.write(f'{str(len(listfest))} ')
    filehandle.write(f'{str(len(listfest[0]))}\n')
    for listitem in listfest:
        for item in listitem:
            filehandle.write(f"{str(item)} ")
        filehandle.write(f'\n')


