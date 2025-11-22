class Ball:
    '''Ball class to simulate the motion of a ball'''
    
    # initialize a ball object
    def __init__(self, vx0=0, vy0=0, vz0=0, g = -9.81):   # TODO
        # check if g is valid
        if g >= 0:
            # if g is invalid
            # raise an exception
            raise RuntimeError("g must be negative")      
            # TODO

        # check if vx0, vy0, vz0 are valid
        if not isinstance(vx0, (int,float)) or \
           not isinstance(vy0, (int,float)) or \
           not isinstance(vz0, (int,float)) or vz0 <= 0:  
            # TODO
            # raise an exception
            raise RuntimeError("Invalid initial velocity")  
            # TODO

                 
        # initialize vx0
        self.vx0 = vx0     
        # TODO
                 
        # initialize vy0
        self.vy0 = vy0     
        # TODO
                 
        # initialize vz0
        self.vz0 = vz0     
        # TODO
                 
        # initialize g
        self.g = g         
        # TODO

        # initialize motion
        self.motion = []   
        # TODO
        
    # calculate the duration the ball will fly
    def duration(self):
        # return the duration
        return -2 * self.vz0 / self.g    
        # TODO
        
    # calculate the theoretical falling point
    def fall(self):
        # calculate x
        x = self.vx0 * self.duration()   
        # TODO
        
        # calculate y
        y = self.vy0 * self.duration()   
        # TODO
        
        return x, y, 0.0     # TODO  (falling z = 0)
    
    # simulate the entire motion
    # dt is the simulation interval, the smaller the more accurate results
    def fly(self, dt):
                 
        # initialize simulation time with 0.0
        t = 0.0     
        # TODO
                 
        # reset list of motion
        self.motion = []     
        # TODO
        
        # loop from time 0 until hitting the ground
        while True:
            
            # calculate x at time t
            x = self.vx0 * t     
            # TODO
                 
            # calculate y at time t
            y = self.vy0 * t     
            # TODO
                 
            # calculate z at time t
            z = self.vz0 * t + 0.5 * self.g * (t**2)     
            # TODO
                 
            # append (t, x, y, z) to motion
            self.motion.append((t, x, y, z))     
            # TODO

            # update t to the next time moment
            t += dt     
            # TODO

            # check if hitting the ground
            if z < 0:     
                # TODO
                # if hit the ground, break out of the loop
                break     
