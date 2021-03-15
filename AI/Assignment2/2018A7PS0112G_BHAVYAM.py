#!/usr/bin/env python3
from Agent import * # See the Agent.py file
import re


#### All your code can go here.
##########################################################
KB=[
    "P11 <=> (~P12 & ~P13 & ~P14 & ~P21 & ~P22 & ~P23 & ~P24 & ~P31 & ~P32 & ~P33 & ~P34 & ~P41 & ~P42 & ~P43 & ~P44)",
    "P12 <=> (~P11 & ~P13 & ~P14 & ~P21 & ~P22 & ~P23 & ~P24 & ~P31 & ~P32 & ~P33 & ~P34 & ~P41 & ~P42 & ~P43 & ~P44)",
    "P13 <=> (~P11 & ~P12 & ~P14 & ~P21 & ~P22 & ~P23 & ~P24 & ~P31 & ~P32 & ~P33 & ~P34 & ~P41 & ~P42 & ~P43 & ~P44)",
    "P14 <=> (~P12 & ~P13 & ~P11 & ~P21 & ~P22 & ~P23 & ~P24 & ~P31 & ~P32 & ~P33 & ~P34 & ~P41 & ~P42 & ~P43 & ~P44)",
    "P21 <=> (~P12 & ~P13 & ~P14 & ~P11 & ~P22 & ~P23 & ~P24 & ~P31 & ~P32 & ~P33 & ~P34 & ~P41 & ~P42 & ~P43 & ~P44)",
    "P22 <=> (~P12 & ~P13 & ~P14 & ~P21 & ~P11 & ~P23 & ~P24 & ~P31 & ~P32 & ~P33 & ~P34 & ~P41 & ~P42 & ~P43 & ~P44)",
    "P23 <=> (~P12 & ~P13 & ~P14 & ~P21 & ~P22 & ~P11 & ~P24 & ~P31 & ~P32 & ~P33 & ~P34 & ~P41 & ~P42 & ~P43 & ~P44)",
    "P24 <=> (~P12 & ~P13 & ~P14 & ~P21 & ~P22 & ~P23 & ~P11 & ~P31 & ~P32 & ~P33 & ~P34 & ~P41 & ~P42 & ~P43 & ~P44)",
    "P31 <=> (~P12 & ~P13 & ~P14 & ~P21 & ~P22 & ~P23 & ~P24 & ~P11 & ~P32 & ~P33 & ~P34 & ~P41 & ~P42 & ~P43 & ~P44)",
    "P32 <=> (~P12 & ~P13 & ~P14 & ~P21 & ~P22 & ~P23 & ~P24 & ~P31 & ~P11 & ~P33 & ~P34 & ~P41 & ~P42 & ~P43 & ~P44)",
    "P33 <=> (~P12 & ~P13 & ~P14 & ~P21 & ~P22 & ~P23 & ~P24 & ~P31 & ~P32 & ~P11 & ~P34 & ~P41 & ~P42 & ~P43 & ~P44)",
    "P34 <=> (~P12 & ~P13 & ~P14 & ~P21 & ~P22 & ~P23 & ~P24 & ~P31 & ~P32 & ~P33 & ~P11 & ~P41 & ~P42 & ~P43 & ~P44)",
    "P41 <=> (~P12 & ~P13 & ~P14 & ~P21 & ~P22 & ~P23 & ~P24 & ~P31 & ~P32 & ~P33 & ~P34 & ~P11 & ~P42 & ~P43 & ~P44)",
    "P42 <=> (~P12 & ~P13 & ~P14 & ~P21 & ~P22 & ~P23 & ~P24 & ~P31 & ~P32 & ~P33 & ~P34 & ~P41 & ~P11 & ~P43 & ~P44)",
    "P43 <=> (~P12 & ~P13 & ~P14 & ~P21 & ~P22 & ~P23 & ~P24 & ~P31 & ~P32 & ~P33 & ~P34 & ~P41 & ~P42 & ~P11 & ~P44)",
    "P44 <=> (~P12 & ~P13 & ~P14 & ~P21 & ~P22 & ~P23 & ~P24 & ~P31 & ~P32 & ~P33 & ~P34 & ~P41 & ~P42 & ~P43 & ~P11)",
    "W11 <=> (~W12 & ~W13 & ~W14 & ~W21 & ~W22 & ~W23 & ~W24 & ~W31 & ~W32 & ~W33 & ~W34 & ~W41 & ~W42 & ~W43 & ~W44)",
    "W12 <=> (~W11 & ~W13 & ~W14 & ~W21 & ~W22 & ~W23 & ~W24 & ~W31 & ~W32 & ~W33 & ~W34 & ~W41 & ~W42 & ~W43 & ~W44)",
    "W13 <=> (~W11 & ~W12 & ~W14 & ~W21 & ~W22 & ~W23 & ~W24 & ~W31 & ~W32 & ~W33 & ~W34 & ~W41 & ~W42 & ~W43 & ~W44)",
    "W14 <=> (~W12 & ~W13 & ~W11 & ~W21 & ~W22 & ~W23 & ~W24 & ~W31 & ~W32 & ~W33 & ~W34 & ~W41 & ~W42 & ~W43 & ~W44)",
    "W21 <=> (~W12 & ~W13 & ~W14 & ~W11 & ~W22 & ~W23 & ~W24 & ~W31 & ~W32 & ~W33 & ~W34 & ~W41 & ~W42 & ~W43 & ~W44)",
    "W22 <=> (~W12 & ~W13 & ~W14 & ~W21 & ~W11 & ~W23 & ~W24 & ~W31 & ~W32 & ~W33 & ~W34 & ~W41 & ~W42 & ~W43 & ~W44)",
    "W23 <=> (~W12 & ~W13 & ~W14 & ~W21 & ~W22 & ~W11 & ~W24 & ~W31 & ~W32 & ~W33 & ~W34 & ~W41 & ~W42 & ~W43 & ~W44)",
    "W24 <=> (~W12 & ~W13 & ~W14 & ~W21 & ~W22 & ~W23 & ~W11 & ~W31 & ~W32 & ~W33 & ~W34 & ~W41 & ~W42 & ~W43 & ~W44)",
    "W31 <=> (~W12 & ~W13 & ~W14 & ~W21 & ~W22 & ~W23 & ~W24 & ~W11 & ~W32 & ~W33 & ~W34 & ~W41 & ~W42 & ~W43 & ~W44)",
    "W32 <=> (~W12 & ~W13 & ~W14 & ~W21 & ~W22 & ~W23 & ~W24 & ~W31 & ~W11 & ~W33 & ~W34 & ~W41 & ~W42 & ~W43 & ~W44)",
    "W33 <=> (~W12 & ~W13 & ~W14 & ~W21 & ~W22 & ~W23 & ~W24 & ~W31 & ~W32 & ~W11 & ~W34 & ~W41 & ~W42 & ~W43 & ~W44)",
    "W34 <=> (~W12 & ~W13 & ~W14 & ~W21 & ~W22 & ~W23 & ~W24 & ~W31 & ~W32 & ~W33 & ~W11 & ~W41 & ~W42 & ~W43 & ~W44)",
    "W41 <=> (~W12 & ~W13 & ~W14 & ~W21 & ~W22 & ~W23 & ~W24 & ~W31 & ~W32 & ~W33 & ~W34 & ~W11 & ~W42 & ~W43 & ~W44)",
    "W42 <=> (~W12 & ~W13 & ~W14 & ~W21 & ~W22 & ~W23 & ~W24 & ~W31 & ~W32 & ~W33 & ~W34 & ~W41 & ~W11 & ~W43 & ~W44)",
    "W43 <=> (~W12 & ~W13 & ~W14 & ~W21 & ~W22 & ~W23 & ~W24 & ~W31 & ~W32 & ~W33 & ~W34 & ~W41 & ~W42 & ~W11 & ~W44)",
    "W44 <=> (~W12 & ~W13 & ~W14 & ~W21 & ~W22 & ~W23 & ~W24 & ~W31 & ~W32 & ~W33 & ~W34 & ~W41 & ~W42 & ~W43 & ~W11)",
    "W11 | W12 | W13 | W14 | W21 | W22 | W23 | W24 | W31 | W32 | W33 | W34 | W41 | W42 | W43 | W44",
    "P11 | P12 | P13 | P14 | P21 | P22 | P23 | P24 | P31 | P32 | P33 | P34 | P41 | P42 | P43 | P44",
    "B11 <=> (P12 | P21)",
    "B12 <=> (P11 | P22 | P13)",
    "B13 <=> (P12 | P14 | P23)",
    "B14 <=> (P13 | P24)",
    "B21 <=> (P11 | P31 | P22)",
    "B22 <=> (P21 | P23 | P12 | P32)",
    "B23 <=> (P22 | P24 | P33 | P13)",
    "B24 <=> (P23 | P14 | P34)",
    "B31 <=> (P21 | P41 | P32)",
    "B32 <=> (P31 | P33 | P22 | P42)",
    "B33 <=> (P32 | P34 | P43 | P23)",
    "B34 <=> (P33 | P24 | P44)",
    "B41 <=> (P42 | P31)",
    "B42 <=> (P41 | P32 | P43)",
    "B43 <=> (P42 | P44 | P33)",
    "B44 <=> (P43 | P34)",
    "S11 <=> (W12 | W21)",
    "S12 <=> (W11 | W22 | W13)",
    "S13 <=> (W12 | W14 | W23)",
    "S14 <=> (W13 | W24)",
    "S21 <=> (W11 | W31 | W22)",
    "S22 <=> (W21 | W23 | W12 | W32)",
    "S23 <=> (W22 | W24 | W33 | W13)",
    "S24 <=> (W23 | W14 | W34)",
    "S31 <=> (W21 | W41 | W32)",
    "S32 <=> (W31 | W33 | W22 | W42)",
    "S33 <=> (W32 | W34 | W43 | W23)",
    "S34 <=> (W33 | W24 | W44)",
    "S41 <=> (W42 | W31)",
    "S42 <=> (W41 | W32 | W43)",
    "S43 <=> (W42 | W44 | W33)",
    "S44 <=> (W43 | W34)",
    "~P11",
    "~W11",
    "~B11",
    "~S11",
    "~W44",
    "~P44"
]
dpllcount=0
maxdpll=0
##########################################################
class Expression:
    def __init__(self,op,*arguments):
        self.operator = op
        self.arguments = list(map(expressionize,arguments))
    def __eq__(self, other):
        iseq = (other is self)
        iseq = iseq or (isinstance(other, Expression) and self.operator == other.operator and self.arguments == other.arguments)
        return iseq
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        hashval = hash(self.operator) ^ hash(tuple(self.arguments))
        return hashval
    def __lshift__(self, other):
        exprval =  Expression('<<', self, other)
        return exprval
    def __or__(self, other):     
        exprval = Expression('|',  self, other)
        return exprval
    def __mod__(self, other):    
        exprval = Expression('<=>',  self, other)
        return exprval
    def __and__(self, other):    
        exprval = Expression('&',  self, other)
        return exprval
    def __invert__(self):        
        exprval = Expression('~',  self)
        return exprval
