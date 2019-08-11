import math

def square_root(x):
  y = math.sqrt(x)
  return y

def get_response(querytext:str, tenant:str):
    if tenant == "nykaa":
        return "Thanks for talking to Nykaa!"