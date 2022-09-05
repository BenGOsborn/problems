def siftdown(heap, i):
    temp = heap[i]

    while True:
        child = 2 * i

        if child >= len(heap):
            break

        if heap[child + 1] > heap[child]:
            child += 1

        if heap[child] > temp:
            heap[i] = heap[child]
        else:
            break

        i = child

    heap[i] = temp


def heapify(heap):
    for i in list(range(1, len(heap) // 2))[::-1]:
        siftdown(heap, i)


heap = [0, 5, 4, 2, 3, 3, 6, 8]

heapify(heap)

print(heap)
