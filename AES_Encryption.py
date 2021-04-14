# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:44:50 2021
@author: Raza_Jutt
"""
plain_text = "54776F204F6E65204E696E652054776F"
key        = "5468617473206D79204B756E67204675"
sbox = ['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76', 
        'CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0', 
        'B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15', 
        '04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75', 
        '09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84', 
        '53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF', 
        'D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8', 
        '51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2', 
        'CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73', 
        '60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB', 
        'E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79', 
        'E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08', 
        'BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A', 
        '70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E', 
        'E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF', 
        '8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']

def hexaToDec(hexval):
    length = len(hexval)
    base = 1
    dec_val = 0
    for i in range(length - 1, -1, -1):
        if hexval[i] >= '0' and hexval[i] <= '9':
            dec_val += (ord(hexval[i]) - 48) * base
            base = base * 16
        elif hexval[i] >= 'A' and hexval[i] <= 'F':
            dec_val += (ord(hexval[i]) - 55) * base
            base = base * 16
    return dec_val

def decToHexa(n):
    hexaDeciNum = ['0'] * 100
    i = 0
    s=""
    while(n != 0):
        temp = 0
        temp = n % 16
        if(temp < 10):
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
        n = int(n / 16)
    j = i - 1
    while(j >= 0):
        s = s+(hexaDeciNum[j])
        j = j - 1
    return s

def bin2dec(binary):   
    decimal, i = 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def dec2bin(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]

def key_set():
    temp= string_To_ary(key)
    for i in range(0,len(temp),4):
        w.append(temp[i:i+4])

def shift(num,ary):
    if num == 3:
        ary = shift(2,ary)
    if num == 2:
        ary = shift(1,ary)
    a = ary[0]
    shifted = []
    for i in range(1,len(ary)):
        shifted.append(ary[i])
    shifted.append(a)
    return shifted

def xor(ary1,ary2):
    ary = []
    for i in range(0,len(ary1)):
        if ary1[i]==ary2[i]:
            ary.append(0)
        else:
            ary.append(1)
    return ary

def comp_len_32(ary):
    temp=[]
    for i in range(0,32-len(ary)):
        temp.append(0)
    for i in ary:
        temp.append(i)
    return temp

def ary_To_string(ary):
    a=""
    for i in ary:
        i = str(i)
        a=a+i
    return a

def string_To_ary(string):
    ary= []
    for i in range(0,len(string),2):
        ary.append(string[i]+string[i+1])
    return ary

def xor_hexas(ary1,ary2):
    binOfHex = ary_To_string(xor(comp_len_32(dec2bin(hexaToDec(ary_To_string(ary1)))),comp_len_32(dec2bin(hexaToDec(ary_To_string(ary2))))))
    ary=[]
    n= 0
    for i in range(8,len(binOfHex),8):
        ary.append(str(decToHexa(bin2dec(int(binOfHex[n:i])))))
        n=i
    ary.append(str(decToHexa(bin2dec(int(binOfHex[n:])))))
    s=""
    for i in range(0,4):
        for j in range(0,2-len(ary[i])):
            s=s+"0"
        ary[i] = s+ary[i]
        s=""
    return ary

def adding_inc(ary):
    replace = ['00','01','02','04','08','10','20','40','80','1B','36']
    for i in range(0,len(replace)):
        if ary[0]==replace[i]:
            ary[0]=replace[i+1]
            return ary

def permutation(ary):
    temp = []
    for i in ary:
        temp.append((sbox[hexaToDec(i[0])*16+hexaToDec(i[1])]))
    return temp

def generating_key_word():
    key_set()
    adding= ["00","00","00","00"]
    for n in range(4,41,4):
        rotated = shift(1,w[n-1])
        sub = permutation(rotated)
        adding = adding_inc(adding)
        w.append(xor_hexas(w[n-4], xor_hexas(sub, adding)))
        w.append(xor_hexas(w[n], w[n-3]))
        w.append(xor_hexas(w[n+1], w[n-2]))
        w.append(xor_hexas(w[n+2], w[n-1]))
        print("Round {0} : ".format(int(n/4)),end="")
        for i in range(n,n+4):
            for j in w[i]:
                print(j,end="")
            print(" ",end="")
        print("")

w = []    
generating_key_word()

def transpos(a,b,c,d):
    ary = []
    for i in range(0,4):
        ary.append(a[i])
        ary.append(b[i])
        ary.append(c[i])
        ary.append(d[i])
    return ary[:4],ary[4:8],ary[8:12],ary[12:16]

def xor_arys(a,b,c,d,w,x,y,z):
    a=xor_hexas(a, w)
    b=xor_hexas(b, x)
    c=xor_hexas(c, y)
    d=xor_hexas(d, z)
    return a,b,c,d

def ary_to_8bit(ary):
    if len(ary)>8:
        return ary[len(ary)-8:]
    a=[]
    for i in range(0,8-len(ary)):
        a.append(0)
    for i in ary:
        a.append(i)
    return a

def comp_word(hexa):
    s=""
    if len(hexa)==0:
        s="00"
    if len(hexa)==1:
        s="0"
    return s+hexa

def hot_bits(ary):
    a = []
    for i in range(0,len(ary)):
        if ary[i]==1:
            a.append(i+1)
    return a

def bin_mul(ary2,ary1):
    ary1.reverse()
    ary2.reverse()
    ary1 = hot_bits(ary1)
    ary2 = hot_bits(ary2)
    ary = []
    bt = [0,0,0,0,0,0,0,0]
    if 1 in ary1:
        for i in ary2:
            ary.append(i)
    if 2 in ary1:
        for i in ary2:
            ary.append(i+1)
    if 9 in ary:
        ary[len(ary)-1]=5
        ary.append(4)
        ary.append(2)
        ary.append(1)
    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):
            if ary[i]==ary[j]:
                ary[i]=ary[j]=0
    for i in ary:
        if i!=0:
            bt[i-1]=1
    bt.reverse()
    return bt

def mix_col(ary):
    ary = transpos(ary[0], ary[1], ary[2], ary[3])
    r = [['02', '03', '01', '01'],
         ['01', '02', '03', '01'],
         ['01', '01', '02', '03'],
         ['03', '01', '01', '02']]
    temp=[]
    for i in range(0,4):
        for j in range(0,4):
            a = xor(bin_mul(ary_to_8bit(dec2bin(hexaToDec(ary[i][0]))) , ary_to_8bit(dec2bin(hexaToDec(r[j][0])))) , bin_mul(ary_to_8bit(dec2bin(hexaToDec(ary[i][1]))) , ary_to_8bit(dec2bin(hexaToDec(r[j][1])))))
            b = xor(bin_mul(ary_to_8bit(dec2bin(hexaToDec(ary[i][2]))) , ary_to_8bit(dec2bin(hexaToDec(r[j][2])))) , bin_mul(ary_to_8bit(dec2bin(hexaToDec(ary[i][3]))) , ary_to_8bit(dec2bin(hexaToDec(r[j][3])))))
            temp.append(comp_word(decToHexa(bin2dec(int(ary_To_string(xor(a,b)))))))
    return transpos(temp[:4],temp[4:8],temp[8:12],temp[12:16])
            
     
plain_text = string_To_ary(plain_text)
a,b,c,d = transpos(plain_text[:4],plain_text[4:8],plain_text[8:12],plain_text[12:16])
w[0],w[1],w[2],w[3] = transpos(w[0],w[1],w[2],w[3])
a,b,c,d = xor_arys(a,b,c,d,w[0],w[1],w[2],w[3])
plain_text = [a,b,c,d]

print("")
for i in range(4,41,4):
    a = permutation(a)
    b = shift(1, permutation(b))
    c = shift(2, permutation(c))
    d = shift(3, permutation(d))
    if i!=40:
        a,b,c,d = mix_col([a, b, c, d])
    w[i],w[i+1],w[i+2],w[i+3] = transpos(w[i],w[i+1],w[i+2],w[i+3])
    a,b,c,d = xor_arys(a,b,c,d,w[i],w[i+1],w[i+2],w[i+3])
    plain_text.append(a)
    plain_text.append(b)
    plain_text.append(c)
    plain_text.append(d)
    print("Chip_Plain {0} : ".format(int(i/4)),end="")
    print_ency = transpos(plain_text[i],plain_text[i+1],plain_text[i+2],plain_text[i+3])
    for k in range(0,4):
        for j in print_ency[k]:
            print(j,end="")
        print(" ",end="")
    print("")
    