##########################################################
def expressionize(s):
    if isinstance(s, Expression): return s
    s = re.sub("<=>",'%',s)
    s = re.sub("=>",'>>',s)
    s = re.sub("(\w+)", r'Expression("\1")', s)
    s = eval(s, {'Expression':Expression})
    return s
##########################################################
def cnfconvert(s):
    if isinstance(s, str):
        s = expressionize(s)
    s = impliestocnf(s)
    s = moveinwards(s)
    return distributing(s)
##########################################################
def impliestocnf(s):
    if not s.arguments or (isinstance(s.operator,str) and s.operator[:1].isalpha()):
        return s
    arguments = list(map(impliestocnf, s.arguments))
    a, b = arguments[0], arguments[-1]
    opimp = ['>>','<=>']
    opnorm = ['&','|','~']
    if s.operator == opimp[0]:
        val = (b | ~a)
        return val
    elif s.operator == opimp[1]:
        val= (a | ~b ) & ( b | ~a)
        return val
    else:
        assert s.operator in opnorm
        return Expression(s.operator, *arguments)
##########################################################
def moveinwards(s):
    oplist = ['~','|','&']
    if s.operator == oplist[0]:
        NOT = lambda b: moveinwards(~b)
        a = s.arguments[0]
        if a.operator == oplist[0]: return moveinwards(a.arguments[0]) # ~~A ==> A
        if a.operator ==oplist[2]:
            optemp = oplist[1]
            operator=optemp
            result = []
            def collect(subargs):
                for arg in subargs:
                    if arg.operator == operator: collect(arg.arguments)
                    else: result.append(arg)
            collect(map(NOT,a.arguments))
            argtemp = result
            # argtemp = dissociate(optemp, map(NOT, a.arguments))
            if len(argtemp) == 0:
                return _op_identity[optemp]
            elif len(argtemp) == 1:
                return argtemp[0]
            else:
                return Expression(optemp,*argtemp)
        if a.operator ==oplist[1]:
            optemp = oplist[2]
            operator=optemp
            result = []
            def collect(subargs):
                for arg in subargs:
                    if arg.operator == operator: collect(arg.arguments)
                    else: result.append(arg)
            collect(map(NOT,a.arguments))
            argtemp = result
            # argtemp = dissociate(optemp, map(NOT, a.arguments))
            if len(argtemp) == 0:
                return _op_identity[optemp]
            elif len(argtemp) == 1:
                return argtemp[0]
            else:
                return Expression(optemp,*argtemp)
        return s
    elif (isinstance(s.operator,str) and s.operator[:1].isalpha()):
        return s
    elif not s.arguments:
        return s
    else:
        return Expression(s.operator, *map(moveinwards, s.arguments))
