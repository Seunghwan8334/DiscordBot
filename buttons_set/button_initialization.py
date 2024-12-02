from .button_data import student_numbers, student_statuses, student_majors 

def button_initialize():

    for i in range(len(student_numbers)):
        student_numbers[i]["custom_id"] = f"student_number_{i+1}"

    for i in range(len(student_statuses)):
        student_statuses[i]["custom_id"] = f"student_status_{i+1}"

    for i in range(len(student_majors)):
        student_majors[i]["custom_id"] = f"student_major_{i+1}"
    
    print("button initialization completed.")