"""Hàm Gaussian 2 chiều và sinh dữ liệu cho BTL01.

f(x) = 1 / (2π·sqrt(det C)) · exp(-1/2 · (x - μ)^T C^{-1} (x - μ))
với μ = (0, 0), C = [[0.3, -0.5], [-0.5, 2]], -2 ≤ x1 ≤ 2, -4 ≤ x2 ≤ 4.
"""
from pathlib import Path

import numpy as np
import pandas as pd

MU = np.array([0.0, 0.0])
COV = np.array([[0.3, -0.5], [-0.5, 2.0]])
X1_RANGE = (-2.0, 2.0)
X2_RANGE = (-4.0, 4.0)

DATA_SEED = 42
SPLIT_SIZES = {"train_pool": 2000, "val": 200, "test": 100}  # thứ tự sinh cố định
COLUMNS = ["x1", "x2", "y"]


def gaussian_2d(x, mu=MU, cov=COV):
    """Mật độ Gaussian 2 chiều tại các điểm x có shape (n, 2) hoặc (2,)."""
    x = np.atleast_2d(np.asarray(x, dtype=np.float64))
    d = x - mu
    cov_inv = np.linalg.inv(cov)
    # (x - μ)^T C^{-1} (x - μ) cho từng hàng
    mahalanobis_sq = np.einsum("ni,ij,nj->n", d, cov_inv, d)
    norm = 1.0 / (2.0 * np.pi * np.sqrt(np.linalg.det(cov)))
    return norm * np.exp(-0.5 * mahalanobis_sq)


def sample_inputs(n, rng):
    """Lấy n điểm phân bố đều trên miền [-2, 2] x [-4, 4]."""
    x1 = rng.uniform(*X1_RANGE, size=n)
    x2 = rng.uniform(*X2_RANGE, size=n)
    return np.column_stack([x1, x2])


def make_split(n, rng):
    x = sample_inputs(n, rng)
    return pd.DataFrame({"x1": x[:, 0], "x2": x[:, 1], "y": gaussian_2d(x)})


def generate_all(seed=DATA_SEED, sizes=SPLIT_SIZES):
    """Sinh train_pool, val, test từ một bộ sinh số ngẫu nhiên duy nhất.

    Ba tập là ba lần rút liên tiếp, không chồng lấn, nên độc lập với nhau.
    Đổi thứ tự hoặc kích thước trong `sizes` sẽ làm thay đổi dữ liệu.
    """
    rng = np.random.default_rng(seed)
    return {name: make_split(n, rng) for name, n in sizes.items()}


def save_splits(splits, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, df in splits.items():
        # LF cố định để mã MD5 giống nhau trên mọi hệ điều hành
        df.to_csv(out_dir / f"{name}.csv", index=False, float_format="%.17g", lineterminator="\n")


def load_split(path):
    """Đọc một file CSV, trả về (X có shape (n, 2), y có shape (n,))."""
    df = pd.read_csv(path)
    return df[["x1", "x2"]].to_numpy(), df["y"].to_numpy()
