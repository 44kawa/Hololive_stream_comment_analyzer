

class Comment:
    def __init__(self, elapsedTime,
                 comment_type,
                 message,
                 author_name,
                 amountString,
                 currency,
                 amountValue,
                 bgColor):
        self.elapsedTime = elapsedTime
        self.type = comment_type
        self.message = message
        self.author_name = author_name
        self.amountString = amountString
        self.currency = currency
        self.amountValue = amountValue
        self.bgColor = bgColor
