str = "Kalki"
# print(str)
# print(str[2])
for i in str:
    print(i)
# K
# a
# l
# k
# i

# strs = "yazdaan"
# # method 1
# str1  = slice(0,3,1)
# print(strs[str1])

strs = "rachit"
str1  = slice(0,len(strs)-1,2)
print(strs[str1])
# output = rci

#Method [:]

strs  = "harsh"
print(strs[0:len(strs)])
# harsh
print(strs[0:4])
# hars
print(strs[0:])
# harsh
print(strs[:3])
#har
print(strs[:])
# harsh
strs1 = "rachit"
print(strs1[0:len(strs1):2])
# rci
