class student:
    def create_student(self, studentid, name, course, email, mobileno):
        self.studentid = studentid
        self.name = name
        self.course = course
        self.email = email
        self.mobileno = mobileno

    def add_student(self):
        # add student to db
        return self.studentid, self.name, self.course, self.email, self.mobileno

    # Interceptor code


s1 = student()
# Interceptor code here

# then create student if not present
s1.create_student(12, 'tejas', 'cs', 'tej@gmail.com', 8998481)


