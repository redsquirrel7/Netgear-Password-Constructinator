# Netgear-Password-Constructinator
Generates default wifi passwords for Netgear routers
Written by: Brad Nelson (Squirrel)
Twitter: redsquirrel_7

# Introduciton
Netgear routers ship with a default ssid and password that seems to be randomly generated. There is a pattern to them however. Most ssids start with NETGEAR and then a number (eg. NETGEAR80, NETGEAR73). Some ISPs will create their own set of ssids. Charter Spectrum here in the PNW changes their ssids to MyCharterWiFi or MySpectrumWiFi plus a number and a letter at the end (eg. MyCharterWiFi2g, MySpectrumWiFi7e). Spotting ssids like this in the wild is a good indication of a Netgear router with a randomly generated default password. The passwords always have a pattern of adjective + noun + three-digit-number, and are always completely lowercase (eg. redoctopus453, beautifuliris967). 

NPCinator.py will take the adjectives and nouns from their respective text files and generate passwords in this pattern sequentially. These passwords can be dumped into a file, or piped into cracking software like aircrack-ng.

# Usage
Output to file: 
'''
python NPCinator.py > passwords.txt
'''

Pipe to aircrack-ng:
'''
python NPCinator.py | aircrack-ng -a 2 -e ASDF asdf-01.cap -w -
'''

# Future Feature Plans
- Add web crawler to crawl dictionary website and create adjective and noun files from all adjectives and nouns in the english language.
