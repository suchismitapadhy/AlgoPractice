def is_substring(s1,s2):
    if s1 in s2:
        return True
    else:
        return False
def is_rotation(s1,s2):
    combined_string = s2+s2
    return is_substring(s1, combined_string)


print(is_rotation("waterbottle","erbottlewat"))

