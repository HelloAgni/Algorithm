def rgb(r, g, b):
    """
    Complete it so that passing in RGB decimal values will result in a hexadecimal
    representation being returned. Valid decimal values for RGB are 0 - 255.
    rgb(255, 255, 255) # returns FFFFFF
    rgb(255, 255, 300) # returns FFFFFF
    rgb(0,0,0) # returns 000000
    rgb(148, 0, 211) # returns 9400D3
    """
    def check_val(x):
        return max(0, min(x, 255))
    return '%02X%02X%02X' % (check_val(r), check_val(g), check_val(b))


def rgb_v2(r, g, b):
    rd = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(rd(r), rd(g), rd(b))


print(rgb(148, 0, 211))
print(rgb_v2(148, 0, 211))
