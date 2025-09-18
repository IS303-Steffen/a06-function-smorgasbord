max_score = 10  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import (
    normalize_text,
    load_student_code,
    format_error_message,
    exception_message_for_students,
    round_match,
    get_similarity_feedback,
    clear_database,
    pc_get_or_create,
    pc_finalize_and_maybe_fail,
    default_module_to_test
)
import re

# Checks if the input prompts (from using input()) contain the expected prompts.
def test_06_min_max_mean(current_test_name, input_test_cases, function_test_cases):
    rec = pc_get_or_create(current_test_name, max_score)
    try:
        # Ensure test_cases is valid and iterable
        if not isinstance(input_test_cases, list):
            input_test_case = {"id_test_case": None}
            exception_message_for_students(ValueError("test_cases should be a list of dictionaries. Contact your professor."), test_case=input_test_case) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.

        input_test_case = input_test_cases[0]
        case_id = input_test_case["id_input_test_case"]
        function_being_tested = 'min_max_mean'
        fuction_test_cases_payload = function_test_cases.get(function_being_tested)

        # Grab the necessary data from the test case dictionary
        inputs = input_test_case["inputs"]
        case_failed_messages = []
        # Load in the student's code using the updated function
        manager_payload = load_student_code(current_test_name, inputs, input_test_case, default_module_to_test, function_tests=fuction_test_cases_payload)
            
        if not manager_payload:
            return # if there was an error in running student code, it's already been logged. Just skip to the next test case.

        

        function_results = manager_payload['function_results']
        if function_results.get("FUNCTION ERROR") is not None:
            custom_message = (f"{function_results.get('FUNCTION ERROR').get('message')}\n\n")
            formatted = format_error_message(
                                    custom_message=custom_message, 
                                    current_test_name=current_test_name,
                                    input_test_case=input_test_case,
                                    )
            rec.fail_case(
                case_id=f"func:{function_being_tested}:setup",
                custom_message=formatted,
                case_type="function",
                label=f"{function_being_tested} (setup)"
            )
            #case_failed_messages.append(formatted)
            return
            
        test_results = function_results.get('function_results')

        for index, test_result in enumerate(test_results, start=1):
            test_inputs = test_result.get('args')
            formatted_test_input = [f"{index}: {'\"' + item + '\"' if isinstance(item, str) else item} "
                                    f"(data type: {type(item).__name__})"
                                    for index, item in enumerate(test_inputs, start=1)]
            test_inputs_str = '\n'.join(formatted_test_input)
            
            expected_result = test_result.get('expected_return_value')
            expected_result = normalize_text(expected_result)
            expected_result_str = f"{str(expected_result)} (data type: {type(expected_result).__name__})"

            actual_result = test_result.get('actual_return_value')[0] # Results are returned in lists. Normally, we only care about the test being run once.
            actual_result = normalize_text(actual_result)
            actual_result_str = f"{str(actual_result)} (data type: {type(actual_result).__name__})"

            arg_preview = ", ".join(repr(a) for a in test_inputs)
            label = f"{function_being_tested}({arg_preview})"

            if not actual_result == expected_result:
                formatted = format_error_message(
                    custom_message=(f"When the function:\n"
                                    f"```\n{function_being_tested}\n```\n"
                                    f"is provided with the following argument(s):\n"
                                    f"```\n{test_inputs_str}\n```\n"
                                    f"the expected return value (ignoring capitalization / punctuation) is:\n"
                                    f"```\n{expected_result_str}\n```\n"
                                    f"However, your function is returning this value (ignoring capitalization / punctuation):\n"
                                    f"```\n{actual_result_str}\n```\n"
                                    f"Make sure your function is returning the proper value and that the logic matches "
                                    f"what the instructions say. If the message above says your function is returning \"None\" when it shouldn't, "
                                    f"that means your function likely doesn't have a return statement. Make sure you are returning "
                                    f"a value, not just printing it out directly in the function."),
                    current_test_name=current_test_name,
                    input_test_case=input_test_case,
                    )
                rec.fail_case(
                    case_id=f"func:{function_being_tested}:{index}",
                    custom_message=formatted,
                    case_type="function",
                    label=label
                )
            else:
                rec.pass_case(
                    case_id=f"func:{function_being_tested}:{index}",
                    case_type="function",
                    label=label
                )
                

    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise
    
    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, input_test_case, current_test_name)

    finally:
        # Record the case result for partial credit
        # if case_failed_messages:
        #     # Join multiple messages (if both a required and invalid check failed)
        #     full_msg = "\n\n".join(case_failed_messages)
        #     rec.fail_case(case_id, custom_message=full_msg)
        # else:
        #     rec.pass_case(case_id)  

        # After all cases, emit a one-line summary or a short failure directing to the MD file
        pc_finalize_and_maybe_fail(rec)