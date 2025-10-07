def calculate_student_results():
    T = int(input())  # number of test cases
    for _ in range(T):
        C = int(input())  # number of courses
        courses = input().split(',')  # course and credit information

        # Parse course credits
        course_credits = []
        total_credits = 0
        for course in courses:
            course_name, credit = course.split(':')
            credit = int(credit)
            course_credits.append(credit)
            total_credits += credit

        S = int(input())  # number of students
        students = []

        # Read students information
        for _ in range(S):
            student_info = input().split(',')
            student_id = student_info[0]
            student_name = student_info[1]
            student_marks = list(map(float, student_info[2:]))

            # Calculate total percentage and failed courses
            total_percentage = 0
            failed_courses = 0
            failed_credits = 0

            for i, mark in enumerate(student_marks):
                credit = course_credits[i]
                total_percentage += mark * credit
                if mark < 55:
                    failed_courses += 1
                    failed_credits += credit

            total_percentage /= total_credits
            failed_semester = (failed_credits > total_credits / 2) if total_credits % 2 == 0 else (failed_credits >= (total_credits // 2 + 0.5))

            students.append({
                'id': student_id,
                'name': student_name,
                'percentage': total_percentage,
                'failed_courses': failed_courses,
                'failed_semester': failed_semester
            })

        requested_ids = input().split(',')  # requested student IDs

        # Filter requested students
        requested_students = [s for s in students if s['id'] in requested_ids]

        # Sort the requested students
        requested_students.sort(key=lambda x: (x['failed_courses'], -x['percentage'], x['name']))

        # Print the results in the desired format
        for rank, student in enumerate(requested_students, 1):
            print(f"{student['name']},{rank},{student['percentage']:.2f},{student['failed_courses']},{str(student['failed_semester']).lower()}")

        # Print a line of dashes after each test case
        print("----------")

# Example usage:
calculate_student_results()


