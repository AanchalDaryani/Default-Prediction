import requests
import json

url = "http://localhost:8080/prediction"

payload = json.dumps({
  "Gender": 0,
  "Married": 0,
  "Dependents": 10,
  "Education": 0,
  "Self_Employed": 1,
  "ApplicantIncome": 1,
  "CoapplicantIncome": 0,
  "LoanAmount": 104300,
  "Loan_Amount_Term": 72,
  "Credit_History": 1,
  "Property_Area": 2
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
