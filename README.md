# Ex.04 Design a Website for Server Side Processing
## Date:17.12.25

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
bmicalculator.html
!DOCTYPE html>
<html>
<head>
    <title>BMI Calculator</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        form {
            width: 300px;
            padding: 20px;
            border: 1px solid #888;
            border-radius: 8px;
            margin-left: 50%;
            transform: translateX(-50%);
        }
        input { width: 100%; margin: 10px 0; padding: 8px; }
        .result { margin-top: 20px; padding: 10px; background: #f1f1f1; }
    </style>
</head>

<body>
    <h2 align="center">BMI Calculator (Server-side in Django)</h2>

    <form method="POST">
        {% csrf_token %}
        <label>Weight (kg)</label>
        <input type="number" step="0.1" name="weight" required>

        <label>Height (cm)</label>
        <input type="number" step="0.1" name="height" required>

        <button type="submit">Calculate BMI</button>
        {% if bmi %}
        <div class="result">
            <strong>Your BMI:</strong> {{ bmi }}<br>
            <strong>Category:</strong> {{ category }}
        </div>
        {% endif %}
    </form>

    
</body>
</html>

view.py
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
    urls.py
    """
URL configuration for BMI_PROJECT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bmi_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmi', views.bmi_calculator, name='bmi'),
]


## SERVER SIDE PROCESSING:

<img width="1920" height="1080" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/174066a8-6e57-4555-8b96-419a755a1801" />


## HOMEPAGE:

<img width="1920" height="1080" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/5927df06-5629-4d93-b7a6-a9acd4c9ea38" />


## RESULT:
The program for performing server side processing is completed successfully.
