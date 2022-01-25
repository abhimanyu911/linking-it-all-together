def postfix_evaluation(s):

    s=s.split()

    n=len(s)

    stack =[]

    for i in range(n):

        if s[i].isdigit():
            stack.append(int(s[i]))

        elif s[i]=="+":
            a=stack.pop()

            b=stack.pop()

            stack.append(int(a)+int(b))

        elif s[i]=="*":
            a=stack.pop()

            b=stack.pop()

            stack.append(int(a)*int(b))

        elif s[i]=="/":
            a=stack.pop()

            b=stack.pop()

            stack.append(int(b)/int(a))

        elif s[i]=="-":
            a=stack.pop()

            b=stack.pop()

            stack.append(int(b)-int(a))            

    return stack.pop()

#space separtor is a must, for solving 2 or more digits .

s="10 2 8 * + 3 -"

res = postfix_evaluation(s)

print(res)