#미분
import sympy as sym
from sympy.abc import x
sym.diff(sym.poly(x**2 + x*2 +3), x)

#경사하강법
"""
Input : gradient, init, lr, eps
Output : var
- gradient : 미분을 계산하는 함수
- init : 시작점
- lr: 학습률
- eps : 알고리즘 종료 조건

var = init
grad = gradient(var)
#미분이 정확히 0이 되는 것은 불가능하므로 eps보다 작을 때 종료하는 조건 필요
while(abs(grad) > eps): 
    var = var - lr * grad
    grad = gradient(var)
"""

def func(val):
    fun = sym.poly(x**2 + 2*x + 3)
    return fun.subs(x, val), fun

def func_gradient(fun, val):
    _, function = fun(val)
    diff = sym.diff(function, x)
    return diff.subs(x, val), diff

import numpy as np

def gradient_descent(fun, init_point, lr_rate = 1e-2, epsilon=1e-5):
    cnt = 0
    val = init_point
    diff, _ = func_gradient(fun, init_point)
    while np.abs(diff) > epsilon:
        val = val - lr_rate*diff
        diff, _ = func_gradient(fun, val)
        cnt += 1

    print("함수: {}, 연산횟수: {}, 최소점: ({}, {})".format(fun(val)[1], cnt, val, fun(val)[0]))
    
gradient_descent(fun = func, init_point=np.random.uniform(-2, 2))

#함수: Poly(x**2 + 2*x + 3, x, domain='ZZ'), 연산횟수: 608, 최소점: (-0.999995076557286, 2.00000000002424)  


"""
벡터가 입력인 다변수 함수의 경우 편미분(partial differentiation)
"""

from sympy.abc import x, y
sym.diff(sym.poly(x**2 + 2*x*y + 3) + sym.cos(x+2*y), x)