import requests
import os
import datetime
import hashlib

date = datetime.datetime.now()
date = str(date)
sha = hashlib.sha1(date.encode("utf-8")).hexdigest()

BASE_DIR = "D:\work\_Software\ML\datasets\MushroomsRussian\\unsorted"
LINKS_FILE = 'D:\work\_Software\ML\grab\links.txt'

KIND = 'Pax'
PEAMBULA = sha
GRAB_DIR = os.path.join(BASE_DIR, KIND)
if os.path.isdir(GRAB_DIR) == False:
    os.makedirs(GRAB_DIR)

def downloadImage(file, url):
    with open(file, 'wb') as handle:
        try:
            response = requests.get(url, stream=True)
            print(url)
            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break
                
                handle.write(block)
        except:
            print("No connection adapters were found for ", url)

with open(LINKS_FILE, 'r') as links:
    for n, line in enumerate(links, 1):
        # Обработка строки 'line'
        line = line.rstrip('\n')
        filename = '{}_{}.jpg'.format(n, PEAMBULA)
        filename = os.path.join(GRAB_DIR, filename)
        downloadImage(filename, line)
        if os.stat(filename).st_size == 0:
            os.remove(filename)
