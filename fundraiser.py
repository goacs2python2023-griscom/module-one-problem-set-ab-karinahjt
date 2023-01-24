#As part of your community service project, you organize a raffle to raise money for a good cause.  
# Tickets cost $5 each and you spent $50 on the prizes.  
# Write a Python function that computes the amount of money you raised. 
def moneyEarned(a):
  if (type(a) != int) or (a<0):
        return "Error"
  else:
    return a*5-50
 
 
print(moneyEarned(36))    # 130
print(moneyEarned(-100))   # error
print(moneyEarned(0))      # -50
print(moneyEarned(10))     # 0
