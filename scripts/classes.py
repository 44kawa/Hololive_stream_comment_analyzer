"""
This module defines the Comment class, which holds information
about comments such as the author, message, and additional details.
"""


class Comment:
    """
    A class used to represent a Comment.

    Attributes
    ----------
    elapsedTime : str
        The time when the comment was posted.
    type : str
        The type of comment.
    message : str
        The content of the comment.
    author_name : str
        The name of the author who posted the comment.
    amountString : str
        The amount in string format.
    currency : str
        The currency associated with the amount.
    amountValue : float
        The numerical value of the amount.
    bgColor : str
        The background color associated with the comment.
    """

    def __init__(self, elapsedTime, comment_type, message, author_name, amountString, currency, amountValue, bgColor):
        """
        Constructs all the necessary attributes for the Comment object.

        Parameters
        ----------
        elapsedTime : str
            The time when the comment was posted.
        comment_type : str
            The type of comment.
        message : str
            The content of the comment.
        author_name : str
            The name of the author who posted the comment.
        amountString : str
            The amount in string format.
        currency : str
            The currency associated with the amount.
        amountValue : float
            The numerical value of the amount.
        bgColor : str
            The background color associated with the comment.
        """
        self.elapsedTime = elapsedTime
        self.type = comment_type
        self.message = message
        self.author_name = author_name
        self.amountString = amountString
        self.currency = currency
        self.amountValue = amountValue
        self.bgColor = bgColor

    def get_summary(self):
        """Returns a brief summary of the comment."""
        return f"{self.author_name}: {self.message} ({self.currency} {self.amountValue})"

    def update_message(self, new_message):
        """Updates the comment's message."""
        self.message = new_message
