import sqlite3

conn = sqlite3.connect("locos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS locomotives (
    loco_number INTEGER UNIQUE,
    type TEXT,
    date_of_commissioning TEXT,
    production_unit TEXT,
    transformer TEXT,
    traction_converter TEXT,
    auxiliary_converter TEXT,
    vcb TEXT,
    hog_availability TEXT,
    hog_make TEXT,
    cab_ac_availability TEXT,
    cab_ac_make TEXT,
    brake_system TEXT,
    rtis_availability TEXT,
    rtis_make TEXT,
    head_lights_type TEXT,
    led_make TEXT,
    led_signal_exchange_availability TEXT,
    signal_exchange_make TEXT,
    hlc_ivc_type TEXT,
    dpwcs_availability TEXT,
    dpwcs_make TEXT,
    kavach_availability TEXT,
    kavach_make TEXT,
    rms_availability TEXT,
    rms_make TEXT,
    rdso_ms_505_impl TEXT
)
""")

conn.commit()