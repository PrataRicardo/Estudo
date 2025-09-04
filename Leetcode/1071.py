def gcdOfStrings(str1, str2):
    
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    gcd_len = gcd(len(str1), len(str2))
    output = str1[:gcd_len]

    if output * (len(str1) // len(output)) == str1 and output * (len(str2) // len(output)) == str2:
        return output
    else:
        return ""
    
str1 = input()
str2 = input()

print(gcdOfStrings(str1, str2))