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
</html>
'''

def generate_root(title, main, plain, extra_style) :
    return Template(root_template).substitute(
        title = title,
        main_container = main,
        plain_container = plain,
        extra_style = extra_style
    )