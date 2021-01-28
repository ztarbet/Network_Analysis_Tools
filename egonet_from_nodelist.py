import pandas
from itertools import combinations 

#Function takes a nodelist and generates edgelist using all possible combinations of nodelist row content.
#Function does not check for appropriateness of data manipulation (i.e. unipartite, bipartite, directed/undirected).
#Outputs edgelist to csv which should be treated as undirected.
def egoNet_from_nodeList(in_name, out_name):
    df=pd.read_csv(in_name)
    df=df.fillna('*') #fill na with '*' for detection and removal later (None, np.nan, or NoneType does not work for some reason)
    ego_out=pd.DataFrame()
    for i,row in df.iterrows():
        edge=list(combinations(row,2))
        edge=[x for x in edge if x[0] != '*' and x[1] != '*']
        ego_out=ego_out.append(edge)
    ego_out.drop_duplicates(inplace=True)
    ego_out.rename(columns={0:'ego',1:'alter'}, inplace=True)    
    ego_out.to_csv(out_name,index=False)
