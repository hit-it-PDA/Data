import html


def to_int(str):
    if str is None or str == '':
        return
    return int(str.replace(",", ""))


def to_str(str):
    if str is None or str == '':
        return
    return str


def decode_html(str):
    return html.unescape(str)


if __name__ == "__main__":
    print(decode_html("HAOHUA 4 7&#47;8 03&#47;14&#47;25"))
    print("수산금융채권(신특)04-03이표12-07호")