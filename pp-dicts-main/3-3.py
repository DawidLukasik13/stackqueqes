import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = queue.LifoQueue()
    pairs = {')':'(', ']':'[', '}':'{'}

    for ch in expression:
        if ch in "([{":
            stack.put(ch)
        elif ch in ")]}":
            if stack.empty():
                return False
            if stack.get() != pairs[ch]:
                return False

    return stack.empty()

for e in [expression1, expression2, expression3]:
    print(e, "OK" if brackets_ok(e) else "INVALID")