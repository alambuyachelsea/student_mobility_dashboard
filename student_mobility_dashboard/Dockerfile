FROM python:3.12

WORKDIR /app

ADD requirements.txt .
ADD university_data.csv .
RUN pip install -r requirements.txt

ADD main_page.py .
ADD university_profile.py .
CMD ["streamlit", "run", "main_page.py", "--server.address", "0.0.0.0"]