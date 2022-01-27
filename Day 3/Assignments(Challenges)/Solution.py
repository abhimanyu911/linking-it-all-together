from heapq import *

n = int(input())
orders = []
p_queue = []

#push arrival times and duration into 'orders' heap
for i in range(n):
    arrival_time, duration =map(int,input().split())
    heappush(orders,(arrival_time,duration))

time_elapsed = 0
wait_list = []
while orders or p_queue:
    #if arrival time of next order is more than elapsed time,
    #p_queue goes empty and time_elapsed is hence set to arrival time of next order
    #(ie cook waits for new order)
    while orders and orders[0][0]<=time_elapsed:
        arrival_time, duration = heappop(orders)
        #push such that min property is maintained
        heappush(p_queue,(duration,arrival_time))

    #p_queue goes empty and time_elapsed is hence set to arrival time of next order
    #(ie cook waits for new order)
    if not p_queue:
        arrival_time, duration = heappop(orders)
        time_elapsed = arrival_time
        heappush(p_queue,(duration,arrival_time))

    #pop fastest order
    duration,arrival_time = heappop(p_queue)
    time_elapsed+=duration
    wait_time = time_elapsed-arrival_time
    wait_list.append(wait_time)

print(int(sum(wait_list)/n))