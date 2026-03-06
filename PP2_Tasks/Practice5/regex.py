#1.Match 'a' followed by zero or more 'b's
import re

def match_a_followed_by_bs(text):
    pattern = r'ab*'
    if re.fullmatch(pattern, text):
        print(f"'{text}' matches")
    else:
        print(f"'{text}' does not match")

# Test
match_a_followed_by_bs("a")      # Match
match_a_followed_by_bs("ab")     # Match
match_a_followed_by_bs("abb")    # Match
match_a_followed_by_bs("abbb")   # Match
match_a_followed_by_bs("b")      # No match
match_a_followed_by_bs("abc")    # No match

#2.Match 'a' followed by two to three 'b's
import re

def match_a_followed_by_2to3_bs(text):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, text):
        print(f"'{text}' matches")
    else:
        print(f"'{text}' does not match")

# Test
match_a_followed_by_2to3_bs("abb")     # Match
match_a_followed_by_2to3_bs("abbb")    # Match
match_a_followed_by_2to3_bs("a")       # No match
match_a_followed_by_2to3_bs("ab")      # No match
match_a_followed_by_2to3_bs("abbbb")   # No match

#3.Find sequences of lowercase letters joined with underscore
import re

def find_lowercase_underscore(text):
    pattern = r'\b[a-z]+_[a-z]+\b'
    matches = re.findall(pattern, text)
    return matches

# Test
text = "hello_world test_example python_program and another_example_here"
result = find_lowercase_underscore(text)
print("Matches:", result)

#4.Find sequences of one upper case letter followed by lower case letters
import re

def find_upper_followed_by_lower(text):
    pattern = r'\b[A-Z][a-z]+\b'
    matches = re.findall(pattern, text)
    return matches

# Test
text = "Hello World Python Programming and JAVA C++"
result = find_upper_followed_by_lower(text)
print("Matches:", result)

#5. Match 'a' followed by anything, ending in 'b'
import re

def match_a_anything_b(text):
    pattern = r'^a.*b$'
    if re.match(pattern, text):
        print(f"'{text}' matches")
    else:
        print(f"'{text}' does not match")

# Test
match_a_anything_b("ab")           # Match
match_a_anything_b("a123b")        # Match
match_a_anything_b("aXYZb")        # Match
match_a_anything_b("acb")          # Match
match_a_anything_b("b")            # No match
match_a_anything_b("abc")          # No match (doesn't end with b)

#6. Replace space, comma, or dot with colon
import re

def replace_with_colon(text):
    pattern = r'[ ,.]'
    result = re.sub(pattern, ':', text)
    return result

# Test
text = "Hello, world. How are you today?"
result = replace_with_colon(text)
print("Original:", text)
print("Replaced:", result)

#7. Convert snake case to camel case
import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    # Capitalize first letter of each component except the first
    camel_str = components[0] + ''.join(x.title() for x in components[1:])
    return camel_str

# Test
snake_strings = ["hello_world", "python_programming", "convert_snake_to_camel"]
for s in snake_strings:
    print(f"{s} -> {snake_to_camel(s)}")

#8. Split a string at uppercase letters
import re

def split_at_uppercase(text):
    # Split at uppercase letters, keep the uppercase letters
    parts = re.findall(r'[A-Z][a-z]*', text)
    return parts

# Test
text = "HelloWorldPythonProgramming"
result = split_at_uppercase(text)
print(f"Original: {text}")
print(f"Split: {result}")
print(f"Joined with spaces: {' '.join(result)}")

#9. Insert spaces between words starting with capital letters
import re

def insert_spaces(text):
    # Insert space before each capital letter (except the first)
    result = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return result

# Test
texts = ["HelloWorld", "PythonProgramming", "CamelCaseExample"]
for t in texts:
    print(f"{t} -> {insert_spaces(t)}")

#10. Convert camel case to snake case
import re

def camel_to_snake(camel_str):
    # Insert underscore before each capital letter and convert to lowercase
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str

# Test
camel_strings = ["helloWorld", "pythonProgramming", "camelCaseExample"]
for s in camel_strings:
    print(f"{s} -> {camel_to_snake(s)}")