FROM python
WORKDIR /XiaomiShop
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=test_results/ /XiaomiShop/tests/