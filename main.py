import time
import thirdparty.httplib2

def download_crl(url):
	conn = thirdparty.httplib2.Http(".cache")
	resp, content = conn.request(url, "GET")


	# Status 200 mü bakılacak
	
	return resp
	

def sum_crl(crl):



def audit():
	print "Dene"


if __name__ == "__main__":
	while True:
		audit()
		time.sleep(2)
