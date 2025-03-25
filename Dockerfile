FROM python:3.12

RUN pip install jupyterlab pandas numpy matplotlib seaborn scikit-learn

EXPOSE 8888

CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
