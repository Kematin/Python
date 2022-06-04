from pyshorteners import Shortener

def short_link(link):
    s = Shortener()
    short = s.tinyurl.short(link)
    return short

def start():
    link = input('Link:\n')
    short = short_link(link)
    print(f'Short link:\n{short}')

if __name__ == '__main__':
    start()
