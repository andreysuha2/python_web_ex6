from ex_6.definitions import PATH_TO_DB, ROOT_DIR
from pathlib import Path
import sqlite3
import sys

def query(sql: str) -> list:
    with sqlite3.connect(PATH_TO_DB) as con:
        cur = con.cursor()
        r = cur.execute(sql)
        return r.fetchall()
    
def main():
    path = Path(f"{ROOT_DIR}/queries/query_{sys.argv[1]}.sql")
    with open(path) as file:
        sql = file.read()
        print(query(sql=sql))
        
if __name__ == "__main__":
    main()
        