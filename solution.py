import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 906914964 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    px = x_success / x_cnt
    py = y_success / y_cnt

    p = (x_success + y_success) / (x_cnt + y_cnt)
    z_obs = (px - py) / np.sqrt(p * (1 - p) * (1/x_cnt + 1/y_cnt))
    z = norm.ppf(0.9)
    res = True
    if z_obs <= z:
      res = False
    return res # Ваш ответ, True или False
