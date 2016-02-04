from collections import namedtuple


def colorize(text, code):
    return '\033[{0}m{1}\033[0m'.format(code, text)


color_codes = namedtuple(
    'ColorCodes',
    """
    strong,weak,underline,negative,hidden,strikethrow,
    black,red,green,yellow,blue,purple,cyan,lightgray,
    black_bg,red_bg,green_bg,yellow_bg,blue_bg,purple_bg,cyan_bg,lightgray_bg
    """
)

color = color_codes(
    strong=lambda x: colorize(x, 1),
    weak=lambda x: colorize(x, 2),
    underline=lambda x: colorize(x, 4),
    negative=lambda x: colorize(x, 7),
    hidden=lambda x: colorize(x, 8),
    strikethrow=lambda x: colorize(x, 9),

    black=lambda x: colorize(x, 30),
    red=lambda x: colorize(x, 31),
    green=lambda x: colorize(x, 32),
    yellow=lambda x: colorize(x, 33),
    blue=lambda x: colorize(x, 34),
    purple=lambda x: colorize(x, 35),
    cyan=lambda x: colorize(x, 36),
    lightgray=lambda x: colorize(x, 37),

    black_bg=lambda x: colorize(x, 40),
    red_bg=lambda x: colorize(x, 41),
    green_bg=lambda x: colorize(x, 42),
    yellow_bg=lambda x: colorize(x, 43),
    blue_bg=lambda x: colorize(x, 44),
    purple_bg=lambda x: colorize(x, 45),
    cyan_bg=lambda x: colorize(x, 46),
    lightgray_bg=lambda x: colorize(x, 47)
)


if __name__ == '__main__':
    print('normal')

    print(color.strong('strong'))
    print(color.weak('weak'))
    print(color.underline('underline'))
    print(color.negative('negative'))
    print(color.hidden('hidden'))
    print(color.strikethrow('strikethrow'))

    print(color.black('black'))
    print(color.red('red'))
    print(color.green('green'))
    print(color.yellow('yellow'))
    print(color.blue('blue'))
    print(color.purple('purple'))
    print(color.cyan('cyan'))
    print(color.lightgray('lightgray'))

    print(color.black_bg('black_bg'))
    print(color.red_bg('red_bg'))
    print(color.green_bg('green_bg'))
    print(color.yellow_bg('yellow_bg'))
    print(color.blue_bg('blue_bg'))
    print(color.purple_bg('purple_bg'))
    print(color.cyan_bg('cyan_bg'))
    print(color.lightgray_bg('lightgray_bg'))
