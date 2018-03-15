import sys

import black

PEP8_LINE_LENGTH = 79


def main():
    """Runs White."""
    sys.argv.extend(['--line-length', str(PEP8_LINE_LENGTH)])
    black.main()

if __name__ == '__main__':
    main()
