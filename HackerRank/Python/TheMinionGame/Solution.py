def minion_game(x):
    vowels = ['A', 'I', 'E', 'O', 'U']
    n = len(x)
    kevin = 0
    stuart = 0
    for i in range(n):
        if x[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i
    if kevin > stuart:
        print('Kevin', kevin)
    elif stuart > kevin:
        print('Stuart', stuart)
    else:
        print('Draw')
s = input()
minion_game(s)