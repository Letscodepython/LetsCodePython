 # Python Semantics

semantic error, also called a logic error. If there is a semantic error in your program,
it will run successfully in the sense that the computer will not generate any error messages.
However, your program will not do the right thing. It will do something else. Specifically,
it will do what you told it to do, not what you wanted it to do.

The following program has a semantic error. Execute it to see what goes wrong:

![](../../../../../Desktop/Teacher%20Notes/pics/07.png)

This program runs and produces a result. However, the result is not what the programmer intended.
It contains a semantic error. The error is that the program performs concatenation instead of addition,
because the programmer failed to write the code necessary to convert the inputs to integers.

With semantic errors, the problem is that the program you wrote is not the program you wanted to write.
The meaning of the program (its semantics) is wrong. The computer is faithfully carrying out the instructions you wrote,
and its results are correct, given the instructions that you provided.
However, because your instructions have a flaw in their design, the program does not behave as desired.

Identifying semantic errors can be tricky because no error message appears to make it obvious
that the results are incorrect.The only way you can detect semantic errors is if you know in advance
what the program should do for a given set of input.Then, you run the program with that input data and 
compare the output of the program with what you expect.
If there is a discrepancy between the actual output and the expected output,
you can conclude that there is either 1) a semantic error or 2) an error in your expected results.

Once you’ve determined that you have a semantic error,
locating it can be tricky because you must work backward by looking at the output of the program and
trying to figure out what it is doing.
