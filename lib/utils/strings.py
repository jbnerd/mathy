def is_palindrome_number(num: int) -> bool:
    num = str(num)
    rev_num = reversed(num)
    for i, j in zip(num, rev_num):
        if i != j:
            return False
    return True
