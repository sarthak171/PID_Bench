class wheelVel:
    V = None # Target velocity
    L = None # Target left wheel velocity
    R = None # Target right wheel velocity
    C = None # Curvature
    T = None # Track width
    
    def calculate(self):
        self.L = self.V * (2 + (self.C * self.T)) / 2
        self.R = self.V * (2 - (self.C * self.T)) / 2
    
    def getLeft(self):
        return self.L
    
    def getRight(self):
        return self.R
    
    def __init__(self, curvature, trackWidth):
        self.C = curvature
        self.T = trackWdith
    
    def __init__(self, curvature, trackWidth, targetVelocity):
        self.C = curvature
        self.T = trackWidth
        self.V = targetVelocity
        self.calculate()