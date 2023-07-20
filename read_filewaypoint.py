fistlist = []
seclist = []
theelist = []

with open("Tmission.waypoints", 'r') as file:
    for line in file:
        grade_data = line.strip().split(',')
        #print(grade_data)
        #print(line)
        fistlist.append(line.strip().split(','))
    #print(fistlist)
    seclist = fistlist[1::]
    print(seclist)
    for i in range(len(seclist)):
        path = seclist[i]
        print(path.replace('\t', ','))
        #print(i.strip().split(','))