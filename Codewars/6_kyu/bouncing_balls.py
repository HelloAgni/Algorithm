def bouncing_ball(h, bounce, window):
    """
    How many times will the mother see the ball pass in front of her window
    (including when it's falling and bouncing?
    Three conditions must be met for a valid experiment:
    Float parameter "h" in meters must be greater than 0
    Float parameter "bounce" must be greater than 0 and less than 1
    Float parameter "window" must be less than h.
    If all three conditions above are fulfilled,
    return a positive integer, otherwise return -1.
    Examples:
    - h = 3, bounce = 0.66, window = 1.5, result is 3
    - h = 3, bounce = 1, window = 1.5, result is -1
    """
    count = -1
    if bounce >= 1 or bounce <= 0:
        return count
    if h < 0 or h < window:
        return count
    while h > window:
        h = h * bounce
        count += 2
    else:
        return count


h = 30  # 9
bounce = 0.5
window = 1.5
print(bouncing_ball(h, bounce, window))
