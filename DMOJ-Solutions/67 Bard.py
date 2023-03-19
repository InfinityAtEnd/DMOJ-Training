# See the problem request at the link down below
# https://dmoj.ca/problem/crci06p1

# my solution:
N = int(input())
evenings = int(input())
villagers = {}
for i in range(N):
	villagers[str(i + 2)] = 0
all_know = ['1']


def nr_of_knows_songs(villagers_present):
	songs = [villagers[i] for i in villagers_present]
	return max(songs)


def event_song_swap(villagers_present):
	if '1' in villagers_present:  # if the bard is present at the event
		for villager in villagers_present:
			if villager != '1':
				villagers[villager] = villagers[villager] + 1  # all attenders learn one new song
	else:
		nr_songs = nr_of_knows_songs(villagers_present)  # max nr of song known by attending villagers
		for villager in villagers_present:
			villagers[villager] = nr_songs  # all attenders swap song so all will know all the songs from the best


for i in range(evenings):
	order = input().split()
	villages_present = [x for x in order[1:]]
	event_song_swap(villages_present)

songs_learned = villagers.values()
max_songs = max(songs_learned)
for k, v in villagers.items():
	if v == max_songs:
		all_know.append(k)
for m in all_know:
	print(m)
