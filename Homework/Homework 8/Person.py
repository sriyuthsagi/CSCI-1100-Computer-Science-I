class person(object):
    def __init__(self, name, radius, home, x, y, dx, dy, current, rewards, points = 0):
        self.name = name
        self.radius = radius
        self.home = home
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.current = current
        self.rewards = rewards
        self.points = points
    
    def __str__(self):
        self.sumreward()
        return '{} of {} in universe {}\n    at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points'.format(self.name, self.home, self.current, self.x, self.y, self.dx, self.dy, len(self.rewards), self.points) 
    
    def addreward(self, reward):
        self.rewards.append(reward)
    
    def rewardprint(self, reward, step):
        return '{} picked up \"{}\" at simulation step {}'.format(self.name, reward[3], step)
    
    def sumreward(self):
        self.points = 0
        for i in self.rewards:
            self.points += i[2]
            
    def newlocation(self):
        self.x += self.dx
        self.y += self.dy
    
    def fullstop(self):
        self.dx == 0
        self.dy == 0
    
    def speedcheck(self):
        if abs(self.dx) < 10 or abs(self.dy) < 10:
            self.fullstop()
    
    def locationsheck(self):
        if self.x <= 0 or self.x >= 1000 or self.y <=0 or self.y >= 1000:
            self.fullstop()
            return True
        else:
            return False
    
    def stopprint(self, step):
        return '{} stopped at simulation step {} at location ({:.1f},{:.1f})'.format(self.name, step, self.x, self.y)
    
    def rewardcheck(self, reward):
        if reward[4] == True and abs(reward[0]-self.x) <= self.radius and abs(reward[1]-self.y) <= self.radius:
            return True
        else:
            return False
    
    def rewardslow(self):
        print('bdx = ', self.dx)
        print('bdy = ', self.dy)
        n = len(self.rewards)
        self.dx = self.dx - (n%2) * (n/6) * self.dx
        self.dy = self.dy - ((n+1)%2) * (n/6) * self.dy
        print('adx = ', self.dx)
        print('ady = ', self.dy)        
    
    def collisioncheck(self, other):
        radius = self.radius + other.radius
        if abs(self.x - other.x) <= radius or abs(self.y - other.y) <= radius:
            return True
        else:
            return False
    
    def rewarddrop(self, universe):
        for i in universe:
            for j in i.rewards:
                if self.rewards[0][3] == reward[3]:
                    reward[4] == True
        del self.rewards[0]
        return reward, i.name
    
    def reverse(self):
        print('collision bdx= ', self.dx)
        print('collision bdy= ', self.dy)
        n = len(self.rewards)
        print(n)
        self.dx = -(self.dx - (n%2) * (n/6) * self.dx)
        self.dy = -(self.dy - ((n+1)%2) * (n/6) * self.dy)
        print('collision adx= ', self.dx)
        print('collision ady= ', self.dy)        
    
    def collisionprint(self, other, step):
        return '{} dropped \"{}\", reward returned to {} at ({:.1f},{:.1f})'.format(self.name, reward[3], home, reward[0], reward[1])
    
    def moving(self):
        if self.dx > 0 and self.dy > 0:
            return True
        else:
            return False
    
    def portalcheck(self, portal):
        if portal[4] == True and abs(portal[0]-self.x) <= self.radius and abs(portal[1]-self.y) <= self.radius:
            return True
        else:
            return False    