class Thingy(object):
    """
        An example thingy.

        :Example:

        >>> t = Thingy()
        >>> print(t.stuff)
        None
        >>> t.stuff == None
        True

    """

    def __init__(self):
        """
        :param self: The instance to initialize
        """
        self.stuff = None
