from db.session import engine
from db.base import Base
from db.models.newStudent import newStudentpy
from db.session import get_db


def create_tables():
	Base.metadata.create_all(bind=engine)

def main():
	create_tables()
	db = get_db().__next__()
	#student = newStudentpy(grade="fifthlevel", age=34)
	#db.add(student)
	#db.commit()
	allstudent = db.query(newStudentpy).all()
	for each in allstudent:
		print(each)
		print()
	
main()
