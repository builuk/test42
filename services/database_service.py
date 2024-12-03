import sqlite3


class Database:
    def __init__(self, db_path="bot_data.db"):
        self.connection = sqlite3.connect(db_path)
        self.create_table()
        self.create_note_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                "CREATE TABLE IF NOT EXISTS user_roles (id INTEGER PRIMARY KEY, user_id INTEGER, role TEXT)"
            )

    def create_note_table(self):
        with self.connection:
            self.connection.execute(
                "CREATE TABLE IF NOT EXISTS user_notes (id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT, note TEXT)"
            )

    def add_user_role(self, user_id, role):
        with self.connection:
            self.connection.execute(
                "INSERT INTO user_roles (user_id, role) VALUES (?, ?)", (user_id, role)
            )

    def add_note_from_buyer(self, user_id, title, note):
        with self.connection:
            self.connection.execute(
                "INSERT INTO user_notes (user_id, title, note) VALUES (?,?,?)", (user_id, title, note)
            )

    def update_user_role(self, user_id, role):
        with self.connection:
            self.connection.execute(
                "UPDATE user_roles SET role = ? WHERE user_id = ?", (role, user_id)
            )

    def get_user_roles(self, user_id):
        with self.connection:
            return self.connection.execute(
                "SELECT role FROM user_roles WHERE user_id = ?", (user_id,)
            ).fetchall()

    def delete_user_role(self, user_id, role):
        with self.connection:
            self.connection.execute(
                "DELETE FROM user_roles WHERE user_id = ? AND role = ?", (user_id, role)
            )

    def delete_note_from_buyer(self, user_id, title):
        with self.connection:
            self.connection.execute(
                "DELETE FROM user_notes WHERE user_id = ? AND title = ?", (user_id, title)
            )
