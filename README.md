#### Assignment 6
# Function Smorgasbord
The purpose of this assignment is twofold:
1. Practice the basics of writing functions in python.
2. Use an AI helper tool <a href="https://chat.chattr.io/chat/python-c/" target="_blank">(link here)</a> and provide feedback <a href="https://byu.az1.qualtrics.com/jfe/form/SV_eEcGxB3rbXUK9ds" target="_blank">(link here)</a>.

This assignment is a little different to past assignments in that you’ll be making several unrelated functions, rather than a single unified program. You will put your code in the `a6_function_smorgasbord.py` and the `a6_my_functions.py` files. Do not edit or delete any other files.

Additionally, to get full credit, you need to use the AI Assistant Chatbot at least once while you complete this assignment, but we recommend using it for the whole assignment (even if you normally wouldn’t) just so you can provide good feedback on how it did or didn’t help you. Use it however you want to complete the assignment. <a href="https://chat.chattr.io/chat/python-c/" target="_blank">Click here to access the AI Assistant Chatbot</a>. 

Additionally, we are doing a research project on how the AI Assistant Chatbot impacted you as you did your assignment. While it is not required and won't impact your grade either way, we STRONGLY encourage you to take the 2-3 minute survey after you complete the assignment. <a href="https://byu.az1.qualtrics.com/jfe/form/SV_eEcGxB3rbXUK9ds" target="_blank">Click here to access the survey.</a> It will help the IS department know how to best use AI in this and future courses.

## Logical Flow:
You must create 9 different functions (most of them unrelated). I provide the function names below using snake_case, but the automated tests will still work if you use camelCase or PascalCase. So if the instructions say to make an `example_function` function, you could name it either `example_function`, `exampleFunction`, or `ExampleFunction`, any of the three would work. But calling it something entirely different, like `my_function` will not work.

You’ll be writing out 9 separate functions, and call each of them. To practice putting code in separate modules, most of the functions will be defined in the `a6_my_functions.py` file, but will be called in the `a6_function_smorgasbord.py` file. Pay attention to the number of parameters and what the functions should return. Remember that when you write out the function you use def, and then the name of the function. When you “call” the function, you just use the name of the function followed by parentheses (and any arguments).

Remember to use the AI Assistant, linked above!

### Function 1: welcome_message

- *location*:
    - Keep this one in `a6_function_smorgasbord.py` just to show you can define and call a function in the same .py module.
- *purpose*:
    - print out a simple message with a person’s name.
- *parameters*:
    - `name`:
        - a string containing a name.
- *logic and return values*
    - the function should take the name parameter and insert it into this message and print it:
        - `Hello <name>, welcome to IS 303!`
    - For example, if I provided “Jacob” as the argument, it should print:
        - `Hello Jacob, welcome to IS 303!`
    - The function should not return anything
- *calling the function*
    - In `a6_function_smorgasbord.py`, call `welcome_message` with `“Diego”` as an argument, and then call it again with `“Mai”` as an argument.

### Function 2: sum_two_numbers
- *location*:
    - For this and all the following functions, define them in the file: `a6_my_functions.py`. Then make sure you import `a6_my_functions.py` into `a6_function_smorgasbord.py` so you can call the functions from `a6_function_smorgasbord.py`.
- *purpose*:
    - adds together 2 numbers and returns the result.
- *parameters*:
    - `a`:
        - a number (could be integer or float)
    - `b`
        - another number (could be integer or float)
- *logic and return values*
    - add `a` and `b` together and return the sum
- *calling the function*
    - In `a6_function_smorgasbord.py`, call `sum_two_numbers` with 5 and 7 as arguments, and then make another call with 1000.5 and -30 as arguments. Print out the result of each call.
    
### Function 3: is_even
- *location*:
    - `a6_my_functions.py`
- *purpose*:
    - tells you whether an integer is even or odd.
- *parameters*:
    - `num`:
        - an integer.
- *logic and return values*:
    - should return `True` if the number is even or `False` if the number is odd.
- *calling the function*:
    - In `a6_function_smorgasbord.py`, call the function with the number 7 and print out the result. Then call it again with the number 120 and print the result.

### Function 4: get_number_parity
- *location*:
    - `a6_my_functions.py`
- *purpose*:
    - returns a message telling you whether an integer is even or odd. Uses the `is_even` function you already wrote
