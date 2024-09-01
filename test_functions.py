from functions import extract_github_details, read_text_file, fetch_github_repo_contents
import pytest

# Working links

test1 = 'https://github.com/BiggestChris/CS50P-Final-Project-V1'
test2 = 'https://github.com/JoshuaHardyAquinas/InversityCrownEstate'
test3 = 'https://github.com/BiggestChris/Companies-House-Unlock.git'

def test_extraction():
    assert extract_github_details(test1) == ('BiggestChris', 'CS50P-Final-Project-V1')
    assert extract_github_details(test2) == ('JoshuaHardyAquinas', 'InversityCrownEstate')
    assert extract_github_details(test3) == ('BiggestChris', 'Companies-House-Unlock')


# Incorrect links

test4 = 'https://github.com/BiggestChris/Companies-House-Unlock/blob/main/functions.py'
test5 = 'https://github.com/BiggestChris/AI-survey-V1/tree/main/templates'
test6 = 'https://github.com/BiggestChris/AI-survey-V1/blob/main/README.md'
test7 = 'https://github.com/BiggestChris/AI-survey-V1/blob/main/.gitattributes'

def test_wrong_link():
    with pytest.raises(ValueError):
        extract_github_details(test4)
        extract_github_details(test5)
        extract_github_details(test6)
        extract_github_details(test7)


# Not GitHub links

test8 = 'https://www.amazon.co.uk/'
test9 = 'https://inversity.co/'
test10 = 'https://www.bbc.co.uk/'

def test_wrong_link():
    with pytest.raises(ValueError):
        extract_github_details(test8)
        extract_github_details(test9)
        extract_github_details(test10)


# Reading txt files

def test_read_text_file():
    read_text_file('./generic.txt') == 'This is a test'

def test_bad_link():
    with pytest.raises(ValueError):
        read_text_file('lemon')
        read_text_file('./app.py')
        read_text_file('./README.md')


# Testing incorrect input into GitHub API

def test_github_API():
    with pytest.raises(Exception):
        fetch_github_repo_contents('lemon','lemon')
        fetch_github_repo_contents('pizza','pepperoni')
        fetch_github_repo_contents(1, 2)