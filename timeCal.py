seconds = int(input('Enter a number of seconds'))

if seconds >= 60:             
    print(seconds/60)

elif seconds >= 3600:
    print(seconds/60)

elif seconds >= 86400:  
    print(seconds/3600)
    
else:
    print(seconds/86400) 