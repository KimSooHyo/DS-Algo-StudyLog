import numpy as np

"""
노름의 종류에 따라 기하학적 성질이 달라짐
-> 목적에 따라 각각 다른 노름을 사용
"""

def l1_norm(x):
    #각 성분의 변화량의 절대값을 모두 더한 것
    x_norm = np.abs(x)
    x_norm = np.sum(x_norm)
    return x_norm

def l2_norm(x):
    #원점에서부터의 거리 (유클리드 거리)
    #l2_norm은 np.linalg.norm을 이용해도 구현 가능
    x_norm = x*x
    x_norm = np.sum(x_norm)
    x_norm = np.sqrt(x_norm)
    return x_norm

def angle(x, y): #두 벡터 사이의 각도
    v = np.inner(x, y) / (l2_norm(x) * l2_norm(y))
    theta = np.arccos(v)
    return theta