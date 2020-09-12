''' SubNet Calculator
 Python script to calculate IP Subnets in an existing subnet
 Trying to follow PEP8 Style Guide.
'''
import os
import sys
import math

def ConvertIPNumToString(iPNumber):
    v1 = iPNumber & 0xff
    v2 = (iPNumber >> 8) & 0xff
    v3 = (iPNumber >> 16) & 0xff
    v4 = (iPNumber >> 24)
    return f'{v4}.{v3}.{v2}.{v1}'


def ConvertIPStringtoNum(IPString):
    IPArray = IPString.split('.')
    if len(IPArray) != 4:
        print("Exit not correct IP network: {}".format(IP1))
        sys.exit(0)
    ipNum1 = int(IPArray[0]) << 24 # equal to IParray * 2 to the power of 24
    ipNum2 = int(IPArray[1]) << 16
    ipNum3 = int(IPArray[2]) << 8
    ipNum4 = int(IPArray[3])
    return (ipNum1 + ipNum2 + ipNum3 + ipNum4)


IP1 = "10.0.0.0" # The main network IP to check subnets in example 10.0.0.0
MASK1 = 8 # The network mask BITS for the main network IP
MASK2 = "255.0.0.0" # Alt mask if simpler
SUBNET1 = 17 # The Subnet bit mask to calculate for.
SUBNET2 = "255.255.255.128" # Alt subnet string mask if simpler

maskType = 1  # 1 or 2 depending on what to test bitmask or stringmask
subNetType = 2  # 1 or 2 depending on subnet type to test bitmask or stringmask

ipNum = ConvertIPStringtoNum(IP1)
print(f'IP Number: {ipNum}')

maskNum = ConvertIPStringtoNum(MASK2)
print(f'Mask Number: {maskNum}')

maskNum2 = 0
for x in reversed(range(32-MASK1, 32)):
    maskNum2 = maskNum2 + (2**x)
    
print(f'Mask Number 2: {maskNum2}')

maskString = ConvertIPNumToString(maskNum)
print(f'Mask String: {maskString}')

maskString2 = ConvertIPNumToString(maskNum2)
print(f'Mask String 2: {maskString2}')

netwworNum = ipNum & maskNum
print(f'Network Num: {netwworNum}')

networkSize = 2**(32-MASK1)
print(f'Network Size: {networkSize}')

networkString = ConvertIPNumToString(netwworNum)
print(f'Network string: {networkString}')

networkMaxNum = netwworNum + networkSize
print(f'Network Max Num: {networkMaxNum}')

networkMaxString = ConvertIPNumToString(networkMaxNum)
print(f'Network Max string: {networkMaxString}')


subnetNum = 0
for x in reversed(range(32-SUBNET1, 32)):
    subnetNum = subnetNum + (2**x)
print(f'SubNet Number: {subnetNum}')

subnet1Size = 2**(32-SUBNET1)
print(f'subnet Size: {subnet1Size}')

subnet1 = ipNum & subnetNum
print(f'subnet Network: {ConvertIPNumToString(subnet1)}')
try:
    os.remove("output44.csv")
except:
    print("file don't exists...creating new")

fileHandle = open("output44.csv", "a")
fileHandle.write("Networks\n")

lastNet = False
while lastNet == False:
    subnet1 = subnet1 + subnet1Size
    if subnet1 >= networkMaxNum:
        lastNet = True
    else:
        fileHandle.write(f'{ConvertIPNumToString(subnet1)}\n')

fileHandle.close()