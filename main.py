if __name__ == "__main__":
  # Comparing Identity With the Python is and is not Operators

  """
  The Python is and is not operators compare the identity of two objects.
  In CPython, this is their memory address.
  Everything in Python is an object, and each oject is stored at a specific memory location.
  The Python is and is not operators check whether two variables refer to the same object in memory.

  Note: Keep in mind that objects with the same value are usally stored at seperate memory address.

  You can use id() to check the identity of an object.
  """
  print(id(id))

  """
  The last line shows the memory address where the built-in function id itself is stored.

  There are some common cases where objects with the same value will have the same id by default.
  For example, the numbers -5 to 256 are interned in CPython.
  Each number is stored at a singular and fixed place in memory, which saves memory for commonly-used integers.

  You can use sys.intern() to intern strings for performance.
  This function allows you to compare their memory address rather than comparing the strings character-by-character:
  """
  from sys import intern

  a = "hello world"
  b = "hello world"

  print(id(a))
  print(id(b))
  print(a is b) # True

  a = intern(a)
  b = intern(b)
  print(a)
  print(b)
  print(id(a))
  print(id(b))
  print(a is b) # True

  """
  The variables a and b initially point to two different objects in memory, as shown  by their different IDs.
  When you intern them, you ensure that a and b point to the same object in memroy.
  Any new string with the value 'hello world' will now be created at a new memory location,
  but when you intern this new string, you make sure that it points to the same memroy address as the first 'hello world' that you interned

  "Note": Even though the memory address of an object is unique at any given time, it varies between runs of the same code,
  and depends on the version of CPython and the machine on which it runs.

  Other objects that are interned by default are None, True, False and simple strings.
  Keep in mind that most of the time, different objects whith the same valie will be stored at seperate memory address.
  This means you should not use the Python is operator to compare values.
  """

  # When Only Some Integers Are Interned

  """
  Behind the scenes, Python interneds objects with commonly-used values (for example, the integers -5 to 255) to save memory.
  The following bit of code shows you how only some integers have a fixed memory address.
  """

  a = 256
  b = 256
  print(id(a))
  print(id(b))
  print(a is b)

  a = 257
  b = 257
  print(id(a))
  print(id(b))
  print(a is b)

  """
  Initially, a and b point to the same interned object in memory, but when their values are outside the range of common integers (ranging from -5 to 256), they're stored at seperate memory addresses.
  """

  # When Multiple Variables Point to the Same Object

  """
  When you use the assignment operator (=) to make one variable equal to the other, you make these variables point to the same object in memory.
  This may lead to unexpected behavior for multiple objects.
  """

  a = [1, 2, 3]
  b = a
  print(a)
  print(b)

  a.append(4)
  print(a)
  print(b)

  print(id(a))
  print(id(b))

  """
  What just happended? You add a new element to a, but now b contains this element too!
  Well. in the line where b = a, you set b to point to the same memory address as a,
  so that both variables now refer to the same object.

  If you define these lists independently of each other, then they're stored at different memory addresses and behave independently
  """

  a = [1, 2, 3]
  b = [1, 2, 3]
  print(id(a))
  print(id(b))
  print(a is b)

  """
  Because a and b now refer different objects in memory, changing one doesn't affect other.
  """

  # Comparing Equality With the Python == and != Operators

  """
  Recall that objects ưith the same value are often stored at seperate memory address.
  Use the equality operators == and != if you ưant to check whether or not two objects have the same value, regardless of whether they're stored in memory.
  In the vast majority of cases, this is what you want to do.
  """

  # When Object Copy Is Equal But Not Identical

  """
  In the example below, you set b to be a copy of a (which is a mutable obejct, such as a list or dictionary).
  Both variables will have the same value, but each will be stored at a different memory address.
  """

  a = [1, 2, 3]
  b = a.copy()
  print(a)
  print(b)
  print(a == b)
  print(a is b)
  print(id(a))
  print(id(b))

  """
  a and b are now stored at different memory addresses, ao a is b will no longer return True/
  However, a == b returns True because both objects have the same value.
  """

  # How Comparing by Equality Works

  """
  The magic of the quality operator == happens in the __eq__() class method of the object to the left of th sign.

  Note: This is the case unless the object on the right is a subclass of the object on the left.
  For more information, check the official documentation.

  This is a magic class method that's called whenever an instance of this class is compared against another object.
  If this method is not implemented, then == compares the memory address of the two objects by default.

  As an exercise, make a SillyString class that inherits from str and implement __eq()__ to compare whether the length of this string is the same as the length of the other object:
  """

  class SillyString(str):
    # This method gets called when using == on the object
    def __eq__(self, other):
      # Return True if self and other have the same length
      return len(self) == len(other)

  # Compare two strings
  print('hello world' == 'world hello')

  # Compare a string with a SillyString
  print('hello world' == SillyString('world hello'))

  # Compare a Silly String with a list
  print(SillyString('hello world') == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

  """
  This is, of course, silly behavior for an object that otherwise behaves as a string, but it does illustrate what happens when you compare two objects using ==.
  The != operator gives the inverse response of this unless a specific __ne__() class method is implemented.

  The example above also clearly shows you why it is good practice to use the Python is operator for comparing with None, instead of the == operator.
  Not only it is faster since it compare memory address, but it's also safer because it doesn't depend on the logic of an __eq__() class methods.
  """

  # Comparing the Python Comparision Operators

  """
  As a rule of thumb, you should always use the equality operators == and !=, except when you're comparing None:

  - Use the Python == and != operators to compare object equality.
  Here, you're generally comparing the value of two objects.
  This is you need if you want to compare whether or not two objects have the same contents, and you don't care about where they're stored in memory.

  - Use the Python is and is not operators when you want to compare object identity.
  Here, you're comparing whether or not two variables point to the same object in memory.
  The main use case for these operators is when you're comparing to None/
  It's faster and safer to compare to None by the memory address that it is by using class methods.

  Variables with the same value are often stored at separate memory addresses.
  This means that you should use == and != to compare their values and use the Python is and is not operators only when you want to check whether two variables point to the same memory address.
  """

  # Conclusion

  """
  In this tutorial, you've learned that == and != compare the value of two objects. whereas the Python is and is not opereators compare whether two variables refer to the same object in  memory.
  If you keep this distinction in mind, then you should be able to prevent unexpected behavior in your code.

  If you want to read more about wonderful world of object interning and the Python is operator, then checkout Why you should almost never use "is" in Python.
  You could also have a look at how you can use sys.intern() to optimize memory usage and comparison times for strings, although the chances are that Python already automatically handles this for you behind-the-scenes.

  Now that you've learned what the equality and idenntity operators do under the hood, you can try writing your own __eq__() class methods, which define how instances of this class are cp,[ared when using the == operator.
  Go and apply youw newfound knowledge of these Python comparision operators.
  """
