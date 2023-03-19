# See the problem request at the link down below
# https://dmoj.ca/problem/crci07p1

# my solution:
nr_platforms = int(input())
platforms = []
pillar_length = 0

for i in range(nr_platforms):
	hight, start, end = input().split()
	platforms.append([int(hight), int(start), int(end)])

platforms.sort(reverse=True)


def on_platform(plat, height, index):  # check if  the pillar from heigh at index falls on another pillar or on the ground
	for platform in plat:
		if platform[0] < height and platform[1] < index < platform[2]:
			return height - platform[0]
	return height


for platform in platforms:
	print(f'calculating for platform {platform}')
	pillar_length_left = on_platform(platforms, platform[0], platform[1] + 0.5)
	pillar_length_right = on_platform(platforms, platform[0], platform[2] - 0.5)
	print(f'left pillar: {pillar_length_left}          right pillar: {pillar_length_right}')
	pillar_length = pillar_length + pillar_length_left + pillar_length_right

print(pillar_length)
