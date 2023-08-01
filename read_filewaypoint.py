import numpy as np

def read_mp(file_mp):
    fistlist = []
    seclist = []
    with open(file_mp, 'r') as file:
        for line in file:
            grade_data = line.replace('\t', ' ')
            fistlist.append(grade_data)
        fistlist = fistlist[1::]

        fistlist = np.array(fistlist)
        #print(fistlist)

        for x in fistlist:
            li = list(x.split(" "))
            print(li)
            if len(li) < 12:
                continue
            lat = float(li[8])
            lon = float(li[9])
            path = (lat,lon)
            seclist.append(path)
                #print(seclist)

        return seclist

if __name__ == "__main__":
    print(read_mp())