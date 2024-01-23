class blockchain(object):
    def __init__(self):
        self.chain = []
        self.curent_trx = []

    def new_block(self):
        ''' create a new block '''
        pass

    def new_trx(self):
        ''' add a new trx to the mempool '''
        pass

    @staticmethod
    def hash(block):
        ''' hash a block '''
        pass

    @property
    def last_block(self):
        ''' return last block '''
        pass

