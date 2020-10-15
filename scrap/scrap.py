from selenium import webdriver
import pandas as pd
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

def récupérerDonnées(keywords):
    browser = webdriver.Firefox()
    browser.get("https://www.legifrance.gouv.fr/")
    time.sleep(6)
    button_administrative = browser.find_element_by_css_selector("li.content-item:nth-child(4) > p:nth-child(1) > span:nth-child(1) > a:nth-child(1)")
    button_administrative.click()
    time.sleep(3)
    search_cell_text = browser.find_element_by_xpath('//*[@id="query"]')
    search_cell_text.send_keys(f"{keywords}")
    time.sleep(3)
    button_search = browser.find_element_by_xpath('//*[@id="submitPreciseSearch"]')
    button_search.click()
    time.sleep(3)
    coche_ja = browser.find_element_by_xpath("/html/body/div[1]/div/main/div/div/form/div/div[1]/div[3]/div[1]/fieldset/div/fieldset/div/div/div/div/fieldset/div/div[1]/div[2]/div[6]/div")
    coche_ja.click()
    time.sleep(3)
    liste_container_jp = browser.find_elements_by_xpath('/html/body/div[1]/div/main/div/div/form/div/div[3]/div[2]/div/article')
#    print(liste_container_jp)
    jp_on_page = range(len(liste_container_jp))
    time.sleep(3)
    button_suivant = browser.find_element_by_css_selector(".pager-next > a:nth-child(1)")
    jurisprudence = browser.find_elements_by_class_name('name-result-item')
    time.sleep(3)
    liste_tribunal = []
    liste_formation = []
    liste_dates = []
    liste_numéro = []
    liste_président = []
    liste_rapporteur = []
    liste_rapporteur_public = []
    liste_avocats = []
    liste_décision = []
    count_jp = 0
    count_pages = 0
    nb_total_jp = browser.find_element_by_css_selector(".nb-result")
    nombre = nb_total_jp.text.split()[0]
    print(nombre)
    while count_jp < int(nombre):
        liste_container_jp = browser.find_elements_by_xpath('/html/body/div[1]/div/main/div/div/form/div/div[3]/div[2]/div/article')
        jp_on_page = range(len(liste_container_jp))
        for i in jp_on_page:
                jurisprudence = browser.find_elements_by_class_name('name-result-item')
                jurisprudence[i].click()
                info = browser.find_element_by_css_selector(".main-title")
                info = info.text.split(',')
                liste_tribunal.append(info[0])
                liste_formation.append(info[1])
                liste_dates.append(info[2])
                liste_numéro.append(info[3])
                time.sleep(3)
                if info[0] == "Conseil d'Etat" or info[0] == "Conseil d'État":
                        liste_président.append(" ")
                        rapporteur = browser.find_element_by_css_selector('div.frame-block:nth-child(3) > div:nth-child(1) > dd:nth-child(2)')
                        liste_rapporteur.append(rapporteur.text)   
                        rapporteur_public = browser.find_element_by_css_selector('div.frame-block:nth-child(3) > div:nth-child(2) > dd:nth-child(2)')
                        liste_rapporteur_public.append(rapporteur_public.text)     
                        avocats = browser.find_element_by_css_selector('div.frame-block:nth-child(3) > div:nth-child(3) > dd:nth-child(2)')
                        liste_avocats.append(avocats.text)
                        time.sleep(3)
                else:        
                    president = browser.find_element_by_css_selector('div.frame-block:nth-child(3) > div:nth-child(1) > dd:nth-child(2)')
                    liste_président.append(president.text)
                    rapporteur = browser.find_element_by_css_selector('div.frame-block:nth-child(3) > div:nth-child(2) > dd:nth-child(2)')
                    liste_rapporteur.append(rapporteur.text)   
                    rapporteur_public = browser.find_element_by_css_selector('div.frame-block:nth-child(3) > div:nth-child(3) > dd:nth-child(2)')
                    liste_rapporteur_public.append(rapporteur_public.text)
                    avocats = browser.find_element_by_css_selector('div.frame-block:nth-child(3) > div:nth-child(4) > dd:nth-child(2)')
                    liste_avocats.append(avocats.text)
                    time.sleep(3)
                décision = browser.find_element_by_css_selector('.content-page')
                liste_décision.append(décision.text)
                count_jp += 1
                print(f'nombre de jp scrappés : {count_jp}')
                browser.back()
                time.sleep(3)
        try:    
            count_pages += 1
            print(f"nombre de pages analysés : {count_pages}")
            button_suivant = browser.find_element_by_css_selector(".pager-next > a:nth-child(1)")
            button_suivant.click()
            time.sleep(3)
        except:
            pass
    else:
        print("c'est bon t'as tout scrappé")
    return liste_tribunal, liste_formation, liste_dates, liste_numéro, liste_président, liste_rapporteur, liste_rapporteur_public, liste_avocats, liste_décision

def créationDataFrame(liste_tribunal, liste_formation, liste_dates, liste_numéro, liste_président, liste_rapporteur, liste_rapporteur_public, liste_avocats, liste_décision):
    df = pd.DataFrame(list(zip(liste_tribunal, liste_formation, liste_dates, liste_numéro, liste_président, liste_rapporteur, liste_rapporteur_public, liste_avocats, liste_décision)),
                 columns = ["tribunal", "formation", "dates", "numéro de la jurisprudence", "nom du président", "nom du rapporteur", "nom du rapporteur public", "avocats", "décision"])
    return df

def save_csv(df, keywords):
    df.to_csv(f"{keywords}.csv", index=False)
    return df



























