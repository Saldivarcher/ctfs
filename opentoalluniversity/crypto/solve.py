import binascii
import base64

e=65537
n=93316706476599055269499475966339632366128494502615145871121575995464851982328545435472014196684471072096400303192326820620207061604879502766225659968844408357170825396781830499510701335893403286437663075046090892593806432944501933137132009929212253957607820275494915496282840988734943909169103512885145466129

flag=b"OTA{REDACTED}"

#TosynjSspLHNIk7NszpHz/phNh5ko35ozxXVjOz+VvyINVIEXnwXdWmg2zlMrtpPpbLo6Ra0zHVl2Qwd/m/pMKJqzHiol1eHWy4nrs0rHQYJUP1zZlZ770XaQWkagc32RNnpM18JhTluPypOr9Uxeztrt+TTG9lqMYIIUUPw+7g=
decode = TosynjSspLHNIk7NszpHz/phNh5ko35ozxXVjOz+VvyINVIEXnwXdWmg2zlMrtpPpbLo6Ra0zHVl2Qwd/m/pMKJqzHiol1eHWy4nrs0rHQYJUP1zZlZ770XaQWkagc32RNnpM18JhTluPypOr9Uxeztrt+TTG9lqMYIIUUPw+7g=

def textToInteger(text):
  return int(b'0x'+binascii.hexlify(text),16)

def integerToText(integer):
  try:
    return binascii.unhexlify(b'%x'%integer)
  except binascii.Error:
    return binascii.unhexlify(b'0'+b'%x'%integer)

print(base64.b64encode(integerToText(pow(textToInteger(flag),e,n))))

#TosynjSspLHNIk7NszpHz/phNh5ko35ozxXVjOz+VvyINVIEXnwXdWmg2zlMrtpPpbLo6Ra0zHVl2Qwd/m/pMKJqzHiol1eHWy4nrs0rHQYJUP1zZlZ770XaQWkagc32RNnpM18JhTluPypOr9Uxeztrt+TTG9lqMYIIUUPw+7g=

