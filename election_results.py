import sqlite3

def connect_to_database():
    return sqlite3.connect('bincom_test.sql')

def display_polling_unit_result(cursor, polling_unit_id):
    cursor.execute("""
        SELECT party_abbreviation, party_score
        FROM announced_pu_results
        WHERE polling_unit_uniqueid = ?
    """, (polling_unit_id,))
    results = cursor.fetchall()
    
    if not results:
        print(f"No results found for polling unit {polling_unit_id}")
    else:
        print(f"\nResults for polling unit {polling_unit_id}:")
        for party, score in results:
            print(f"{party}: {score}")

def display_lga_total_result(cursor, lga_id):
    cursor.execute("""
        SELECT party_abbreviation, SUM(party_score) as total_score
        FROM announced_pu_results
        JOIN polling_unit ON announced_pu_results.polling_unit_uniqueid = polling_unit.uniqueid
        WHERE polling_unit.lga_id = ?
        GROUP BY party_abbreviation
    """, (lga_id,))
    results = cursor.fetchall()
    
    if not results:
        print(f"No results found for LGA {lga_id}")
    else:
        print(f"\nTotal results for LGA {lga_id}:")
        for party, score in results:
            print(f"{party}: {score}")

def store_new_polling_unit_results(cursor, conn):
    polling_unit_id = input("Enter new polling unit ID: ")
    
    parties = ['PDP', 'DPP', 'ACN', 'PPA', 'CDC', 'JP']  
    for party in parties:
        score = input(f"Enter score for {party}: ")
        cursor.execute("""
            INSERT INTO announced_pu_results 
            (polling_unit_uniqueid, party_abbreviation, party_score)
            VALUES (?, ?, ?)
        """, (polling_unit_id, party, score))
    
    conn.commit()
    print("Results stored successfully!")

def main():
    conn = connect_to_database()
    cursor = conn.cursor()

    while True:
        print("\n1. Display result for a polling unit")
        print("2. Display total result for an LGA")
        print("3. Store results for a new polling unit")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            polling_unit_id = input("Enter polling unit ID: ")
            display_polling_unit_result(cursor, polling_unit_id)
        elif choice == '2':
            lga_id = input("Enter LGA ID: ")
            display_lga_total_result(cursor, lga_id)
        elif choice == '3':
            store_new_polling_unit_results(cursor, conn)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()