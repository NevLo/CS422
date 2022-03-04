import math as math
def gradient_descent(gfunc, init, rate):
    precision = 0.00001
    previous_step_size = 10 #
    prev_x = 0
    while previous_step_size > precision :
        prev_x = init 
        init = init - rate * gfunc(init) 
        previous_step_size = math.dist(init, prev_x)
    return prev_x