- *parameters*:
    - `num`:
        - an integer.
- *logic and return values*:
    - You need to call `is_even` from within `get_number_parity`. It should return `<number> is even.` if the number is even or `<number> is odd.` if the number is odd.
- *calling the function*:
    - In `a6_function_smorgasbord.py`, call the function with 5 as the argument and print out the result. Then call it again with the number 10 and print the result.

### Function 5: fahrenheit_to_celsius
- *location*:
    - `a6_my_functions.py`
- *purpose*:
    - converts a temperature in Fahrenheit to Celsius.
- *parameters*:
    - `fahrenheit`:
        - an integer or float expressing a temperature in Fahrenheit.
- *logic and return values*:
    - The function should take the `fahrenheit` parameter and convert it to Celsius using this formula:
        - `°C = (°F - 32) * (5/9)`
    - Then return the Celsius value.
- *calling the function*:
    - In `a6_function_smorgasbord.py`, call the function with 32 as the argument and print out the returned value. Then call it with 75 as the argument and print out the returned value.

### Function 6: min_max_mean
- *location*:
    - `a6_my_functions.py`
- *purpose*:
    - shows the smallest number, biggest number, and mean when given a list of numbers.
- *parameters*:
    - `numbers_list`:
        - a list that contains only integers or floats.
- *logic and return values*:
    - The function should return a list that has the lowest number in the first position, the highest number in the second position, and the mean of all numbers in the third position.
        - `[<lowest number>, <highest number>, <mean>]`
- *calling the function*:
    - In `a6_function_smorgasbord.py`, call the function using the list below as an argument, and print out the result:
        - `numbers_list_1 = [20, 45, 23, 2, 87, 3]`

### Function 7: dog_message
- *location*:
    - `a6_my_functions.py`
- *purpose*:
    - returns a message about a dog and its age.
- *parameters*:
    - `name`:
        - a string representing a dog’s name.
    - `age`:
        - an integer representing a dog’s age. It should have a default value of 0.
- *logic and return values*:
    - The function should return a string that includes the parameters for the dog’s `name` and `age`. Make sure the `age` displays as 0 if no argument for `age` is provided.
        - `I am a dog named <name> and I'm <age> years old!`
- *calling the function*:
    - In `a6_function_smorgasbord.py`, call the function twice, once using "Spot" for the `name` and 7 for the `age`, and another time using just "Peppy" for the `name`. Print out the returned values.

### Function 8: classify_age
- *location*:
    - `a6_my_functions.py`
- *purpose*:
    - returns a string that classifies an age into one of 3 groups.
- *parameters*:
    - `age`:
        - an integer representing a person’s age.
    - `senior_age`:
        - an integer representing the age at which someone is considered a “Senior”. It should have a default value of 65.
- *logic and return values*:
    - The function should reference the `age` provided and return a string based on how old the person is.
        - If the `age` is below 18, it should return the string `Minor`.
        - If `age` is below the `senior_age`, it should return the string `Adult`.
        - If the `age` is equal to or above the `senior_age`, it should return the string `Senior`.
- *calling the function*:
    - In `a6_function_smorgasbord.py`, call the function twice, once using 60 for the `age` and 55 for the `senior_age`. Call the function another time using just 62 for the `age`. Print out the returned values.

### Function 9: calculate_total
- *location*:
    - `a6_my_functions.py`
- *purpose*:
    - Calculates the total amount paid for a quantity of a product based on the quantity being bought, the discount percent, and whether a bonus discount is applied.
- *parameters*:
    - `price`:
        - a number representing the price of a single product.
    - `quantity`:
        - an integer representing how many units of the product are being purchased.
    - `discount_percent`:
        - a percent expressed as a decimal (float). Represents the base discount that will be applied. For example, a 10% discount would be `.1`
    - `threshold_total`:
        - The threshold for the total price (`price * quantity`) that needs to be passed for the `bonus_discount` to be applied. The default value should be 100.
    - `bonus_discount`:
        - a percent expressed as a decimal (float). Represents the discount that will be added to the `discount_percent` if the `threshold_total` is met. The default value should be 0.02.
