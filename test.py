import sys
import time 
import math

def print_progress(cur,total,length,title="In Progress"):
    done = math.ceil((cur*length)/total)
    remain = length-done

    done_str = '#'*int(done)
    remain_str = '.'*int(remain)
    # cur_str = '0'*int(len(str(total))-len(str(cur)))+str(cur)

    print(f'\t⌛ {title}: [{done_str}{remain_str}] {cur}/{total} done', end='\r')
    if total == cur:
        print('\t✅')

r = 100
p = 0
for i in range(r):
    p+=1
    print_progress(p,r,10)
    time.sleep(0.02)