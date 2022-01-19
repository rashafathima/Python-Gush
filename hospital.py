import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='hospitals',
                                         user='root',
                                         password='')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_hospital_detail(HID):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from hospital where HID = %s"""
        cursor.execute(select_query, (HID,))
        records = cursor.fetchall()
        print("Printing Hospital record")
        for row in records:
            print("Hospital Id:", row[0], )
            print("Hospital Name:", row[1])
            print("Bed Count:", row[2])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctor_detail(DID):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from doctor where DID = %s"""
        cursor.execute(select_query, (DID,))
        records = cursor.fetchall()
        print("Printing Doctor record")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)




def get_specialist_doctors_list(Speciality, Salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """select * from doctor where Speciality=%s and Salary > %s"""
        cursor.execute(sql_select_query, (Speciality, Salary))
        records = cursor.fetchall()
        print("Printing doctors whose specialty is", Speciality, "and Salary greater than", Salary, "\n")
        for row in records:
            print("Doctor Id: ", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_hospital_name(HID):
    # Fetch Hospital Name using Hospital id
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where HID = %s"""
        cursor.execute(select_query, (HID,))
        record = cursor.fetchone()
        close_connection(connection)
        return record[1]
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctors(HID):
    # Fetch Hospital Name using Hospital id
    try:
        hospital_name = get_hospital_name(HID)
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """select * from doctor where HID = %s"""
        cursor.execute(sql_select_query, (HID,))
        records = cursor.fetchall()

        print("Printing Doctors of the Hospital")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Hospital Name:", hospital_name)
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting doctor's data", error)



def update_doctor_experience(DID):
    # Update Doctor Experience in Years
    try:
        # Update doctor's Experience now
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """update Doctor set Experience = 5 where Doctor_Id =%s"""
        cursor.execute(sql_select_query, (experience, doctor_id))
        connection.commit()
        print("Doctor Id:", doctor_id, " Experience updated to ", experience, " years")
        close_connection(connection)

    except (Exception, mysql.connector.Error) as error:
        print("Error while getting doctor's data", error)





print("------Q1------")
print("\n")
print("\n")
get_hospital_detail(2)
print("\n")
get_doctor_detail(103)
print("------Q2------")
print("\n")
print("\n")
print("------Q3------")
get_specialist_doctors_list("ENT", 25000)
print("\n")
print("\n")
print("------Q4------")
print("\n")
print("\n")
get_doctors(1)