##########################################################
def distributing(s):
    oplist=['|','&']
    if s.operator == oplist[0]:
        optemp = oplist[0]
        operator=optemp
        result = []
        def collect(subargs):
            for arg in subargs:
                if arg.operator == operator: collect(arg.arguments)
                else: result.append(arg)
        collect(s.arguments)
        argtemp = result
        # argtemp = dissociate(optemp, s.arguments)
        if len(argtemp) == 0:
            s = _op_identity[optemp]
        elif len(argtemp) == 1:
            s = argtemp[0]
        else:
            s =  Expression(optemp,*argtemp)
        if s.operator != oplist[0]:
            return distributing(s)
        counter=0
        for vall in s.arguments:
            counter=counter+1
        if counter == 0:
            return False
        if counter == 1:
            retval = distributing(s.arguments[0])
            return retval
        conj=None
        for arg in s.arguments:
            if arg.operator==oplist[1]:
                conj=arg
                break
        if not conj:
            return s
        others = [a for a in s.arguments if a is not conj]
        optemp = oplist[0]
        operator=optemp
        result = []
        def collect(subargs):
            for arg in subargs:
                if arg.operator == operator: collect(arg.arguments)
                else: result.append(arg)
        collect(others)
        argtemp = result
        # argtemp = dissociate(optemp, others)
        if len(argtemp) == 0:
            rest= _op_identity[optemp]
        elif len(argtemp) == 1:
            rest= argtemp[0]
        else:
            rest= Expression(optemp,*argtemp)
        optemp = oplist[1]
        operator=optemp
        result = []
        def collect(subargs):
            for arg in subargs:
                if arg.operator == operator: collect(arg.arguments)
                else: result.append(arg)
        collect([distributing(c|rest) for c in conj.arguments])
        argtemp = result
        if len(argtemp) == 0:
            return _op_identity[optemp]
        elif len(argtemp) == 1:
            return argtemp[0]
        else:
            return Expression(optemp,*argtemp)
    elif s.operator == oplist[1]:
        optemp = oplist[1]
        operator=optemp
        result = []
        def collect(subargs):
            for arg in subargs:
                if arg.operator == operator: collect(arg.arguments)
                else: result.append(arg)
        collect(map(distributing, s.arguments))
        argtemp = result
        if len(argtemp) == 0:
            return _op_identity[optemp]
        elif len(argtemp) == 1:
            return argtemp[0]
        else:
            return Expression(optemp,*argtemp)
    else:
        return s

