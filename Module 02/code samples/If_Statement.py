"""
if <conditional>:
      <Statement to be executed if the conditional evaluates to be True>

Here <conditional> can be any condition based on a combination of one or more variables.
The output of this conditional is a boolean expression that evaluates to be either 0 or 1 and based on the
same statement or the set of statements mentioned under this conditional is executed
If this conditional evaluates to be true then the statement is executed else skipped
The colon(:) following the <conditional> is required, else python will throw an error.
"""

# Examples of Conditional Statements in Python

# Example 1
var1 = 1
var2 = 200
if var2 > var1:
    print("var2 is greater than var1")

# Example 2
var1 = 1000
var2 = 200
if var2 > var1:
    print("var2 is greater than var1")

# Example 3
"""
if <conditional>:
     <Statement 1 to be executed if the conditional evaluates to be True>
else:
     <Statement 2 to be executed if the conditional evaluates to be False>

In this case, if the conditional evaluates to be true then statement 1 gets executed, 
else if the conditional evaluates to be false then statement 2 gets executed.

That’s how the else clause works with the if conditional.
"""

var1 = 1000
var2 = 200
if var2 > var1:
    print("var2 is greater than var1")
else:
    print("var1 is greater than var2")

# Example 4
"""
if <conditional 1>:
     <Statement 1 to be executed if the conditional 1 evaluates to be True>
elif <conditional 2>:
     <Statement 2 to be executed if the conditional 2 evaluates to be True and conditional 1 evaluates to be false>
else:
     <Statement 3 to be executed if the conditional evaluates to be conditional 1 and 2 evaluates to be false>

In this case, conditional 1 evaluates to be true then statement 1 gets executed, 
else if conditional 2 evaluates to be true then statement 2 gets executed, else statement 2 gets executed.

That’s how the elif clause works with the if conditional if in case we want to test for multiple conditions.
"""

var1 = 1000
var2 = 1000
if var2 > var1:
    print("var2 is greater than var1")
elif var2 == var1:
    print("var1 is equal to var2")
else:
    print("var1 is greater than var2")

"""
if <conditional 1>: <Statement 1 to be executed if the conditional 1 evaluates to be True>
It is totally permissible to write the statement as well in a single line, moreover,
there can be multiple statements as well aligned to a single conditional as well as mentioned below:
"""
