FROM python:3.13
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

WORKDIR /app
COPY . .
RUN pip install numpy pandas scikit-learn wandb opencv-python-headless matplotlib
RUN python verify_files.py
CMD ["python", "distance_classification.py"]