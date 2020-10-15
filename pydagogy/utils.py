colors = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "purple": 35,
    "cyan": 36,
    "white": 37,
}

styles = {"normal": 0, "bold": 1, "underline": 2}


def text_format(text, color="black", style="normal"):
    if color not in colors:
        raise ValueError(f"Requested color '{color}' not available")

    if style not in styles:
        raise ValueError(f"Requested style '{style}' not available")

    format_code = f"\033[{styles[style]};{colors[color]}m"
    clear_code = f"\033[0m"

    return "".join([format_code, text, clear_code])
