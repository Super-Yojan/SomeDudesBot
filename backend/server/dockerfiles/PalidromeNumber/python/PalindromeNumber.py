def palindrome_number(num):
    new_num = 0
    copy_num = num
    while(copy_num/10>0):
        new_num = (new_num*10) + copy_num %10
        copy_num = copy_num // 10
    return new_num == num
