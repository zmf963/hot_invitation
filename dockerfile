FROM python:3.9

WORKDIR /opt/hot_invitation/hot_invitation
COPY . /opt/hot_invitation/
RUN pip install -r /opt/hot_invitation/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ENTRYPOINT  ["python","main.py"]