# Grant - grantslone

def base_conv(num, frombase, tobase):
    try:
        frombase = int(frombase)
        tobase = int(tobase)
        num_dec = int(num, frombase)
        b = [2,8,10,16]
        for x in [frombase, tobase]:
            if x not in b:
                raise ValueError
    except ValueError:
        return "ValueError: Please use a valid number and/or base"
    
    base_dict = {
        2: ':b',
        8: ':o',
        10: ':d',
        16: ':x'
    }
    return "Converting " + str(num_dec) + " from Base(" + str(frombase) + ") to Base(" + str(tobase) + ") \nResult: "\
    + ('{' + base_dict[tobase] + '}').format(num_dec)

num = input("Enter a number: ")
fbase = input("Please enter a base to start from [2, 8, 10, 16]: ")
tbase = input("Please enter a base you wish to convert to [2, 8, 10, 16]: ")

print(base_conv(num, fbase, tbase))