class LogicalGate:
    
    def __init__(self,n):
        self.label = n
        self.output = None
        
    def getLabel(self):
        return self.label
        
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
        
class BinaryGate(LogicalGate):
    
        def __init__(self,n):
            LogicalGate.__init__(self,n)
            
            self.pinA = None
            self.pinB = None
        
        def getPinA(self):
            return int(input("Enter pin A input for gate " + self.getLabel() + "-->"))
        
        def getPinB(self):
            return int(input("Enter pin B input for gate " + self.getLabel() + "-->"))
        
        def setNextPin(self,source):
            if self.pinA == None:
                self.PinA = source
            else:
                if self.pinB == None:
                    self.pinB = source
                else:
                    raise RuntimeError("Error: NO EMPTY PINS")
                    
            
class UnaryGate(LogicalGate):
    
    def __init__(self,n):
        LogicalGate.__init__(self,n)
        
        self.pin = None
        
    def getPin(self):
        return int(input("Enter pin input for gate " + self.getLabel() + "-->"))
    
    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")
            
class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):         
    
    def __init__(self,n):
        BinaryGate.__init__(self,n)
        
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 or b == 1:
            return 1
        else:
            return 0
            
class NotGate(UnaryGate):
    
    def __init__(self,n):
        UnaryGate.__init__(self,n)
    
    def performGateLogic(self):
        a = self.getPin()
        
        if a == 0:
            return 1
        else:
            return 0

class Connector:
    
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate =tgate
        
        tgate.setNextPin(self)
    
    def getFrom(self):
        return self.fromgate
        
    def getTo(self):
        return self.togate
        


g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
c3 = Connector(g3,g4)

