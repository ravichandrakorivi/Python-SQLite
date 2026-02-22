import sqlite3
from pathlib import Path

import rdso_load_tables
from te_dry import te_dry


DB_PATH = Path(__file__).parent / "train_dynamics.db"


def build_database():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # -----------------------------
    # RDSO LOAD CHART TABLE
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rdso_load_chart (
        loco_type TEXT,
        weather TEXT,
        curve INTEGER,
        gradient REAL,
        speed_step INTEGER,
        trailing_load INTEGER,
        PRIMARY KEY (loco_type, weather, curve, gradient, speed_step)
    )
    """)

    for loco, weather_data in rdso_load_tables.load_tables.items():
        for weather, curves in weather_data.items():
            for curve, gradients in curves.items():
                for gradient, steps in gradients.items():
                    for speed_step, trailing_load in enumerate(steps):
                        cursor.execute(
                            """
                            INSERT OR REPLACE INTO rdso_load_chart
                            VALUES (?, ?, ?, ?, ?, ?)
                            """,
                            (
                                loco,
                                weather,
                                curve,
                                float(gradient),
                                speed_step,
                                trailing_load
                            )
                        )

    # -----------------------------
    # TE DRY TABLE
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS te_dry (
        loco_type TEXT,
        speed_step INTEGER,
        tractive_effort REAL,
        PRIMARY KEY (loco_type, speed_step)
    )
    """)

    for loco, te_values in te_dry.items():
        for speed_step, te in enumerate(te_values):
            cursor.execute(
                """
                INSERT OR REPLACE INTO te_dry
                VALUES (?, ?, ?)
                """,
                (loco, speed_step, float(te))
            )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    build_database()
    print("✔ SQLite database created / updated successfully")
