class Luhn(object):
    
    def checkLuhn(self, purportedCC=''):
        sum_ = 0
        parity = len(purportedCC) % 2
        for i, digit in enumerate([int(x) for x in purportedCC]):
            if i % 2 == parity:
                digit *= 2
                if digit > 9:
                    digit -= 9
            sum_ += digit
        return sum_ % 10 == 0

    def indexMany(self, s, str):   #str是要查询的字符
        length = len(s)     #获取该字符串的长度
        str1 = s            #拷贝字符串
        list = []
        sum = 0             #用来计算每次截取完字符串的总长度
        try:
            while str1.index(str)!=-1:      #当字符串中没有该字符则跳出
                n = str1.index(str)         #查询查找字符的索引
                str2 = str1[0:n + 1]        #截取的前半部分
                str1 = str1[n + 1:length]   #截取的后半部分
                sum = sum + len(str2)       #计算每次截取完字符串的总长度
                list.append(sum - 1)        #把所有索引添加到列表中
                length=length-len(str2)     #截取后半部分的长度
        except ValueError:
            return list
        return list
    
    def listmatrix(self, num, length):
        a = list(str(num))
        b =[0] * length
        j = 0
        for i in a:
            b[j] = int(i)
            j += 1
        return b

    def replacenumber(self, replace = '', numbers = '', number = ''):
        i = 0
        final = ''
        a = list(number)
        for j in replace:
            a[j] = str(numbers[i])
            i += 1
        b = ''.join(a)
        return b

    def listnumber(self, number = ''):
        replace = self.indexMany(number,'*')
        total_num = 10 ** len(replace)
        final = ''
        for i in range(total_num):
            numbers = self.listmatrix(i, len(replace))
            final = self.replacenumber(replace, numbers, number)
            i += 1
            print(final)
        
    def listsinglenumber(self, numberr, number = ''):
        final = ''
        replace = self.indexMany(number,'*')
        numbers = self.listmatrix(numberr, len(replace))
        final = self.replacenumber(replace, numbers, number)
        return final
    
    def checkallLuhn(self, number = ''):
        replace = self.indexMany(number,'*')
        total_num = 10 ** len(replace)
        final = ''
        for i in range(total_num):
            numbers = self.listmatrix(i, len(replace))
            final = self.replacenumber(replace, numbers, number)
            i += 1
            if self.checkLuhn(final):
                print(final)
            else:
                pass