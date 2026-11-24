# Ham Gaussian 2 chieu va ham doc du lieu cho BTL01
import numpy as np
import pandas as pd

MU = np.array([0.0, 0.0])
COV = np.array([[0.3, -0.5], [-0.5, 2.0]])
X1_RANGE = (-2.0, 2.0)
X2_RANGE = (-4.0, 4.0)


def gaussian_2d(x, mu=MU, cov=COV):
    # f(x) = 1 / (2*pi*sqrt(det C)) * exp(-0.5 * (x-mu)^T C^-1 (x-mu)), x co shape (n, 2)
    x = np.atleast_2d(np.asarray(x, dtype=np.float64))
    d = x - mu
    cov_inv = np.linalg.inv(cov)
    q = np.einsum("ni,ij,nj->n", d, cov_inv, d)
    norm = 1.0 / (2.0 * np.pi * np.sqrt(np.linalg.det(cov)))
    return norm * np.exp(-0.5 * q)  # giu dung thu tu phep tinh nay, doi thu tu se lech y o chu so cuoi


def read_split(path):
    # round_trip: doc lai dung gia tri da ghi (mac dinh pandas co the lech ~1e-15)
    return pd.read_csv(path, float_precision="round_trip")


def load_split(path):
    df = read_split(path)
    return df[["x1", "x2"]].to_numpy(), df["y"].to_numpy()
