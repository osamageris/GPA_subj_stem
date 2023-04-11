math=[1,1,0.5] # math results
science=[0.99,1,1] # science results
english=[0.95,0.85,0.6] # english results
computer=[1,1,0.6] # computer results
subject=[math, science , english,computer]
subj_stem=[math, science , english]
subj_n=["math", "science" , "english","computer"]
st_name=["AH" , "SM" , "KF" ] # students's names 
st_nam=["AH" , "SM" , "KF"]   # students's result 
st_avg=["AH" , "SM" , "KF"]   # students's percentage 
st_full=["AH" , "SM" , "KF"]  # students's number of full marks 

print("") # print separete line 
 
subjAA=[] # array of A+ students
subjF=[]  # array of failed students
for n in range(len(st_name)):  # loop for calculating total and pecentage results of sudents 
 st_nam[n]=[]
 st_avg[n]=[]
 st_full[n]=[]
 
 
 resul=0
 for t in range (len(subj_stem)):
  stem_subj=subj_stem[t]
  
    
  resultt=stem_subj[n]
  if(resultt>=1):
     st_full[n].append(1)
 
 for j in range(len(subject)): # Loop for subjects completing for calculating total and pecentage results of sudents
  
  subj=subject[j]
  resul+=subj[n]
  
 
     
     

 st_nam[n].append(resul)
 st_avg[n].append(resul/len(subject))
 
print("total",st_nam)
print("total aveg",st_avg)


for b in range (len(st_name)): # Loop for finding accepted or not accepted students in STEM Education
  

 if(((st_avg[b][0]>=0.95) and (len(st_full[b])>=2)) or ((st_avg[b][0]>=0.98) and (len(st_full[n])>=1))):
  print("acepted in STEM")
 else:
  print("not acepted in STEM")
print("foll" ,st_full)
fol=[]
for h in range(len(subject)): # Loop for finding results and GPA and A+ and failed students
 print("students' names",st_name , "thier", subj_n[h]," degrees:" , subject[h])
 subj=subject[h]
 full=[]
 subjAA=[]
 subjF=[]
#result=float(input("eneter student degree :" ))
 print("GPA")
 for i in range(len(subj)):
    
    result=subj[i]
    if(result>= 1):
     print("full mark")
     full.append(st_name[i])
     fol.append(st_name[i])
    elif(result>= 0.95):
     print("A +") 
     subjAA.append(st_name[i])
    elif(result>= 0.9): 
     print("A ")
    elif(result>= 0.85): 
     print("B+") 
    elif(result>= 0.8): 
     print("B") 
    elif(result>= 0.75): 
     print("C+ ")
    elif(result>= 0.7): 
     print("C")
    elif(result>= 0.65): 
     print("D+")
    elif(result>= 0.6): 
     print("D ")
    else:
     print("F")
     subjF.append(st_name[i])
 
 print(subj_n[h] ,"full mark",full," A+ :", subjAA ," faild" ,subjF) # printing  A+ and failed students
print("full mark",fol) # printing Full mark students