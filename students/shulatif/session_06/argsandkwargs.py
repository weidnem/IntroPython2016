

def html_colors(fore_color='black', back_color='white', link_color='orange', visited_color='red'):
    """
    This will print the colors used in a website with defaults already set.
    :param fore_color: The foreground color to use.
    :param back_color: The background color to use.
    :param link_color: The link colors.
    :param visited_color: The color of the link after it's been visited.
    :return: Just the list of colors
    """
    print(fore_color, back_color, link_color, visited_color)

html_colors()
html_colors('red')
html_colors('orange', 'pink', 'brown', 'violet')
html_colors(fore_color='white', back_color='black')
html_colors('white', back_color='black')

bg_text = ('white', 'black')
links = {'link_color': 'red', 'visited_color': 'pink'}
html_colors(*bg_text, **links)


def html_colors_gen(*args, **kwargs):
    """
    This will print any argument you give it.
    :param args:
    :param kwargs:
    :return: prints the arguments
    """
    print(*args, **kwargs)

html_colors_gen('red', 'black', 'green', 5)