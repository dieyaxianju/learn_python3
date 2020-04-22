
"""
1*1=1
1*2=2 2*2=4
1*3=3


横：从1到9
竖的 从1到9
"""

for b in range(1,10):
    for a in range(1,10):
        if a<=b:
            print(a)
            print(b)
            print(a * b)
            # m = '{0}x{1}={2}'.format(1, 2, 1 * 2)
            # print(m,end='/t')
