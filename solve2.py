

#Question: Write a Python function to reverse the order of words in a given sentence
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

# Test the function
sentence = "Hello world! Python is awesome."
result = reverse_sentence(sentence)
print(result)







class Calculator:
    def add(self, *args):
        return sum(args)

# Create an object
calc = Calculator()

# Call the add method with different numbers of arguments
print(calc.add(2, 3))      # Output: 5
print(calc.add(2, 3, 4))   # Output: 9


#What does len() do?
#len() is an inbuilt function used to calculate the length of sequences like list, python string, and array.

my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)

# How to remove values to a python array?
#Elements can be removed from a python array by using pop() or remove() methods.

#pop(): This function will return the removed element .

#remove():It will not return the removed element
import array

x = array.array('d', [8.1, 2.4, 6.8, 1.1, 7.7, 1.2, 3.6])
print(x.pop())
print(x.pop(3))
x.remove(8.1)
print(x)


