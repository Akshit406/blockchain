# Python Blockchain

This project implements a **simple blockchain in Python** with Flask as the web interface. Users can **mine blocks, validate the chain, and add transactions** within a decentralized ledger.

## Features
- Proof-of-Work (PoW) mining  
- Flask-based API for blockchain interaction  
- Blockchain integrity validation  
- Basic transaction handling  

---

## Installation and Setup

### 1. Clone the Repository
```
git clone https://github.com/Akshit406/blockchain
cd python-blockchain 
python -m venv venv 
```

### 2. Install Dependencies
```
pip install flask requests
```

### 3. Run the Blockchain Server

```
python app.py
```
The Flask API will start at http://127.0.0.1:5000/. 



### API Usage
> Mine a Block

```
curl http://127.0.0.1:5000/mine_block
```
Adds a new block to the blockchain.

> Retrieve the Blockchain
```
curl http://127.0.0.1:5000/get_chain
```
Returns the entire blockchain.

> Validate Blockchain Integrity
```
curl http://127.0.0.1:5000/is_valid
```
Checks whether the blockchain is valid.
