seconds = int(input('Enter a number of seconds'))

if seconds >= 60:             
    if seconds >= 3600:        
        if seconds >= 86400:  
           print(seconds/86400) 
        else:
           print(seconds/3600)
    else:
        print(seconds/60)
else:
    print(seconds)