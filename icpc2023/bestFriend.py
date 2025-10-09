

t = int(input())
for _ in range(t):
    nsubject = int(input())
    subjects = input().strip().split(",")
    subject_credits = []
    for subject in subjects:
        name, credit = subject.split(":")
        subject_credits.append((name.strip(), int(credit)))

    nstudent = int(input())
    students = [list(map(str.strip, input().split(','))) for _ in range(nstudent)]
    requested = list(map(str.strip, input().split(",")))

    total_credit = sum(c for _, c in subject_credits)
    max_total_score = total_credit * 100

    result = []

    for student in students:
        sid = student[0]
        name = student[1]
        scores = list(map(float, student[2:]))

        failed_courses = 0
        total_failed_credit = 0
        obtained_scores = 0

        for i, (subj, credit) in enumerate(subject_credits):
            score = scores[i]
            obtained_scores += score * credit
            if score < 55:
                failed_courses += 1
                total_failed_credit += credit

        half_credit = total_credit / 2
        fail_semester = total_failed_credit > (half_credit + 0.5)
        total_percentage = obtained_scores / max_total_score * 100

        result.append([sid, name, total_percentage, failed_courses, fail_semester])

    # sort by: fewer failed courses, higher percentage, then name
    result.sort(key=lambda x: (x[3], -x[2], x[1]))

    formatedResult = {}
    for rank, rs in enumerate(result, start=1):
        sid, name, total_percentage, failed_courses, fail_semester = rs
        formatedResult[sid] = [name, rank, f"{total_percentage:.2f}", failed_courses, fail_semester]

    # print requested students sorted by rank
    output = [formatedResult[r] for r in requested if r in formatedResult]
    output.sort(key=lambda x: x[1])

    for out in output:
        print(f"{out[0]},{out[1]},{out[2]},{out[3]},{str(out[4]).lower()}")

    print('-' * 10)


# # 0 100
# #  less than 55 fail that subject
# # more than 50% fail that semester

# import math
# t=int(input())
# for _ in range(t):
#     nsubject=int(input())
#     subjects=input().strip().split(",")
#     subject_credits=[]
#     for subject in subjects:
#         name,credit=subject.split(":")
#         credit=int(credit)
#         subject_credits.append((name,credit))
#     nstudent=int(input())
#     students=[input().split(',') for _ in range(nstudent)]
#     requested=input().strip().split(",")
#     # output format
#     # std_name,rank,total_percentage, upto 2 decimal,failed course,failed semester
#     result=[]
#     total_scores= 0
#     total_credit=0
#     for subject in subject_credits:
#         credit=int(subject[1])
#         total_credit +=credit
#         total_scores += credit * 100
#     for student in students:
#         id=student[0]
#         name=student[1]
#         scores=list(map(int,student[2:]))
#         failed_courses=0
#         total_failed_credit=0
#         fail_semester=False
#         total_percentage=0
#         obtained_scores=0
        
#         for i,subject in enumerate(subject_credits):
#             score=scores[i]
#             credit=int(subject[1])
#             obtained_scores+=(score * credit)
#             if score < 55:
#                 failed_courses +=1
#                 total_failed_credit +=credit
#         if total_failed_credit > math.ceil(total_credit/2) :
#             fail_semester=True
#         total_percentage=  obtained_scores * 100 / total_scores
#         result.append([id,name,total_percentage,failed_courses,fail_semester])
#     result.sort(key= lambda x: x[2],reverse=True)
#     print(result)
#     formatedResult={}
#     rank=1
#     for rs in result:
#         id,name,total_percentage,failed_courses,fail_semester=rs
#         formatedResult[id]=[name,rank,f"{total_percentage:.2f}",failed_courses,fail_semester]
#         rank+=1
#     output=[]
#     for r in requested:
#         output.append(formatedResult[r])
#     output.sort(key=lambda x: x[1])
#     for out in output:
#         print(out)



# 2 
# 5 
# English:3,Mathematics:4,00P:4,Sport:2,Database:4    
# 4 
# 1,Wali,80,95,86,90,97 
# 2,Bashir,96,98,50,99,92 
# 3, Halim,84,76,88,90,64 
# 4,Omid, 100,81,85,94,95 
# 2,1 
# 2 
# A:4,B:2 
# 5 
# 1,S1,80,56 
# 2,S5,100,0 
# 3,S3,100,100 
# 4,S4,56,89 
# 5,52,49,92 
# 3,1,5        


