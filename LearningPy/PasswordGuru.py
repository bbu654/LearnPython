"""     https://realpython.com/documenting-python-code/
    
    
    Additionally, you should use the following four essential 
    RULES as suggested by Jeff Atwood (aka Coding Horror 
        {Code tells you how; Comments tell you why.}):

Keep comments as close to the code being described as possible. 
    Comments that aren’t near their describing code 
    are frustrating to the reader 
    and easily missed when updates are made.

Don’t use complex formatting (such as tables or ASCII figures). 
    Complex formatting leads to distracting content 
    and can be difficult to maintain over time.

Don’t include redundant information. 
    Assume the reader of the code has a basic understanding 
    of programming principles and language syntax.

Design your code to comment itself. 
    The easiest way to understand code is by reading it. 
    When you design your code using clear, easy-to-understand concepts, 
    the reader will be able to quickly conceptualize your intent.

Class docstrings should contain the following information:
    A brief summary of its purpose and behavior
    Any public methods, along with a brief description
    Any class properties (attributes)
    Anything related to the interface for subclassers, 
        if the class is intended to be subclassed
The class constructor parameters should be documented 
    within the __init__ class method docstring. 
    Individual methods should be documented using their individual docstrings. 
    Class method docstrings should contain the following:
        A brief description of what the method is and what it’s used for
        Any arguments (both required and optional) 
            that are passed including keyword arguments
        Label any arguments that are considered optional 
            or have a default value
        Any side effects that occur when executing the method
        Any exceptions that are raised
        Any restrictions on when the method can be called
Let’s take a simple example of a data class that represents an Animal. 
    This class will contain a few class properties, 
    instance properties, a __init__, and a single instance method:
"""
class Animal:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    says_str = "A {name} says {sound}"

    def __init__(self, name, sound, num_legs=4):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """

        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def says(self, sound=None):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """

        if self.sound is None and sound is None:
            raise NotImplementedError("Silent Animals are not supported!")

        out_sound = self.sound if sound is None else sound
        print(self.says_str.format(name=self.name, sound=out_sound))
    #reStructured Text Example
    """Gets and prints the spreadsheet's header columns

    :param file_loc: The file location of the spreadsheet
    :type file_loc: str
    :param print_cols: A flag used to print the columns to the console
        (default is False)
    :type print_cols: bool
    :returns: a list of strings representing the header columns
    :rtype: list
    """