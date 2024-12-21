from Database import student_numbers, student_statuses, student_majors, student_genders

def button_initialize():
    #각 버튼들의 custom_id를 초기화 해준다.
    #버튼들의 interaction을 custom_id로 감지해주기 때문
    for i in range(len(student_numbers)):
        student_numbers[i]["custom_id"] = f"student_number_{i+1}"

    for i in range(len(student_statuses)):
        student_statuses[i]["custom_id"] = f"student_status_{i+1}"

    for i in range(len(student_majors)):
        student_majors[i]["custom_id"] = f"student_major_{i+1}"
    
    for i in range(len(student_genders)):
        student_genders[i]["custom_id"] = f"student_gender_{i+1}"
    
    print("button initialization completed.")