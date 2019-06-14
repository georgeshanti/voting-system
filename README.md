
# Voting System

## Setup

Configure db connection through config.yaml

	db_server:
	  server: mysql
	  host: 127.0.0.1
	  user: root
	  password: password
	  db_name: votingsystem

Install dependancies and initialize database 

	pip install -r requirements.txt
	python setup.py

## Run

	python run.py

## API Endpoints

	URL: /api/voter
	Method: POST
	Required: JSON
	Fields name, age, adsress, constituency

	URL: /api/constituency
	Method: GET
	Returns: List of constituencies

	URL: /api/constituency/:c_name:/voter/:v_id:/
	Method: GET
	Returns: Voter details of voter id v_id in constituency c_name

	URL: /api/constituency/:c_name:/party/
	Method: GET
	Returns: List of parties in constituency

	URL: /api/constituency/:c_name:/result/
	Method: GET
	Returns: Results of election in constituency c_name

	URL: /api/constituency/:c_name:/vote/
	Method: POST
	Required: JSON
	Fields: party name, voter id

	URL: /api/result/
	Method: GET
	Returns: Results of overall election

	URL: /api/result/winner
	Method: GET
	Returns: List of parties with highest votes

## Benchmarking  

The benchmark was setup using JMeter as a certain no of users polling the following two endpoints 10 times each:

1. /api/constituency/ - List of constituencies
2. /api/constituency/Ernakulam/party/ - List of parties in constituency Ernakulam

### User count = 10

	Average response time = 17ms
	Throughtput = 164.3 requests/sec
	Upload Speed = 22.47 KB/sec
	Download Speed = 40.2 KB/sec

### User count = 100

	Average response time = 578ms (x34)
	Throughtput = 157.5 requests/sec
	Upload Speed = 21.54 KB/sec
	Download Speed = 38.54 KB/sec

### User count = 1000

	Average response time = 3976ms (x233)
	Throughtput = 133.1 requests/sec
	Upload Speed = 17.85 KB/sec
	Download Speed = 38.36 KB/sec

The network load was largely unafffected by increase in users since it was all done within the localhost. Response time on the other hand increased drastically with increase in no of users. This is likely cause by the number of concurrent requests being made to the same server. An easy solution to this would be to have several servers running the REST API webserver and a load balancer to distribute the incoming requests to the web servers.
