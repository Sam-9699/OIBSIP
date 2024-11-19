def calculate_bmi(weight, height):
    """Calculate BMI using the formula: weight (kg) / height (m)^2."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify the BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("\n<<---Welcome to the BMI Calculator!--->>\n")
    
    # Get user input
    try:
        weight = float(input("Enter your weight (in kilograms): "))
        height = float(input("Enter your height (in meters): "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Get BMI category
        category = classify_bmi(bmi)
        
        # Display the result
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}\n")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()