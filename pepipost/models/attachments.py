# -*- coding: utf-8 -*-

"""
    pepipost.models.attachments

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class Attachments(object):

    """Implementation of the 'Attachments' model.

    TODO: type model description here.

    Attributes:
        file_content (string): TODO: type description here.
        file_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_content":'fileContent',
        "file_name":'fileName'
    }

    def __init__(self,
                 file_content=None,
                 file_name=None):
        """Constructor for the Attachments class"""

        # Initialize members of the class
        self.file_content = file_content
        self.file_name = file_name


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        file_content = dictionary.get('fileContent')
        file_name = dictionary.get('fileName')

        # Return an object of this model
        return cls(file_content,
                   file_name)


