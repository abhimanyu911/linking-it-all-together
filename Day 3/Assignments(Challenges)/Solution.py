from heapq import *

n = int(input())
orders = []
p_queue = []

#push arrival times and duration into heap
for i in range(n):
    arrival_time, duration =map(int,input().split())
    heappush(orders,(arrival_time,duration))

time_elapsed = 0
wait_list = []
while orders or p_queue:
    while orders and orders[0][0]<=time_elapsed:
        arrival_time, duration = heappop(orders)
        heappush(p_queue,(duration,arrival_time))

    if not p_queue:
        arrival_time, duration = heappop(orders)
        time_elapsed = arrival_time
        heappush(p_queue,(duration,arrival_time))

    duration,arrival_time = heappop(p_queue)
    time_elapsed+=duration
    wait_time = time_elapsed-arrival_time
    wait_list.append(wait_time)

print(int(sum(wait_list)/n))