
def grade_level(g):
    if g>=9.5:
        return "Excellent"
    elif g>=9:
        return "Very good"
    elif g >=8:
        return "Good"
    else:
        return "Needs Improvement"

def cgpa_strategy():
    subjects=[]

    n=int(input("Enter number of subjects:"))

    for i in range (n):
        print("\nSubject",i+1)

        name=input("Name: ")
        credit=float(input("Credits: "))
        grade=float(input("Expected grade point(0-10): "))
        hours=float(input("Available study hours/week: "))

        subjects.append({
            "name": name,
            "credit": credit,
            "grade": grade,
            "hours": hours
        })

    total_credit= sum(s["credit"] for s in subjects)

    total_points = sum(s["credit"] * s["grade"]  for s in subjects)

    cgpa = total_points/total_credit

    print("\n========== CGPA ANALYSIS ==========")
    print("Expected CGPA:",round(cgpa, 2))
    print("Performance:",grade_level(cgpa))

    if cgpa >= 9.5:
        print("TARGET: 9.5 + ACHIEVED")
    else:
        print("TARGET: 9.5 + NOT YET ACHIEVED")

        required= 9.5 * total_credit- total_points
        print("Additional weighted points needed:", round(required, 2))

    print("\n========= STUDY PRIORITY ==========")

    # priority= credits * marks needed for improvement

    for s in subjects:
        s["priority"] = s["credit"]*(10-s["grade"])

    subjects.sort(key=lambda x: x["priority"], reverse=True)

    for i, s in enumerate(subjects,1):
        print(i, ".", s["name"],"| Grade:", s["grade"],"|credits:", s["credit"],"|Priority:",round(s["priority"],2))

    print("\n========== STRATEGY==========")

    for s in subjects:
        if s["priority"] > 3:
            extra = 2
        elif s["priority"] > 1:
            extra = 1
        else:
            extra = 0

        print(s["name"],"-Study", extra, "extra hour(s)/week")

cgpa_strategy()
              