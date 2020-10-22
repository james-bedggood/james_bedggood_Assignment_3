#10 String Fucntions Assignment

#1 Capitalize

def yell_converter (yell_text):

    """convert all lowercase letters to uppercase letters

    Args:
    yell_text= string representing text to be converted into uppercase

    """

    return yell_text.upper()

yell_converter ("i am yelling at you")



#2 Convert to lowercase

def whisper_converter (whisper_text):

    """convert all uppercase letters to lowercase

    Args:
    whisper_text = string representing text to be converted into lowercase

    """
    return whisper_text.lower()

whisper_converter ("REMAIN CALM")

#3 Password Detector

def password_detect (todays_pw):



    pw_result = todays_pw.endswith("key")
    return pw_result

password_detect ("it is key")



#4 Image Sequence formatter

def sequence_formatter (filename, totalframes):

    empty_space = ""

    if totalframes < 10:
        return filename + empty_space.zfill(1)
    if totalframes < 100:
        return filename + empty_space.zfill(2)
    if totalframes < 1000:
        return filename + empty_space.zfill(3)

sequence_formatter ("finalrender", 12)


#5 Lyric total detector

def lyric_counter (word, lyrics):

    """count and return the number a word appears in a given phrase

    Args:
    word = string representing the word to be counted
    lyrics = string representing the phrase/lyrics/sentence to search
    lyric_total = integer representing the total amount the word appears in the lyrics

    """

    lyric_total = lyrics.count(word)

    return "That word appears {} times in the lyrics you have entered".format(lyric_total)


lyric_counter ("na", "na, na, na na, na na, na na, na, na. Hey Jude. na, na, na na, na na, na na, na, na. Hey Jude")

#6 Quietmaker

def quiet_maker (phrase):

    """Return a reponse depending on whether or not a string is all caps

    Args:
    phrase: string representing the text to be tested
    """

    if phrase.isupper() == True:
        return "Please be quiet"
    if phrase.isupper() == False:
        return "Thank you for keeping your voice down"

quiet_maker ("hello")

#7 Binary converter

def binary_convert (number_input):

    """Convert the inputed number to binary format

    Args:
    number_input = number to be converted
    binary result = number after binary conversion to be added to phrase in the return line
    """

    binary_result = bin(number_input)

    return  " This number in binary is {}".format(binary_result)

binary_convert (12)

#8 Name Striker

def name_striker (name_text):

    """Replace chosen names with "------"

    Args:
    name_text = string to be edited
    censor_1 = first name to be removed
    censor_2 = second name to be removed
    """

    censor_1 = name_text.replace ("James", "------")

    censor_2 = censor_1.replace ("Bill", "------")

    #3rd Name edit
    return censor_2.replace ("Fred", "------")

name_striker ("Hello Bill, it's James, did you hear what Fred did?")

#9 Smallest and largest Item Checker

def item_sizes (item_1, item_2, item_3, item_4, item_5):

    """Returns the smallest number in a given list

    Args:
    item_1 - item_5 = number to be checked
    smallest = result of min function, to be used in return line
    biggest = result of max function, to be used in return line
    """

    smallest = min(item_1, item_2, item_3, item_4, item_5)
    biggest = max(item_1, item_2, item_3, item_4, item_5)

    return "The smallest item is {0}, the largest item is {1}".format(smallest, biggest)

item_sizes (3, 45, 5, 12000303, 7)

#10 Title Maker

def title_maker (essay_title):

    """format an essay name into a proper title, capitilizing text, but excluding "is" and "and"

    Args:
    essay_title = the title to be corrected
    corrected_title = first conversion (the first letter of each word into uppercase)
    further correct_1 = replacing "Is' with "is" in the result of essay_title
    further correct_2 = replacing "And' with "and" in the result of further_correct_1, to be used in the return line
    """


    corrected_title = essay_title.title()

    further_correct_1 = corrected_title.replace("Is", "is")
    further_correct_2 = further_correct_1.replace("And", "and")

    return further_correct_2

title_maker ("vegetarianism and you, is giving up meat the right choice?")
