from stack import Stack

class honoiTower:
    
    def __init__(self):
        self.poles = [None] * 3
        self.poles[0] = [8,7,6,5,4,3,2,1]
        self.poles[1] = []
        self.poles[2] = []
   
    def printStatus(self):
        print self.poles[0]
        print self.poles[1]
        print self.poles[2]
    
    def moveTower(self,height, fromPole, toPole, withPole):
        if height >= 1:
            self.moveTower(height-1,fromPole,withPole,toPole)
            self.moveDisk(fromPole,toPole)
            self.moveTower(height-1,withPole,toPole,fromPole)

    def moveDisk(self,fp,tp):
        if len(self.poles[fp])==0:
            return;
        
        value = self.poles[fp].pop()
    
        if len(self.poles[tp])==0 or value < self.poles[tp][-1]:
            self.poles[tp].append(value)
            print "moving ",str(value)," from",fp,"to",tp," "
        else:
            self.poles[fp].append(value)
        


       
       
_honoi = honoiTower()
_honoi.moveTower(8,0,1,2)
_honoi.printStatus()