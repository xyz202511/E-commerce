from sqlalchemy import create_engine, text

# Path to your SQLite database
db_path = 'instance/products.db'
engine = create_engine(f'sqlite:///{db_path}')

# Connect and delete all rows from the user table
with engine.connect() as connection:
    try:
        connection.execute(text('DELETE FROM user'))
        print("✅ All user data deleted successfully!")
    except Exception as e:
        print("⚠️ Error:", e)
