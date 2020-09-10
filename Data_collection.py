import os
import time 
import request
import sys

def retrive_html():
	for year in range(2013,2018):
		
		for month in range(1,13):

			if(month < 10):

				url="https://en.tutiempo.net/climate/{}-{}/ws-432950.html".format(month,year)
			
			else:

				url="https://en.tutiempo.net/climate/{}-{}/ws-432950.html".format(month,year)

			source_text = request.get(url)
			text_utf = source_text.text.encode('utf-8')

			if not os.path.exists("Data/html_data/{}".format(year)):
				os.makedirs("Data/html_data/{}".format(year)

				with open("Data/html_data/{}/{}".format(month,year),"wb") as output:

					output.write(text_utf)


	sys.stdout.flush()


if __name__ == '__main__':

	start_time = time.time()

	retrive_html()

	stop_time = time.time()

	print("Time taken {}".format(start_time - stop_time))