# Solution for problem Blackjack in Sutton's Reinforcement Learning books



## Language

- python 3

## Package required

- numpy

- random

## Setting details
- Action： a =0 or 1
  + a=0  stick 
  + a=1  twist // automatically twist if sum of cards < 12

- State：  s = [my_sum, ace_own, s_card]   //[13,0,8]
  + my_sum  ：the current sum of my cards.  
  + ace_own ：agent own a ace card or not      // 0 for yes 1 ;for no
  + s_card     ：host showing card

- POLICY： pai[1] = [0.4, 0.6]                 //  under State[1], prob for stick is 0.4, prob for twist is 0.6

- Value function：  Q [2] [0]  =23          //  q of (State[1], stick) is 23 
