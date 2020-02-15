import random

def rand_(a, b):
    x = random.randint(a, b)
    if x > 10: x = 10
    return x

class ENV():
    def __init__():
        pass
    def get_reward(s,a):
        M = s[0]
        H = s[2]
        s_ = s      #后继状态
        r  = 0      #状态s下采取行为a后的反馈信号
        if a == 0:
            #停止要牌，一分高下
            h_hidden_card = rand_(1, 13)
            H = H + h_hidden_card
            if h_hidden_card == 1 and H + 9 < 22:
                H = H+9           #host的另一张卡是不是ace
            if M > H:
                r = 1
            if M == H:
                r = 0
            if M < H:
                r = -1
            s_=0
        else:
            #要牌
            new_card = rand_(1, 13)
            M = M + new_card
            if M > 21:
                r = -1
                s_ = 0
            else:
                s_[0] = s_[0] + new_card
        
        return r,s_