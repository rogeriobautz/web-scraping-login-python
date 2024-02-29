# Scraping Websites with CSRF Token Authentication for Login

from dotenv import load_dotenv
from bs4 import BeautifulSoup 
import requests
import os

load_dotenv()

login_url = os.getenv('LOGIN_URL_CSRF')
username = os.getenv('USERNAME_CSRF')
password = os.getenv('PASSWORD_CSRF')

with requests.session() as s: 
	req = s.get(login_url).text 
	html = BeautifulSoup(req,"html.parser") 
	token = html.find("input", {"name": "authenticity_token"}). attrs["value"] 
	time = html.find("input", {"name": "timestamp"}).attrs["value"] 
	timeSecret = html.find("input", {"name": "timestamp_secret"}). attrs["value"]
 
	payload = {
		"authenticity_token": token, 
		"login": username, 
		"password": password, 
		"timestamp": time, 
		"timestamp_secret": timeSecret 
	}

	r = s.post(login_url, data=payload) 

	repos_url = "https://github.com/" + username + "/?tab=repositories" 
	r = s.get(repos_url) 
	soup = BeautifulSoup(r.content, "html.parser")

	usernameDiv = soup.find("span", class_="p-nickname vcard-username d-block") 
	print("Username: " + usernameDiv.getText()) 
	repos = soup.find_all("h3",class_="wb-break-all") 

	for r in repos: 
		repoName = r.find("a").getText()
		print("Repository Name: " + repoName)