- *logic and return values*:
    - The function should calculate the total price (`price * quantity`), and depending on the total price, the discount applied will be different. 
    - If the total price is equal to or below the `threshold_total`, then the discount applied would just be the `discount_percent`.
    - If the total price is above the `threshold_total`, then the applied discount should be the `discount_percent + bonus_discount`.
    - Return the total price, rounded to the second decimal, after the discount is applied.
    - You can reference the table below for example inputs and outputs. In the first row, the bonus_discount is not applied since it doesn’t reach the threshold_total, but in the second row, the bonus_discount is applied since the price*quantity is over 100.
    - | **Price** | **Quantity** | **Discount_percent** | **Threshold_total** | **Bonus_discount** | **Returned value** |
        |-----------|--------------|----------------------|---------------------|--------------------|--------------------|
        | 5         | 15           | 0.1                  | 100                 | 0.02               | 67.5               |
        | 5         | 25           | 0.1                  | 100                 | 0.02               | 110.0                |
- *calling the function*:
    - In `a6_function_smorgasbord.py`, write a loop that runs 2 times. In each iteration, ask the user to input:
        - a `price`:
            - `Enter the price for the product purchased: `
        - a `quantity`
            - `Enter the quantity of the product purchased: `
        - a `discount_percent`
            - `Enter the discount percent (formatted as a decimal): `
    - Then call the function using the `price`, `quantity`, and `discount_percent` gathered and print out a message using the returned value that shows the total:
        - `The total price after discounts is: $<total price returned from calculate_total>`

Push your code up to your GitHub repository to receive credit. If you pass all the automated tests you will receive full credit. Remember to consider leaving feedback on the AI Assistant by <a href="https://byu.az1.qualtrics.com/jfe/form/SV_eEcGxB3rbXUK9ds" target="_blank">clicking here.</a>

## Example Output

```
Hello Diego, welcome to IS 303!
Hello Mai, welcome to IS 303!
12
970.5
False
True
5 is odd.
10 is even.
0.0
23.88888888888889
[2, 87, 30.0]
I am a dog named Spot and I'm 7 years old!
I am a dog named Peppy and I'm 0 years old!
Senior
Adult
Enter the price for the product purchased: 5
Enter the quantity of the product purchased: 15
Enter the discount percent (formatted as a decimal): .1
The total price after discounts is: $67.5
Enter the price for the product purchased: 5
Enter the quantity of the product purchased: 25
Enter the discount percent (formatted as a decimal): .1
The total price after discounts is: $110.0
```

## Rubric
This assignment contains the automated tests listed below. The tests will ignore spacing, capitalization, and punctuation, but you will fail the tests if you spell something wrong or calculate something incorrectly.

After this table, see the Test Cases table below to see what inputs will be run for each of the tests below. To receive points for a test, the test must pass each of the individual test cases.

