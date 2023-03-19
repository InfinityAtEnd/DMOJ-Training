# See the problem request at the link down below
# https://dmoj.ca/problem/coci12c5p1

# my solution:
melody = list(input())
previous_tone = '|'
last_tone = ''
A_main_tones = 0
C_main_tones = 0

for i in melody:
	if previous_tone == '|':
		if i == 'E' or i == 'A' or i == 'D':
			A_main_tones += 1
			previous_tone = i
		elif i == 'C' or i == 'F' or i == 'G':
			C_main_tones += 1
			previous_tone = i
		else:
			previous_tone = i
	else:
		previous_tone = i

last_tone = melody[-1]

if A_main_tones == C_main_tones:
	if last_tone == 'A':
		print('A-mol')
	else:
		print('C-dur')
else:
	if A_main_tones > C_main_tones:
		print('A-mol')
	else:
		print('C-dur')
