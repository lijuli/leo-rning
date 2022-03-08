key = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def new_method(arr, string, idx):
    if len(string) <= idx:
        print(arr)
        return

    string = arr[idx]

    for c in string:
        new_method(arr, idx+1, res + c)





arr0 = ['abc', 'def', 'pqrs']
# arr = ['abc', 'def']
# arr =['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
#
# arr0 = []
arr = new_method(arr0, '', 0)
print(arr)

# arr1 = new_method(arr, 'def')
# print(arr1)
#
# arr2 = new_method(arr1, 'pqrs')
# print(arr2)
