a =int(input('no of rows,limit for the row is 3'))
b= int(input('no of columns,limit for the column is 3'))
if a==1 and b==1:
    p= int(input('row AND COLUMN 1'))
    C=[p]
    print(C)
    s=input('do you want to do further calaculation like add,sub,multiplication,determinant type yes or no')
    if s== 'yes':
        op=int(input('1,2,3,4 for add,sub,multiplication,determinant respectively'))
        if op==1:
            num = int(input('what you want to add'))
            add = C+num
            print(add)
        elif op ==2:
            num = int(input('num you want to sub'))
            sub=C-num
            print(sub)
        elif op==3:
            print('now here you have to give the order of maxtrix b whom you will multiply with the first matrix.limit for the row and column is 3')
            rows_B = int(input('row_b = '))
            column_b = int(input('column_B = '))
            if rows_B==1 and column_b==1:
                mult=int(input('num you want to multiply'))
                print(mult*p)
            elif rows_B==1 and column_b==2:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                print([p*b11,p*b12])
            elif rows_B==1 and column_b==3:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b13 = int(input('b13'))
                print([p*b11,p*b12,p*b13])
            else:
                print('please give the suitable rows and column for matrix b as per maths')
        elif op==4:
            print(C,' is the determinant of ',p)
        else:
            print('please select valid operations')
    elif s== 'no':
        print('ok,thank you')
    else:
        print('please type valid answer')
