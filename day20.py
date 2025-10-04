#stack
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Top element:", stack[-1])

print("Popped:", stack.pop())
print("Stack now:", stack)


#queue
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

print("Dequeued:", queue.popleft())
print("Queue now:", queue)

#hash table
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

top = sorted(freq.items(), key = lambda x: x[1], reverse = True)[0]
print("The word that appeared most times:", top[0])

