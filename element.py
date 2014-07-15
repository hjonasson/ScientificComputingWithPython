import numpy as np
import pylab as plt

class element:
    def __init__(self,x0,x1,LtoG):
        self.x0 = x0
        self.x1 = x1
        self.LtoG = LtoG
        self.dx = x1-x0

    def basis(self,x):
        if x < self.x0 or x > self.x1:
            return [0.0, 0.0]
        return [ (self.x1-x)/self.dx, (x-self.x0)/self.dx ]

    def dbasis(self,x):
        if x < self.x0 or x > self.x1:
            return [0.0, 0.0]
        return [ -1.0/self.dx, 1.0/self.dx ]

    def interp(self,x,d):
        N = self.basis(x)
        dN = self.dbasis(x)
        u = 0.
        du = 0.
        for a in range(2):
            u += N[a]*d[self.LtoG[a]]
            du += dN[a]*d[self.LtoG[a]]
        return u,du

    def plot(self,d,res=100):
        xs = np.linspace(self.x0,self.x1,res)
        u = []
        du = []
        for x in xs:
            sol,der = self.interp(x,d)
            u.append(sol)
            du.append(der)
        plt.subplot(211)
        plt.plot(xs,u,'-b')
        plt.subplot(212)
        plt.plot(xs,du,'-g')
