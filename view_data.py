#!/usr/bin/env python3
"""
BedsideBot Data Viewer
Quick script to view all stored data
"""

import sqlite3
import json
from datetime import datetime

def view_all_data():
    """Display all data stored in BedsideBot database"""
    
    db_path = "instance/bedsidebot.db"
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("🏥 BEDSIDEBOT DATABASE CONTENTS")
        print("=" * 50)
        
        # Check if database exists and has tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        if not tables:
            print("❌ No tables found. Database might be empty.")
            return
        
        print(f"📋 Found {len(tables)} tables:")
        for table in tables:
            print(f"   • {table[0]}")
        print()
        
        # View Hospitals
        print("🏥 HOSPITALS:")
        cursor.execute("SELECT * FROM hospitals")
        hospitals = cursor.fetchall()
        if hospitals:
            for hospital in hospitals:
                print(f"   • {hospital[1]} (ID: {hospital[2]})")
        else:
            print("   No hospitals registered")
        print()
        
        # View Staff
        print("👨‍⚕️ STAFF:")
        cursor.execute("SELECT * FROM staff")
        staff = cursor.fetchall()
        if staff:
            for member in staff:
                print(f"   • {member[2]} - {member[3]} ({member[1]})")
        else:
            print("   No staff registered")
        print()
        
        # View Patients
        print("🛏️ PATIENTS:")
        cursor.execute("SELECT * FROM patients")
        patients = cursor.fetchall()
        if patients:
            for patient in patients:
                print(f"   • {patient[2]} (ID: {patient[1]}) - Room: {patient[11]}, Bed: {patient[12]}")
                print(f"     Condition: {patient[6]}, Department: {patient[13]}")
        else:
            print("   No patients registered")
        print()
        
        # View Patient Requests
        print("📞 PATIENT REQUESTS:")
        cursor.execute("SELECT * FROM patient_requests ORDER BY timestamp DESC LIMIT 10")
        requests = cursor.fetchall()
        if requests:
            request_types = {1: "Call Nurse", 2: "Water", 3: "Food", 4: "Bathroom", 5: "Emergency"}
            for req in requests:
                req_type = request_types.get(req[2], "Unknown")
                print(f"   • {req[1]} - {req_type} ({req[3]}) at {req[5]}")
        else:
            print("   No patient requests")
        print()
        
        # View Caregivers
        print("👥 CAREGIVERS:")
        cursor.execute("SELECT * FROM caregivers")
        caregivers = cursor.fetchall()
        if caregivers:
            for caregiver in caregivers:
                print(f"   • {caregiver[1]} - {caregiver[2]}")
        else:
            print("   No caregivers registered")
        print()
        
        # Database Statistics
        print("📊 DATABASE STATISTICS:")
        cursor.execute("SELECT COUNT(*) FROM hospitals")
        hospital_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM staff")
        staff_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM patients")
        patient_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM patient_requests")
        request_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM caregivers")
        caregiver_count = cursor.fetchone()[0]
        
        print(f"   • Hospitals: {hospital_count}")
        print(f"   • Staff: {staff_count}")
        print(f"   • Patients: {patient_count}")
        print(f"   • Requests: {request_count}")
        print(f"   • Caregivers: {caregiver_count}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    except FileNotFoundError:
        print("❌ Database file not found. Run the app first to create it.")

if __name__ == "__main__":
    view_all_data()