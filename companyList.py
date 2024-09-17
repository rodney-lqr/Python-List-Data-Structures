companyNames = [
    'Google',
    'Facebook',
    'Microsoft',
    'Gcash',
    'Grab',
    'Oracle',
    'Verizon',
    'Cisco',
    'Riot Games',
    'Tencent'
]

print()
print(companyNames)
print() 
print("The 7th index is: ", companyNames[6])
print()
companyNames[4] = "Apple"
del companyNames[7]

for x in companyNames:
    print(x)

print()
print("The last index is: ", companyNames[-1])