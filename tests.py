from sqlite_connector import SqliteConnector


connector = SqliteConnector('test_db.db')
connector.execute_query(""" CREATE TABLE "subjects" (
                            "SubjectId"	INTEGER NOT NULL UNIQUE,
                            "SubjectName"	TEXT,
                            "LearningHours"	INTEGER,
                            PRIMARY KEY("SubjectId" AUTOINCREMENT)) """)
connector.execute_query("""INSERT INTO subjects (SubjectName, LearningHours) VALUES ('ИИ', 86)""")
results_df = connector.get_data('SELECT * FROM subjects')
print(results_df)

