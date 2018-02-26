''' disassemble our if statement a != a '''
from dis import dis

a = 0
count = 0

code_str = '''
if a != a:
    count += 1
'''
print(dis(code_str))










#  if a != a:
#   LOAD_NAME               0 (a)
#      << a can be changed here >>
#   LOAD_NAME               0 (a)
#   COMPARE_OP              3 (!=)
#   POP_JUMP_IF_FALSE       16