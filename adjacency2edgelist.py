#Transforms generic adjacency matrix to nodelist
#Returns output file
import csv
def adjacency_to_nodelist(in_file,out_file):
    with open(in_file, 'r') as csvfile:
        f=open(out_file,'w')
        readit = csv.reader(csvfile,delimiter=',') #set input delimiter here
        c=-1
        for i, data in enumerate(readit):
            c+=1
            if c == 0:
                head=data #designate first row as column header
                id_cell=[head[x].replace(head[x], 'id') for x in range(1) if len(head[x]) == 0] #if first item in header is blank, replace with 'id'
                head_col=id_cell+[head[x] for x in range(2,len(data))]
            if c != 0:
                row_head=[data[x] for x in range(1)]
                nodes=[head[x] for x in range(2,len(data)) if int(data[x]) != 0]
                row=row_head+nodes+['\r']
                row = ','.join([str(elem) for elem in row])
                f.write(row)
    return out_file
