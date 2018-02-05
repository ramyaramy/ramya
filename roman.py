def roman(s):
     value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
     val = 0
     for i in range(len(s)):
        if i > 0 and value[s[i]] > value[s[i - 1]]:
                val += value[s[i]] - 2 * value[s[i - 1]]
        else:
                val +=value[s[i]]
     return val
string = input("Enter the roman no")
print(roman(string))
