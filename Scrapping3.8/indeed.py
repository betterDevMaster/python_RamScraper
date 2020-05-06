# python -m pip install beautifulsoup4
# python -m pip install requests
# python -m pip install --upgrade lxml
# python -m pip install cssselect

from bs4 import BeautifulSoup
import requests
import csv
import time
import os

pages = [10, 20, 30, 40, 50]
# pages = [10]

with open('E:\WorkStation\python\Scrapping3.8\scrapping.csv', 'a', encoding='utf-8', newline='') as f_output:
    csv_print = csv.writer(f_output)
    file_is_empty = os.stat('E:\WorkStation\python\Scrapping3.8\scrapping.csv').st_size == 0
    if file_is_empty:
        csv_print.writerow({'Job_Title', 'Company', 'Location', 'Summary', 'Salary'})

    for page in pages:
        source = requests.get('https://www.indeed.com/jobs?q=data+scientist&start={}'.format(page)).text

        soup = BeautifulSoup(source, 'lxml')
        # print(soup)
        # break
        for jobs in soup.find_all(class_='result'):
            try:
                title = jobs.h2.text.strip()
            except Exception as e:
                title = None
            print('Job title:', title)

            try:
                company = jobs.span.text.strip()
            except Exception as e:
                company = None
            print('Company:', company)

            try:
                location = jobs.find('span', class_='location').text.strip()
            except Exception as e:
                location = None
            print('Location:', location)

            try:
                summary = jobs.find('span', class_='summary').text.strip()
            except Exception as e:
                summary = None
            print('Summary:', summary)

            try:
                salary = jobs.find('span', class_='no-wrap').text.strip()
            except Exception as e:
                salary = None
            print('Salary:', salary)

            csv_print.writerow([title, company, location, summary, salary])

            print('----------')

            time.sleep(0.5)