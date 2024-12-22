from Database import student_numbers, student_statuses, student_majors, student_genders

def button_initialize():
    #각 버튼들의 custom_id를 초기화 해준다.
    #버튼들의 interaction을 custom_id로 감지해주기 때문
    for i in range(len(student_numbers)):
        label = student_numbers[i]["label"]
        student_numbers[i]["custom_id"] = f"number_{label}"

    for i in range(len(student_statuses)):
        label = student_statuses[i]["label"]
        student_statuses[i]["custom_id"] = f"status_{label}"

    for i in range(len(student_majors)):
        label = student_majors[i]["label"]
        student_majors[i]["custom_id"] = f"major_{label}"
    
    for i in range(len(student_genders)):
        label = student_genders[i]["label"]
        student_genders[i]["custom_id"] = f"gender_{label}"
    
    print("button initialization completed.")