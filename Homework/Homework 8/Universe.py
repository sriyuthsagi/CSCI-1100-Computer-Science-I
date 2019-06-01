
class universe(object):
    def __init__(self, name, rewards = [], portals = []):
        self.name = name
        self.rewards = rewards
        self.portals = portals
        for i in self.rewards:
            i.append(True)
    
    def __str__(self):
        return 'Universe: {} ({} rewards and {} portals)'.format(self.name, len(self.rewards), len(self.portals))
    
    def prewards(self):
        newrewards = ['Rewards:']
        if len(self.rewards) >= 1:
            i = 0
            while i < len(self.rewards):
                newrewards.append('at ({},{}) for {} points: {}'
                                       .format(self.rewards[i][0], self.rewards[i][1],
                                               self.rewards[i][2], self.rewards[i][3]))
                i += 1
            return newrewards
        else:
            newrewards.append(None)
            return newrewards
    
    def pportals(self):
        newportals = ['Portals:']
        if len(self.portals) >= 1:
            i = 0
            while i < len(self.portals):
                newportals.append('{}({},{}) -> ({},{})'
                                       .format(self.name, self.portals[i][0], self.portals[i][1],
                                               self.portals[i][2], self.portals[i][3], self.portals[i][4]))
                i += 1
            return newportals
        else:
            newportals.append(None)
            return newportals        
        