_op_identity = {'&':True, '|':False, '+':0, '*':1}
##########################################################
def propositionsymbols(x):
    if not isinstance(x, Expression):
        return []
    elif (isinstance(x.operator,str) and x.operator[:1].isalpha()):
        if x.operator[0].isupper() and x.operator != True and x.operator != False:
            return [x]
    else:
        return list(set(symbol for arg in x.arguments for symbol in propositionsymbols(arg)))
##########################################################
def propositionassign(exp, model={}):
    operator, arguments = exp.operator, exp.arguments
    oplist = ['~','|','&','>>','<=>']
    if exp == True:
        return True
    elif exp == False:
        return False
    elif (isinstance(operator, str) and operator[:1].isalpha()):
        if operator[0].isupper() and operator != True and operator != False:
            rettemp = model.get(exp)
            return rettemp
    elif operator == oplist[0]:
        p = propositionassign(arguments[0], model)
        if p is None: return None
        else: return not p
    elif operator == oplist[1]:
        result = False
        for arg in arguments:
            p = propositionassign(arg, model)
            if p is True: 
                return True
            if p is None: 
                result = None
        return result
    elif operator == oplist[2]:
        result = True
        for arg in arguments:
            p = propositionassign(arg, model)
            if p is False: 
                return False
            if p is None: 
                result = None
        return result
    p, q = arguments
    if operator == oplist[3]:
        rettemp = propositionassign(~p | q, model)
        return rettemp
    pt = propositionassign(p, model)
    if pt is None: 
        return None
    qt = propositionassign(q, model)
    if qt is None: 
        return None
    if operator == oplist[4]:
        return pt == qt
