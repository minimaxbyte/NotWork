FROM python:latest
RUN apt -qq update && apt -qq install -y git python3-dev ffmpeg
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3","bot.py"]
