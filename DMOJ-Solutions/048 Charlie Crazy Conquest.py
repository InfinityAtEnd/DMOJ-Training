# See the problem request at the link down below
# https://dmoj.ca/problem/dmopc19c5p2

# my solution:
N, H = input().split()
moves = int(N)
charlie_health = int(H)
enemy_health = int(H)
c_moves = [input().split() for _ in range(moves)]
e_moves = [input().split() for _ in range(moves)]
battle_result = 'I hate this problem'
for i in range(moves):
	if i == 0:
		if c_moves[i][0] == 'A':
			enemy_health -= int(c_moves[i][1])
		elif c_moves[i][0] == 'D' and e_moves[i][0] != "A":
			charlie_health -= int(c_moves[i][1])
	else:
		if c_moves[i][0] == 'A' and e_moves[i - 1][0] != 'D':
			enemy_health -= int(c_moves[i][1])
		elif c_moves[i][0] == 'D' and e_moves[i][0] != 'A':
			charlie_health -= int(c_moves[i][1])
	if charlie_health <= 0:
		battle_result = 'DEFEAT'
		break
	elif enemy_health <= 0:
		battle_result = 'VICTORY'
		break
	if i == moves - 1:
		if e_moves[i][0] == 'A' and c_moves[i][0] != 'D':
			charlie_health -= int(e_moves[i][1])
		elif e_moves[i][0] == 'D':
			enemy_health -= int(e_moves[i][1])
	else:
		if e_moves[i][0] == 'A' and c_moves[i][0] != 'D':
			charlie_health -= int(e_moves[i][1])
		elif e_moves[i][0] == 'D' and c_moves[i + 1][0] != 'A':
			enemy_health -= int(e_moves[i][1])
	if charlie_health <= 0:
		battle_result = 'DEFEAT'
		break
	elif enemy_health <= 0:
		battle_result = 'VICTORY'
		break

if charlie_health > 0 and enemy_health > 0:
	battle_result = 'TIE'

print(battle_result)
