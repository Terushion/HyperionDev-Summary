SELECT Student.first_name, Student.mark, Course.course_name
FROM Student
INNER JOIN Course ON Course.course_code = Student.stu_subject_code
WHERE Student.mark >= 70;