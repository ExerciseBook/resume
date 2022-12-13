from string import Template

main_container = '''
<div class="main-container">
    <div class="top-padding only-screen-can-see"></div>
    ${title} 
    ${profile_container}
    ${section_parts}
    <div class="buttom-padding only-screen-can-see"></div>
</div>
'''

main_title = '''
<h1 class="title-h1">${title}</h1>
'''

profile_item_main = '''
<img class="profile-icon" src="${src}" alt="${alt}"/>${content}
'''

profile_item_url = '''
<a href="${url}">${content}</a>
'''

profile_item = '''
<span>${content}</span>
'''

section_parts_template = '''
<h2 class="section-title">${title}</h2>
<div class="section-container">
    <div class="section-left-padding"></div>
    <div class="section-list">
        ${section_list}
    </div>
</div>    
'''

section_list_item = '''
<div class="section-item">
<div class="section-item-title">
    ${title}
</div>
${content}
</div>
'''

section_list_title_with_screen_class = '''
<p class="only-screen-can-see">
    ${content}
</p>
'''

section_list_title_with_print_class = '''
<p class="only-print-can-see">
    ${content}
</p>
'''

section_list_title_without_class = '''
<p>
    ${content}
</p>
'''

section_list_title_period = '''
<span class="section-list-title-period">${content}</span>
'''

section_list_title_logo = '''
<img class="section-item-logo" src="${src}" alt=${alt}/>
'''

section_list_content_with_screen_class = '''
<div class="section-item-content only-screen-can-see">
    ${content}
</div>
'''

section_list_content_with_print_class = '''
<div class="section-item-content only-print-can-see">
    ${content}
</div>
'''

section_list_content_without_class = '''
<div class="section-item-content">
    ${content}
</div>
'''

def generate_profile_item(s) :
    t = Template(profile_item_main).substitute(
        src = s["src"],
        alt = s["alt"],
        content = s["content"],
    )

    if s["url"] != None :
        t = Template(profile_item_url).substitute(
            content = t,
            url = s["url"]
        )
    
    return Template(profile_item).substitute(content = t)

def generate_main_title(s) :
    return Template(main_title).substitute(title = s)

def generate_main_page_entry(title, profile_container, section_parts) :
    return Template(main_container).substitute(
        title = title,
        profile_container = profile_container,
        section_parts = section_parts
    )

def generate_section_list_item_title(s) :
    ret = ""

    if s["title"] == None :
        return ret

    if s["logo_src"] != None :
        ret += Template(section_list_title_logo).substitute(
            src = s["logo_src"],
            alt = s["logo_alt"]
        )

    if s["title_plain"] == None :
        ret += Template(section_list_title_without_class).substitute(
            content = s["title"],
        )
    else :
        ret += Template(section_list_title_with_screen_class).substitute(
            content = s["title"],
        )
        ret += Template(section_list_title_with_print_class).substitute(
            content = s["title_plain"],
        )     

    if s["period"] != None :
        ret += Template(section_list_title_period).substitute(
            content = s["period"],
        )

    return ret


def generate_section_list_item_content(s) :
    ret = ""

    if s["content_plain"] == None :
        ret += Template(section_list_content_without_class).substitute(
            content = s["content"].replace("\r", "").replace("\n", ""),
        )
    else :
        ret += Template(section_list_content_with_screen_class).substitute(
            content = s["content"].replace("\r", "").replace("\n", ""),
        )
        ret += Template(section_list_content_with_print_class).substitute(
            content = s["content_plain"].replace("\r", "").replace("\n", ""),
        )     

    return ret


def generate_section_list_item(s) :
    return Template(section_list_item).substitute(
            title = generate_section_list_item_title(s),
            content = generate_section_list_item_content(s),
        )

def generate_section_list(s) :
    if len(s) == 0 :
        return '<div class="section-item">Empty</div>'
    else :
        ret = ""
        for i in s :
            ret += generate_section_list_item(i)
        return ret

def generate_section(s) :
    return Template(section_parts_template).substitute(
        title = s["title"],
        section_list = generate_section_list(s["list"]),
    )

def generate_main_page(content) :
    # 标题栏
    main_title = generate_main_title(content["name"])

    main_profile = '<div class="profile-container">'
    for i in content["profile"] :
        main_profile += generate_profile_item(i)
    main_profile += "</div>"

    main_sections = ""
    for i in content["sections"] :
        main_sections += generate_section(i)

    return generate_main_page_entry(main_title, main_profile, main_sections)