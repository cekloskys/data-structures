class madlib:
    """The madlib class includes methods that generate madlibs.
    """    
    def __init__(self, noun: str, verb: str, adverb: str, adjective: str):
        """Initializes a madlib using the specified noun, verb, adverb, and adjective.

        Args:
            noun (str): specified noun
            verb (str): specified verb
            adverb (str): specified adverb
            adjective (str): specified adjective

        Raises:
            ValueError: indicates specified noun is None
            ValueError: indicates specified verb is None
            ValueError: indicates specified adverb is None
            ValueError: indicates specified adjective is None
        """        
        try:
            if (noun is None):
                raise ValueError("Noun may not be none.")
            elif(verb is None):
                raise ValueError("Verb may not be none.")
            elif(adverb is None):
                raise ValueError("Adverb may not be none.")
            elif(adjective is None):
                raise ValueError("Adjective may not be none.")
        except ValueError as e:
            exit(e)
        finally:
            self.__noun = noun
            self.__verb = verb
            self.__adverb = adverb
            self.__adjective = adjective

    def getNoun(self):
        """Returns the noun of the calling madlib.

        Returns:
            str: noun
        """        
        return self.__noun
    
    def setNoun(self, noun):
        """Sets the noun in the calling madlib to the specified noun.

        Args:
            noun (str): specified noun

        Raises:
            ValueError: indicates specified noun is None
        """        
        try:
            if (noun is None):
                raise ValueError("Noun may not be none.")
        except ValueError as e:
            exit(e)
        finally:
            self.__noun = noun

    def getVerb(self):
        """Returns the verb of the calling madlib.

        Returns:
            str: verb
        """ 
        return self.__verb
    
    def setVerb(self, verb):
        """Sets the verb in the calling madlib to the specified verb.

        Args:
            verb (str): specified verb

        Raises:
            ValueError: indicates specified verb is None
        """
        try:
            if (verb is None):
                raise ValueError("Verb may not be none.")
        except ValueError as e:
            exit(e)
        finally:
            self.__verb = verb

    def getAdverb(self):
        """Returns the adverb of the calling madlib.

        Returns:
            str: adverb
        """ 
        return self.__adverb
    
    def setAdverb(self, adverb):
        """Sets the adverb in the calling madlib to the specified adverb.

        Args:
            adverb (str): specified adverb

        Raises:
            ValueError: indicates specified adverb is None
        """
        try:
            if (adverb is None):
                raise ValueError("Adverb may not be none.")
        except ValueError as e:
            exit(e)
        finally:
            self.__adverb = adverb

    def getAdjective(self):
        """Returns the adjective of the calling madlib.

        Returns:
            str: adjective
        """ 
        return self.__adjective
    
    def setAdjective(self, adjective):
        """Sets the adjective in the calling madlib to the specified adjective.

        Args:
            adjective (str): specified adjective

        Raises:
            ValueError: indicates specified adjective is None
        """
        try:
            if (adjective is None):
                raise ValueError("Adjective may not be none.")
        except ValueError as e:
            exit(e)
        finally:
            self.__adjective = adjective

    def __str__(self):
        """Returns string representation of the calling madlib.

        Returns:
            str: string representation of the calling madlib
        """        
        return f"madlib noun={self.__noun} verb={self.__verb} adverb={self.__adverb} adjective={self.__adjective}"
    
    def __eq__(self, other):
        """Tests if the calling madlib is equal to the specified object.

        Args:
            other: the specified object

        Returns:
            Boolean: True if the calling madlib is equal to the specified
            object, else False
        """
        if other is not None:
            if isinstance(other, madlib):
                if other.__noun == self.__noun:
                    if self.__verb == self.__verb:
                        if self.__adverb == self.__adverb:
                            if self.__adjective == self.__adjective:
                                return True
                
        return False
    
    def generate(self):
        """Formats noun, verb, adverb, and adjective in the madlib for the calling madlib.

        Returns:
            str: formatted madlib
        """        
        return f"Do you {self.__verb} your {self.__adjective} {self.__noun} {self.__adverb}? That's hilarious!"
    
    @staticmethod
    def show(): 
        """Displays madlib without noun, verb, adverb, and adjective.
        """        
        underline = "_____"

        print("Do you", underline, "your", underline, underline, underline, "? That's hilarious!")