# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1369564899.559977
_enable_loop = True
_template_filename = '/home/ale/Projects/Python/look/templates/login/forwarder.html'
_template_uri = '/home/ale/Projects/Python/look/templates/login/forwarder.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('<html><head> <meta http-equiv="refresh" content="0; URL=')
        __M_writer(str(url))
        __M_writer('"></head></html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


