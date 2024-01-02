# min - heap

import heapq

min_heap = [5, 3, 9, 4, 1, 2, 6]
heapq.heapify(min_heap)
heapq.heappop(min_heap)  # dequeue //O(logN)
heapq.heappush(min_heap, 1)  # enqueue //O(logN)


# max - heap

max_heap = [5, 3, 9, 4, 1, 2, 6]
# heapq._heapify_max(max_heap)
# value = heapq._heappop_max(max_heap)

max_heap = [i * -1 for i in max_heap]
heapq.heapify(max_heap)
weight = heapq.heappop(max_heap)
value = -1 * weight

# max_heap = [(-1 * i , i) for i in max_heap]
# heapq.heapify(max_heap)
# weight, value = heapq.heappop(max_heap)
