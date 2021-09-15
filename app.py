from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)




@app.route("/")
def home():
    tech_point = requests.get("https://techpoint.africa/").text
    techcabal = requests.get("https://techcabal.com/category/startups/").text
    disrupt = requests.get("https://disrupt-africa.com/").text

    soup_point = BeautifulSoup(tech_point, 'lxml')
    soup_cabal = BeautifulSoup(techcabal, 'lxml')
    soup_disrupt = BeautifulSoup(disrupt, 'lxml')

    point = soup_point.find_all('h4', class_="entry-title")
    cabal = soup_cabal.find_all('a', class_="article-list-title")
    rupt = soup_disrupt.find_all('a', class_="post-title")


    news_point = [{'news':n.find('a').text,'link':n.find('a')['href']} for n in point]
    news_cabal = [{'news':n.text.strip(),'link':n["href"].strip()} for n in cabal]
    news_rupt = [{'news': n.text.strip(), 'link': n["href"].strip()} for n in rupt]



    return render_template('news.html',news_rupt=news_rupt, news_cabal=news_cabal, news_point=news_point)



if __name__ == "__main__":
    app.run(debug=True)