

class Employee:
    def __init__(self, emp_code, designation, name, age, gender, email, hired_location, dob, doj, experience, proof_id,
                 contact, status, address):
        self.emp_code = emp_code
        self.designation = designation
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.hired_location = hired_location
        self.dob = dob
        self.doj = doj
        self.experience = experience
        self.proof_id = proof_id
        self.contact = contact
        self.status = status
        self.address = address

    def save(self, db_manager):
        query = "INSERT INTO employee (emp_code, designation, name, age, gender, email, hired_location, dob, doj, experience, proof_id, contact, status, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (self.emp_code, self.designation, self.name, self.age, self.gender, self.email, self.hired_location, self.dob, self.doj, self.experience, self.proof_id, self.contact, self.status, self.address)
        db_manager.execute_query(query, params)
        db_manager.commit()

    def update(self, db_manager):
        query = "UPDATE employee SET designation = %s, name = %s, age = %s, gender = %s, email = %s, hired_location = %s, dob = %s, doj = %s, experience = %s, proof_id = %s, contact = %s, status = %s, address = %s WHERE emp_code = %s"
        params = (self.designation, self.name, self.age, self.gender, self.email, self.hired_location, self.dob, self.doj, self.experience, self.proof_id, self.contact, self.status, self.address, self.emp_code)
        db_manager.execute_query(query, params)
        db_manager.commit()

    def delete(self, db_manager):
        query = "DELETE FROM employee WHERE emp_code=%s"
        params = (self.emp_code,)
        db_manager.execute_query(query, params)
        db_manager.commit()
