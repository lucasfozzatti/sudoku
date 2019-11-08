FROM python:3

RUN git clone https://github.com/lucasfozzatti/sudoku.git
COPY requirements.txt /sudoku
WORKDIR /sudoku


RUN pip install -r requirements.txt
RUN pip install parameterized

CMD [ "python3", "test_sudoku.py"]