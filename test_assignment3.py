from Assignment3 import *


def test_yell_converter():
    """Test the yell_converter function"""
    result = yell_converter ("i am yelling at you")
    expected = "I AM YELLING AT YOU"
    assert (expected == result)

def test_whisper_converter():
    """test the result of the whisper_converter function"""
    result = whisper_converter ("REMAIN CALM")
    expected = ("remain calm")
    assert (expected == result)

def test_password_detect():
    """test the result of password_detect"""
    result = password_detect ("it is key")
    expected = True
    assert (expected == result)

def test_sequence_formatter():
    """test the result of the sequence_formatter function"""
    result = sequence_formatter("finalrender", 12)
    expected = 'finalrender00'
    assert (expected == result)

def test_lyric_counter():
    """test the result of the lyric_counter function"""
    result = lyric_counter ("na", "na, na, na na, na na, na na, na, na. Hey Jude. na, na, na na, na na, na na, na, na. Hey Jude")
    expected = 'That word appears 20 times in the lyrics you have entered'
    assert (expected == result)

def test_quiet_maker():
    """test the result of the quiet_maker function"""
    result = quiet_maker("hello")
    expected = 'Thank you for keeping your voice down'
    assert (expected == result)

def test_binary_convert():
    """test the result of the binary_convert function"""
    result = binary_convert (12)
    expected = ' This number in binary is 0b1100'
    assert (expected == result)

def test_name_striker():
    """test the result of the name_striker function"""
    result = name_striker ("Hello Bill, it's James, did you hear what Fred did?")
    expected = "Hello ------, it's ------, did you hear what ------ did?"
    assert (expected == result)

def test_item_sizes():
    """test the result of the item_sizes function"""
    result = item_sizes (3, 45, 5, 12000303, 7)
    expected = 'The smallest item is 3, the largest item is 12000303'
    assert (expected == result)

def test_title_maker():
    """test the result of the title_maker function"""
    result = title_maker ("vegetarianism and you, is giving up meat the right choice?")
    expected = 'Vegetarianism and You, is Giving Up Meat The Right Choice?'
    assert (expected == result)

