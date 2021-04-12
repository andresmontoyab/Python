# Jinja

Jinja is a modern and designer-friendly templating language for Python.

```html
<title>{% block title %}{% endblock %}</title>
<ul>
{% for user in users %}
  <li><a href="{{ user.url }}">{{ user.username }}</a></li>
{% endfor %}
</ul>
```

- sandboxed execution
- powerful automatic HTML escaping system for XSS prevention
- template inheritance
- compiles down to the optimal python code just in time
- optional ahead-of-time template compilation
- easy to debug. Line numbers of exceptions directly point to the correct line in the template.
- configurable syntax

## Instalation

pip install Jinja2

## Template Designer Documentation

A Jinja template is simply a text file. Jinja can generate any text-based format

A template contains variables and/or expressions, which get replaced with values when a template is rendered

## Template File Extension

As stated above, any file can be loaded as a template, regardless of file extension. Adding a .jinja extension, like user.html.jinja may make it easier for some IDEs or editor plugins, but is not requir