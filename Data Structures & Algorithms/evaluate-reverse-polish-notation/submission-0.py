class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

    
        # stack to hold numbers as we go
        stack = []

        # go through each token one by one
        for token in tokens:

            # if we hit an operator, pop the top two numbers
            # first pop is the RIGHT side, second pop is the LEFT side
            if token == "+":
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)

            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)

            elif token == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)

            elif token == "/":
                b, a = stack.pop(), stack.pop()
                # use int() instead of // to truncate toward zero (not floor)
                stack.append(int(a / b))

            # if its none of the operators, its a number
            # convert string to int and push onto stack
            else:
                stack.append(int(token))

        # after the loop, one value remains in the stack -- thats the answer
        return stack[0]