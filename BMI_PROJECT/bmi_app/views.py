from django.shortcuts import render

# Create your views here.
def bmi_calculator(request):
    bmi = None
    category = None

    if request.method == "POST":
        weight = float(request.POST.get("weight"))
        height = float(request.POST.get("height"))

        # Convert height from cm to meters
        height_m = height / 100

        # BMI formula
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)

        # Classification
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

    return render(request, "bmicalculator.html", {
        "bmi": bmi,
        "category": category
    })

# Create your views here.
