# Student ID: 007830903
# Name: Sheldon Handler

from package import Package, Status
import sqlite3

conn = sqlite3.connect(database="../data/database.db")
conn.execute("CREATE TABLE IF NOT EXISTS package (package_id INT PRIMARY KEY, address, city, state, postal, weight, "
             "deadline, note, status)")
conn.execute("CREATE TABLE IF NOT EXISTS status (status_id INT PRIMARY KEY, status TEXT)")

newPackage = Package(package_id=0, address="012 Test St", city="Test City", state="NY", postal="01234", weight=21,
                     deadline="12:30", note="g", status=Status.NOT_AVAILABLE)

conn.row_factory.append(newPackage).commit()

# conn.execute("INSERT INTO package (package_id, address, city, state, postal, weight, deadline, note, status) VALUES ("
#              "?, ?, ?, ?, ?, ?, ?, ?, ?)",
#              [newPackage.package_id, newPackage.address, newPackage.city, newPackage.state, newPackage.postal,
#               newPackage.weight, newPackage.deadline,
#               newPackage.note, newPackage.status])
conn.commit()
