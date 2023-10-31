no_step_string = ""
step_string = ""
test_case = 20
while(test_case > 0):

    for i in range(0, test_case + 1):
        if (i % 2 == 0):
            no_step_string += str(i) + " "

    for i in range(0, test_case + 1, 2):
        step_string += str(i) + " "

    print(f'''no_step_string:{no_step_string}
step_string:   {step_string}
test_case:{test_case}
%s'''%("\n"*2))

    no_step_string = ""
    step_string = ""
    test_case -= 1
