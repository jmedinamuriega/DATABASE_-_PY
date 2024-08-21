from database_connection import connect_database

conn = connect_database()
cursor = conn.cursor()

def add_trainer(name, age):
    try:
        query = "INSERT INTO trainers (name, age) VALUES (%s, %s)"
        cursor.execute(query, (name, age))
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        print(f"Error adding trainer: {e}")
        conn.rollback() 
        return None


def add_member(name, age, trainer_id):
    try:
        query = "INSERT INTO members (name, age, trainer_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, age, trainer_id))
        conn.commit()
    except Exception as e:
        print(f"Error adding member: {e}")
        conn.rollback() 
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        query = "INSERT INTO workout (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
        conn.commit()
        print("Workout session added successfully.")
    except Exception as e:
        print(f"Error adding workout session: {e}")
        conn.rollback()



if conn is not None:
    try:
        trainer_id = add_trainer("pepe", 35)
        if trainer_id:
            add_member("Raul", 55, trainer_id)
            print("Added sucesfully")
        else:
            print("Failed to add trainer.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