##########################################################
KBclauses=[]
def KBtocnf():
    global KBclauses    
    def collect(subargs):
        for arg in subargs:
            if arg.operator == operator: collect(arg.arguments)
            else: result.append(arg)
    for kbi in KB:
        operator='&'
        result = []
        collect([cnfconvert(expressionize(kbi))])
        KBclauses.extend(result)
def dpll_satisfiable(s):
    global KBclauses
    operator='&'
    result = []
    def collect(subargs):
        for arg in subargs:
            if arg.operator == operator: collect(arg.arguments)
            else: result.append(arg)
    collect([cnfconvert(s)])
    clauses = result
    symbols = propositionsymbols(s)
    for kbi in KB:
        symbols.extend(propositionsymbols(expressionize(kbi)))
    symbols=list(set(x for x in symbols))
    clausetemp=KBclauses.copy()
    clausetemp.extend(clauses)
    global dpllcount
    dpllcount=0
    return dpll(clausetemp, symbols, {})
def dpll(clauses, symbols, model):
    global dpllcount,maxdpll
    dpllcount = dpllcount+1
    maxdpll = max(maxdpll,dpllcount+1)
    unknown_clauses = [] ## clauses with an unknown truth value
    for c in clauses:
        val =  propositionassign(c, model)
        if val == False:
            return val
        if val != True:
            unknown_clauses.append(c)
    if not unknown_clauses:
        return model
    # puresymbolflag=0
    # symbols=sorted(symbols,reverse=True, key=symbols.count)
    # for s in symbols:
    #     found_pos, found_neg = False, False
    #     for c in unknown_clauses:
    #         operator='|'
    #         result = []
    #         def collect(subargs):
    #             for arg in subargs:
    #                 if arg.operator == operator: collect(arg.arguments)
    #                 else: result.append(arg)
    #         collect([c])
    #         if not found_pos and s in result: found_pos = True
    #         if not found_neg and ~s in result: found_neg = True
    #     if found_pos != found_neg: 
    #         P, value = s, found_pos
    #         puresymbolflag=1
    #         break
    # if puresymbolflag==0:
    #     P, value =None, None
    # # P, value = find_pure_symbol(symbols, unknown_clauses)
    # if P:
        # return dpll(clauses, [x for x in symbols if x != P], modelassign(model, P, value))
    unitclauseflag=0
    for clause in clauses:
        unitclauseassignflag=0
        Punitassign, valueunitassign = None, None
        operator='|'
        result = []
        def collect(subargs):
            for arg in subargs:
                if arg.operator == operator: collect(arg.arguments)
                else: result.append(arg)
        collect([clause])
        for literal in result:
            if literal.operator == '~':
                symbol, positive = literal.arguments[0], False
            else:
                symbol, positive = literal, True
            if symbol in model:
                if model[symbol] == positive:
                    Punit, valueunit = None, None  # clause already True
                    unitclauseassignflag=1
                    break
            elif Punitassign:
                Punit, valueunit = None, None      # more than 1 unbound variable
                unitclauseassignflag=1
                break
            else:
                Punitassign, valueunitassign = symbol, positive
        if unitclauseassignflag==0:
            Punit,valueunit = Punitassign, valueunitassign
        if Punit: 
            P, value = Punit, valueunit
            unitclauseflag=1
            break
    if unitclauseflag==0:
        P, value = None, None
    if P:
        return dpll(clauses, [x for x in symbols if x != P], modelassign(model, P, value))
    P, symbols = symbols[0], symbols[1:]
    return (dpll(clauses, symbols, modelassign(model, P, True)) or dpll(clauses, symbols, modelassign(model, P, False)))
