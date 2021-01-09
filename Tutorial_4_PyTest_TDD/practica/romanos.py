def num_romano(a): 
    num = [1, 4, 5, 9, 10, 40, 50, 90, 
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", 
           "L", "XC", "C", "CD", "D", "CM", "M"]
    romano = ""
    i = 12
    valor = a
    while valor:
        div = valor // num[i]
        valor %= num[i]
        while div:
            romano = romano + sym[i]
            div -= 1
        i -= 1

    return romano

def romano_num(n):
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(0, len(n)):
        if i == 0 or roman_dic[n[i]] <= roman_dic[n[i - 1]]:
            res += roman_dic[n[i]]
        else:
            res += roman_dic[n[i]] - 2 * roman_dic[n[i - 1]]
    return res
