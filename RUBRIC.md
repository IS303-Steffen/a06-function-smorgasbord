# Rubric
Your grade is based on whether you pass the automated tests, listed below.

The tests will ignore spacing, capitalization, and punctuation, but you will fail the tests if you spell something wrong or calculate something incorrectly.


<table border="1" style="width: 100%; text-align: center;">
<thead style="text-align: center;">
    <tr>
        <th style="text-align: center;">Test</th>
        <th style="text-align: center;">Description</th>
        <th style="text-align: center;">Points</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>1. welcome message</td>
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
        <td>
        <b>Input test cases used:</b> 1, 2<br><br>
        Your input prompts must be the same as the expected input prompts of each input test case. 
        <br>
        <br>
        See the <code>descriptions_ot_test_cases</code> folder for expected input prompts for each input test case.
        </td> 
        <td>5</td>
    </tr>
    <tr>
        <td>11. Printed Messages</td>
        <td>
        <b>Input test cases used:</b> 1, 2<br><br>
        Your printed output must be the same as the expected output of each input test case. This includes the correct BMI calculations and BMI categories.
        <br>
        <br>
        See the <code>descriptions_ot_test_cases</code> folder for expected printed messages for each input test case.       
        </td>
        <td>4</td>
    </tr>
    <tr>
        <td>12. Sufficient Comments </td>
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

## Test Cases
If you fail a test during a specific test case, see the `descriptions_of_test_cases` folder for the following:
<table border="1" style="width: 100%; text-align: left;">
  <tr>
    <th>Test Case</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Input Test Case 01</td>
    <td>Using 5 as product price, different quantities</td>
  </tr>
  <tr>
    <td>Input Test Case 02</td>
    <td>Different prices and quantities</td>
  </tr>
</table>
