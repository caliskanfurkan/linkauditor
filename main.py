# CRL Auditor v 0.1
# Furkan CALISKAN

import time
import datetime
import httplib2


crl_list = ["http://LINK1,http://LINK2,http://LINK3"]

def download_crl(url):
        conn = httplib2.Http()
        resp, content = conn.request(url, "GET")
        return resp.status

def audit():
        for i in crl_list:
                state = download_crl(i)
		print state
		if state != 200:
			now = datetime.datetime.now()
			d=now.date()
			t=now.time()
			to_print = str(d) + "  " + str(t) + " " + str(i) + "\n"
			with open("error.txt","a") as myfile:
					myfile.write(to_print)
		print "\n"


if __name__ == "__main__":
        while True:
                audit()
                time.sleep(120)
		print "---------------------------------------------"


