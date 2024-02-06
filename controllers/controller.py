from models.database import Database

db = Database('db_mass_messages.db')

db.create_tables()


db.conn.commit()
db.close()