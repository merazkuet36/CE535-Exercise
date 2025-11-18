import os


def test_numerical_analysis_module():
    try:
        import NumericalAnalysis
        assert True
    except ImportError:
        assert False


def test_numerical_integration_module():
    try:
        from NumericalAnalysis import NumericalIntegration
        assert True
    except ImportError:
        assert False


def test_ode_module():

    try:
        from NumericalAnalysis import ODE
        assert True
    except ImportError:
        assert False


def test_nonlinear_system_module():

    try:
        from NumericalAnalysis import NonlinearSystem
        assert True
    except ImportError:
        assert False


def test_linear_system_module():
    try:
        from NumericalAnalysis import LinearSystem
        assert True
    except ImportError:
        assert False


def test_midpoint_rule_class():
    try:
        from NumericalAnalysis.NumericalIntegration.MidpointRule import MidpointRule
        rule = MidpointRule(a=0.0, b=1.0, n=10)
        print(rule)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_trapezoid_rule_class():
    try:
        from NumericalAnalysis.NumericalIntegration.TrapezoidRule import TrapezoidRule
        rule = TrapezoidRule(a=0.0, b=1.0, n=10)
        print(rule)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_simpson_rule_class():
    try:
        from NumericalAnalysis.NumericalIntegration.SimpsonRule import SimpsonRule
        rule = SimpsonRule(a=0.0, b=1.0, n=10)
        print(rule)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_gauss_rule_class():
    try:
        from NumericalAnalysis.NumericalIntegration.Gauss import Gauss
        rule = Gauss(a=0.0, b=1.0, n=10)
        print(rule)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_euler_method_class():
    try:
        from NumericalAnalysis.ODE.Euler import Euler
        method = Euler()
        print(method)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_runge_kutta_method_class():
    try:
        from NumericalAnalysis.ODE.RungeKutta import RungeKutta
        method = RungeKutta()
        print(method)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_multi_step_method_class():
    try:
        from NumericalAnalysis.ODE.MultiStep import MultiStep
        method = MultiStep()
        print(method)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_newton_method_class():
    try:
        from NumericalAnalysis.NonlinearSystem.Newton import Newton
        method = Newton()
        print(method)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_modified_newton_method_class():
    try:
        from NumericalAnalysis.NonlinearSystem.ModifiedNewton import ModifiedNewton
        method = ModifiedNewton()
        print(method)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_secant_newton_method_class():
    try:
        from NumericalAnalysis.NonlinearSystem.SecantNewton import SecantNewton
        method = SecantNewton()
        print(method)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_krylov_newton_method_class():
    try:
        from NumericalAnalysis.NonlinearSystem.KrylovNewton import KrylovNewton
        method = KrylovNewton()
        print(method)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_jacobi_method_class():
    try:
        from NumericalAnalysis.LinearSystem.Jacobi import Jacobi
        method = Jacobi()
        print(method)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_sor_method_class():
    try:
        from NumericalAnalysis.LinearSystem.SOR import SOR
        method = SOR()
        print(method)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_cg_method_class():
    try:
        from NumericalAnalysis.LinearSystem.CG import CG
        method = CG()
        print(method)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_gmres_method_class():
    try:
        from NumericalAnalysis.LinearSystem.GMRES import GMRES
        method = GMRES()
        print(method)
        assert True
    except Exception as e:
        print(e)
        assert False

