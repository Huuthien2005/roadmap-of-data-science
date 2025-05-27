import numpy as np
rng=np.random.default_rng(seed=42)
grades= rng.integers(50,101,size=(20,5))
print(grades)
# Mean grade per student
student_avg=grades.mean(axis=1)# axis =0 across columns(horizontally)
print(student_avg)
#Mean grade per subject
subject_avg=grades.mean(axis=0)# axis =1 across columns(vertically)
print(subject_avg)
#highest grade in whole class
highest= grades.max()
print(highest)
#lowest grade in whole class
lowest=grades.min()
print(lowest)
# Standard deviation of grades
std_dev=grades.std()
print(std_dev)
#ranking
rank=np.argsort(-student_avg)#argsort return indices
for idx in rank:
    print(f"Student {idx}: {student_avg[idx]}")
#choose top student whose grades is above 85
#[0] return 1st array in tuple// mean the rows,[1] return 2nd array in tuple// mean the columns
top_student=np.where(grades>85)[0]
print(top_student)
# find student who scored is below 60
student_below_60=np.any(grades<60,axis=1)
struggle_student=np.where(student_below_60)[0]
print(f"struggle student(indices): ", struggle_student)
#add 5 bonus scores for student who have at least 2 subject that below 60
low_score=grades<60
print(low_score)
low_score_count=np.sum(low_score,axis=1)
bonus_mark=low_score_count>=2

grades_with_bonus=grades.copy()
grades_with_bonus[bonus_mark]+=5
grades_with_bonus=np.clip(grades_with_bonus,0,100)
print(grades_with_bonus)
# ends