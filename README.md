## Brain Stroke Prediction

In this project, I developed a website that utilizes a machine learning model to predict whether a patient had a stroke or not. The goal was to provide a tool that could assist healthcare professionals in diagnosing stroke based on patient information.

I used Python as the primary programming language and Pandas for data manipulation. To handle class imbalance in the dataset, I employed the __Synthetic Minority Over-sampling Technique (SMOTE)__. This technique helps in creating synthetic samples of the minority class to balance the dataset and improve the model's performance.

For the predictive modeling, I chose the __Random Forest Classifier__ algorithm, known for its effectiveness in handling complex datasets and producing accurate predictions. After training the model, it achieved an impressive accuracy of 97%, indicating its ability to reliably predict stroke cases.

To create the user interface for the model, I utilized __Streamlit__, a popular Python library for building interactive web applications. Streamlit allowed me to design a user-friendly interface where users can input various parameters related to the patient's health, such as age, gender, hypertension, heart disease, etc.

Overall, this project demonstrates the application of machine learning in healthcare and provides a practical tool for predicting strokes based on patient information.
