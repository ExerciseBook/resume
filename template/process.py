from string import Template
from bs4 import BeautifulSoup

import template.root_template
import template.main_container
import template.plain_container

def compose(content, filename):
    main_page = template.main_container.generate_main_page(content)
    plain_page = template.plain_container.generate_plain_page(content)
    extra_style = ""
    if (content["extra_style"] != None) :
        extra_style = Template('<link rel="stylesheet" type="text/css" href="style/${extra_style}">').substitute(extra_style = content["extra_style"])

    locale = "en-US"
    if (content["locale"] != None) :
        locale = content["locale"]
    
    root = template.root_template.generate_root(content["title"], main_page, plain_page, extra_style, locale)
    soup = BeautifulSoup(root, features = "lxml")
    # print(soup.prettify())

    with open(filename, "w", encoding='utf-8') as file:
        file.write(soup.prettify())