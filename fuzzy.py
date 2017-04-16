import math as m
from collections import defaultdict

class input_range(object):
    def __init__(self,l,r,m=None):
        self.left=l
        self.mid=m
        self.right=r
    
    def get_mean(self):
        if self.mid==None:
            return (self.left+self.right)*0.5
        else:
            return self.mid

class rules(object):
    def __init__(self,prop1,prop2,operator,result):
        self.prop1=prop1
        self.prop2=prop2
        self.operator=operator
        self.result=result

def take_prop():
    return int(input("Enter no.of properties: "))

def take_properties(p):
    properties={}
    for i in range(p):
        name=input("Enter name: ")
        a=[int(i) for i in input("Enter range: ").split(' ')]
        properties[name]=input_range(*a)
    return properties

class fuzzyset(object):
    def __init__(self):
        self.num_properties=take_prop()
        self.properties=take_properties(self.num_properties)
    
    def fuzzify(self,member):
        fuzz={}
        for vec in self.properties:
            mean=self.properties[vec].get_mean()
            if self.properties[vec].mid==None:
                if self.properties[vec].left<=member<=self.properties[vec].right:
                    if member>=mean:
                        fuzz[vec]=abs((member-self.properties[vec].right)/(self.properties[vec].right-mean))
                    else:
                        fuzz[vec]=abs((member-self.properties[vec].left)/(self.properties[vec].left-mean))
            else:
                if self.properties[vec].mid<=member<=self.properties[vec].right:
                    fuzz[vec]=abs((member-self.properties[vec].right)/(self.properties[vec].right-self.properties[vec].mid))
                if self.properties[vec].left<=member<=self.properties[vec].mid:
                    fuzz[vec]=abs((member-self.properties[vec].left)/(self.properties[vec].left-self.properties[vec].mid))
                if member<=self.properties[vec].mid and self.properties[vec].mid!=self.properties[vec].right:
                    fuzz[vec]=1.0
                if self.properties[vec].mid==self.properties[vec].right and member>=self.properties[vec].mid:
                    fuzz[vec]=1.0
        return fuzz
        
    def defuzzify(self,fuzz,rules):
        output={};fin=0;den=0
        for name in self.properties:
            if self.properties[name].mid==None:
                raise ValueError("Constant number for {0} is not given".format(name))
        for r in rules:
            if rules[r].operator=='or':
                ouput[rules[r].result]=max(fuzz[rules[r].prop1],fuzz[rules[r].prop2])
            else:
                output[rules[r].result]=min(fuzz[rules[r].prop1],fuzz[rules[r].prop2])
        for vec in output:
            fin+=self.properties[vec].mid*output[vec]
            den+=output[vec]
        print(output)
        return fin/den

def main():
    input_dict={};output={}
    inp=int(input("Enter no.of inputs: "))
    for i in range(inp):
        name=input("Enter name for the input: ")
        input_dict[name]=fuzzyset()
    name=input("Enter output name: ")
    output[name]=fuzzyset()
    rule={}
    rule[1]=rules('sunny','warm','and','fast')
    rule[2]=rules('partcloud','cool','and','slow')
    final={}
    for vec in input_dict:
        input_param=int(input("Enter {0} input parameters: ".format(vec)))
        final.update(input_dict[vec].fuzzify(input_param))
    print(final)
    print(output["speed"].defuzzify(final,rule))        

if __name__=="__main__":
    main()

    
    
            
        