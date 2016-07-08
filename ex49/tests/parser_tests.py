from nose.tools import *
from ex49.parser import *

def test_sentence():
    x = parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(x.subject, 'player')
    assert_equal(x.verb, 'run')
    assert_equal(x.obj, 'north')

def test_exception():
    assert_raises(ParserError, parse_sentence, [('direction', 'north'), ('verb', 'run')])