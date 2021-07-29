def balance_parentheses(n, s, open, close):
    if n == 0:
        return

    if n == 1:
        s += ')'
        close += 1
        if open == close:
            print(s)
        return

    else:
        if open >= close:
            balance_parentheses(n - 1, s + '(', open + 1, close)
            balance_parentheses(n - 1, s + ')', open, close + 1)
        else:
            return


if __name__ == "__main__":
    n = int(input())
    balance_parentheses(n*2, '', 0, 0)