<table border="1" style="width: 100%; text-align: center;">
<thead style="text-align: center;">
    <tr>
        <th style="text-align: center;">Test</th>
        <th style="text-align: center;">Test Cases Used </th>
        <th style="text-align: center;">Description</th>
        <th style="text-align: center;">Points</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>1. welcome message</td>
        <td>1</td>
        <td>
            <table border="1" style="width: 100%; text-align: center;">
                    <thead>
                            <tr>
                                    <th style="text-align: center;">Arguments</th>
                                    <th style="text-align: center;">Return Values</th>
                            </tr>
                    </thead>
                    <tbody>
                            <tr>
                                    <td><code>Diego</code></td>
                                    <td><code>None</code></td>
                            </tr>
                            <tr>
                                    <td><code>Mai</code></td>
                                    <td><code>None</code></td>
                            </tr>
                    </tbody>
            </table>
        </td>
        <td>5</td>
    </tr>
        <tr>
        <td>2. sum two numbers</td>
        <td>1</td>
        <td>
            <table border="1" style="width: 100%; text-align: center;">
                    <thead>
                            <tr>
                                    <th style="text-align: center;">Arguments</th>
                                    <th style="text-align: center;">Return Values</th>
                            </tr>
                    </thead>
                    <tbody>
                            <tr>
                                    <td><code>1, 1</code></td>
                                    <td><code>2</code></td>
                            </tr>
                            <tr>
                                    <td><code>-3, 7</code></td>
                                    <td><code>4</code></td>
                            </tr>
                            <tr>
                                    <td><code>2000, 42</code></td>
                                    <td><code>2042</code></td>
                            </tr>
                    </tbody>
            </table>
        </td>
        <td>5</td>
    </tr>
    <tr>
        <td>3. is even</td>
        <td>1</td>
        <td>
            <table border="1" style="width: 100%; text-align: center;">
                    <thead>
                            <tr>
                                    <th style="text-align: center;">Arguments</th>
                                    <th style="text-align: center;">Return Values</th>
                            </tr>
                    </thead>
                    <tbody>
                            <tr>
                                    <td><code>1</code></td>
                                    <td><code>False</code></td>
                            </tr>
                            <tr>
                                    <td><code>-3</code></td>
                                    <td><code>False</code></td>
                            </tr>
                            <tr>
                                    <td><code>64</code></td>
                                    <td><code>True</code></td>
                            </tr>
                    </tbody>
            </table>
        </td>
        <td>5</td>
    </tr>
    <tr>
        <td>4. get number parity</td>
        <td>1</td>
        <td>
            <table border="1" style="width: 100%; text-align: center;">
                    <thead>
                            <tr>
                                    <th style="text-align: center;">Arguments</th>
                                    <th style="text-align: center;">Return Values</th>
                            </tr>
                    </thead>
                    <tbody>
                            <tr>
                                    <td><code>1</code></td>
                                    <td><code>1 is odd.</code></td>
                            </tr>
                            <tr>
                                    <td><code>-3</code></td>
                                    <td><code>-3 is odd.</code></td>
                            </tr>
                            <tr>
                                    <td><code>64</code></td>
                                    <td><code>64 is even.</code></td>
                            </tr>
                    </tbody>
            </table>
        </td>
        <td>10</td>
    </tr>
    <tr>
        <td>5. fahrenheit to celsius</td>
        <td>1</td>
        <td>
            <table border="1" style="width: 100%; text-align: center;">
                    <thead>
                            <tr>
                                    <th style="text-align: center;">Arguments</th>
                                    <th style="text-align: center;">Return Values</th>
                            </tr>
                    </thead>
                    <tbody>
                            <tr>
                                    <td><code>32</code></td>
                                    <td><code>0</code></td>
                            </tr>
                            <tr>
                                    <td><code>122</code></td>
                                    <td><code>50</code></td>
                            </tr>
                            <tr>
                                    <td><code>-13</code></td>
                                    <td><code>-25</code></td>
                            </tr>
                    </tbody>
            </table>
        </td>
        <td>10</td>
    </tr>
    <tr>
        <td>6. min max mean</td>
        <td>1</td>
        <td>
            <table border="1" style="width: 100%; text-align: center;">
                    <thead>
                            <tr>
                                    <th style="text-align: center;">Arguments</th>
                                    <th style="text-align: center;">Return Values</th>
                            </tr>
                    </thead>
                    <tbody>
                            <tr>
                                    <td><code>[1, 2, 3]</code></td>
                                    <td><code>[1, 3, 2.0]</code></td>
                            </tr>
                            <tr>
                                    <td><code>[354, 87, -7, 92, 34]</code></td>
                                    <td><code>[-7, 354, 112.0]</code></td>
                            </tr>
                    </tbody>
            </table>
        </td>
        <td>10</td>
    </tr>
    <tr>
        <td>7. dog message</td>
        <td>1</td>
        <td>
            <table border="1" style="width: 100%; text-align: center;">
                    <thead>
                            <tr>
                                    <th style="text-align: center;">Arguments</th>
                                    <th style="text-align: center;">Return Values</th>
                            </tr>
                    </thead>
                    <tbody>
                            <tr>
                                    <td><code>Jet</code></td>
                                    <td><code>I am a dog named Jet and I'm 0 years old!</code></td>
                            </tr>
                            <tr>
                                    <td><code>Poof, 92</code></td>
                                    <td><code>I am a dog named Poof and I'm 92 years old!</code></td>
                            </tr>
                    </tbody>
            </table>
        </td>
        <td>10</td>
    </tr>
    <tr>
        <td>8. classify age</td>
        <td>1</td>
        <td>
            <table border="1" style="width: 100%; text-align: center;">
                    <thead>
                            <tr>
                                    <th style="text-align: center;">Arguments</th>
                                    <th style="text-align: center;">Return Values</th>
                            </tr>
                    </thead>
                    <tbody>
                            <tr>
                                    <td><code>18</code></td>
                                    <td><code>Adult</code></td>
                            </tr>
                            <tr>
                                    <td><code>1, 78</code></td>
                                    <td><code>Minor</code></td>
                            </tr>
                            <tr>
                                    <td><code>70</code></td>
                                    <td><code>Senior</code></td>
                            </tr>
                            <tr>
                                    <td><code>70, 75</code></td>
                                    <td><code>Adult</code></td>
                            </tr>
                    </tbody>
            </table>
        </td>
        <td>15</td>
    </tr>
    <tr>
        <td>9. calculate total</td>
        <td>1</td>
        <td>
            <table border="1" style="width: 100%; text-align: center;">
                    <thead>
                            <tr>
                                    <th style="text-align: center;">Arguments</th>
                                    <th style="text-align: center;">Return Values</th>
                            </tr>
                    </thead>
                    <tbody>
                            <tr>
                                    <td><code>10, 9, 0.3</code></td>
                                    <td><code>63</code></td>
                            </tr>
                            <tr>
                                    <td><code>10, 11, 0.3</code></td>
                                    <td><code>74.8</code></td>
                            </tr>
                            <tr>
                                    <td><code>10, 11, 0.3, 120</code></td>
                                    <td><code>77</code></td>
                            </tr>
                            <tr>
                                    <td><code>10, 11, 0.3, 90, 0.5</code></td>
                                    <td><code>22</code></td>
                            </tr>
                    </tbody>
            </table>
        </td>
        <td>20</td>
    </tr>
    <tr>
        <td>10. Input Prompts</td>
        <td>1-2</td>
        <td>All the these tests are expecting 3 <code>input()</code> prompts to be present in your code (repeated twice in a loop). You must use <code>input()</code> to ask the user the following prompts, depending on the input the user provides:
        <ul>
          <li><code>Enter the discount percent (formatted as a decimal): </code></li>
        </ul>
        <ul>
          <li><code>Enter the price for the product purchased:  </code></li>
        </ul>
        <ul>
          <li><code>Enter the quantity of the product purchased:  </code></li>
        </ul>
        </td>
        <td>5</td>
    </tr>
    <tr>
        <td>11. Printed Messages</td>
        <td>1-2</td>
        <td>Your printed output must contain these phrases, but order doesn't matter. You will not be docked if you print out any extra statements not included here:
          <ul>
            <li><code>Hello Diego, welcome to IS 303!</code></li>
            <li><code>Hello Mai, welcome to IS 303!</code></li>
            <li><code>0.0</code></li>
            <li><code>10 is even.</code></li>
            <li><code>12</code></li>
            <li><code>23.88888888888889</code></li>
            <li><code>5 is odd.</code></li>
            <li><code>970.5</code></li>
            <li><code>Adult</code></li>
            <li><code>False</code></li>
            <li><code>True</code></li>
            <li><code>[2, 87, 30.0]</code></li>
            <li><code>I am a dog named Peppy and I'm 0 years old!</code></li>
            <li><code>I am a dog named Spot and I'm 7 years old!</code></li>
            <li><code>Senior</code></li>
            <li><code>The total price after discounts is: &lt;price&gt;</code></li>
          </ul>        
        </td>
        <td>4</td>
    </tr>
    <tr>
        <td>12. Sufficient Comments </td>
        <td>None</td>
        <td>Your code must include at least <code>10</code> comments. You can use any form of commenting:
        <ul>
          <li><code>#</code></li> 
          <li><code>''' '''</code></li>
          <li><code>""" """</code></li>
        </ul>
        </td>
        <td>1</td>
    </tr>
    <tr>
        <td colspan="2">Total Points</td>
        <td>100</td>
  </tr>
