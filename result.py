#Kurā gadā bija dibināts vecākais Omānas reģiona uzņēmums (informācija ir pieejama kolonnā Founded)?
#Kāds ir darbinieku skaits, kas strādā Latvijā?
#Kāds ir darbinieku skaits kas strādā telekomunikācijas jomā Latvijā.  (Industry = Telecommunications, Country = Latvia) ?
#Cik no datu bāze esošajiem Latvijas kompānijām ir SSL sertifikāts? (SSL sertifikāts ir kompānijām, kuram tīmekļa adrese sākas ar https://)
#Cik reizes datu bāzē tiek minēts domēna vārds .org reģionam Latvia?


import pandas as pd

read_file = pd.read_csv (r'data.txt')
read_file.to_csv(r'data1.csv', index=None)


print("Kurā gadā bija dibināts vecākais Omānas reģiona uzņēmums (informācija ir pieejama kolonnā Founded)?")

df=pd.read_csv("data1.csv")
year = df['Founded'].tolist() #list with values of years
print(min(year))




print("Kāds ir darbinieku skaits, kas strādā Latvijā?")

df = pd.read_csv('data1.csv', delimiter=',')
info_list = [list(row) for row in df.values] #converting csv to list of lists
values = []
for row in info_list:
    if row[4] == ("Latvia"): #checking for the region in 2nd row
        values.append(row[8]) #pievieno cilveku skaitu saraksta
print(sum(values)) #saskaita visas vērtības


print("Kāds ir darbinieku skaits kas strādā telekomunikācijas jomā Latvijā.  (Industry = Telecommunications, Country = Latvia) ?")

darbnieki = []
for row in info_list:
    if row[4] == ("Latvia") and row[7] == ("Telecommunications"): #checking for the industry and for latvijas iedzivotajiem
        darbnieki.append(row[8]) #pievieno cilvēku skaitu sarakstā
print(sum(darbnieki))

print("Cik no datu bāze esošajiem Latvijas kompānijām ir SSL sertifikāts? (SSL sertifikāts ir kompānijām, kuram tīmekļa adrese sākas ar https://)")

#df_AB = df[['Website', 'Region']]
#print(df_AB)
#word_count = 0 
#for word in df_AB:
    #if word[4] == "s": #s is the letter with index 4, counting from zero in "https"
        #word_count += 1 
#print(word_count)
ssl = []
for row in info_list:
    if row[3][4] == ("s") and row[5] == ("Latvia"): #
        ssl.append(row[8]) #
print(sum(ssl))
