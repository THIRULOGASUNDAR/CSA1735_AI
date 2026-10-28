# Decision Tree classifier without sklearn

X = [
    [1, 50], [2, 55], [3, 60], [4, 65],
    [5, 75], [6, 80], [7, 85], [8, 95]
]

y = [0, 0, 0, 0, 1, 1, 1, 1]

hours = float(input("Enter hours studied: "))
attendance = float(input("Enter attendance percentage: "))

# Decision tree rules
if hours <= 4:
    prediction = 0
else:
    prediction = 1

if prediction == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")
