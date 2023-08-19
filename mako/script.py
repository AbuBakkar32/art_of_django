from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['.'])

mytemplate = Template(filename='person.txt', lookup=mylookup)
print(mytemplate.render())