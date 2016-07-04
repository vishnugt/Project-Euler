list_ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
list_tens1 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
list_tens = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]

def massfun(l1):
    tempsum = 0
    tempstr = ""
    for i in l1:
        tempsum = tempsum + i
    if tempsum == 0:
        return ""
    else:
        if not(l1[0] == 0):
            tempstr = list_ones[l1[0]] + " Hundred "
        if l1[1] == 1:
            return tempstr + list_tens1[l1[2]]
        if l1[1] == 0:
            if l1[2] == 0:
                return tempstr
            else:
                return tempstr + list_ones[l1[2]]
        else:
            tempstr = tempstr + list_tens[l1[1]]
        if l1[2] == 0:
            return tempstr[0:len(tempstr) - 1]
        else:
            return tempstr + list_ones[l1[2]]

def sumlist(l1):
    sum1 = 0
    for i in l1:
        sum1 = sum1 + i
    if sum1 == 0:
        return False
    return True

for t in range(int(raw_input())):
    n = int(raw_input())
    string = ""
    list_digits = list(str(n))
    list_digits = [0 for i in range(12 - len(list_digits))] + [int(i) for i in list_digits]
    l1 = list_digits[0:3]
    l2 = list_digits[3:6]
    l3 = list_digits[6:9]
    l4 = list_digits[9:12]
    tempstr1, tempstr2, tempstr3, tempstr4 ="", "", "", ""
    if sumlist(l1):
        tempstr1 = massfun(l1) + " Billion "
    if sumlist(l2):
        tempstr2 = massfun(l2) + " Million "
    if sumlist(l3):
        tempstr3 = massfun(l3) + " Thousand "
    if sumlist(l4):
        tempstr4 = massfun(l4)
        if(tempstr4[len(tempstr4) - 1] == " "):
            tempstr4 = tempstr4[0:len(tempstr4) - 1]
            #print "ya"
    print tempstr1 + tempstr2 + tempstr3 + tempstr4