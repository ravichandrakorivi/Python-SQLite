import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent / ".." / "create_database" / "train_dynamics.db"


def get_connection():
    """
    Returns a SQLite connection to the train dynamics database.
    """
    return sqlite3.connect(DB_PATH)
