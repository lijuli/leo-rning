def find(s1, s2):
    if len(s1) > len(s2):
        return False

    i = 0
    j = 0
    while j < len(s1) and i < len(s2):
        if s2[i] == s1[j]:
            j += 1
            i += 1
            continue
        i += 1
    if j == len(s1):
        return True
    return False


def new_find(s1, s2, i, j):
    if s1 == '':
        return True

    if s2 == '':
        return False

    if len(s1) > len(s2):
        return False

    new_find(s1[i+1:], s2[j+1:], i+1, j+1)


if __name__ == "__main__":
    # seq_a = input()
    # seq_b = input()
    seq_a = 'abc'
    seq_b = 'ahbgdcu'

    # print(find(seq_a, seq_b))

    print(new_find(seq_a, seq_b, 0, 0))
