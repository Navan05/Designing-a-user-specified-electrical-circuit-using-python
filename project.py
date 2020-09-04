print("for a DC circiut click 1","for an AC circuit click 2")
da=int(input("enter the desired circuit"))
if da==1:
    
    print('the selected circuit is a DC')
    input('')
    print("let's begin")
    input('')
    print('for series resistance click 1')
    print(' for a parallel resistance click 2')
    print('for series-parallel combination click 3')
    while True:
     sr=int(input('enter number desired'))  
     if sr==1 or sr==2:
        nr=int(input('enter number of resistors'))
     if sr==1:
       v=int(input('enter the voltage'))
       import turtle
       for i in range(0,nr):
           t=turtle
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
           r=int(input('enter the values of the resistance'))
           l=l+r
       print('series eq is',l)
       print('the current in this circuit is',v/l)
      elif sr==2:
        import project2
        v1=int(input('enter the voltage of the circuit'))
        k=0
        for j in range(1,nr+1):
          r2=int(input('enter the value of the resistance'))
          k=k+1/r2
        print(1/k)
        print('the total current in the circuit is',v1*k)
      elif sr==3:
        print('click1')
        print('click2')
        q=int(input('enter'))
        if q==1:
            import pro3
        else:
            import proj2
      elif sr not in [1,2,3]:
        print("invalid statement")
                    
    
        
        