</tbody>
</table>

<br><br>

## Test Cases Summary
<table>
  <tr>
    <th>Test Case Description</th>
    <th>Inputs</th>
  </tr>
  <tr>
    <td><a href="#testcase1">1: Using 5 as product price, different quantities</a></td>
    <td><ul>
  <li><code>5</code></li>
  <li><code>15</code></li>
  <li><code>.1</code></li>
  <li><code>5</code></li>
  <li><code>25</code></li>
  <li><code>.1</code></li>
</ul></td>
  </tr>
  <tr>
    <td><a href="#testcase2">2: Different prices and quantities</a></td>
    <td><ul>
  <li><code>2</code></li>
  <li><code>2000</code></li>
  <li><code>.4</code></li>
  <li><code>4</code></li>
  <li><code>5</code></li>
  <li><code>.3</code></li>
</ul></td>
  </tr>
</table>

<h3 id="testcase1">Test Case 1 Details - Using 5 as product price, different quantities</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>5</code></li>
  <li><code>15</code></li>
  <li><code>.1</code></li>
  <li><code>5</code></li>
  <li><code>25</code></li>
  <li><code>.1</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter the price for the product purchased:</code></li>
  <li><code>Enter the quantity of the product purchased:</code></li>
  <li><code>Enter the discount percent (formatted as a decimal):</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Input Prompts</td>
    <td></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>Hello Diego, welcome to IS 303!</code></li>
  <li><code>Hello Mai, welcome to IS 303!</code></li>
  <li><code>12</code></li>
  <li><code>970.5</code></li>
  <li><code>False</code></li>
  <li><code>True</code></li>
  <li><code>5 is odd.</code></li>
  <li><code>10 is even.</code></li>
  <li><code>0.0</code></li>
  <li><code>23.88888888888889</code></li>
  <li><code>[2, 87, 30.0]</code></li>
  <li><code>I am a dog named Spot and I'm 7 years old!</code></li>
  <li><code>I am a dog named Peppy and I'm 0 years old!</code></li>
  <li><code>Senior</code></li>
  <li><code>Adult</code></li>
  <li><code>The total price after discounts is: $67.5</code></li>
  <li><code>The total price after discounts is: $110.0</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Printed Messages</td>
    <td><ul>
  <li><code>The total price after discounts is: $14.0</code></li>
  <li><code>The total price after discounts is: $2320.0</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Hello Diego, welcome to IS 303!
