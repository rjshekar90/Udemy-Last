

# Balanced parantheses

def bal_check(s):

    if len(s)%2 != 0:
        return False

    opening = set('({[')

    matches = ([('(',')'), ('{','}'), ('[',']')])

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)

        else:
            if len(stack) == 0:
                return False

            else:
                last_open = stack.pop()
                if (last_open, paren) not in matches:
                    return False

    return True

print bal_check('[](){([[[]]])}')
