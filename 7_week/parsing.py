data = open("test.pcap","rb")
s=data.read()
#global header
print('-----------global header------------')
magic_number=s[0:4]
print('magic number :',list(map(hex,magic_number)))
print('version major :',list(map(hex,s[4:6])))
print('version minor :',list(map(hex,s[6:8])))
print('this zone :',list(map(hex,s[8:12])))
print('sigfigs :',list(map(hex,s[12:16])))
print('snaplen :',list(map(hex,s[16:20])))
print('network :',list(map(hex,s[20:24])))
n=24
while s[n]!='':
    print('-------------packet header-------------')
    print('ts_sec :',list(map(hex,s[n:n+4])))
    print('ts_usec :',list(map(hex,s[n+4:n+8])))
    print('incl_len :',list(map(hex,s[n+8:n+12])))
    print('orig_len :',list(map(hex,s[n+12:n+16])))
    n=n+s[n+8]+16