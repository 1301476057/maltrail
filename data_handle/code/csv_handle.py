
import os
import pandas as pd

def delete_same(inFile,outFile):
    lines_seen = set()

    infile= open(inFile,"r")
    outfile=open(outFile,"w")

    for line in infile:
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)

    infile.close()
    outfile.close()
    print ("Succeed to deletesame !")



path=os.path.abspath(os.path.join(os.getcwd(), "..")) 

readFile=path+'/data/lastest_all_deletesame.csv'
wirteFile=path+'/data/lastest_some_deletesame.csv'
outFile=path+'/data/lastest_some_deletesame2.csv'


df=pd.read_csv(readFile,sep='\a',usecols=['ip_dst','full_uri','host','path','query_parameter','user_agent','accept_language','accept_encoding'])

# df2=pd.DataFrame(data=df['Timestamp'])
# df2['Timestamp']=df['Timestamp']
# df2['Label']=df['Label']

#df.sort_values(by='Timestamp')

df.to_csv(wirteFile,index=False,sep='\a')


delete_same(wirteFile,outFile)





