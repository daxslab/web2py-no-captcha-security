web2py-thumbnails
=================

No Captcha Security, plugin for the web2py framework to enable bot protection using no-captcha techniques.

Includes a Honeypot implementation and a js generated checkbox


Installation
============

- Download The plugin installer (.w2p file) and install it via the web2py interface.

Usage
=====

The usage is similar to the [Recaptcha functionality](http://web2py.com/books/default/chapter/29/09/access-control#CAPTCHA-and-reCAPTCHA) included in the framework 

```python
# coding: utf8

# Honeypot
# ========

# import Honeypot
from plugin_ncs.ncs import Honeypot

# include in form
form.append(Honeypot())
# it can also be inserted in a any SQLFORM by injection:
# form.element('form').insert(-1, Honeypot())

# JsCheckbox
# ==========

# import JsCheckbox
from plugin_ncs.ncs import JsCheckbox

# include in form
form.append(Honeypot())
# it can also be inserted in a any SQLFORM by injection:
# form.element('form').insert(-1, Honeypot())


```