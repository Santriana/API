from calculation import *

mid_score = 90
overall_mid_weight = 25
mid_weight = 25

final_score = 80
overall_final_weight = 25
final_weight = 0

quiz_score = 80
overall_quiz_weight = 25
quiz_weight = 20

performance = 80
overall_perform_weight = 25
perform_weight = 20

AKHLAK = 80

CO_mid_weight = [25,25,25,25,0,0,0,0,0,0]
CO_final_weight = [0,0,0,0,30,20,25,25,0,0]
CO_quiz_weight = [20,10,10,10,20,10,10,10,0,0]
CO_perform_weight = [20,10,10,10,20,10,10,10,0,0]
contribution = [5,0,0,0,0,0,0,0,0,0]

credit = [3,3,2,1,1,10]
course = [90,80,80,80,80,80]

a = score_subcourse(mid_score,overall_mid_weight, mid_weight, final_score, overall_final_weight, final_weight, quiz_score, overall_quiz_weight, quiz_weight, performance, overall_perform_weight, perform_weight, AKHLAK)
b = score_course(mid_score, overall_mid_weight, final_score, overall_final_weight, CO_mid_weight, CO_final_weight, quiz_score, overall_quiz_weight, CO_quiz_weight, contribution)
c = score_grouping(mid_score, overall_mid_weight, CO_mid_weight, final_score, overall_final_weight, CO_final_weight, quiz_score, overall_quiz_weight, CO_quiz_weight, performance, overall_perform_weight, CO_perform_weight, AKHLAK, contribution)
d = ipk(credit, course)

print ("Score Course : ", b)
print ("Score Detailed Comptency: ",a)
print('Score Grouping: ', c)
print('IPK: ', d)