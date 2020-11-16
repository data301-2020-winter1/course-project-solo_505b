[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=315718&assignment_repo_type=GroupAssignmentRepo)
# Group 505 - Predict Heart Disease using local lp norm

## Topic Description
World Health Organization has estimated 12 million deaths occur worldwide; every year due to Heart diseases. Half the deaths in the United States and other developed countries are due to *cardiovascular diseases*. The early prognosis of cardiovascular diseases can aid in making decisions on lifestyle changes in high risk patients and in turn reduce the complications. This project intends to predict the overall risk using **local lp norm** method. The main goal of this project is apply our newly developed method on a dataset with a categorical (binary in this case) response variable to compare MSE (Mean Squared Error) of the ordinary logistic regression and local lp norm. Also pinpoint the most relevant/risk factors of heart disease and analyze the correlation between explanatory variables. By the end of this project, we're going study the performance of *local lp method* on a categorical data.

## Dataset Description
The dataset is publicly available on the Kaggle website, and it is from an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. The classification goal is to predict whether the patient has 10-year risk of future coronary heart disease (CHD). The dataset provides the patients’ information. It includes over *4,000 records* and *15 attributes*. Each attribute is a potential risk factor. There are both demographic, behavioral and medical risk factors.
Demographic:
- Sex: male or female (Nominal)
- Age: Age of the patient;(Continuous - Although the recorded ages have been truncated to whole numbers, the concept of age is continuous)
Behavioral
- Current Smoker: whether the patient is a current smoker (Nominal)
- Cigs Per Day: the number of cigarettes that the person smoked on average in one day. (can be considered continuous as one can have any number of cigarettes, even half a cigarette.)
Medical(history)
- BP Meds: whether the patient was on blood pressure medication (Nominal)
- Prevalent Stroke: whether the patient had previously had a stroke (Nominal)
- Prevalent Hyp: whether the patient was hypertensive (Nominal)
- Diabetes: whether the patient had diabetes (Nominal)
Medical(current)
- Tot Chol: total cholesterol level (Continuous)
- Sys BP: systolic blood pressure (Continuous)
- Dia BP: diastolic blood pressure (Continuous)
- BMI: Body Mass Index (Continuous)
- Heart Rate: heart rate (Continuous - In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of large number of possible values.)
- Glucose: glucose level (Continuous)
Predict variable (desired target)
- 10-year risk of coronary heart disease CHD (binary: “1”, means “Yes”, “0” means “No”)

## Team Members

Ladan Tazik - I love hanging out with my friends!

## References
[Kaggle-Farmingham Dataset](https://www.kaggle.com/amanajmera1/framingham-heart-study-dataset)

