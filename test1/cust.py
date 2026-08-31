"""24.	Write a Python program to check whether a customer is eligible for a service based on age and a minimum score."""
def check_eligibility(age, score, min_age, min_score):
    if age >= min_age and score >= min_score:
        return "Customer is eligible for the service."
    else:
        return "Customer is not eligible for the service."
    
min_age = 18
min_score = 70
age = int(input("Enter customer's age: "))
score = int(input("Enter customer's score: "))
result = check_eligibility(age, score, min_age, min_score)
print(result)