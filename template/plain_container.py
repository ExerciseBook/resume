from string import Template
from bs4 import BeautifulSoup

plain_template = '''
<div class="plain-container">
    <pre>
${content}
    </pre>
</div>
'''

LF = "\n"

def generate_section_item(s) :
    ret = ""

    if s["title"] != None :
        if s["title_plain"] == None :
            ret += BeautifulSoup(s["title"], features = "lxml").text + LF
        else :
            ret += BeautifulSoup(s["title_plain"], features = "lxml").text + LF
        
        if s["period"] != None :
            ret += s["period"] + LF

    if s["content_plain"] == None :
        ret += BeautifulSoup(s["content"], features = "lxml").text.replace("\r", "").replace("\n\n", "") + LF
    else :
        ret += BeautifulSoup(s["content_plain"], features = "lxml").text.replace("\r", "").replace("\n\n", "") + LF

    return ret


def generate_section(s) :
    ret = ""

    ret += Template("[${title}]").substitute(title = s["title"]) + LF
      
    if len(s["list"])  == 0 :
        ret += "Empty" + LF
    else :
        for i in s["list"]  :
            ret += generate_section_item(i)

    return ret


def generate_entry(s) :
    ret = ""

    ret  += s["name"]  + LF
    for i in s["profile"] :
        ret += Template("${title}: ${content}" + LF).substitute(
            title = i["alt"],
            content = i["content"],
        )
    ret += LF

    for i in s["sections"] :
        ret += generate_section(i) + LF

    return ret

def generate_plain_page(s) :
    return Template(plain_template).substitute(
        content = generate_entry(s)
    )