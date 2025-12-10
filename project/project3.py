import numpy as np
import matplotlib.pyplot as plt

class Ball:
    '''Simulate the motion the ball'''
    
    # Start
    def __init__(self, vx0=0.0, vy0=0.0, vz0=0.0, g=-9.81):
        
        
        if g >= 0:
            raise RuntimeError('g should be negative')
        
        # check vz0 
        if not isinstance(vz0, (int, float)):
            raise RuntimeError('vz0 should be a number')

        # vz0 non negative 
        if float(vz0) < 0:
            raise RuntimeError('vz0 should not be negative')

         # initializing vx0, vy0, vz0, g
        self.vx0 = float(vx0)
        self.vy0 = float(vy0)
        self.vz0 = float(vz0)
        self.g = float(g)
        self.motion = []

    # function of the ball 
    def __str__(self):
        return f"Ball(vx0={self.vx0:.2f}, vy0={self.vy0:.2f}, vz0={self.vz0:.2f}, g={self.g})"
        
    # theoritical flying duration 
    def duration(self):
        return -2 * (self.vz0 / self.g)
        
    # going down
    def fall(self):
        x = -2 * ((self.vz0 * self.vx0) / self.g)
        y = -2 * ((self.vz0 * self.vy0) / self.g)
        z = 0.0
        return x, y, z
    
    # modelling
    def fly(self, dt):
        
        t = 0.0
        self.motion = []
        
        # initial velocity 
        dv = np.random.normal(0.0, 0.1, 3)
        eff_vx0 = self.vx0 + dv[0]
        eff_vy0 = self.vy0 + dv[1]
        eff_vz0 = self.vz0 + dv[2]

        while True:
            
            
            dw = np.random.normal(0.0, 0.2, 3)
            dwx, dwy, dwz = dw[0], dw[1], abs(dw[2])
            
            x = eff_vx0 * t + dwx * dt
            y = eff_vy0 * t + dwy * dt
            z = eff_vz0 * t + 0.5 * self.g * t**2 + dwz * dt
            
            if z < 0 and t > 0:
                break
            
            self.motion.append((t, x, y, z))
            t += dt


class ASBL:

    def __init__(self, numBalls):
        # init function from project2
        if numBalls <= 0:
            raise ValueError("Number of balls must be positive")
        self.balls = [Ball() for i in range(numBalls)]

    def launch(self, vx0, vy0, vz0, dt):

        # launch function from project2
        for ball in self.balls:
            ball.vx0 = float(vx0)
            ball.vy0 = float(vy0)
            ball.vz0 = float(vz0)
            ball.fly(dt)

        # stats function
        self._stats()

        
        self._show()


    def _show(self):
        # plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        
        for ball in self.balls:
           
            motion = np.array(ball.motion)

          
            x = motion[:, 1]

           
            y = motion[:, 2]

            
            z = motion[:, 3]

            
            ax.plot(x, y, z)

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        plt.title("Projectile Motion of Balls")
        plt.show()


    def _stats(self):
        # initialize xf, yf, and tf 
        xf = []
        yf = []
        tf = []

        
        for ball in self.balls:
            # append t, x, y to xf, yf, tf
            tf.append(ball.motion[-1][0])
            xf.append(ball.motion[-1][1])
            yf.append(ball.motion[-1][2])

        # print 
        print(f"theoretical location: ({self.balls[0].fall()[0]}, {self.balls[0].fall()[1]})")
        print(f"theoretical duration: {self.balls[0].duration()}")

        print(f"average location: ({np.average(xf)}, {np.average(yf)})")
        print(f"average duration: {np.average(tf)}")

        print(f"median location: ({np.median(xf)}, {np.median(yf)})")
        print(f"median duration: {np.median(tf)}")

        print(f"std location: ({np.std(xf)}, {np.std(yf)})")
        print(f"std duration: {np.std(tf)}")




#test

device = ASBL(200)
 
print(f"The device launched {len(device.balls)} balls")
 
device.launch(vx0=1, vy0=1, vz0=10, dt=0.001)