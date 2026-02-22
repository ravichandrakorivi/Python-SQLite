from .database import get_connection


def get_trailing_load(
    loco_type,
    weather,
    curve,
    gradient,
    speed_step
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT trailing_load
        FROM rdso_load_chart
        WHERE loco_type = ?
          AND weather = ?
          AND curve = ?
          AND gradient = ?
          AND speed_step = ?
    """, (
        loco_type,
        weather,
        curve,
        gradient,
        speed_step
    ))

    row = cur.fetchone()
    conn.close()

    return row[0] if row else None


def get_tractive_effort(
    loco_type,
    speed_step
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT tractive_effort
        FROM te_dry
        WHERE loco_type = ?
          AND speed_step = ?
    """, (
        loco_type,
        speed_step
    ))

    row = cur.fetchone()
    conn.close()

    return row[0] if row else None

## How your simulation will use this (example)
#from db.repository import get_trailing_load, get_tractive_effort

#load = get_trailing_load("WAG9", "DRY", 2, 1.0, speed_step=15)
#te   = get_tractive_effort("WAG9", speed_step=15)
