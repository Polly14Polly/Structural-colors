for N in range(967, 2, -1):
    a = '9' + '6'*N
    while '666' in a or '9909' in a or '66' in a:
        a = a.replace('666', '999', 1)
        a = a.replace('9909', '6', 1)
        a = a.replace('66', '0', 1)
    if len(a) == 10:
        print(N)
        break
