import sys
from misc.helperstr import UMT


class WarningError(Exception):
    """
    Warning error exception class.
    """

    def __init__(self, msg=None):

        highlight = ''
        normal    = ''

        if sys.stderr.isatty():
            highlight = UMT.YELLOW.value + UMT.BOLD.value
            normal    = UMT.NORMAL.value

        self.message = '%sWARNING%s: %s\n' % (highlight, normal, msg)

    def __str__(self):
        return self.message


class FatalError(Exception):
    """
    Fatal error exception class.
    """

    def __init__(self, msg=None):

        highlight = ''
        normal    = ''

        if sys.stderr.isatty():
            highlight = UMT.RED.value + UMT.BOLD.value
            normal    = UMT.NORMAL.value

        self.message = '%sFATAL%s: %s\n' % (highlight, normal, msg)

    def __str__(self):
        return self.message


def debug(msg):
    """
    Issue debug message to stderr
    """

    highlight = ''
    normal    = ''

    if sys.stderr.isatty():
        highlight = UMT.BLUE.value + UMT.BOLD.value
        normal    = UMT.NORMAL.value

    end = '' if msg.endswith('\n') else '\n'
    sys.stderr.write('\n%sDEBUG%s: %s' % (highlight, normal, msg + end))