elif a==1 and b==2:
    p=int(input(' num for a11'))
    q=int(input('num for a12'))
    c=[p,q]
    print(c)
    s = input('do you want to do further calaculation like add,sub,multiplication,determinantt type yes or no ')
    if s == 'yes':
        op = int(input('1,2,3,4 for add,sub,multiplication,determinant respectively'))
        if op == 1:
            b11=int(input('b11'))
            b12=int(input('b12'))
            add=[p+b11,q+b12]
            print(add)
        elif op == 2:
            b11 = int(input('b11'))
            b12 = int(input('b12'))
            sub=[p-b11,q-b12]
            print(sub)
        elif op == 3:
            print('now here you have to give the order of matrix b whom you will multiply with the first matrix.limit for the row and column is 3')
            rows_B = int(input('row_b = '))
            column_b = int(input('column_B = '))
            if rows_B==2 and column_b==1:
                b11 = int(input('b11'))
                b21 = int(input('b21'))
                print([(p*b11)+(q*b21)])
            elif rows_B==2 and column_b==2:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                print([(p*b11)+(q*b21),(p*b12)+(q*b22)])
            elif rows_B==2 and column_b==3:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b13 = int(input('b13'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                b23 = int(input('b23'))
                print([(p*b11)+(q+b21),(p*b12)+(q*b22),(p*b13)+(q*b23)])
            else:
                print('please give the suitable rows and column for matrix b as per maths')
        elif op == 4:
            print('cant find determinant because it has only 1 row')
        else:
            print('please select valid operations')
    elif s == 'no':
        print('ok,thank you')
    else:
        print('please type valid answer')
elif a==1 and b==3:
    p = int(input('num for a11'))
    q = int(input('a12'))
    r = int(input('a13'))
    c = [p,q,r]
    print(c)
    s = input('do you want to do further calaculation like add,sub,multiplication,determinant type yes or no')
    if s == 'yes':
        op = int(input('1,2,3,4 for add,sub,multiplication,determinant respectively'))
        if op == 1:
            b11 = int(input('b11'))
            b12 = int(input('b12'))
            b13 = int(input('b13'))
            print([p+b11,q+b12,r+b13])
        elif op == 2:
            b11 = int(input('b11'))
            b12 = int(input('b12'))
            b13 = int(input('b13'))
            print([p - b11, q - b12, r - b13])
        elif op == 3:
            print('now here you have to give the order of matrix b whom you will multiply with the first matrix.limit for the row and column is 3')
            rows_B = int(input('row_b = '))
            column_b = int(input('column_B = '))
            if rows_B==3 and column_b==1:
                b11 = int(input('b11'))
                b21 = int(input('b21'))
                b31 = int(input('b31'))
                print([(p*b11)+(q*b21)+(r*b31)])
            elif rows_B==3 and column_b==2:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                b31 = int(input('b31'))
                b32 = int(input('b32'))
                print([(p*b11)+(q*b21)+(r*b31),(p*b12)+(q*b22)+(r*b32)])
            elif rows_B==3 and column_b==3:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b13 = int(input('b13'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                b23 = int(input('b23'))
                b31 = int(input('b31'))
                b32 = int(input('b32'))
                b33 = int(input('b33'))
                print([(p * b11) + (q * b21) + (r * b31), (p * b12) + (q * b22) + (r * b32) , (p*b13)+(q*b23)+(r*b33)])
            else:
                print('please give the suitable rows and column for matrix b as per maths')
        elif op == 4:
            print('cant find determinant because it has only 1 row')
        else:
            print('please select valid operations')
    elif s == 'no':
        print('ok,thank you')
    else:
        print('please type valid answer')
elif a==2 and b==1:
    p=int(input('a11'))
    q=int(input('a21'))
    c=[[p],[q]]
    print(c)
    s = input('do you want to do further calaculation like add,sub,multiplication,determinant type yes or no')
    if s == 'yes':
        op = int(input('1,2,3,4 for add,sub,multiplication,determinant respectively'))
        if op == 1:
            b11 = int(input('b11'))
            b21 = int(input('b21'))
            print([[p+b11],[q+b21]])
        elif op == 2:
            b11 = int(input('b11'))
            b21 = int(input('b21'))
            print([[p - b11], [q - b21]])
        elif op == 3:
            print('now here you have to give the order of matrix b whom you will multiply with the first matrix.limit for the row and column is 3')
            rows_B = int(input('row_b = '))
            column_b = int(input('column_B = '))
            if rows_B==1 and column_b==1:
                b11 = int(input('b11'))
                print([[p * b11], [q * b11]])
            elif rows_B==1 and column_b==2:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                print([[p * b11, p * b12], [q * b11, q * b12]])
            elif rows_B== 1 and column_b==3:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b13 = int(input('b13'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                b23 = int(input('b23'))
                print([[p*b11,p*b12,p*b13],[q*b21,q*b22,q*b23]])
            else:
                print('please give the suitable rows and column for matrix b as per maths')
        elif op == 4:
            print('determinant cant be calculated because it has only one column')
        else:
            print('please select valid operations')
    elif s == 'no':
        print('ok,thank you')
    else:
        print('please type valid answer')
elif a==2 and b==2:
    p=int(input('a11'))
    q=int(input('a12'))
    e=int(input('a21'))
    r=int(input('a22'))
    c=[[p,q],[e,r]]
    print(c)
    s = input('do you want to do further calaculation like add,sub,multiplication,determinant type yes or no')
    if s == 'yes':
        op = int(input('1,2,3,4 for add,sub,multiplication,determinant respectively'))
        if op == 1:
            b11 = int(input('b11'))
            b12 = int(input('b12'))
            b21 = int(input('b21'))
            b22 = int(input('b22'))
            print([[(p+b11),(q+b12)],[(e+b21),(r+b22)]])
        elif op == 2:
            b11 = int(input('b11'))
            b12 = int(input('b12'))
            b21 = int(input('b21'))
            b22 = int(input('b22'))
            print([[(p - b11), (q - b12)], [(e - b21), (r - b22)]])
        elif op == 3:
            print('now here you have to give the order of matrix b whom you will multiply with the first matrix.limit for the row and column is 3')
            rows_B = int(input('row_b = '))
            column_b = int(input('column_B = '))
            if rows_B==2 and column_b==1:
                b11=int(input('b11'))
                b21=int(input('b21'))
                print([[(p*b11)+(q*b21)],[(e*b11)+(r*b21)]])
            elif rows_B==2 and column_b==2 :
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                print([[(p * b11) + (q * b21),(p*b12)+(q*b22)], [(e * b11) + (r * b21),(e*b12)+(r*b22)]])
            elif rows_B==2 and column_b==3 :
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b13 = int(input('b13'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                b23 = int(input('b23'))
                print([[(p * b11) + (q * b21), (p * b12) + (q * b22),(p*b13)+(q*b23)], [(e * b11) + (r * b21), (e * b12) + (r * b22),(e*b13)+(r*b23)]])
            else:
                print('please give the suitable rows and column for matrix b as per maths')
        elif op == 4:
            k=p*r
            K=q*e
            print(k-K,'is determinant of ',c)
        else:
            print('please select valid operations')
    elif s == 'no':
        print('ok,thank you')
    else:
        print('please type valid answer')
elif a==2 and b==3:
    p=int(input('a11'))
    q=int(input('a12'))
    e=int(input('a13'))
    r=int(input('a21'))
    t=int(input('a22'))
    i=int(input('a23'))
    c=[[p,q,e],[r,t,i]]
    print(c)
    s = input('do you want to do further calaculation like add,sub,multiplication,determinant type yes or no')
    if s == 'yes':
        op = int(input('1,2,3,4 for add,sub,multiplication,determinant respectively'))
        if op == 1:
            b11 = int(input('b11'))
            b12 = int(input('b12'))
            b13 = int(input('b13'))
            b21 = int(input('b21'))
            b22 = int(input('b22'))
            b23 = int(input('b23'))
            print([[(p+b11),(q+b12),(e+b13)],[(r+b21),(t+b22),(i+b23)]])
        elif op == 2:
            b11 = int(input('b11'))
            b12 = int(input('b12'))
            b13 = int(input('b13'))
            b21 = int(input('b21'))
            b22 = int(input('b22'))
            b23 = int(input('b23'))
            print([[(p - b11), (q - b12), (e - b13)], [(r - b21), (t - b22), (i - b23)]])
        elif op == 3:
            print('now here you have to give the order of matrix b whom you will multiply with the first matrix.limit for the row and column is 3')
            rows_B = int(input('row_b = '))
            column_b = int(input('column_B = '))
            if rows_B==3 and column_b==1:
                b11 = int(input('b11'))
                b21 = int(input('b21'))
                b31 = int(input('b31'))
                print([[(p * b11) + (q * b21) + (e * b31)],[(r * b11) + (t * b21) + (i * b31)]])
            elif rows_B==3 and column_b==2:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                b31 = int(input('b31'))
                b32 = int(input('b32'))
                print([[(p*b11)+(q*b21)+(e*b31),(p*b12)+(q*b22)+(e*b32)],[(r*b11)+(t*b21)+(i*b31),(r*b12)+(t*b22)+(i*b32)]])
            elif rows_B==3 and column_b==3:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b13 = int(input('b13'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                b23 = int(input('b23'))
                b31 = int(input('b31'))
                b32 = int(input('b32'))
                b33 = int(input('b33'))
                print([[(p*b11)+(q*b21)+(e*b31),(p*b12)+(q*b22)+(e*b32),(p*b13)+(q*b23)+(e*b33)],[(r*b11)+(t*b21)+(i*b31),(r*b12)+(t*b22)+(i*b32),(r*b13)+(t*b23)+(i*b33)]])
            else:
                print('please give the suitable rows and column for matrix b as per maths')
        elif op == 4:
            print('cant find the determinant because it does not have equal rows and columns')
        else:
            print('please select valid operations')
    elif s == 'no':
        print('ok,thank you')
    else:
        print('please type valid answer')
elif a==3 and b==1:
    p=int(input('a11'))
    q=int(input('a21'))
    w=int(input('a31'))
    c=[[p],[q],[w]]
    print(c)
    s = input('do you want to do further calaculation like add,sub,multiplication,determinant type yes or no')
    if s == 'yes':
        op = int(input('1,2,3,4 for add,sub,multiplication,determinant respectively'))
        if op == 1:
            b11 = int(input('b11'))
            b21 = int(input('b21'))
            b31 = int(input('b31'))
            print([[p+b11],[q+b21],[w+b31]])
        elif op == 2:
            b11 = int(input('b11'))
            b21 = int(input('b21'))
            b31 = int(input('b31'))
            print([[p - b11], [q - b21], [w - b31]])
        elif op == 3:
            print('now here you have to give the order of matrix b whom you will multiply with the first matrix.limit for the row and column is 3')
            rows_B = int(input('row_b = '))
            column_b = int(input('column_B = '))
            if rows_B==1 and column_b==1:
                b11 = int(input('b11'))
                print([[p * b11],[q * b11],[w * b11]])
            elif rows_B==1 and column_b==2:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                print([[p * b11, p * b12, ], [q * b11, q * b12], [w * b11, w * b12]])
            elif rows_B==1 and column_b==3:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b13 = int(input('b13'))
                print([[p*b11,p*b12,p*b13],[q*b11,q*b12,q*b13],[w*b11,w*b12,w*b13]])
            else:
                print('please give the suitable rows and column for matrix b as per maths')
        elif op == 4:
            print('cant find the determinant because it does not have equal rows and columns')
        else:
            print('please select valid operations')
    elif s == 'no':
        print('ok,thank you')
    else:
        print('please type valid answer')
elif a==3 and b==2:
    p=int(input('a11'))
    q=int(input('a12'))
    o=int(input('a21'))
    e=int(input('a22'))
    m=int(input('a31'))
    n=int(input('a32'))
    c=[[p,q],[o,e],[m,n]]
    print(c)
    s = input('do you want to do further calaculation like add,sub,multiplication,determinant type yes or no')
    if s == 'yes':
        op = int(input('1,2,3,4 for add,sub,multiplication,determinant respectively'))
        if op == 1:
            b11 = int(input('b11'))
            b12 = int(input('b12'))
            b21 = int(input('b21'))
            b22 = int(input('b22'))
            b31 = int(input('b31'))
            b32 = int(input('b32'))
            print([[p+b11, q+b12], [o+b21, e+b22], [m+b31, n+b32]])
        elif op == 2:
            b11 = int(input('b11'))
            b12 = int(input('b12'))
            b21 = int(input('b21'))
            b22 = int(input('b22'))
            b31 = int(input('b31'))
            b32 = int(input('b32'))
            print([[p - b11, q - b12], [o - b21, e - b22], [m - b31, n - b32]])
        elif op == 3:
            print('now here you have to give the order of matrix b whom you will multiply with the first matrix.limit for the row and column is 3')
            rows_B = int(input('row_b = '))
            column_b = int(input('column_B = '))
            if rows_B==2 and column_b==1:
                b11 = int(input('b11'))
                b21 = int(input('b21'))
                print([[(p * b11) + (q * b21)], [(o * b11) + (e * b21)],[(m * b11) + (n * b21)]])
            elif rows_B==2 and column_b==2:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                print([[(p * b11) + (q * b21), (p * b12) + (q * b22)],[(o * b11) + (e * b21), (o * b12) + (e * b22)],[(m * b11) + (n * b21), (m * b12) + (n * b22)]])
            elif rows_B==2 and column_b==3:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b13 = int(input('b13'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                b23 = int(input('b23'))
                print([[(p*b11)+(q*b21),(p*b12)+(q*b22),(p*b13)+(q*b23)],[(o*b11)+(e*b21),(o*b12)+(e*b22),(o*b13)+(e*b23)],[(m*b11)+(n*b21),(m*b12)+(n*b22),(m*b13)+(n*b23)]])
            else:
                print('please give the suitable rows and column for matrix b as per maths')
        elif op == 4:
            print('cant find the determinant because it does not have equal rows and columns')
        else:
            print('please select valid operations')
    elif s == 'no':
        print('ok,thank you')
    else:
        print('please type valid answer')
elif a==3 and b==3:
    p = int(input('a11'))
    q = int(input('a12'))
    d = int(input('a13'))
    o = int(input('a21'))
    e = int(input('a22'))
    i = int(input('a23'))
    m = int(input('a31'))
    n = int(input('a32'))
    u = int(input('a33'))
    c=[[p,q,d],[o,e,i],[m,n,u]]
    print(c)
    s = input('do you want to do further calculation like add,sub,multiplication,determinant,type yes or no ')
    if s == 'yes':
        op = int(input('1,2,3,4 for add,sub,multiplication,determinant respectively'))
        if op == 1:
            b11 = int(input('b11'))
            b12 = int(input('b12'))
            b13 = int(input('b13'))
            b21 = int(input('b21'))
            b22 = int(input('b22'))
            b23 = int(input('b23'))
            b31 = int(input('b31'))
            b32 = int(input('b32'))
            b33 = int(input('b33'))
            print([[p+b11, q+b12, d+b13], [o+b21, e+b22, i+b23], [m+b31, n+b32, u+b33]])
        elif op == 2:
            b11 = int(input('b11'))
            b12 = int(input('b12'))
            b13 = int(input('b13'))
            b21 = int(input('b21'))
            b22 = int(input('b22'))
            b23 = int(input('b23'))
            b31 = int(input('b31'))
            b32 = int(input('b32'))
            b33 = int(input('b33'))
            print([[p - b11, q - b12, d - b13], [o - b21, e - b22, i - b23], [m - b31, n - b32, u - b33]])
        elif op == 3:
            print('now here you have to give the order of matrix b whom you will multiply with the first matrix.limit for the row and column is 3')
            rows_B = int(input('row_b = '))
            column_b = int(input('column_B = '))
            if rows_B==3 and column_b==1:
                b11 = int(input('b11'))
                b21 = int(input('b21'))
                b31 = int(input('b31'))
                print([[(p * b11) + (q * b21) + (d * b31)],[(o * b11) + (e * b21) + (i * b31)],[(m * b11) + (n * b21) + (u * b31)]])
            elif rows_B==3 and column_b==2:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                b31 = int(input('b31'))
                b32 = int(input('b32'))
                print([[(p * b11) + (q * b21) + (d * b31), (p * b12) + (q * b22) + (d * b32)],[(o * b11) + (e * b21) + (i * b31), (o * b12) + (e * b22) + (i * b32)],[(m * b11) + (n * b21) + (u * b31), (m * b12) + (n * b22) + (u * b32)]])
            elif rows_B==3 and column_b==3:
                b11 = int(input('b11'))
                b12 = int(input('b12'))
                b13 = int(input('b13'))
                b21 = int(input('b21'))
                b22 = int(input('b22'))
                b23 = int(input('b23'))
                b31 = int(input('b31'))
                b32 = int(input('b32'))
                b33 = int(input('b33'))
                print([[(p*b11)+(q*b21)+(d*b31),(p*b12)+(q*b22)+(d*b32),(p*b13)+(q*b23)+(d*b33)],[(o*b11)+(e*b21)+(i*b31),(o*b12)+(e*b22)+(i*b32),(o*b13)+(e*b23)+(i*b33)],[(m*b11)+(n*b21)+(u*b31),(m*b12)+(n*b22)+(u*b32),(m*b13)+(n*b23)+(u*b33)]])
            else:
                print('please give the suitable rows and column for matrix b as per maths')
        elif op == 4:
            z=p*((e*u)-(i*n))
            y=q*((o*u)-(i*m))
            E=d*((o*n)-(e*m))
            print('determinant of ',c,' is ',z-y+E)
        else:
            print('please select valid operations')
    elif s == 'no':
        print('ok,thank you')
    else:
        print('please type valid answer')
else:
    print('please select the valid rows and columns')