# Scripts

## My random collection of scripts for stuff.

### obj2shell
```
obj2shell - Parses objdump(1) input and converts it to shellcode

michael@mainz(dev):$ objdump -D shellcode.o|./obj2shell.py 
Shellcode: 36 bytes
\x31\xc0\x50\x68\x2e\x74\x78\x74\x68\x66\x6c\x61\x67\x50\x68\x2f\x63\x61\x74\x68\x2f\x62\x69\x6e\x89\xe5\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80
