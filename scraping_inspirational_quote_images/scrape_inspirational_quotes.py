import bs4
import requests
import os
import time
current_dir = os.getcwd()
url = 'https://www.passiton.com/inspirational-quotes?page='
pages = int(input("Enter the page no. you want to scrape inspirational quotes images :"))
for j in range(1,pages+1):
    folder_name = 'quotes of page '+str(j)
    new_folder = os.path.join(current_dir,folder_name)
    os.mkdir(new_folder)
    print(f'folder {j} is created')
    new_url = url + str(j)
    response = requests.get(new_url)
    soup = bs4.BeautifulSoup(response.content,"lxml")
    images = soup.findAll('img')
    print(f"Scrapping the page {j} is started")
    for i,image in enumerate(images[2:-2]):
        #print(i,image['src'])
        filepath = os.path.join(new_folder,'inspirational {}.jpg'.format(i+1))
        with open(filepath,'wb') as file:
            img_url = image['src']
            response = requests.get(img_url)
            file.write(response.content)
            print(f'quote {i+1} is successfully saved') 
    
