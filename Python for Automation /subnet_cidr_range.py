cidr =  input("enter a your cidr range: ")
mask_bit = int(cidr.split('/')[1])
while (mask_bit > 28 or mask_bit < 16):
    cidr =  input("enter a valid cidr range(range can be 16-28): ")
    mask_bit = int(cidr.split('/')[1])
intput_string = input("enter availability regions with space: ").split()
#print(intput_string)
count = len(intput_string)
adict = {}
for avail in intput_string:
    for i in range(count):
        sub = "string"
        sub +="i"
    sub = int(input("enter a count of subnets you need in"+" "+avail+": "))
    adict[avail] = sub
#print(adict)
sum_val = sum(adict.values())
host_id_size = (32 - mask_bit)
bit_cal1 = (host_id_size - 8)
no_of_ips = (2**bit_cal1)
if (host_id_size <= 8):
    bit_cal2 = int(2**host_id_size)
    if (bit_cal2%sum_val == 0):
        cidr_range = bit_cal2//sum_val
        for i in range(cidr_range,bit_cal2+1,cidr_range):
            i = str(i-1)
            print(cidr.replace(cidr.split('.')[3],i)+'/'+str(mask_bit))
    else:
       print("cidr range can not be divided according to total provided subnets")
else:
    ips_bit_cal1 = int(2**bit_cal1)
    if(ips_bit_cal1%sum_val == 0):
        cidr_range = ips_bit_cal1//sum_val
        for i in range(cidr_range,ips_bit_cal1+1,cidr_range):
            i = str(i-1)
            print(cidr.replace(cidr.split('.0.')[1],i)+".255/"+str(mask_bit))
    else:
        print("cidr range can not be divided according to total provided subnets")