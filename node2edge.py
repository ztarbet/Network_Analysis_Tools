import csv
#Generic function for making edgelists out of nodelists
def makeEdgeList(in_file, out_file):
    with open(in_file, 'r',encoding='latin') as csvfile:
        f=open(out_file,'w')
        readit = csv.reader(csvfile,delimiter=',')
        for index, data in enumerate(readit):
            if data: #Quick and dirty way of filtering out 'falsy' list items
                rd=len(data) #Get numeric value of items in list
                for i in range(rd): #iterate through list index with item count
                    if i != 0: #Don't repeat the first item, just the ones after it
                        f.write(data[0]+','+data[i]+'\r')
                    if i == 0 and rd == 1: #Keep isolated rows
                        f.write(data[0]+'\r')
