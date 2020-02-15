'''
RL for Black Jack

author@dynmiWang 

State  = {cur_sum, ace_yes, s_card}
    |———— cur_sum 12,13,14,...,21
    |———— ace_yes 1,0
    |____ s_card  ace,2,3,...,10

ACTION = { stick,twist }

REWARD
    |——— stick
        | +1 if sum_mine > sum_dealers 
        |  0 if sum_mine = sum_dealers
        | -1 if sum_mine < sum_dealers
    |——— twist
        | -1 if sum_mine > 21
        |  0 otherwise
Transitions
    |   automatically twist if sum of cards < 12

'''

import random as rd
import numpy as np

State = [[a, b, c] for a in range(12, 22) for b in range(0, 2) for c in range(1, 11)]

Action = [0, 1]
# pai[1]=[pa,pb]         pai(stick | State[0]) = pa; pai(twist | State[1]) = pb
pai   = [ [0.5,0.5] for s in State ]
# Q[0][0][9]=[?,?]       cur_sum is 12; ace_yes is yes; s_card is 10 
Q     = [[0 for a in Action] for s in State]

alpha = 0.1
epsilon = 0.9

def rand_(a, b):
    x = rd.randint(a, b)
    if x > 10: x = 10
    return x

def policy(s,a):
    p = State.index(s)
    return pai[p][a]

def get_reward(s, a):
    # s:state   a:action
    M = s[0]
    D = s[2]
    r = 0
    if a == 1:
        #停牌，比输赢
        hidden_card = rand_(1,13)
        D = D +hidden_card
        if M > D:
            r = 1
        if M == D:
            r = 0
        if M < D:
            r = -1
        return [0,0,0],r
    else:
        new_card = rand_(1, 13)
        M = M + new_card 
        if M > 21:
            return [0,0,0],-1
        else:
            return [M,s[1],D],0


def get_q(s, a):
    p = State.index(s)
    return Q[p][a]

def policy_evaluation(episode=100):
   alpha = 0.9
   for e in range(episode):
       #蒙特卡洛采样
       S_sa = []
       S_r = []
       s_card   = rand_(1, 10)
       my_1     = rand_(1, 13)
       my_2 = rand_(1, 13)
       ace  = 1 if my_1==1 or my_2==1 else 0
       my_sum_ = my_1+my_2
       if my_sum_<12: my_sum_ = 12
       S = [my_sum_, ace, s_card]
       while True:
            dic = rd.random()
            a_ = 0 if dic < policy(S,0) else 1
            S, r = get_reward(S, a_)
            if S[0]==0:break
            s_  = State.index(S)
            S_sa.append([s_,a_])
            S_r.append(r)
       
       #遍历样本
       for s, a in S_sa:
           G = np.sum( S_r[S_sa.index([s,a]):] )
           Q[s][a] = Q[s][a] + alpha * (G-Q[s][a])
           

def policy_improvement():
    for s,_ in enumerate(State):
        pai_ = [epsilon/len(Action) for a in Action]
        max_ = Q[s].index( max(Q[s]) )
        pai_[max_] = pai_[max_] + 1 - epsilon
        pai[s] = pai_

if __name__ == "__main__":
    for i in range(5):
        policy_evaluation()
        policy_improvement()
        print(Q)