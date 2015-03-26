# -*- coding: utf-8 -*-
"""
DISCOS extension for Sphinx
Author: Marco Buttu <mbuttu@oa-cagliari.inaf.it>
"""

import re

from pygments.lexer import Lexer, RegexLexer, bygroups, include
from pygments.style import Style
from pygments.token import Punctuation, Text, Comment, Operator, \
                           Keyword, Name, String, Number, Generic


class DISCOSStyle(Style):
    default_style = ""
    styles = {
        Generic.Prompt: 'bold #0033ff',
        Generic.Output: '#006600',
        Generic.Error: '#8F0000',
    }


class DISCOSLexer(RegexLexer):

    name = 'discos'
    aliases = ['discos']
    filenames = ['*.discos']

    tokens = {
        'root': [
            include('basic'),
            (r'`', String.Backtick, 'backticks'),
            include('data'),
            include('interp'),
        ],
        'interp': [
            (r'\$\(\(', Keyword, 'math'),
            (r'\$\(', Keyword, 'paren'),
            (r'\$\{#?', String.Interpol, 'curly'),
            (r'\$#?(\w+|.)', Name.Variable),
        ],
        'basic': [
            (r'\b(derotatorSetup|derotatorGetActualSetup|'
             r'derotatorSetConfiguration|derotatorGetConfiguration|'
             r'derotatorIsReady|'
             r'derotatorSetRewindingMode|derotatorGetRewindingMode|'
             r'derotatorSetPosition|derotatorGetPosition)(\s*)\b',
             bygroups(Keyword, Text)),
            (r'\b(getTpi|setAttenuation|'
             r'tsys)\s*\b(?!\.)',
             Name.Builtin),
            (r'#.*\n', Comment),
            (r'\\[\w\W]', String.Escape),
            (r'(\b\w+)(\s*)(=)', bygroups(Name.Variable, Text, Operator)),
            (r'[\[\]{}()=]', Operator),
            (r'<<<', Operator),  # here-string
            (r'<<-?\s*(\'?)\\?(\w+)[\w\W]+?\2', String),
            (r'&&|\|\|', Operator),
            (r'^>', Generic.Prompt), 
            (r'^Error -.*\n', Generic.Error),
            (r'^[^"].*', Generic.Output),
        ],
        'data': [
            (r'(?s)\$?"(\\\\|\\[0-7]+|\\.|[^"\\$])*"', String.Double),
            (r'"', String.Double, 'string'),
            (r"(?s)\$'(\\\\|\\[0-7]+|\\.|[^'\\])*'", String.Single),
            (r"(?s)'.*?'", String.Single),
            (r';', Punctuation),
            (r'&', Punctuation),
            (r'\|', Punctuation),
            (r'\s+', Text),
            (r'\d+(?= |\Z)', Number),
            (r'[^=\s\[\]{}()$"\'`\\<&|;]+', Text),
            (r'<', Text),
        ],
        'string': [
            (r'"', String.Double, '#pop'),
            (r'(?s)(\\\\|\\[0-7]+|\\.|[^"\\$])+', String.Double),
            include('interp'),
        ],
        'curly': [
            (r'\}', String.Interpol, '#pop'),
            (r':-', Keyword),
            (r'\w+', Name.Variable),
            (r'[^}:"\'`$\\]+', Punctuation),
            (r':', Punctuation),
            include('root'),
        ],
        'paren': [
            (r'\)', Keyword, '#pop'),
            include('root'),
        ],
        'math': [
            (r'\)\)', Keyword, '#pop'),
            (r'[-+*/%^|&]|\*\*|\|\|', Operator),
            (r'\d+#\d+', Number),
            (r'\d+#(?! )', Number),
            (r'\d+', Number),
            include('root'),
        ],
        'backticks': [
            (r'`', String.Backtick, '#pop'),
            include('root'),
        ],
    }

def setup(sphinx):
    sphinx.add_lexer("discos", DISCOSLexer())
