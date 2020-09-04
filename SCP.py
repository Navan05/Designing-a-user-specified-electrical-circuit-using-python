while True:
#    n=int(input('Press 1.Series in series with parallel circuit 2.Parallel in series with parallel'))
    try:
        n=int(input('Press 1.Series in series with parallel circuit 2.Parallel in series with parallel'))
    except ValueError:
        print('Enter valid input')
    if n>0 and n<3:
        if n==1:
            print('The chosen circuit is series in series with parallel circuit')
#Series
            r=int(input('Enter the number of resistors in series'))
            l=0
            for i in range(1,r+1):
                q=int(input('Enter the value of the resistor'))
                l+=q
            v=print('The series equivalent resistance is',l)
            k=0
            s=int(input('Enter the number of resisitors in parallel'))
            for j in range(1,s+1):
                r2=int(input('Enter the value of the resistance'))
                k=k+1/r2
            w=print('The parallel equivalent resistance is',1/k)
            print('The equivalent resistance of the chosen circuit is',l+1/k)
        if n==2:
            print('The chosen cicuit is parallel in series with parallel')
#Parallel in series with parallel
            z=int(input('Enter the number of branches of parallel circuits'))
            for p in range(1,z+1):
                s=int(input('Enter the number of resisitors in 1st branch of parallel connection'))
                k=0
                for j in range(1,s+1):
                    r1=int(input('Enter the value of the resistance'))
                    k=k+1/r1
                w=print('The value of resistance in 1st branch of parallel connection is',1/k)
                t=int(input('Enter the number of resistors in 2nd branch of parallel connection'))
                n=0
                for k in range(1,t+1):
                    r2=int(input('Enter the value of resstance'))
                    n=n+1/r2
                x=print('The value of resistance in the 2nd branch of parallel connection is',1/n)
            print('The equivalent resistance of the circuit is',n+k)            
    else:
        print('Invalid input')
        print('Enter again')
   
