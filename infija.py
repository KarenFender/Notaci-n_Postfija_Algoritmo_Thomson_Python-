#Código para expresiones regulare de Infija a Postfija

lpos = []
pila = ['n']


expresion = raw_input("ingresa tu expresion regular: ")
print "\n"


for i in expresion:
    if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
        lpos.append(i) 
    else:
        if pila == [] or pila[len(pila)-1] == "(" or i == "(":
            pila.append(i) 
        elif i == "+" or i == "*":
            if pila[len(pila)-1] == "+" or pila[len(pila)-1] == "*":
                lpos.append(i)
            else:
                pila.append(i)
        elif i == "-":
            #print "len(pila)"
            #print len(pila)

            while pila[len(pila)-1] == "+" or pila[len(pila)-1] == "*":
                lpos.append(pila.pop())
                #print len(pila)
            if pila[len(pila)-1] == "-":
                lpos.append(i)
            else:
                pila.append(i)
        elif i == "|":
            while pila[len(pila)-1] == "+" or pila[len(pila)-1] == "*" or pila[len(pila)-1] == "-":
                lpos.append(pila.pop())
            if pila[len(pila)-1] == "|":
                lpos.append(i)
            else:
                pila.append(i)
        else:
            while pila[len(pila)-1] != "(":
                lpos.append(pila.pop())
            pila.pop()

while len(pila) > 1:
    lpos.append(pila.pop())

print "\n"
print "Notacion posfija \n"
print lpos
