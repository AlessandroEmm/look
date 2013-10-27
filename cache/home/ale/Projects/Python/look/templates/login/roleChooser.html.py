# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1369564899.6582
_enable_loop = True
_template_filename = '/home/ale/Projects/Python/look/templates/login/roleChooser.html'
_template_uri = '/home/ale/Projects/Python/look/templates/login/roleChooser.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        availableRoles = context.get('availableRoles', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('<!DOCTYPE html>\n<!--[if lt IE 7 ]> <html lang="en" class="ie6 ielt8"> <![endif]-->\n<!--[if IE 7 ]>    <html lang="en" class="ie7 ielt8"> <![endif]-->\n<!--[if IE 8 ]>    <html lang="en" class="ie8"> <![endif]-->\n<!--[if (gte IE 9)|!(IE)]><!--> <html lang="en"> <!--<![endif]-->\n<head>\n<meta charset="utf-8">\n<title>Paper Stack</title>\n<link rel="stylesheet" type="text/css" href="static/login/style/style.css" />\n</head>\n<body>\n<div class="container">\n\t<section id="content">\n\n\n\t\t\t<div style="border-bottom-style:dotted;"><h1>Rollen</h1></div>\n\t\t\n\t\t\t\t')
        # SOURCE LINE 18
        __M_writer(str(availableRoles))
        __M_writer('\n\t\t\n\n\t\n\t</section><!-- content -->\n</div><!-- container -->\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


