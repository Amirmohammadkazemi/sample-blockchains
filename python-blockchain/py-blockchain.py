class blockchain():
    def __init__(self):
        self.chain = []
        self.current_trx = []

    def new_block(self):
        ''' create a new block '''
        pass

    def new_trx(self, sender, recipient, amount):
        ''' add a new trx to the mempool '''
        self.current_trx.append({'sender' : sender,
                                 'recipient' : recipient,
                                 'amount' : amount })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        ''' hash a block '''
        pass

    @property
    def last_block(self):
        ''' return last block '''
        pass

