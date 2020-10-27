"""
Pseudocode:
1) Open file and parse line by line
2) Use two dictionaries, {service-:[QPS,Throughput]} and {cell,:[QPS,Throughput]}
3) If either keys are in any of the dictionary, add up the throughput and QPS

Big O: O(n)
"""

def traffic_check(filename):

    servicedict = dict()
    celldict = dict()

    with open(filename, 'r') as file:
        for linenum, line in enumerate(file):
            if linenum == 0:
                continue
            else:
                columns = line.split()
                service = columns[0]
                cell = columns[1]
                qps = int(columns[2])
                throughput = int(columns[3])

                # if it's not in servicedict it is also not in celldict
                if service not in servicedict:
                    servicedict[service] = [qps, throughput]
                elif service in servicedict:
                    servicedict[service] = [servicedict[service][0]+qps, servicedict[service][1]+throughput]
                if cell not in celldict:
                    celldict[cell] = [qps, throughput]
                elif cell in celldict:
                    celldict[cell] = [celldict[cell][0]+qps, celldict[cell][1]+throughput]
        
        print(celldict)
        print(servicedict)

traffic_check('data.txt')



            
