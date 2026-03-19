import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sqlite3

scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

sheet = client.open_by_key("1VWLCnQ5AHMS-WEDVWqDEsDSjb74ZryiUsWaMYcQYmok").worksheet("Population")

rows = sheet.get_all_records(head=2)

conn = sqlite3.connect("locos.db")
cursor = conn.cursor()

for row in rows:
    cursor.execute("""
        INSERT OR IGNORE INTO locomotives VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
    """, (
        row['Loco Number'],
        row['Type'],
        row['Date of Commissioning'],
        row['Production Unit'],
        row['Transformer'],
        row['Traction Converter'],
        row['Auxilliary Converter'],
        row['VCB'],
        row['HOG Availability'],
        row['HOG Make'],
        row['CAB AC Availability'],
        row['CAB AC Make'],
        row['Brake System'],
        row['RTIS Availability'],
        row['RTIS Make'],
        row['Head Lights type'],
        row['LED make'],
        row['LED signal exchange lights availability'],
        row['Make of Signal Exch. Light'],
        row['HLC IVC type'],
        row['DPWCS Availability'],
        row['DPWCS Make'],
        row['KAVACH Availability'],
        row['KAVACH Make'],
        row['RMS Availability'],
        row['RMS Make'],
        row['Whether  RDSO MS 505 (Rev-1) Implemented']
    ))

cursor.execute("SELECT COUNT(*) FROM locomotives")
count = cursor.fetchone()[0]
print("Total rows in database:", count)

cursor.execute("SELECT * FROM locomotives LIMIT 5")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM locomotives WHERE loco_number = 30631")
print(cursor.fetchone())

print("Rows inserted during this run:", conn.total_changes)

conn.commit()
conn.close()
