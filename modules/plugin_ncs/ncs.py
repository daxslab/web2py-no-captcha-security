__author__ = 'cccaballero'

from gluon import *


class Honeypot(DIV):

    def __init__(self,
                 input_id='honney-input',
                 input_name='honney-description',
                 input_label='Keep this field blank',
                 div_id='plugin_honney_div',
                 hide_with_css=True,
                 hide_with_js=False,
                 ):
        self.attributes = {}
        self.components = []
        self.input_id = input_id
        self.input_name = input_name
        self.input_label = input_label
        self.div_id = div_id
        self.hide_with_css = hide_with_css
        self.hide_with_js = hide_with_js

    def _validate(self):
        if current.request.post_vars[self.input_name]:
            return False
        else:
            return True

    def xml(self):
        div_elements = []

        if self.hide_with_css:
            div_elements.append(STYLE("""
                #%s {
                    display: none;
                }
            """ % self.div_id))

        if self.hide_with_js:
            div_elements.append(SCRIPT("""
                $(document).ready(function(){
                    $('#%s').hide();
                });
            """ % self.div_id))

        div_elements.append(LABEL(
            self.input_label,
            _for=self.input_name,
        ))

        div_elements.append(INPUT(
                _id=self.input_id,
                _name=self.input_name
            ))

        honey_container = DIV(
            *div_elements,
            _id=self.div_id
        )
        return XML(honey_container).xml()


class JsCheckbox(DIV):

    def __init__(self,
                 input_id='checkbox-input',
                 input_name='checkbox-form',
                 div_id='plugin_checkbox_div',
                 label='Click if you are a human'):
        self.attributes = {}
        self.components = []
        self.input_id = input_id
        self.input_name = input_name
        self.div_id = div_id
        self.label=label

    def _validate(self):
        if current.request.post_vars[self.input_name]:
            return True
        else:
            return False

    def xml(self):
        honney_container = DIV(
            SCRIPT("""
                $(document).ready(function(){{
                    addCheckbox();

                    var form = $('#{input_id}').closest('form');
                    var submit_button = $('#{input_id}').closest('form').find(':submit');
                    submit_button.prop('disabled', true);

                    $('#{input_id}').change(function() {{
                        if($(this).is(":checked")) {{
                            submit_button.prop('disabled', false);
                        }} else {{
                            submit_button.prop('disabled', true);
                        }}
                    }});

                }});

                function addCheckbox() {{
                   var container = $('#{container_id}');
                   var inputs = container.find('input');

                   container.append($('<label />', {{ 'for': '{input_id}', text: '{label}:' }}));
                   container.append($('<input />', {{ type: 'checkbox', id: '{input_id}', name: '{input_name}' }}));

                }}
            """.format(
                input_name=self.input_name,
                container_id=self.div_id,
                label=self.label,
                input_id= self.input_id,
            )),
            _id=self.div_id
        )
        return XML(honney_container).xml()