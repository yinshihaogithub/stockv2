def humanize_float_cn(num: float, num_digits: int = 2):
    """
    num：数字
    num_digits:小数点保留位数
    """
    units = ['', '万', '亿', '兆(10^12)', '京(10^16)', '垓(10^20)', '秭(10^24)']

    def strofsize(num, level):
        if level >= len(units) - 1:
            return num, level
        elif abs(num) >= 10000:
            num /= 10000
            level += 1
            return strofsize(num, level)
        else:
            return num, level

    num, level = strofsize(num, 0)
    if level > len(units):
        level -= 1
    return f'{round(num, num_digits)}{units[level]}'