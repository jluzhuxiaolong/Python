class Person:
	def __init__(self,name):
		self.name=name
	def SayHello(self):
	    print ('My name is:',self.name);

				  
p = Person('p');
p1 = Person('p1');
print (p);
p.SayHello();
p1.SayHello();