Hello Mai, welcome to IS 303!
12
970.5
False
True
5 is odd.
10 is even.
0.0
23.88888888888889
[2, 87, 30.0]
I am a dog named Spot and I'm 7 years old!
I am a dog named Peppy and I'm 0 years old!
Senior
Adult
Enter the price for the product purchased: 5
Enter the quantity of the product purchased: 15
Enter the discount percent (formatted as a decimal): .1
The total price after discounts is: $67.5
Enter the price for the product purchased: 5
Enter the quantity of the product purchased: 25
Enter the discount percent (formatted as a decimal): .1
The total price after discounts is: $110.0
```

<h3 id="testcase2">Test Case 2 Details - Different prices and quantities</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>2</code></li>
  <li><code>2000</code></li>
  <li><code>.4</code></li>
  <li><code>4</code></li>
  <li><code>5</code></li>
  <li><code>.3</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter the price for the product purchased:</code></li>
  <li><code>Enter the quantity of the product purchased:</code></li>
  <li><code>Enter the discount percent (formatted as a decimal):</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Input Prompts</td>
    <td></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>Hello Diego, welcome to IS 303!</code></li>
  <li><code>Hello Mai, welcome to IS 303!</code></li>
  <li><code>12</code></li>
  <li><code>970.5</code></li>
  <li><code>False</code></li>
  <li><code>True</code></li>
  <li><code>5 is odd.</code></li>
  <li><code>10 is even.</code></li>
  <li><code>0.0</code></li>
  <li><code>23.88888888888889</code></li>
  <li><code>[2, 87, 30.0]</code></li>
  <li><code>I am a dog named Spot and I'm 7 years old!</code></li>
  <li><code>I am a dog named Peppy and I'm 0 years old!</code></li>
  <li><code>Senior</code></li>
  <li><code>Adult</code></li>
  <li><code>The total price after discounts is: $2320.0</code></li>
  <li><code>The total price after discounts is: $14.0</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Printed Messages</td>
    <td><ul>
  <li><code>The total price after discounts is: $67.5</code></li>
  <li><code>The total price after discounts is: $110.0</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Hello Diego, welcome to IS 303!
Hello Mai, welcome to IS 303!
12
970.5
False
True
5 is odd.
10 is even.
0.0
23.88888888888889
[2, 87, 30.0]
I am a dog named Spot and I'm 7 years old!
I am a dog named Peppy and I'm 0 years old!
Senior
Adult
Enter the price for the product purchased: 2
Enter the quantity of the product purchased: 2000
Enter the discount percent (formatted as a decimal): .4
The total price after discounts is: $2320.0
Enter the price for the product purchased: 4
Enter the quantity of the product purchased: 5
Enter the discount percent (formatted as a decimal): .3
The total price after discounts is: $14.0
```

