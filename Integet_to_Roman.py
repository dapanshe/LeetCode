class Solution:
    # @return a string
    def intToRoman(self, num):
        n = int(num/1000)
        num -= 1000*n
        ans = ''
        while n > 0:
            ans += 'M'
            n -= 1
        if num >= 900:
            num -= 900
            ans += 'CM'
        if num >= 500:
            num -= 500
            ans += 'D'
        if num >= 400:
            num -= 400
            ans += 'CD'
        n = int(num/100)
        num -= n*100
        while n > 0:
            ans += 'C'
            n -= 1
        if num >= 90:
            num -= 90
            ans += 'XC'
        if num >= 50:
            num -= 50
            ans += 'L'
        if num >= 40:
            num -= 40
            ans += 'XL'
        n = int(num/10)
        num -= 10*n
        while n > 0:
            ans += 'X'
            n -= 1
        if num >= 9:
            num -= 9
            ans += 'IX'
        if num >= 5:
            num -= 5
            ans += 'V'
        if num >= 4:
            num -= 4
            ans += 'IV'
        while num > 0:
            ans += 'I'
            num -= 1
        return ans
