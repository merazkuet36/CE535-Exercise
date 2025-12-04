import numpy as np

# motion of a ball
class Ball:
    def __init__(self, vx0=0, vy0=0, vz0=1, g=-9.81):
        
        if g >= 0:
            raise RuntimeError("g must be negative")

        
        if not isinstance(vx0, (int, float)) or \
           not isinstance(vy0, (int, float)) or \
           not isinstance(vz0, (int, float)) or vz0 <= 0:
            raise RuntimeError("Invalid initial velocity")

        # velocities and gravity
        self.vx0 = vx0
        self.vy0 = vy0
        self.vz0 = vz0
        self.g = g

        # motion list
        self.motion = []

    def duration(self):
        """the time ball will be in the air"""
        return -2 * self.vz0 / self.g

    def fall(self):
        """theoretical falling point"""
        x = self.vx0 * self.duration()
        y = self.vy0 * self.duration()
        return x, y, 0.0

    def fly(self, dt):
        """considering wind and velocity variations"""
        t = 0.0  # initialize time
        self.motion = []  # reset the motion list

        # random velocity variations
        dvx, dvy, dvz = np.random.normal(0.0, 0.1, 3)
        # random wind speeds 
        wind = np.random.normal(0.0, 0.2, 3)

        while True:
            # variations to the velocities
            vx = self.vx0 + dvx + wind[0]  # wind effect to vx
            vy = self.vy0 + dvy + wind[1]  # wind effect to vy
            vz = self.vz0 + dvz + wind[2]  # wind effect to vz

            # position at time t
            x = vx * t
            y = vy * t
            z = vz * t + 0.5 * self.g * t**2

            self.motion.append((t, x, y, z))  # motion data
            t += dt  # increment time

            if z < 0:  
                break


# ASBL class to simulate launching multiple balls with initial velocities
class ASBL:
    def __init__(self, numBalls, vx0=1, vy0=1, vz0=10):
        if numBalls <= 0:
            raise RuntimeError("numBalls must be greater than 0")
        # multiple Ball objects with the specified initial velocities
        self.balls = [Ball(vx0, vy0, vz0) for _ in range(numBalls)]

    def launch(self, vx0, vy0, vz0, dt):
        """Launch all balls with the same initial velocities"""
        for ball in self.balls:
            ball.vx0 = vx0
            ball.vy0 = vy0
            ball.vz0 = vz0
            ball.fly(dt)


# print & stuff
if __name__ == "__main__":
    # Creating an ASBL object with 10 balls 
    device = ASBL(10, vx0=1, vy0=1, vz0=10)  
    print(f"The device has {len(device.balls)} balls")

    # Launching the balls 
    device.launch(vx0=1, vy0=1, vz0=10, dt=0.001)

    # Print 
    index = 1
    for ball in device.balls:
        print(f"Ball {index}: theoretical falling point = {ball.fall()}")
        print(f"    actual falling point = {ball.motion[-1][1:4]}")  # Last position (x, y, z)
        index += 1
