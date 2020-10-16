# Pydagogy
Pydagogy is a Python library for automated code checking in online courses.

Content developers create the tests with hints, solutions, and other messaging. Students import the tests and run them in their exercise code to get feedback.

## Usage

Content developers create tests by subclassing `pydagogy.tests.BaseTest`, or using one of the built-in tests like `ValueTest`. There are assert functions available that automatically print out messages when tests fail. This way you can have multiple checks within a test without breaking execution.

For example, you could create a test that checks for string equality.
```python
import pydagogy as pgy

class MyTest(pgy.tests.BaseTest):
    def check(self, value):
        expected = "example string"
        message =  "Sorry, your result doesn't look correct."
        if pgy.assert_true(value == expected, message):
            self.success

# Create the test and add feedback for students
test_p1 = MyTest()
test_p1.hint = "Example hint text"
test_p1.solution = "Example solution text"
test_p1.success = "Nicely done!"
```

This test is imported into the student exercise code.

```python
from test_file import test_p1

# students do something to generate a string
out_string = some_func()

test_p1.check(out_string)

# Uncomment the line below to see a hint
# test_p1.hint

# Uncomment the line below to see the solution
# test_p1.solution
```

The check function will print out the success message ("Nicely done!" in this example), if the student's string is the same as the expected string. Otherwise, it will print out the fail messsage.

Students can look at the hint and solution if they want, uncommenting those lines will print out the text.

## Dependencies

Python 3.6 because f-strings. Seriously, update to 3.6 just for f-strings. You'll thank me.