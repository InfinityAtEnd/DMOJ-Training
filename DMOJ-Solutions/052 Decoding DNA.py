# See the problem request at the link down below
# https://dmoj.ca/problem/ecoo12r1p2

# my solution:
strands = [input() for _ in range(5)]
promoter = 'TATAAT'
results = []


def comp_revers(strand):  # used to reverse then get the complementary unit
	reverse = ''
	complementary = ''
	for k in range(len(strand)):
		reverse += strand[len(strand) - 1 - k]
	for j in reverse:
		if j == 'A':
			complementary += 'T'
		elif j == 'T':
			complementary += 'A'
		elif j == 'C':
			complementary += 'G'
		elif j == 'G':
			complementary += 'C'
	return complementary


def rna_translator(strand):  # used to get the complementary of the RNA and changing Thumine to Uracil
	rna = ''
	for k in strand:
		if k == 'A':
			rna += 'U'
		elif k == 'T':
			rna += 'A'
		elif k == 'C':
			rna += 'G'
		elif k == 'G':
			rna += 'C'
	return rna


for line in strands:  # looking for promoter unit and get the index where the transcription unit starts
	trans_unit_start = None
	trans_unit_end = None
	terminator1 = ''
	terminator2 = ''  # reversed and complementary of terminator1 ... optain with the function: comp_revers
	RNA = ''
	for i in range(len(line) - 6):
		if line[i:i + 6] == promoter:
			trans_unit_start = i + 10
			break

	look_for_terminator = line[trans_unit_start:]  # cuff of the start of DNA so we start at 0 with transcription unit
	ter_lenght = 6  # minimum lenght of terminator unit
	promoter_found = False
	while ter_lenght <= len(look_for_terminator) and not promoter_found:
		for i in range(len(look_for_terminator) - ter_lenght):
			terminator1 = look_for_terminator[i:i + ter_lenght]
			terminator2 = comp_revers(terminator1)
			if terminator2 in look_for_terminator[i + ter_lenght:]:
				trans_unit_end = i  # if terminator found we got the end point index of transcription unit
				promoter_found = True
				break
		ter_lenght += 1  # increase the lenght of terminator in case there isn't one with previour lenght

	if len(line) <= 22:
		results.append(None)
	elif not trans_unit_start:  # no RNA since there is no promoter found
		results.append(None)
	elif not trans_unit_end:  # means there isn't a terminator and the whole  string could be a transcription unit
		results.append(rna_translator(look_for_terminator))
	else:
		RNA = look_for_terminator[:trans_unit_end]
		results.append(rna_translator(RNA))
for st in range(len(results)):
	if results[st]:
		print(f'{st + 1}: {results[st]}')
	else:
		print(f'{st + 1}:')
