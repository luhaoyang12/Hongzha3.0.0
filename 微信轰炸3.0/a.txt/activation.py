import os
with open(os.path.join(os.getcwd(),'activation.txt'), "r+", encoding='UTF-8')as f:
    if f.read()=='00000000':
        f.seek(0)
        f.truncate()
        f.write('12344321')
    else:
        f.seek(0)
        f.truncate()
        f.write('00000000')
