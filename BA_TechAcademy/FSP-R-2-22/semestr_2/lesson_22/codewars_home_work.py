# 3. https://www.codewars.com/kata/6339de328a3b8f0016cc5b8d

# for referance, this is what a tree looks like:
"""
o     <= tree canopy
|
|     <= tree trunk
|
"""
def magic_plant(p_field,split,n):
    t = p_field.count("|") - n
    s = split ** n
    r = ['o' * s ]
    
    r.extend("|" * s for _ in range(t))
    return "\n".join(r)


# 4. https://www.codewars.com/kata/62f96f01d67d0a0014f365cf/train/python


def ball_test(s, r):
    trevel , y = 0,0
    for i in r:
        if trevel == s : s,trevel,y = s - (y+1),0,0
        if i == 'x': y+=1
        trevel += 1
    return True if s > 0 else False 
    




# 5. https://www.codewars.com/kata/579ba41ce298a73aaa000255/train/python


"""l1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
      'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
      'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', '']
l2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
      'eighty', 'ninety']


def name_that_number(x):
    result = ''
    if not x:
        return 'zero'
    elif x % 100 <= 19:
        result += l1[x % 100 - 1]
    else:
        result = result + l2[x % 100 // 10 - 2] +  ' ' + l1[x % 10 - 1]
    return result
    
    
#  модифицыровал    
    """

units = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
        8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 14: "fourteen"}
tens = {3: "thir", 5: "fif", 2: "twen", 4: "for", 8: "eigh"}

def name_that_number(x):
    if x in units:
        return units[x]
    ten, unit = divmod(x, 10)
    if x <= 19:
        return "{}teen".format(tens.get(unit, units[unit]))
    else:
        return "".join(("{}ty".format(tens.get(ten, units[ten])), " {}".format(units[unit]) if unit else ""))
