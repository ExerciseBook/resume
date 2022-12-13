from string import Template

root_template = '''
<html>
    <header>
        <title>${title}</title>
        <link rel="stylesheet" type="text/css" href="style/common.css">
        ${extra_style}
    </header>
    
    <body>
        ${main_container}
        ${plain_container}
    </body>

    <script>
        (() => {
            const present = new Intl.DateTimeFormat('${locale}',{month:'2-digit', year:'numeric'}).format(new Date())
            for (let item of document.getElementsByClassName("section-list-title-period")) { item.innerText = item.innerText.replace("{PRESENT}", present) }
            for (let item of document.getElementsByClassName("plain-container")) { item.innerText = item.innerText.replace("{PRESENT}", present) }
        })()
    </script>
</html>
'''

def generate_root(title, main, plain, extra_style, locale) :
    return Template(root_template).substitute(
        title = title,
        main_container = main,
        plain_container = plain,
        extra_style = extra_style,
        locale = locale,
    )