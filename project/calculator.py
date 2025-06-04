from model import GPA

def grade_to_point(grade: str) -> float:
    grade_points = {
        "A+": 4.5,
        "A": 4.0,
        "B+": 3.5,
        "B": 3.0,
        "C+": 2.5,
        "C": 2.0,
        "D+": 1.5,
        "D": 1.0,
        "F": 0.0
    }
    return grade_points.get(grade, 0.0)

def calculate_gpa(student_data: GPA) -> dict:
    total_credits = 0
    total_grade_points = 0

    for course in student_data.courses:
        credits = course.credits
        grade_point = grade_to_point(course.grade)
        
        total_credits += credits
        total_grade_points += credits * grade_point

    gpa = total_grade_points / total_credits if total_credits > 0 else 0

    return {
        "student_summary": {
            "student_id": student_data.student_id,
            "name": student_data.name,
            "gpa": round(gpa, 2),
            "total_credits": total_credits
        }
    }