import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    
    browser = init_browser()
    
    # Visit the following URL
    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    current_news_title = soup.find('div', id='news').find('div', class_='content_title').text
    current_news_p = soup.find('div', id='news').find('div', class_='article_teaser_body').text

    # # EXTRACT NASA SPACE IMAGES

    url = "https://spaceimages-mars.com"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Image source
    img_source = soup.findAll('img','headerimage fade-in')

    image_url =[]
    for image in img_source:
        #print image source
        image_url.append(image['src'])
        
    
    #Build Complete Path
    base_url = "https://spaceimages-mars.com/"

    # the image URL
    featured_image_url = base_url + image_url[0]

    # # EXTRACT MARS FACTS

    url = "https://galaxyfacts-mars.com"
    browser.visit(url)

    #html = browser.html
    #soup = BeautifulSoup(html, "html.parser")
    #table = soup.find_all('table')[0]

    mars_facts = pd.read_html(url)[0]

    # Converting table to html
    mars_table = mars_facts.to_html()

    # # MARS HEMISPHERES PICTURES

    base_url = "https://marshemispheres.com/"
    cerberus_emisphere_url = "https://marshemispheres.com/cerberus.html"
    schiaparelli_emisphere_url = "https://marshemispheres.com/schiaparelli.html"
    syrtis_emisphere_url = "https://marshemispheres.com/syrtis.html"
    valles_emisphere_url= "https://marshemispheres.com/valles.html"


    # Image source
    browser.visit(cerberus_emisphere_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    hemispheres = []
    img_source = soup.find('div',class_='downloads').a['href']
    hemispheres.append(base_url + img_source)

    # Image source
    browser.visit(schiaparelli_emisphere_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    img_source = soup.find('div',class_='downloads').a['href']
    hemispheres.append(base_url + img_source)
          
    # Image source
    browser.visit(syrtis_emisphere_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    img_source = soup.find('div',class_='downloads').a['href']
    hemispheres.append(base_url + img_source)

    # Image source
    browser.visit(valles_emisphere_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    img_source = soup.find('div',class_='downloads').a['href']
    hemispheres.append(base_url + img_source)
        
    #Python dictionary to store the data using the keys `img_url` and `title`.
    hemispheres_list =['Cerberus Hemisphere', 'Schiaparelli Hemisphere','Syrtis Major Hemisphere','Valles Marineris']

    hemisphere_data_1 = [{'title': hemispheres_list[0], 'img_url':hemispheres[0]}]
    hemisphere_data_2 = [{'title': hemispheres_list[1], 'img_url':hemispheres[1]}]
    hemisphere_data_3 = [{'title': hemispheres_list[2], 'img_url':hemispheres[2]}]
    hemisphere_data_4 = [{'title': hemispheres_list[3], 'img_url':hemispheres[3]}]

    #Close the browser after scraping
    browser.quit()

    #Dictionary
    mars_data = {
        "mars_news_headlines": current_news_title,
        "mars_news_abstract": current_news_p,
        "mars_featured_image": featured_image_url,
        "mars_facts":mars_table,
        "mars_hemisphere_1_name": hemispheres_list[0],
        "mars_hem_1_url": hemispheres[0],
        "mars_hemisphere_2_name": hemispheres_list[1],
        "mars_hem_2_url": hemispheres[1],
        "mars_hemisphere_3_name": hemispheres_list[2],
        "mars_hem_3_url": hemispheres[2],
        "mars_hemisphere_4_name": hemispheres_list[3],
        "mars_hem_4_url": hemispheres[3]
    }

    return mars_data

#if __name__ == "__main__":
 #   data = scrape()
  #  print(data)

