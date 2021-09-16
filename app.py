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
    bd = requests.get("https://www.benjamindada.com/").text

    soup_point = BeautifulSoup(tech_point, 'lxml')
    soup_cabal = BeautifulSoup(techcabal, 'lxml')
    soup_disrupt = BeautifulSoup(disrupt, 'lxml')
    soup_bd = BeautifulSoup(bd, 'lxml')

    point = soup_point.find_all('h4', class_="entry-title")
    cabal = soup_cabal.find_all('a', class_="article-list-title")
    rupt = soup_disrupt.find_all('a', class_="post-title")
    ben = soup_bd.find_all('a', class_="post-card-content-link")


    news_point = [{'news':n.text, 'link':n.a["href"]} for n in point]
    news_cabal = [{'news':n.text.strip(),'link':n["href"].strip()} for n in cabal if n.text !=""]
    news_rupt = [{'news': n.text.strip(), 'link': n["href"].strip()} for n in rupt]
    news_bd = [{'news':r.h2.text,'link':f'https://www.benjamindada.com{r["href"]}'} for r in ben if r.find('span',class_="post-card-tags")]


    return render_template('news.html',news_rupt=news_rupt, news_cabal=news_cabal, news_point=news_point, news_bd=news_bd)



if __name__ == "__main__":
    app.run()