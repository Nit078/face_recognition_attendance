import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-attenda-f4353-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Nitin Srivastava",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 1,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "011322":
        {
            "name": "Virat Kholi",
            "major": "Science",
            "starting_year": 2001,
            "total_attendance": 13,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "011323":
        {
            "name": "Ama de Armas",
            "major": "Biology",
            "starting_year": 2010,
            "total_attendance": 7,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)