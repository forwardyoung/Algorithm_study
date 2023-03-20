ipv6 = input()
ipv6 = ipv6.split(':')
if ipv6[0] == '':
    ipv6 = ipv6[1:]
if ipv6[-1] == '':
    ipv6 = ipv6[:-1]

result = ''
for i in ipv6:
    if i == '':
        result += '0000:'*(8-len(ipv6)+1)
    else:
        result += i.zfill(4)+':' # zfill() 지정한 자릿수 중 모자란 자릿수 0으로 채움

print(result[:-1])