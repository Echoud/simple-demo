# Echoud simple demo
The blockchain source code is based on [Learn Blockchains by Building One](https://github.com/dvf/blockchain)

## Run in Docker

Another option for running this blockchain program is to use Docker.  Follow the instructions below to create a local Docker container:

1. Clone this repository
2. Build the docker container

```
$ docker build -t blockchain .
```

3. Run the container

```
$ docker run --rm -p 80:5000 blockchain
```

4. To add more instances, vary the public port number before the colon:

```
$ docker run --rm -p 81:5000 blockchain
$ docker run --rm -p 82:5000 blockchain
$ docker run --rm -p 83:5000 blockchain
```

## Use
* Check chain status using url `http://0.0.0.0/chain`

* Mine a new block using url `http://0.0.0.0/mine`

* List all accounts using url `http://0.0.0.0/accounts`

* Start a new transcation, use command
```
curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "8956C56C35E6B9E3F6E5096A11A06200",
 "recipient": "F0004B1D688113006405C2EC3C268180",
 "amount": 5
}' "http://0.0.0.0/transactions/new"
```

##Echocloud Voice Interface

Document url `http://docs.0mzl.com/introduction/quick_start/`(http://docs.0mzl.com/introduction/quick_start/)