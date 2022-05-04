# import test

def bmi(weight, height):
    bmi = weight / (height*height)
    if bmi > 30:
        return "Obese"
    if bmi <= 30.0:
        return "Overweight"
            elif bmi <= 25.0:
                return "Normal"
                elif bmi <= 18.5:
                    return "Underweight"


print(bmi(63, 158))


# def fixed_tests():
#     @test.it('Basic Test Cases')
#
#     def basic_test_cases():
#         test.assert_equals(bmi(50, 1.80), "Underweight")
#         test.assert_equals(bmi(80, 1.80), "Normal")
#         test.assert_equals(bmi(90, 1.80), "Overweight")
#         test.assert_equals(bmi(110, 1.80), "Obese")
#         test.assert_equals(bmi(50, 1.50), "Normal")