import subprocess
import time
import json
url = "http://localhost:8080/v1/models/mnist:predict"
qps = 1
max_qps = 100
increment = 5
SERVICE_HOSTNAME = "torchserve.default.example.com"
file = "mnist.json"
type = "application/json"
test_duration = 600

def run_test():
	curr_qps = qps
	end_time = time.time() + test_duration
	
	while time.time() < end_time:
		cmd = f"hey -z 10s -c {curr_qps} -m POST -host {SERVICE_HOSTNAME} -T {type} -D {file} {url}"
		
		subprocess.run(cmd, shell=True)
		print(curr_qps)
		curr_qps += increment
		if curr_qps > max_qps:
			curr_qps = max_qps
		
if __name__ == "__main__":
	run_test()
