import simpleeval
import app.functions.abs as abs
import app.functions.e as e
import app.functions.ePower as ePower
import app.functions.factorial as factorial
import app.functions.mad as mad
import app.functions.PI as PI
import app.functions.power as power
import app.functions.sd as sd
import app.functions.sin as sin
import app.functions.sqrt as sqrt
import app.functions.tenPower as tenPower

class MathTool:
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if MathTool.__instance == None:
          MathTool()
        return MathTool.__instance

    def __init__(self):
        """ Virtually private constructor. """
        other_functions = {"abs": abs.abs, "e": e.E(), "ePower": ePower.ePower, 
                        "factorial": factorial.factorial, "MAD":mad.mad, "π": PI.PI(), 
                        "power":power.power, "σ":sd.sd, "sin": sin.sin, 
                        "sqrt" : sqrt.sqrt, "tenPower": tenPower.tenPower}
        self.se = simpleeval.SimpleEval()
        self.se.functions = simpleeval.DEFAULT_FUNCTIONS.copy()
        self.se.functions.update(other_functions)
        self.precision = 10
        self.angleMode = 'deg'
        if MathTool.__instance != None:
          raise Exception("This class is a MathTool!")
        else:
          MathTool.__instance = self