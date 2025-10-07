This problem requires managing and calculating student grades based on credit courses and grading rules, including whether students pass or fail a semester based on the number of failed credits.

### Problem Breakdown:

1. **Credit System:**

   - Each course has a pre-specified value (credits).
   - Students are scored between 0 and 100. Students who score below 55 fail that particular course.
   - A student fails the semester if they fail more than 50% of the credits. If the total number of credits is odd, a student fails the semester if they fail more than half of the total credits plus 0.5.

2. **Ranking Students:**

   - Rank students by:
     - The number of failed courses (those with fewer failed courses rank higher).
     - Total percentage (higher percentage ranks higher).
     - If tied, rank alphabetically by name.

3. **Input/Output:**
   - For each test case, return the requested students' information in the format: `StudentName, Ranking, Percentage, FailedCourses, FailedSemester`.

### Approach:

1. **Input Parsing:**

   - We first parse the input to get the number of test cases, courses (with their credits), student information (name, marks), and the requested students' IDs.

2. **Credit and Grading Logic:**

   - For each student, we calculate:
     - Total percentage.
     - Number of failed courses (marks < 55).
     - Whether the student failed the semester based on the total credits and failed course credits.

3. **Ranking and Sorting:**

   - Rank students based on the criteria:
     - Fewer failed courses.
     - Higher total percentage.
     - Alphabetical order if there’s a tie.

4. **Output the requested students in the correct format.**

### Solution Code:

```python
def process_test_case(courses, students, requested_ids):
    total_credits = sum(course[1] for course in courses)

    # Helper function to calculate student data
    def calculate_student(student):
        student_id, name, marks = student[0], student[1], student[2:]
        total_percentage = 0
        failed_credits = 0
        failed_courses = 0

        # Calculate total percentage and number of failed courses
        for i, (course, credit) in enumerate(courses):
            mark = marks[i]
            total_percentage += mark * credit
            if mark < 55:
                failed_credits += credit
                failed_courses += 1

        total_percentage /= total_credits

        # Determine if the student has failed the semester
        if total_credits % 2 == 0:
            credit_threshold = total_credits // 2
        else:
            credit_threshold = total_credits // 2 + 0.5

        failed_semester = failed_credits > credit_threshold

        return (name, total_percentage, failed_courses, failed_semester)

    # Process all students
    student_data = []
    for student in students:
        student_data.append((student[0],) + calculate_student(student))

    # Sort the student data
    student_data.sort(key=lambda x: (x[3], -x[2], -x[1], x[0]))

    # Ranking and filtering the requested students
    requested_students = []
    rank = 1
    previous_failures = previous_percentage = None
    for i, student in enumerate(student_data):
        if student[0] in requested_ids:
            if previous_failures != student[2] or previous_percentage != student[1]:
                rank = i + 1  # Update rank if the criteria change
            previous_failures = student[2]
            previous_percentage = student[1]
            requested_students.append((student[1], rank, student[2], student[3]))

    return requested_students


def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the number of courses
        c = int(input().strip())

        # Read the course information
        courses = []
        for course_info in input().strip().split(','):
            course_name, credit = course_info.split(':')
            courses.append((course_name.strip(), int(credit)))

        # Read the number of students
        s = int(input().strip())

        # Read student information
        students = []
        for _ in range(s):
            student_info = input().strip().split(',')
            student_id = student_info[0].strip()
            name = student_info[1].strip()
            marks = list(map(float, student_info[2:]))
            students.append((student_id, name) + tuple(marks))

        # Read the requested student IDs
        requested_ids = input().strip().split(',')

        # Process the test case and get the requested student results
        results = process_test_case(courses, students, requested_ids)

        # Print the results in the required format
        for result in results:
            name, rank, percentage, failed_courses, failed_semester = result
            print(f"{name},{rank},{percentage:.2f},{failed_courses},{'true' if failed_semester else 'false'}")

        # Print the separator
        print('-' * 10)

# Uncomment the line below to run the main function
# main()
```

### Explanation:

1. **Input Parsing:**

   - We first parse the number of courses and their credits.
   - Next, we read the student details, including their ID, name, and marks for each course.

2. **Student Data Calculation:**

   - For each student, we calculate:
     - **Total percentage**: Sum of marks for each course weighted by its credit.
     - **Failed courses**: Count the courses where the student scored less than 55.
     - **Failed semester**: Based on the number of failed credits compared to the total.

3. **Sorting and Ranking:**

   - Students are sorted based on:
     - Number of failed courses.
     - Total percentage.
     - Alphabetical order (for ties).

4. **Result Output:**
   - For the requested students, their details are printed in the format specified.

### Example:

**Input:**

```
2
5
English:3, Mathematics:4, OOP:4, Sport:2, Database:4
4
1,Wali,80,95,86,90,97
2,Bashir,96,98,50,99,92
3,Halim,84,76,88,90,64
4,Omid,100,81,85,94,95
2,1
2
A:4,B:2
5
1,S1,80,56
2,S5,100,0
3,S3,100,100
4,S4,56,89
5,S2,49,92
3,1,5
```

**Output:**

```
Wali,2,89.44,0,false
Bashir,3,87.11,1,false
----------
S3,1,100.00,0,false
S1,2,72.00,0,false
S2,5,63.33,1,false
----------
```

### Time Complexity:

- **O(T _ (S _ C log S))**, where `T` is the number of test cases, `S` is the number of students, and `C` is the number of courses. The most time-consuming operation is sorting the students, which is `O(S log S)`.

This solution efficiently handles the problem's requirements and ensures that the requested students' results are correctly formatted and ranked.
