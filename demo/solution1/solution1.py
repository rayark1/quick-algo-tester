import heapq
n, k = map(int, input().split())

jewels = []
for _ in range(n):
    jewels.append(list(map(int, input().split())))
bag = []
for _ in range(k):
    bag.append(int(input()))

jewels.sort(key=lambda x: x[0])
# 가방도 무게 기준으로 정렬
bag.sort()
result = 0
# 가치를 저장할 우선순위 큐(최대 힙)
max_heap = []
jewel_index = 0
# 가방을 무게가 작은 순서부터 순회
for weight in bag:
    # 현재 가방에 넣을 수 있는 보석들을 우선순위 큐에 추가
    while jewel_index < n and jewels[jewel_index][0] <= weight:
        heapq.heappush(max_heap, -jewels[jewel_index][1])  # 최대 힙을 구현하기 위해 음수로 추가
        jewel_index += 1
    
    # 우선순위 큐에서 가장 가치가 높은 보석 선택
    if max_heap:
        result -= heapq.heappop(max_heap)
print(result)