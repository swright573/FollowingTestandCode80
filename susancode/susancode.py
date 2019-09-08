"""
Following along with TestandCode episode 80
"""

__version__ = '0.01'


# docstring and __version__ number are required by flit for packaging


def uppercase(sentence):
    return sentence.upper


def outtext(sentence):
    print(sentence)
    return


def main():
    outtext('Hello world ... Susan here.')
    return


if __name__ == "__main__":
    main()
