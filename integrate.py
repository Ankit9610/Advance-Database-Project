import json
import pymysql
from pymongo import MongoClient

# -----------------------------
# Load JSON Files
# -----------------------------
# Note: Ensure the filename on your disk matches "finance_tracker.categories.json"
with open("data/finance_tracker.users.json", "r") as f:
    users_data = json.load(f)

with open("data/finance_tracker.categories.json", "r") as f:
    categories_data = json.load(f)

with open("data/finance_tracker.transaction_logs.json", "r") as f:
    logs_data = json.load(f)


# -----------------------------
# SQL Connection
# -----------------------------
sql_conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Golden$Sky!33_Valley',
    db='FinanceTracker'
)
sql_cursor = sql_conn.cursor()


# -----------------------------
# MongoDB Connection
# -----------------------------
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["FinanceTracker"]


# -----------------------------
# Clear Existing Data (SQL + MongoDB)
# -----------------------------
def clear_data():
    print("🧹 Clearing old data to prevent duplicates...")

    # 1. Clear MongoDB Collections
    mongo_db.users.delete_many({})
    mongo_db.categories.delete_many({})
    mongo_db.transaction_logs.delete_many({})
    print("   ✅ MongoDB collections cleared.")

    # 2. Clear SQL Tables
    # We disable Foreign Key checks temporarily to truncate tables freely
    try:
        sql_cursor.execute("SET FOREIGN_KEY_CHECKS = 0;") 
        sql_cursor.execute("TRUNCATE TABLE Transactions;")
        sql_cursor.execute("TRUNCATE TABLE Users;")
        sql_cursor.execute("TRUNCATE TABLE Categories;")
        sql_cursor.execute("SET FOREIGN_KEY_CHECKS = 1;") 
        sql_conn.commit()
        print("   ✅ SQL tables truncated (IDs reset).")
    except Exception as e:
        print(f"   ⚠️ SQL Truncate warning: {e}")


# -----------------------------
# Insert Users (SQL + MongoDB)
# -----------------------------
def insert_users():
    print("Inserting Users ...")

    for user in users_data:
        sql_cursor.execute(
            "INSERT INTO Users (user_id, name, email, income, total_transactions) VALUES (%s, %s, %s, %s, %s)",
            (user["user_id"], user["name"], user["email"], user["income"], 0)
        )

        mongo_db.users.insert_one({
            "user_id": user["user_id"],
            "name": user["name"],
            "email": user["email"],
            "income": user["income"]
        })

    sql_conn.commit()
    print("Users inserted successfully!")


# -----------------------------
# Insert Categories (SQL + MongoDB)
# -----------------------------
def insert_categories():
    print("Inserting Categories ...")

    for cat in categories_data:
        sql_cursor.execute(
            "INSERT INTO Categories (category_id, category_name, type, budget) VALUES (%s, %s, %s, %s)",
            (cat["category_id"], cat["name"], cat["type"], cat["budget"])
        )

        mongo_db.categories.insert_one(cat)

    sql_conn.commit()
    print("Categories inserted successfully!")


# -----------------------------
# Insert Transaction Logs (MongoDB + SQL Transactions) 
# -----------------------------
def insert_transaction_logs():
    print("Inserting Transaction Logs ...")

    # MongoDB Insert
    if isinstance(logs_data, list):
        mongo_db.transaction_logs.insert_many(logs_data)
    else:
        mongo_db.transaction_logs.insert_one(logs_data)
    
    # SQL Insert (Triggers will fire automatically)
    print("Inserting into SQL Transactions table...")
    for log in logs_data:
        try:
            sql_cursor.execute(
                """
                INSERT INTO Transactions (user_id, category_id, amount, transaction_date) 
                VALUES (%s, %s, %s, %s)
                """,
                (
                    log["user_id"], 
                    log.get("category_id", 1),  # Default to category 1 if missing
                    float(log["amount"]),       # Ensure decimal
                    log["date"]                 # Use JSON date string
                )
            )
        except Exception as e:
            print(f"Skipping log {log.get('log_id', 'unknown')}: {e}")
    
    sql_conn.commit()  # Commit SQL changes
    print("✅ Transaction logs inserted into MongoDB + SQL Transactions!")
    print("✅ Trigger fired - Users.total_transactions updated!")


# -----------------------------
# Main Function
# -----------------------------
def main():
    clear_data()               # <--- This cleans the DB before inserting
    insert_users()
    insert_categories()
    insert_transaction_logs()
    print("All JSON data successfully inserted into SQL + MongoDB!")


if __name__ == "__main__":
    main()