from mathlamp_pocket.repl import REPL
from mathlamp_pocket.lines import CodeRunner

def test_repl():
    console = REPL()
    result = console.runLine("1 + 1")
    assert result == 2
    result = console.runCodeLines("""
    1 + 1
    2 * 2
    """)
    assert 2 in result
    assert 4 in result

def test_runner():
    console = CodeRunner()
    result = console.runCodeLines("""
    1 + 2
    out[1 + 1]
    out[2 * 2]
    """)
    assert 2 in result
    assert 4 in result
    assert 3 not in result