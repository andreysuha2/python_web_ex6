from pathlib import Path
from ex_6.definitions import ROOT_DIR, PATH_TO_DB
import sqlite3

def create_db(script_file: str, db_file: str):
    print(script_file, db_file)
    with open(script_file, 'r') as f:
        sql = f.read()
    
    with sqlite3.connect(db_file) as con:
        cur = con.cursor()
        cur.executescript(sql)
        
if __name__ == "__main__":
    create_db(script_file=Path(f"{ROOT_DIR}/college.sql"), db_file=PATH_TO_DB)