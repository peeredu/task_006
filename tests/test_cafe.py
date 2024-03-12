from subprocess import run, PIPE
import pytest

B_FILE_PATH = './bin/cafe'

def test_cafe_1():
    result = run([B_FILE_PATH], input='ORDER pizza 500 beer 200 BAR KITCHEN', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == 'beer\npizza\n'

def test_cafe_2():
    result = run([B_FILE_PATH], input='ORDER pizza 500 beer 200 ORDER soup 300 cola 100 BAR BAR', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == 'beer\ncola\n'

def test_cafe_3():
    result = run([B_FILE_PATH], input='ORDER pizza 500 beer 200 KITCHEN STATS', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == 'pizza\nKITCHEN 1 500\nBAR 0 0\n'

def test_cafe_4():
    result = run([B_FILE_PATH], input='STATS', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == 'KITCHEN 0 0\nBAR 0 0\n'

def test_cafe_5():
    result = run([B_FILE_PATH], input='CHECKOUT', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == 'UNKNOWN COMMAND\n'

if __name__ == "__main__":
    pytest.main()