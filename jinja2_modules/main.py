from jinja2 import Environment,PackageLoader
env = Environment(loader=PackageLoader('main','templates'))

template = env.get_template('index.html')
with open('index.html','w')as f:
    f.write(template.render(title='welcome',welcome='Hello jinja2'))