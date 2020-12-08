from urllib.request import Request, urlopen
import re
import os
##############################
#### Creator: Peanutstick ####
#########################################################
### This script gona generate HTML file with links of ###
### streaming or torrent web-site                     ###
#########################################################
google = "https://www.google.fr/search?q="
film = str(input("Can I have you'r request Sir? \n:"))
film = film.replace(" ","+") # replace space by + cuz google don't like space
req = Request(google+film+"+streaming", headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
links = re.findall(r'https://lumendatabase.org/(.*?)&amp', str(webpage))#take all links (just half cuz i'm bad in regex)
i = 1
for link in links:
    link = "https://lumendatabase.org/"+link #I complet the link (cuz I'm ... nvm)
    print(str(i)+" : " +link) # just print something to show what it's going one
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read().decode('utf-8')    
    sitestream = re.findall(r'infringing_url">(.*?) - ', webpage)
    fichier = open(str(i)+" - "+film+".html", "a")
    for site in sitestream: #for each url ...
        if site == "[REDACTED]": # I look if the file gone be empty 
            fichier.close() #close and delet the file
            os.remove(str(i)+" - "+film+".html")
            break
        else:
            fichier.write("<a href=http://"+site+">"+site+"</a><br>") # else I put all links in my file
    fichier.close()
    i = i + 1# this is the number of my html file
    
