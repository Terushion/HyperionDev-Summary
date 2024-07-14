SELECT Student.first_name, Student.last_name
FROM Student
INNER JOIN Course ON Course.course_code = Student.stu_subject_code
WHERE Course.course_code = 'DS03';