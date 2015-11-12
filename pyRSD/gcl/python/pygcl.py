import gcl
from gcl import ClassCosmology
from gcl import ClassParams
from gcl import Cosmology
from gcl import Engine

from gcl import Constants

from gcl import CubicSpline
from gcl import LinearSpline
from gcl import Spline

from gcl import xi_to_pk, pk_to_xi
from gcl import ComputeXiLM, compute_xilm_fftlog as ComputeXiLM_fftlog
from gcl import IntegrationMethods

class PickalableSWIG:
 
    def __setstate__(self, state):
        self.__init__(*state['args'])
 
    def __getstate__(self):
        return {'args': self.args}
    
            
#-------------------------------------------------------------------------------
# Cosmology
class Cosmology(gcl.Cosmology, PickalableSWIG):
    
    def __init__(self, *args):
        self.args = args
        self.args += ('__init__',)
        gcl.Cosmology.__init__(self, *args)    
        
    def __getstate__(self):
        args = self.args
        return {'args': args} 
    
    def __setstate__(self, state):
        args = state['args']
        
        # this is either __init__ or from_power
        if args[-1] == '__init__':
            cls = self.__init__
        elif args[-1] == 'from_power':
            cls = Cosmology.from_power
        else:
            raise ValueError("do not recognize constructor `%s` in __setstate__" %args[-1])
        toret = cls(*args[:-1])
        
        # if initialized with from_power, copy the dict
        if toret is not None:
            self.__dict__ = toret.__dict__

    @classmethod
    def from_power(cls, param_file, pkfile):
        # class the underlying c++ method
        toret = cls.FromPower(param_file, pkfile)
        
        # do what __init__ and promote the class
        toret.__class__ = Cosmology
        toret.args = (param_file, pkfile)
        toret.args += ('from_power',)
        return toret
        
    @classmethod
    def from_file(cls, param_file, tkfile):
        return cls(param_file, tkfile)
            
    def __getitem__(self, key):
        if hasattr(self, key):
            f = getattr(self, key)
            if callable(f):
                return f()
        raise KeyError("Sorry, cannot return parameter '%s' in dict-like fashion" %key)
            
#-------------------------------------------------------------------------------
# CorrelationFunction
class CorrelationFunction(gcl.CorrelationFunction, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = args
        gcl.CorrelationFunction.__init__(self, *args)    
        
    def __getstate__(self):
        args = self.args
        if len(args) < 3: args = (args[0], self.GetKmin(), self.GetKmax())
        return {'args': args}    

#-------------------------------------------------------------------------------
# Kaiser
class Kaiser(gcl.Kaiser, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = args
        gcl.Kaiser.__init__(self, *args)

    def __getstate__(self):
        args = self.args
        if len(args) == 2: args += (self.GetLinearBias(),)
        return {'args': args}
        
#-------------------------------------------------------------------------------
# NonlinearPS
class NonlinearPS(gcl.NonlinearPS, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = args
        gcl.NonlinearPS.__init__(self, *args)
        
#-------------------------------------------------------------------------------
# LinearPS
class LinearPS(gcl.LinearPS, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = args
        gcl.LinearPS.__init__(self, *args)

#-------------------------------------------------------------------------------

# Imn
class Imn(gcl.Imn, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = args
        gcl.Imn.__init__(self, *args)

#-------------------------------------------------------------------------------

# Jmn
class Jmn(gcl.Jmn, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = args
        gcl.Jmn.__init__(self, *args)

#-------------------------------------------------------------------------------

# Kmn
class Kmn(gcl.Kmn, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = args
        gcl.Kmn.__init__(self, *args)

#-------------------------------------------------------------------------------

# ImnOneLoop
class ImnOneLoop(gcl.ImnOneLoop, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = args
        gcl.ImnOneLoop.__init__(self, *args)

#-------------------------------------------------------------------------------

# OneLoopPdd
class OneLoopPdd(gcl.OneLoopPdd, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = (args[0],)
        gcl.OneLoopPdd.__init__(self, *args)
        
    def __getstate__(self):
        args = self.args
        args += (self.GetEpsrel(), self.GetOneLoopPower())
        return {'args': args}

#-------------------------------------------------------------------------------

# OneLoopPdv
class OneLoopPdv(gcl.OneLoopPdv, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = (args[0],)
        gcl.OneLoopPdv.__init__(self, *args)
        
    def __getstate__(self):
        args = self.args
        args += (self.GetEpsrel(), self.GetOneLoopPower())
        return {'args': args}
#-------------------------------------------------------------------------------

# OneLoopPvv
class OneLoopPvv(gcl.OneLoopPvv, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = (args[0],)
        gcl.OneLoopPvv.__init__(self, *args)
        
    def __getstate__(self):
        args = self.args
        args += (self.GetEpsrel(), self.GetOneLoopPower())
        return {'args': args}
#-------------------------------------------------------------------------------

# OneLoopP22Bar
class OneLoopP22Bar(gcl.OneLoopP22Bar, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = (args[0],)
        gcl.OneLoopP22Bar.__init__(self, *args)
    
    def __getstate__(self):
        args = self.args
        args += (self.GetEpsrel(), self.GetOneLoopPower())
        return {'args': args}
#-------------------------------------------------------------------------------

# ZeldovichPS
class ZeldovichPS(gcl.ZeldovichPS, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = (args[0],)
        gcl.ZeldovichPS.__init__(self, *args)
        
    def __getstate__(self):
        args = self.args
        args += (self.GetSigma8AtZ(), self.GetSigmaSq(), self.GetXZel(), self.GetYZel())
        return {'args': args}

#-------------------------------------------------------------------------------

# ZeldovichP00
class ZeldovichP00(gcl.ZeldovichP00, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = args
        gcl.ZeldovichP00.__init__(self, *args)
        
#-------------------------------------------------------------------------------

# ZeldovichP01
class ZeldovichP01(gcl.ZeldovichP01, PickalableSWIG):
 
    def __init__(self, *args):
        self.args = args
        gcl.ZeldovichP01.__init__(self, *args)

#-------------------------------------------------------------------------------
        
