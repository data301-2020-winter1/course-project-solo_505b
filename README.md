[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=315718&assignment_repo_type=GroupAssignmentRepo)
# Group 505 - Predict Heart Disease using local lp norm

## Topic Description
Cardiovascular diseases (CVDs) are the number one cause of death worldwide with an estimated 17.9 million deaths per year [1](https://www.who.int/health-topics/cardiovascular-diseases/#tab=tab_1). One person dies every 36 seconds in the United States from cardiovascular disease[2](https://www.cdc.gov/heartdisease/facts.htm). Early prognosis of cardiovascular disease can help make choices about lifestyle improvements in high-risk patients and in exchange, reduce risks. In this project I'm going to  predict the overall risk using **logistic regression** method and compare the accuracy of logistic regression to our newly developed method **local lp norm**. In addition, highlight the most relevant/risk factors for heart failure and examine the correlation between explanatory variables( aka features).

## Dataset Description
This dataset is part of the continuing cardiovascular research of residents of Framingham Area, Massachusetts which is public on the Kaggle website. The classification aim is to predict whether a patient has a 10-year chance of potential coronary heart disease (CHD). The dataset over *4,000 records* and *15 feature*. Each feature is a possible risk factor. Three kinds of factors had been collected in this dataset.

Demographic:
- Sex : 1 indicates male and 0 indicates female
- Age: Age of the patient

Behavioral:
- Current Smoker: whether the patient is a current smoker
- Cigs Per Day: The number of cigarettes the person smoked in one day on average.

Medical(history):
- BP Meds: If the patient used blood pressure drugs
- Prevalent Stroke: If the patient suffered a stroke in the past
- Prevalent Hyp: If the patient is hypertensive
- Diabetes: If the patient has diabetes<br>
Medical(current):
- Tot Chol: total cholesterol level 
- Sys BP: systolic blood pressure
- Dia BP: diastolic blood pressure 
- BMI: Body Mass Index 
- Heart Rate: heart rate
- Glucose: glucose level

Predict variable (desired target)
- if patient has a 10-year chance of coronary heart disease

## Team Members

Ladan Tazik - I love hanging out with my friends!

## References
[Kaggle-Farmingham Dataset](https://www.kaggle.com/amanajmera1/framingham-heart-study-dataset)

