import sqlite3

class NoteManager:
    def __init__(self, db_name='notes.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL
                )
            ''')

    def add_note(self, title, content):
        with self.conn:
            self.conn.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))

    def get_all_notes(self):
        with self.conn:
            cursor = self.conn.execute('SELECT id, title FROM notes')
            return cursor.fetchall()

    def search_notes(self, keyword):
        with self.conn:
            cursor = self.conn.execute('SELECT id, title FROM notes WHERE content LIKE ?', ('%'+keyword+'%',))
            return cursor.fetchall()

    def get_note_details(self, note_id):
        with self.conn:
            cursor = self.conn.execute('SELECT title, content FROM notes WHERE id = ?', (note_id,))
            return cursor.fetchone()

    def delete_note(self, note_id):
        with self.conn:
            self.conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))