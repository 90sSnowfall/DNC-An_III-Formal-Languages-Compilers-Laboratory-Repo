
'''Problema 1 definire metode'''
class Problema1:
    @staticmethod
    def concatenate(first_string, second_string):
        return first_string + second_string

    @staticmethod
    def reverse(the_string):
        return the_string[::-1]

    @staticmethod
    def substitute(the_string, a, b):
        return [char if char != a else b for char in the_string]

    @staticmethod
    def length(the_string):
        return len(the_string)
    
    @staticmethod
    def createString(The_Alphabet):
        # the_string = ''.join(The_Alphabet[0]+The_Alphabet[1]+The_Alphabet[2])
        the_string = []
        the_string.append(The_Alphabet[0])
        the_string.append(The_Alphabet[1])
        the_string.append(The_Alphabet[2])
        return the_string;

'''Problema 2 definire metode'''
class Problema2:

    '''Se concateaza s1 la finalul lui s2, conform cerintei :/'''
    @staticmethod
    def concat(first_string, second_string):
        return second_string + first_string
    
    @staticmethod
    def repeat(the_string, numberRepetitions):
        temp = []
        for _ in range(numberRepetitions):
            temp.extend(the_string)
        return temp
    
    '''reverse(s) este definita in problema 1'''
    @staticmethod
    def extract(the_string,i,j):
        if i < 0 or j >= len(the_string) or i > j:
            return "Index out of bounds."
        return the_string[i:j+1]
    
    @staticmethod
    def replace(the_string, sub, new_sub):

        sub = Problema2.convertArrayToString(sub)
        new_sub = Problema2.convertArrayToString(new_sub)
        the_string = Problema2.convertArrayToString(the_string)
        
        index = the_string.find(sub)

        if index != -1:
            # Creează noul șir înlocuind sub-șirul cu new_sub
            new_string = the_string[:index] + new_sub + the_string[index + len(sub):]
            return new_string

        return the_string
    
    @staticmethod
    def convertArrayToString(givenArray):
        the_string = ''.join(str(x) for x in givenArray)
        return the_string
    

'''Problema 1 rezolvare'''
A = ['a','b','c']
B = ['x', 'y', 'z']
C = ['1', '2', '3']


s1 = Problema1.createString(A);
s2 = Problema1.createString(B);

print("Concatenated string:", Problema2.convertArrayToString(Problema1.concatenate(s1, s2)))
print("Reversed string:", Problema2.convertArrayToString(Problema1.reverse(s2)))
print("Substituted string:", Problema2.convertArrayToString(Problema1.substitute(s1, 'a', 'b')))
print("Length of string:", Problema1.length(s1))

'''Problema 2 rezolvare'''
sigma1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sigma2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k']
sigma3 = ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5']

A = Problema1.createString(sigma1);
B = Problema1.createString(sigma2);
C = Problema1.createString(sigma3);


print("A concat B = ", Problema2.convertArrayToString(Problema2.concat(A,B)))
print("A repeat 5 = ", Problema2.convertArrayToString(Problema2.repeat(A,5)))
print("B reversed = ", Problema2.convertArrayToString(Problema1.reverse(B)))
print("extraction of index 0 and 1 from C = ", Problema2.convertArrayToString(Problema2.extract(C,0,1)))
print("replace from A 01 with 45 =",Problema2.replace(A,"01","45"))

#exemplu care dovedeste ca se inlocuieste doar primul substring
#stringTest = "123423"
#print("replace from A 01 with 45 =",Problema2.replace(stringTest,"23","45"))