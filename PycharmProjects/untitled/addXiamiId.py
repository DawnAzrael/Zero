# -*- coding:utf-8 -*-
import sys


add_user_id = sys.argv[1]
# id to file  --> add

# 244467287
# 355159433
# 24253649

try:
    idPool = open('./idpool.txt', 'a')
    idPool.writelines(add_user_id + '\n')
except:
    pass
idPool.close()
