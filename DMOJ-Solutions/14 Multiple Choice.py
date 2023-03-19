# See the problem request at the link down below
# https://dmoj.ca/problem/ccc11s2

# my solution:
N = int(input())
student_coices = []
correct_answers = []
correct_answers_by_students = 0

for i in range(N):
	student_coices.append(input())
for i in range(N):
	correct_answers.append(input())

for i in range(N):
	if student_coices[i] == correct_answers[i]:
		correct_answers_by_students += 1

print(correct_answers_by_students)
