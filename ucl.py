def ucl():
    n=int(input('enter number of groups to find the rankings'))
    x=[]
    print('enter all the match details')
    for i in range(0,n):
        d=[]
        for j in range(0,12):
            f=input('')
            d.append(f)        
        x.append(d)       
    tn=[]
    p=[]
    pp=[]
    for r in range(0,n):
        e=[]
        gd={}
        w={}
        for s in range(0,12):            
            y=[]
            z=x[r][s]
            y=z.split(' ')
            if y[0] not in e:
                e.append(y[0])
            if y[4] not in e:
                e.append(y[4])
            m=int(y[1])
            n=int(y[3])
            aw=m-n
            al=n-m
            if y[0] in w.keys():
                if m>n:
                    w[y[0]]=3+w[y[0]]
                    gd[y[0]]=aw+gd[y[0]]
                elif m==n:
                    w[y[0]]=1+w[y[0]]
                    gd[y[0]]=aw+gd[y[0]]
                else:
                    w[y[0]]=0+w[y[0]]
                    gd[y[0]]=aw+gd[y[0]]

            else:
                if m>n:
                    w[y[0]]=3
                    gd[y[0]]=m-n
                elif m==n:
                    w[y[0]]=1
                    gd[y[0]]=m-n
                else:
                    w[y[0]]=0
                    gd[y[0]]=m-n
            if y[4] in w.keys():
                if m>n:
                    w[y[4]]=0+w[y[4]]
                    gd[y[4]]=al+gd[y[4]]
                elif m==n:
                    w[y[4]]=1+w[y[4]]
                    gd[y[4]]=al+gd[y[4]]
                else:
                    w[y[4]]=3+w[y[4]]
                    gd[y[4]]=al+gd[y[4]]
            else:
                if m>n:
                    w[y[4]]=0
                    gd[y[4]]=al
                elif m==n:
                    w[y[4]]=1
                    gd[y[4]]=al
                else:
                    w[y[4]]=3
                    gd[y[4]]=al

        l=list(w.values())
        p.append(l)
        p1=list(gd.values())
        pp.append(p1)
        tn.append(e)
    ra=[]
    ra1=[]
    for i in range(0,len(p)):
        ran=sorted(p[i])
        ra.append(ran)
    for i in range(0,len(pp)):
        ran=sorted(pp[i])
        ra1.append(ran)
    for i in range(0,len(p)):
        for j in range(0,len(p[i])):
            if p[i][j]==ra[i][3] and pp[i][j]==ra1[i][3]:
                s=tn[i][j]
            if p[i][j]==ra[i][2] and pp[i][j]==ra1[i][2]:
                d=tn[i][j]
            if p[i][j]==ra[i][1] and pp[i][j]==ra1[i][1]:
                f=tn[i][j]
            if p[i][j]==ra[i][0] and pp[i][j]==ra1[i][0]:
                a=tn[i][j]
                
        print(s+' '+d+' '+f+' '+a)        
                
           
            
