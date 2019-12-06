import sqlite3

conn = sqlite3.connect('bryanshop.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE parts
          (id INTEGER PRIMARY KEY ASC, 
           manufacturer VARCHAR(50) NOT NULL,
           model VARCHAR(50) NOT NULL,
           sale_price FLOAT NOT NULL,
           cost FLOAT NOT NULL,
           stock INTEGER NOT NULL,
           release_date DATETIME NOT NULL,
           is_discontinued INTEGER NOT NULL,
           type VARCHAR(6) NOT NULL,
           
           clock_speed_ghz FLOAT,
           boost_clock_ghz FLOAT,
           clock_speed_mhz FLOAT,
           boost_clock_mhz FLOAT,
           length_cm FLOAT,
           thickness_cm  FLOAT,
           pcie_ver  FLOAT,
           core_count INTEGER,
           hyperthread INTEGER,
           socket VARCHAR(20),
           chipset VARCHAR(20))
          ''')

conn.commit()
conn.close()
