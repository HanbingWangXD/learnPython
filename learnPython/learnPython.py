import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '(localdb)\\mssqllocaldb' 
database = 'MinerNetCoreContext-a1444177-fc59-44fd-8ed6-b0d6e8652d1e' 
Trusted_Connection='yes'
MultipleActiveResultSets='true'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection='+Trusted_Connection+';MultipleActiveResultSets='+ MultipleActiveResultSets)

cursor = cnxn.cursor()
cursor.execute("select * from Miner")
while True:
    row = cursor.fetchone()
    if not row:
        break
    print('ID:', row.MinerID)          
    print('IP:', row.IP)
    print('Location', row.LocationHolder)


