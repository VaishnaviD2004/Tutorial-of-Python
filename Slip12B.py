check_string="ChitaliPathardiAhmednagarMaharashtraIndia"
dict={}
for i in check_string:
    if i in dict:
        dict[i] +=1
    else:
        dict[i] =1
        
for k in dict:
    print(k,"-",dict[k])
            