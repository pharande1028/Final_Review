import sqlite3
import os

def show_database_schema():
    """Show the actual database schema and structure"""
    
    db_path = "instance/bedsidebot.db"
    
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return
    
    print("🗄️ BEDSIDEBOT DATABASE BACKEND STORAGE")
    print("=" * 60)
    print(f"📁 File Location: {os.path.abspath(db_path)}")
    print(f"📊 File Size: {os.path.getsize(db_path)} bytes")
    print()
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        print(f"📋 Database contains {len(tables)} tables:")
        print()
        
        for table_name in tables:
            table = table_name[0]
            print(f"🗂️ TABLE: {table}")
            
            # Get table schema
            cursor.execute(f"PRAGMA table_info({table});")
            columns = cursor.fetchall()
            
            print("   COLUMNS:")
            for col in columns:
                col_name = col[1]
                col_type = col[2]
                not_null = "NOT NULL" if col[3] else "NULL"
                primary_key = "PRIMARY KEY" if col[5] else ""
                print(f"   • {col_name} ({col_type}) {not_null} {primary_key}")
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table};")
            count = cursor.fetchone()[0]
            print(f"   📊 Records: {count} rows")
            print()
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")

if __name__ == "__main__":
    show_database_schema()