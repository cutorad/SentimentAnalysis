import Tkinter
import numpy as np
import matplotlib.pyplot as plt
from Tkconstants import *
from matplotlib import pyplot
from numpy import arange
import bisect
from pylab import *
import math
poslines= open('C:/Users/sarthak/Desktop/Minor_Project/rt-polarity.pos.txt', 'r')
a=poslines.read().splitlines()
neglines= open('C:/Users/sarthak/Desktop/Minor_Project/rt-polarity.neg.txt', 'r')
b=neglines.read().splitlines()
N= 4800
poslinesTrain= a[:N]
neglinesTrain= b[:N]
poslinesTest= a[N:]
neglinesTest= b[N:]
trainset= [(x,1) for x in poslinesTrain] + [(x,-1) for x in neglinesTrain]
testset= [(x,1) for x in poslinesTest] + [(x,-1) for x in neglinesTest]
poswords={} 
negwords={} 
for line,label in trainset:
    for word in line.split():       
      
        if label==1: poswords[word]= poswords.get(word, 0) + 1 
        else: negwords[word]= negwords.get(word, 0) + 1
            
            
#evaluate the test set
wrong=0 
for line,label in testset:
    
    totpos, totneg= 0.0, 0.0
    for word in line.split():
        
        
		
        a= poswords.get(word,0.0) + 1.0
        b= negwords.get(word,0.0) + 1.0
        
        totpos+= a/(a+b)
        totneg+= b/(a+b)
        
    prediction=1
    if totneg>totpos: prediction=-1
    
    
class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.text=Tkinter.Text(self,height=25,width=70,background='white')
        self.text.grid()
        
        self.text.bind("<Return>", self.OnPressEnter)
        

        button = Tkinter.Button(self,text=u"Click me !", command=self.OnButtonClick)
        button.grid(column=1,row=0)
        
        button = Tkinter.Button(self,text=u"Click for bar graph !", command=self.OnButtonClick1)
        button.grid(column=0,row=2)
        button = Tkinter.Button(self,text=u"Click for pie chart !", command=self.OnButtonClick2)
        button.grid(column=0,row=3)
        

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Enter your text above:")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

    def OnButtonClick(self):
         
        totpos1,totneg1=0.0,0.0
        c= self.text.get('0.0',END)

        
        
        for word in c.split(): 
            a= poswords.get(word,0.0) + 1.0
            b= negwords.get(word,0.0) + 1.0
        
        
            totpos1+= a/(a+b)
            totneg1+= b/(a+b)
           
            if totneg1>totpos1: totneg1 =totneg1 +0.5
            else :
             totpos1= totpos1 + 0.5
           
        self.labelVariable.set( c + "  " +" Posscore ="+ str(totpos1)+ "  " + "Negscore=" +str(totneg1))    
        

       
    def OnButtonClick1(self):
        
        totpos1,totneg1=0.0,0.0
        c= self.text.get('0.0',END)

        for word in c.split(): 
            a= poswords.get(word,0.0) + 1.0
            b= negwords.get(word,0.0) + 1.0
        
        
            totpos1+= a/(a+b)
            totneg1+= b/(a+b)
           
            if totneg1>totpos1: totneg1 =totneg1 +0.5
            else :
             totpos1= totpos1 + 0.5        
        N=1
        positive   = totpos1
        negative = totneg1
        ind = np.arange(N)   
        width = 0.35       

        p1 = plt.bar(ind, positive,   width, color='g')
        p2 = plt.bar(ind, negative, width, color='r',
             bottom=positive)

        

        plt.ylabel('Scores')
        plt.title('Scores by positive and negative')
        plt.xticks(ind+width/2., ('Graphical Analysis of Sentiment') )
        s= int(totpos1+totneg1)
        plt.yticks(np.arange(0,s+1,1))
        plt.legend( (p1[0], p2[0]), ('Positive Score', 'Negative Score') )

        plt.show()
       
    def OnButtonClick2(self):
        totpos1,totneg1=0.0,0.0
        c= self.text.get('0.0',END)

        for word in c.split(): 
            a= poswords.get(word,0.0) + 1.0
            b= negwords.get(word,0.0) + 1.0
        
        
            totpos1+= a/(a+b)
            totneg1+= b/(a+b)
           
            if totneg1>totpos1: totneg1 =totneg1 +0.5
            else :
             totpos1= totpos1 + 0.5
        def little_pie(breakdown,location,size):
            breakdown = [0] + list(np.cumsum(breakdown)* 1.0 / sum(breakdown))
            for i in xrange(len(breakdown)-1):
                x = [0] + np.cos(np.linspace(2 * math.pi * breakdown[i], 2 * math.pi *    
                          breakdown[i+1], 20)).tolist()
                y = [0] + np.sin(np.linspace(2 * math.pi * breakdown[i], 2 * math.pi * 
                          breakdown[i+1], 20)).tolist()
                xy = zip(x,y)
               

        
        ab1= (100*totpos1/(totpos1+totneg1) )   
        ab2= (100*totneg1/(totpos1+totneg1) )    
        fracs = [ab1,ab2]
        labels = ["Positive Score", "Negative Score"]
        pie(fracs,labels=labels, autopct='%1.1f%%')
        show()

   
        
    def OnPressEnter(self,event):
        self.labelVariable.set( self.text.get()+" (You pressed ENTER)" )

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Sentilysis')
    app.mainloop()

