def replace_space(astr):
    new_str = ""
    for i in range(len(astr)):
        if astr[i] == " ":
            new_str+= "%20"
        else:
            new_str+= astr[i]
    return new_str

def replace_space(astr):
    return "%20".join(astr.split())

def main():
    print(replace_space("radha nihar"))

main()

#string does not support item assignment
#string is immutable
