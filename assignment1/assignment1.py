#Task 1
from os import times


def hello():
    return "Hello!"
print(hello())

#Task 2
def greet(name):
    return f"Hello, {name}!"
print(greet("Sam"))

#Task 3
def calc(value1, value2, operation="multiply"):
    try:
        match operation:
            case "add":
                return value1 + value2
            case "subtract":
                return value1 - value2
            case "multiply":
                return value1 * value2
            case "divide":
                return value1 / value2
            case "modulo":    
                return value1 % value2
            case "int_divide":
                return value1 // value2
            case "power":
                return value1 ** value2
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc(10, 5, "add"))
print(calc(10, 5, "subtract"))
print(calc(10, 5, "multiply"))
print(calc(10, 5, "divide"))
print(calc(10, 5, "modulo"))
print(calc(10, 5, "int_divide"))
print(calc(10, 5, "power"))
print(calc(10, 0, "divide"))

#Task 4
def data_type_conversion(value, type):
    try:
        match type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."

print(data_type_conversion("10", "int"))
print(data_type_conversion("10.5", "float"))
print(data_type_conversion(10, "str"))

#Task 5
def grade(*score):
    try:
        total_score = sum(score)
        average_score = total_score / len(score)
    except Exception:
        return "Invalid data was provided."

    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
        return "C"
    elif average_score >= 60:
        return "D"
    else:
        return "F"
    
print(grade(90, 85, 92))

#Task 6
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

print(repeat("flower", 7))

#Task 7
def student_scores(position, **kwargs):
    try:
       if position == "best":
           best_student = None
           best_score = -1
           for student, score in kwargs.items():
               if score > best_score:
                   best_score = score
                   best_student = student
           return best_student
       elif position == "mean":
           total_score = sum(kwargs.values())
           mean_score = total_score / len(kwargs)
           return mean_score
    except Exception:
        return "Invalid data was provided."
    
print(student_scores("best", Sarah=88, Steve=92, Carla=97))
print(student_scores("mean", Sarah=88, Steve=92, Carla=97))

#Task 8
def titleize(string):
    little_words = [ "a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    result = []
    for i, word in enumerate(words):
        if i == 0:
            result.append(word.capitalize())
        elif i == len(words) - 1:
            result.append(word.capitalize())
        elif word.lower() not in little_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return " ".join(result)

print(titleize("going over the mountains"))
print(titleize("the beauty of the sun"))

#Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

print(hangman("galaxy", "aeiou"))

#Task 10
def pig_latin(string):
    vowels = "aeiou"
    words = string.split()
    result = []
    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            index = 0
            while index < len(word):
                if word[index:index+2] == "qu":
                    index += 2
                elif word[index] in vowels:
                    break
                else:
                    index += 1
            result.append(word[index:] + word[:index] + "ay")
    return " ".join(result)

print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("queen"))