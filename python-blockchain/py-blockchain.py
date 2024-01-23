import json
from time import time

class blockchain():
    def __init__(self):
        self.chain = []
        self.current_trxs = []
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        ''' create a new block '''
        block = {
            'index' : len(self.chain) + 1,
            'timeStamp' : time(),
            'trxs' : self.current_trxs,
            'proof' : proof,
            'previous_hash' : self.hash(self.chain[-1]),
                }
        self.current_trxs = []
        self.chain.append(block)

        return block

    def new_trx(self, sender, recipient, amount):
        ''' add a new trx to the mempool '''
        self.current_trxs.append({'sender' : sender,
                                 'recipient' : recipient,
                                 'amount' : amount })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        ''' hash a block '''
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        ''' return last block '''
        pass

    @staticmethod
    def valid_proof(last_proof, proof):
        ''' check if this proof is fine or not '''
        this_proof = f'{proof}{last_proof}'.encode()
        this_proof_hash = hashlib.sha256(this_proof).hexdigest()
        return this_proof_hash[:4] == '0000'

    def proof_of_work(self, last_proof):
        ''' shows that the work is done '''
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

