import requests
import sqlite3
import json

resp = requests.get('https://api.deezer.com/album/302127')
print("status code is: ", resp.status_code)
print(resp.headers)

res = json.loads(resp.text)
print(res)
dictt = json.dumps(res, indent=4)
print(dictt)

#ბაზაში ვინახავ ალბომ discovery-ის სიმღერების აიდის, სახელსა და იმას, დიზერში წაკითხვადია თუ არა.
#ამ შემთხვევაში 0 ნიშნავს false-ს.
conn = sqlite3.connect("Album.sqlite3")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS albums
                (id INTEGER,
                title VARCHAR(100),
                readable VARCHAR(100));''')

res = resp.json()["tracks"]["data"]

for i in res:
    data = (i["id"], i["title"], i["readable"])
    query = "INSERT INTO albums (id, title, readable) VALUES (?, ?, ?)"
    cursor.execute(query, data)
    conn.commit()
conn.close()
