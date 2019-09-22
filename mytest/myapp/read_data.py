
def read_data():
    cache_data=open('../mytest/myapp/cache.txt','r+')
    datalines=cache_data.readlines()
    if len(datalines) != 0:
        if datalines[0] == 'NEW\n':
            for dataline in datalines:
                num=len(dataline)
                if dataline[num-2] == 'A':
                    UA=float(dataline[3:num-2])
                    print(UA)
                elif dataline[num-2] == 'B':
                    UB=float(dataline[3:num-2])
                    print(UB)
                elif dataline[num - 2] == 'C':
                    UC = float(dataline[3:num - 2])
                    print(UC)
                elif dataline[num - 2] == 'D':
                    IA = float(dataline[3:num - 2])
                    print(IA)
                elif dataline[num - 2] == 'E':
                    IB = float(dataline[3:num - 2])
                    print(IB)
                elif dataline[num - 2] == 'F':
                    IC = float(dataline[3:num - 2])
                    print(IC)
        else:
            UA, UB, UC, IA, IB, IC=0.0
            print("没有新数据")
            return (UA, UB, UC, IA, IB, IC)
    else:
        UA, UB, UC, IA, IB, IC = 0.0
        print("没有新数据")
        return (UA, UB, UC, IA, IB, IC)
    # cache_data.seek(0)
    # cache_data.truncate()
    cache_data.close()

    return (UA,UB,UC,IA,IB,IC)