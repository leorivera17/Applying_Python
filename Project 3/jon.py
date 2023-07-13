def remove_upper(string):
    answer = ''

    for i in string:

        if i in 'abcdefghijklmnopqrstuvwxyz':
            answer += i
    print(answer)
    return answer
remove_upper('Hi There, BYe!')