##########################################################
def modelassign(s, var, val):
    s2 = s.copy()
    s2[var] = val
    return s2
##########################################################
def check_safety(row,column):
    _check_expr = expressionize("P%d%d | W%d%d"%(row,column,row,column))
    return not dpll_satisfiable(_check_expr)
##########################################################
def sortfunc(val):
    return (8-val[0]-val[1])
##########################################################
#### You can change the main function as you wish. Run this program to see the output. Also see Agent.py code.
def main():
    path=[]
    rooms=[]
    global KBclauses
    KBtocnf()
    ag = Agent()
    visited={}
    validMoves = [[0,1],[0,-1],[-1,0],[1,0]]
    while(ag.PerceiveCurrentLocation()!=[None,None]):
        rooms.append(ag.FindCurrentLocation())
        print('curLoc',ag.FindCurrentLocation())
        if tuple(ag.FindCurrentLocation()) in visited.keys():
            visited[tuple(ag.FindCurrentLocation())]+=1
        else:
            visited[tuple(ag.FindCurrentLocation())]=1
        x=ag.FindCurrentLocation()[0]
        y=ag.FindCurrentLocation()[1]
        # print('Percept [breeze, stench] :',ag.PerceiveCurrentLocation())
        if ag.PerceiveCurrentLocation()[0]==True:
            str1=("B%d%d"%(x,y))
            if str1 not in KB:
                KB.append("B%d%d"%(x,y))
                KBclauses.extend([cnfconvert(str1)])
        else:
            str2=("~B%d%d"%(x,y))
            if str2 not in KB:
                KB.append("~B%d%d"%(x,y))
                KBclauses.extend([cnfconvert(str2)])
        if ag.PerceiveCurrentLocation()[1]==True:
            str3=("S%d%d"%(x,y))
            if str3 not in KB:
                KB.append("S%d%d"%(x,y))
                KBclauses.extend([cnfconvert(str3)])
        else:
            str4=("~S%d%d"%(x,y))
            if str4 not in KB:
                KB.append("~S%d%d"%(x,y))
                KBclauses.extend([cnfconvert(str4)])
        newLoc = []
        for ind,inc in enumerate(validMoves):
            zx = x + inc[0] #increment location index
            zy = y + inc[1]
            if zx>4 or zx<1 or zy>4 or zy<1 or not check_safety(zx,zy):
                continue                
            newLoc.append([zx,zy])
        flagg=0
        newLoc.sort(key=sortfunc)
        for i,valu in enumerate(newLoc):
            if tuple(valu) not in visited.keys():
                v=[newLoc[i][0]-x,newLoc[i][1]-y]
                index = validMoves.index(v)
                if index==0:
                    ag.TakeAction('Up')
                    path.append('Up')
                    flagg=1
                    break
                elif index==1:
                    ag.TakeAction('Down')
                    path.append('Down')
                    flagg=1
                    break
                elif index==2:
                    ag.TakeAction('Left')
                    path.append('Left')
                    flagg=1
                    break
                elif index==3:
                    ag.TakeAction('Right')
                    path.append('Right')
                    flagg=1
                    break
        if flagg==0:
            minn=200
            minpos=None
            for pos,lel in enumerate(newLoc):
                if len(newLoc)>1:
                    if (visited[tuple(lel)] + (8-lel[0]-lel[1])<minn) and lel != rooms[len(rooms)-2]:
                        minn=visited[tuple(lel)] + (8-lel[0]-lel[1])
                        minpos=pos
                else:
                    if (visited[tuple(lel)] + (8-lel[0]-lel[1])<minn):
                        minn=visited[tuple(lel)] + (8-lel[0]-lel[1])
                        minpos=pos
            v=[newLoc[minpos][0]-x,newLoc[minpos][1]-y]
            index=validMoves.index(v)
            if index==0:
                ag.TakeAction('Up')
                path.append('Up')
            elif index==1:
                ag.TakeAction('Down')
                path.append('Down')
            elif index==2:
                ag.TakeAction('Left')
                path.append('Left')
            elif index==3:
                ag.TakeAction('Right')
                path.append('Right')
    rooms.append(ag.FindCurrentLocation())
    print(rooms)
    print(path)
    print(maxdpll)
if __name__=='__main__':
    main()
