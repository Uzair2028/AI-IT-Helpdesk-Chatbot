import sqlite3
from datetime import datetime

DB_NAME = "tickets.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issue TEXT NOT NULL,
        status TEXT DEFAULT 'Open',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def create_ticket(issue):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tickets(issue)
        VALUES(?)
        """,
        (issue,)
    )

    conn.commit()

    ticket_id = cursor.lastrowid

    conn.close()

    return ticket_id


def get_all_tickets():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM tickets
    ORDER BY id DESC
    """)

    tickets = cursor.fetchall()

    conn.close()

    return tickets


def get_open_tickets():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM tickets
    WHERE status='Open'
    ORDER BY id DESC
    """)

    tickets = cursor.fetchall()

    conn.close()

    return tickets


def update_ticket_status(ticket_id, status):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tickets
    SET status=?
    WHERE id=?
    """, (status, ticket_id))

    conn.commit()

    conn.close()


def delete_ticket(ticket_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM tickets
    WHERE id=?
    """, (ticket_id,))

    conn.commit()

    conn.close()


if __name__ == "__main__":

    initialize_database()

    print("Database Ready")