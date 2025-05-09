from flask import Flask, jsonify, request
from blockchain import Blockchain 


app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine_block', methods=['GET'])
def mine_block():
    """Mine a new block and add it to the blockchain."""
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    
    block = blockchain.create_block(proof, previous_hash)

    response = {
        "message": "New block mined!",
        "index": block['index'],
        "proof": block['proof'],
        "previous_hash": block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    """Retrieve the entire blockchain."""
    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/is_valid', methods=['GET'])
def is_valid():
    """Check if the blockchain is valid."""
    valid = blockchain.is_chain_valid(blockchain.chain)
    response = {"message": "Blockchain is valid!"} if valid else {"message": "Blockchain is NOT valid!"}
    return jsonify(response), 200


# Run Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
