import time
import pdb
import sys
sys.breakpointhook = lambda *args, **kwargs: print("Hello")
# Hàm này thực thi khi breakpoint() được gọi

print(time.time_ns())

print('a')
pdb.set_trace()  # viết n rồi enter để tiếp tục thực thi
# == breakpoint()
print('b')
