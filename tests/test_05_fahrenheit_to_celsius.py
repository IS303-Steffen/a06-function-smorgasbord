max_score = 10  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import normalize_text, load_student_code, format_error_message, exception_message_for_students
import pytest

# Checks if the input prompts (from using input()) contain the expected prompts.
def test_05_fahrenheit_to_celsius(current_test_name, input_test_cases, function_test_cases):
    try:
        # Ensure test_cases is valid and iterable
        if not isinstance(input_test_cases, list):
            input_test_case = {"id_test_case": None}
            exception_message_for_students(ValueError("test_cases should be a list of dictionaries. Contact your professor."), test_case=input_test_case) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.

        input_test_case = input_test_cases[0]
        function_being_tested = 'fahrenheit_to_celsius'
        fuction_test_cases_payload = function_test_cases.get(function_being_tested)

        # Grab the necessary data from the test case dictionary
        inputs = input_test_case["inputs"]

        # Load in the student's code using the updated function
        manager_payload = load_student_code(current_test_name, inputs, input_test_case, function_tests=fuction_test_cases_payload)

        function_results = manager_payload['function_results']
        if function_results.get("FUNCTION ERROR") is not None:
            custom_message = (f"{function_results.get('FUNCTION ERROR').get('message')}\n\n")
            formatted_message = format_error_message(
                                    custom_message=custom_message, 
                                    current_test_name=current_test_name,
                                    input_test_case=input_test_case,
                                    )
            pytest.fail(formatted_message)
            
        test_results = function_results.get('function_results')

        for test_result in test_results:
            test_inputs = test_result.get('args')
            test_inputs_str = ', '.join(str(item) for item in test_inputs)
            
            expected_result = test_result.get('expected_return_value')
            expected_result = normalize_text(expected_result)

            actual_result = test_result.get('actual_return_value')[0] # Results are returned in lists. Normally, we only care about the test being run once.
            actual_result = normalize_text(actual_result)

            assert actual_result == expected_result, format_error_message(
                custom_message=(f"When the function: {function_being_tested}\nis provided with the following argument(s):\n\n"
                                f"{test_inputs_str}\n\n"
                                f"the expected return value (ignoring capitalization / punctuation) is:\n\n"
                                f"{expected_result}\n\n"
                                f"However, your function is returning this value (ignoring capitalization / punctuation):\n\n"
                                f"{actual_result}\n\n"
                                f"Make sure your function is returning a value and that the logic matches "
                                f"what the instructions say. If the message above says your function is returning \"None\" when it shouldn't, "
                                f"that means your function likely doesn't have a return statement. Make sure you are returning "
                                f"a value, not just printing it out directly in the function."),
                current_test_name=current_test_name,
                input_test_case=input_test_case,
            )

    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise
    
    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, input_test_case, current_test_name)