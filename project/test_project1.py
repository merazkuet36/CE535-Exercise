import numpy as np
import pytest
from project1 import Ball

# generate 10 random initial velocities
data = [
    [-0.5850141849120472, 6.266454282347757, 6.907479321898604, 1.4082526650150058,
        (-0.8238477849739718, 8.824750943310924), (1.4089999999999556, -0.8242849865410484, 8.829434083827712)],
    [-7.973994559685562, -8.928943115558091, 6.361905812040836, 1.2970246303854913,
        (-10.342467346472086, -11.581059144189812), (1.2979999999999678, -10.350244938471603, -11.589768163994115)],
    [2.8745721146067726, 7.208207858286892, 4.8880397211733335, 0.9965422469262657,
        (2.8646325540418203, 7.183283655408785), (0.9970000000000008, 2.8659483982629546, 7.186583234712037)],
    [0.3243952114155424, -9.149490750724716, 8.55844301105835, 1.7448405731005807,
        (0.566017926597379, -15.964402685072978), (1.7449999999999186, 0.5660696439200951, -15.965861360013886)],
    [-9.131496642657101, 0.5198000940798231, 5.646002706172572, 1.1510708881085774,
        (-10.510999950223802, 0.598326755931384), (1.151999999999984, -10.519484132340834, 0.5988097083799478)],
    [-4.449186968522014, 8.149741645519049, 1.8394246441718876, 0.37501012113596077,
        (-1.6684901440219784, 3.056235601712882), (0.3760000000000003, -1.6728943001642784, 3.0643028587151644)],
    [0.0366105334019462, 2.9921590759398087, 2.8257351839777134, 0.5760927999954564,
        (0.021091064696854366, 1.7237613000899816), (0.5770000000000004, 0.021124277772922972, 1.7264757868172709)],
    [-2.897355283069658, -0.8774458860757073, 7.533516885510122, 1.5358851958226547,
        (-4.450005086305246, -1.3476561465591705), (1.5359999999999416, -4.450337714794825, -1.3477568810122351)],
    [8.45953293069573, 2.408322100892075, 6.846206335013639, 1.3957607206959508,
        (11.807483780099, 3.3614413912091092), (1.395999999999957, 11.809507971250875, 3.3620176528452337)],
    [8.284814140989855, -3.619675370898243, 1.2667168589520317, 0.2582501241492419,
        (2.139554280464025, -0.9347816139144247), (0.2590000000000002, 2.145766862516374, -0.9374959210626457)]
]

def test_positive_g():
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=0, vz0=0, g=0)
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=0, vz0=0, g=1)
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=0, vz0=0, g=2)

def test_invalid_vx0():
    with pytest.raises(RuntimeError):
        Ball(vx0='a', vy0=0, vz0=0, g=-9.81)
    with pytest.raises(RuntimeError):
        Ball(vx0=None, vy0=0, vz0=0, g=-9.81)
    with pytest.raises(RuntimeError):
        Ball(vx0=[1, 2, 3], vy0=0, vz0=0, g=-9.81)
    with pytest.raises(RuntimeError):
        Ball(vx0=np.array([1, 2, 3]), vy0=0, vz0=0, g=-9.81)
        
def test_invalid_vy0():
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0='a', vz0=0, g=-9.81)
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=None, vz0=0, g=-9.81)
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=[1, 2, 3], vz0=0, g=-9.81)
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=np.array([1, 2, 3]), vz0=0, g=-9.81)
        
def test_invalid_vz0():
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=0, vz0='a', g=-9.81)
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=0, vz0=None, g=-9.81)
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=0, vz0=[1, 2, 3], g=-9.81)
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=0, vz0=np.array([1, 2, 3]), g=-9.81)
        
def test_negative_vz0():
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=0, vz0=-1, g=-9.81)
        
def test_duration():
    for line in data:
        vx0, vy0, vz0, duration, fall, motion = line
        ball = Ball(vx0, vy0, vz0, -9.81)
        assert abs(ball.duration() - duration) < 0.1
        
def test_fall():
    for line in data:
        vx0, vy0, vz0, duration, fall, motion = line
        ball = Ball(vx0, vy0, vz0, -9.81)
        fall_x, fall_y, fall_z = ball.fall()
        assert abs(fall_x - fall[0]) < 0.1
        assert abs(fall_y - fall[1]) < 0.1

def test_fly_invalid_dt():
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=0, vz0=0, g=-9.81).fly(0)
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=0, vz0=0, g=-9.81).fly(-1)
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=0, vz0=0, g=-9.81).fly(np.array([1, 2, 3]))
    with pytest.raises(RuntimeError):
        Ball(vx0=0, vy0=0, vz0=0, g=-9.81).fly(np.array([-1, 2, 3]))
        
def test_fly():
    for line in data:
        vx0, vy0, vz0, duration, fall, motion = line
        ball = Ball(vx0, vy0, vz0, -9.81)
        ball.fly(0.001)
        assert abs(ball.motion[-1][0] - motion[0]) < 0.1
        assert abs(ball.motion[-1][1] - motion[1]) < 0.1
        assert abs(ball.motion[-1][2] - motion[2]) < 0.1