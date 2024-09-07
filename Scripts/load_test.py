import subprocess
import time
import json
url = "http://localhost:8080/v1/models/flower-sample:predict"
qps = 1
max_qps = 100
increment = 5
SERVICE_HOSTNAME = "flower-sample.default.example.com"
file = "input-tf.json"
	
test_duration = 60

def run_test():
	curr_qps = qps
	end_time = time.time() + test_duration
	
	while time.time() < end_time:
		cmd = f"hey -z 60s -c 1 -m POST -host {SERVICE_HOSTNAME} -D {file} {url}"
		
		subprocess.run(cmd, shell=True)
		print(curr_qps)
		curr_qps += increment
		if curr_qps > max_qps:
			curr_qps = max_qps
		
if __name__ == "__main__":
	run_test()
