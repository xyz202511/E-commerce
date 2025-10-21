from sqlalchemy import create_engine, text

# Path to your SQLite database
db_path = 'instance/products.db'
engine = create_engine(f'sqlite:///{db_path}')

# Connect and alter the table
with engine.connect() as connection:
    try:
        connection.execute(text('ALTER TABLE user ADD COLUMN gender VARCHAR(10)'))
        connection.execute(text('ALTER TABLE user ADD COLUMN age INTEGER'))
        connection.execute(text('ALTER TABLE user ADD COLUMN mobile VARCHAR(15)'))
        print("✅ Columns added successfully to 'user' table!")
    except Exception as e:
        print("⚠️ Error:", e)
