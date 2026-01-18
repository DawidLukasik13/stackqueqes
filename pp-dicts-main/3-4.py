import queue

n = int(input("Natural number: "))

stack = queue.LifoQueue()
num = n

while num > 0:
    remainder = num % 2
    stack.put(remainder)
    num //= 2

binary = ""
while not stack.empty():
    binary += str(stack.get())

print("Binary number:", binary)
