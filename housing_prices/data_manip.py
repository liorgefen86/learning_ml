import os
import tarfile
import urllib.request
import pandas as pd


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(url=HOUSING_URL, path=HOUSING_PATH):
    os.makedirs(path, exist_ok=True)
    tgz_path = os.path.join(path, "housing.tgz")
    urllib.request.urlretrieve(url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=path)
    housing_tgz.close()


def load_house_data(path=HOUSING_PATH):
    csv_path = os.path.join(path, 'housing.csv')
    return pd.read_csv(csv_path)


if __name__ == '__main__':
    fetch_housing_data()