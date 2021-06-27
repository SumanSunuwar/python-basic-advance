students = [
			{"studentID":1212,"student_name":"luke","grade":"IX"},
			{"studentID":1215,"student_name":"Mark","grade":"VII"},
			{"studentID":1214,"student_name":"john","grade":"XI"},
			{"studentID":1213,"student_name":"david","grade":"X"}
			]

def find_id(name):
	for student in students:
		if student["student_name"] == name:
			print(student["studentID"])

find_id("luke")