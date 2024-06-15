from typing import List

answers = []
visited = []

def backtrack(n: int, *, history: List[int]=[]):
    if n == 1:
        answers.append(history.copy())
        history.pop()
        return

    for k in range(n, 1, -1):
        an_case_odd = history[-1] - 3
        an_case_even = 2 * history[-1]
        
        if (k-1, an_case_odd) not in visited:
            visited.append((k-1, an_case_odd))

            if an_case_odd % 2 != 0:
                history.append(an_case_odd)
                backtrack(k-1, history=history)
            else:
                backtrack(k, history=history)

        elif (k-1, an_case_even) not in visited:
            visited.append((k-1, an_case_even))

            if an_case_even % 2 == 0:
                history.append(an_case_even)
                backtrack(k-1, history=history)
            else:
                backtrack(k, history=history)

        else:
            history.pop()
            return


def start(n: int, initial_value: int):
    backtrack(n, history=[initial_value])

start(5, 5)

print('\n'.join(map(str, answers)))

print('\n'.join(map(lambda x: str(list(reversed(x))), answers)))
    