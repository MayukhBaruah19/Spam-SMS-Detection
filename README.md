# spam/mail sms prediction : 
Spam message/email prediction using machine learning and natural language processing (NLP) involves training algorithms
to automatically identify and filter out unwanted or malicious messages. By analyzing the content, structure, and metadata 
of emails or messages, NLP techniques extract meaningful features such as keywords, frequency of certain terms, and syntactic 
patterns. Machine learning models—such as Naive Bayes, Support Vector Machines, or deep learning—are then trained on labeled 
datasets of spam and non-spam messages to learn the differences between them. Once trained, the model can accurately classify 
new, incoming messages as spam or legitimate, improving email security and user experience.

![image](https://miro.medium.com/v2/resize:fit:1400/1*hsyCZOYoGrX6BJsj4Lgrhg.png)
# About this project :
I developed a spam email/SMS detection model using machine learning and natural language processing techniques. The project involved 
text preprocessing with NLTK to clean and tokenize the messages, and data manipulation with Pandas. For data visualization and exploratory
analysis, I used Matplotlib and Seaborn to better understand the distribution and patterns in the dataset. A Naive Bayes classifier was trained 
on the processed data to distinguish between spam and non-spam messages. After training, the model was saved as a ```.pkl``` file for reuse.
To make the model user-friendly, I built an interactive graphical user interface (GUI) using Streamlit, allowing users to input messages 
and get instant spam predictions.
# Demo :
spam Prediction :
![image](https://github.com/MayukhBaruah19/Spam-SMS-Detection/blob/main/templets/Screenshot%202025-07-23%20002549.png)
Ham prediction :
![image](https://github.com/MayukhBaruah19/Spam-SMS-Detection/blob/main/templets/Screenshot%202025-07-23%20002636.png)
# Dataset used :
[Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
# How to run ? 
- Clone the repository
  ```Bash
  git clone https://github.com/MayukhBaruah19/Spam-SMS-Detection.git
  ```
- Create a conda environment after opening the repository and activate it
  
  ```Bash
  conda create -p venv python=3.13 -y
  ```
  ```Bash
  conda activate venv
  ```
- install the requirements
  
  ```Bash
  pip install -r requirements.txt
  ```
- Run the main.py file
  
  ```Bash
  streamlit run main.py
  ```  
  
