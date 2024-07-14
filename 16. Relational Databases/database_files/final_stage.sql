SELECT Student.email
FROM Student
LEFT OUTER JOIN Course ON Course.course_code = Student.stu_subject_code
WHERE Course.course_level = 3;