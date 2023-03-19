# See the problem request at the link down below
# https://dmoj.ca/problem/ccc20j2

# my solution:
max_infected = int(input())
infected = int(input())
infection_rate = int(input())
day = 0
infected_so_far = infected
while infected_so_far <= max_infected:
    day += 1
    infected = infected * infection_rate
    infected_so_far = infected_so_far + infected

print(day)
