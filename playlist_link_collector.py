from selenium import webdriver
import yaml


def link_collector(url_path):

    path = "/home/madlad/chromedriver"
    driver = webdriver.Chrome(executable_path=path)

    #url = "https://www.youtube.com/playlist?list=PLfNW_1ECVaThQynVe4QDlBM5S6Kzy8CeJ"
    url = url_path
    driver.get(url)
    links = driver.find_elements_by_tag_name("a")
    links_watch = []
    for link in links:
            test = link.get_attribute("href")
            if test!=None and ("/watch" in test and "&index" in test):
                print(test)
                links_watch.append(test)
    links_watch = set(links_watch)
    driver.close()

    with open("links.txt","w+") as f:
        for link in links_watch:
            f.write(link+"\n")

with open("config.yml") as f:
    config = yaml.load(f)

link_collector(config["playlist_path"])