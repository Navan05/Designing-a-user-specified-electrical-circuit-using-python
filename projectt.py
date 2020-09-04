def fn():
    print("For a DC circiut click 1","\nFor an AC circuit click 2")
    da=int(input("Enter the desired circuit"))
    if da==1:
        
        print('The selected circuit is a DC')
        input('')
        print("Let's begin")
        input('')
        print('For a series resistance cinnection, click 1')
        print(' For a parallel resistance connection ,click 2')
        print('For series-parallel combination circuit, click 3')
        sr=int(input('enter number desired'))  
        if sr==1 or sr==2:
            nr=int(input('Enter number of resistors'))
        if sr==1:
           v=int(input('Enter the voltage'))
           import turtle
           for i in range(0,nr):
               t=turtle
               t.color('red')
               t.forward(100)
               t.left(45)
               t.forward(10)
               t.right(90)
               t.forward(10)
               t.left(90)
               t.forward(10)
               t.right(90)
               t.forward(10)
               t.left(90)
               t.forward(10)
               t.right(90)

               t.forward(10)
               t.left(90)                   
               t.forward(10)
               t.right(90)
               t.forward(10)
               t.left(45)
               t.forward(25)
           t.right(90)
           t.forward(35)
           t.right(90)
           t.forward(25)
           t.forward(52)
           t.right(90)
           t.forward(10)
           t.right(180)
           t.forward(20)
           t.right(180)
           t.forward(10)
           t.penup()
           t.left(90)
           t.forward(5)
           t.pendown()
           t.right(90)
           t.forward(20)
           t.right(180)
           t.forward(40)
           t.right(180)
           t.forward(20)
           t.left(90)
           t.forward(100)
           for i in range(1,nr):
               t.forward(180)
           t.right(90)
           t.forward(32)
           l=0
           for i in range(1,nr+1):
               r=int(input('Enter the values of the resistance'))
               l=l+r
           print('Series eq is',l)
           print('The current in this circuit is',v/l)
        if sr==2:
            import parallel
            v1=int(input('Enter the voltage of the circuit'))
            k=0
            for j in range(1,nr+1):
              r2=int(input('Enter the value of the resistance'))
              k=k+1/r2
            print(1/k)
            print('The total current in the circuit is',v1*k)
            
        if sr==3:
            print('Click1 for a parallel connection in series with a parallel connection ')
            print('Click2 for a series connection in series with a parallel connection')
            q=int(input('Enter the number desired '))
            if q==1:
                import PSP
                
            else:
                import SSP
         
    else:
        import AC
fn()
s=input('Do you wish to re-run for another circuit? Y/N')
if s=='Y':
    fn()
else:
    print('THANK YOU')


    
    
            
