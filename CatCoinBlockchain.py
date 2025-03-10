import hashlib

class CatCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + self.previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Catie sends 3.1 CC to Urvesh"
t2 = "Jack sends 4.6 CC to Urvesh"
t3 = "Urvesh sends 0.7 CC to Catie"
t4 = "Sharon sends 1 CC to Urvesh"
t5 = "Oscar sends 0.5 CC to Lola"
t6 = "Oscar sends 2.7 CC to Jack"

initial_block = CatCoinBlock("Initialise", [t1, t2])
print("Initial Block Data:", initial_block.block_data)
print("Initial Block Hash:", initial_block.block_hash)

second_block = CatCoinBlock(initial_block.block_hash, [t3, t4])
print("Second Block Data:", second_block.block_data)
print("Second Block Hash:", second_block.block_hash)

third_block = CatCoinBlock(second_block.block_hash, [t5, t6])
print("Third Block Data:", third_block.block_data)
print("Third Block Hash:", third_block.block_hash)