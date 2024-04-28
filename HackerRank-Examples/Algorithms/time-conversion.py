

def time_conversion(s):
    output = ''
    num_s = int(s[0:2])
    if s.endswith('PM'):
        if num_s != 12:
            num_s = 12 + num_s
            output = str(num_s) + s[2:len(s)-2]
        else:
            output = s[:len(s)-2]
    else:
        if num_s == 12:
            output = '00' + s[2:len(s)-2]
        else:
            output = s[:len(s)-2]
    return output


if __name__ == '__main__':
    s = '07:05:45PM'
    print(time_conversion(s))
