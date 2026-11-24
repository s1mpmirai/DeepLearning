# BTL01 - Xấp xỉ hàm Gaussian 2 chiều bằng MLP (PyTorch)

Dùng mạng MLP viết bằng PyTorch để xấp xỉ hàm mật độ Gaussian 2 chiều với μ = (0, 0), C = [[0.3, -0.5], [-0.5, 2]] trên miền -2 ≤ x1 ≤ 2, -4 ≤ x2 ≤ 4. Sau đó khảo sát ảnh hưởng của số mẫu train (A), số nơ-ron tầng ẩn (B) và số tầng ẩn (C).

## Cài đặt

```bash
pip install -r requirements.txt
```

Nhóm chạy trên Python 3.13, PyTorch 2.14 (CPU). Không cần GPU.

## Thư mục

```
tuan7/
├── data/            train_pool.csv, val.csv, test.csv, metadata.json
├── document/        đề bài và tài liệu mẫu
├── preprocessing/   gaussian.py, generate_data.ipynb
├── eda/             eda.ipynb, các bảng thống kê .csv, figures/
├── models/          mlp.py, train.py, plots.py, experiment.py, exp_A/B/C.ipynb
├── exps/            exp_A/, exp_B/, exp_C/: log, runs.csv, summary.csv, .pth, hình
├── experiments.xlsx
├── Report.docx, Report.pdf
└── Slides.pptx, Slides.pdf
```

## Dữ liệu

| File | Số mẫu | Dùng để |
|---|---|---|
| data/train_pool.csv | 2000 | train. Exp A lấy `train_pool[:A]`, Exp B và C lấy `train_pool[:1000]` |
| data/val.csv | 200 | early stopping, lưu checkpoint, chọn mô hình |
| data/test.csv | 100 | chỉ để báo cáo kết quả, không dùng để chọn gì cả |

Mỗi file có 3 cột `x1, x2, y`. x1, x2 lấy ngẫu nhiên đều trong miền, y = f(x1, x2) không có nhiễu. Ba tập được rút lần lượt train_pool, val, test từ cùng một `np.random.default_rng(42)`.

Dữ liệu chỉ sinh một lần rồi commit. Chạy lại `generate_data.ipynb` sẽ không ghi đè mà chỉ kiểm tra lại. MD5 của từng file nằm trong `data/metadata.json`.

Lưu ý: NumPy không đảm bảo `default_rng` cho ra cùng dãy số ở mọi phiên bản, nên nếu máy khác báo không khớp thì cứ dùng file CSV đã commit.

### Đọc dữ liệu trong notebook ở models/

```python
import sys
from pathlib import Path
ROOT = Path.cwd() if (Path.cwd() / "preprocessing").is_dir() else Path.cwd().parent
sys.path.insert(0, str(ROOT))

from preprocessing.gaussian import load_split, gaussian_2d
X_train, y_train = load_split(ROOT / "data" / "train_pool.csv")  # X: (n, 2), y: (n,)
```

`load_split` trả về float64, đưa vào PyTorch thì đổi sang float32. `gaussian_2d(X)` tính giá trị thật của hàm, dùng khi vẽ bề mặt thật hoặc heatmap lỗi.

## Chạy

Chạy từ thư mục `tuan7/`:

```bash
python -m nbconvert --to notebook --execute --inplace preprocessing/generate_data.ipynb   # sinh / kiểm tra dữ liệu
python -m nbconvert --to notebook --execute --inplace eda/eda.ipynb                       # hình và bảng EDA
python -m nbconvert --to notebook --execute --inplace models/exp_A.ipynb                  # Exp A -> exps/exp_A/
python -m nbconvert --to notebook --execute --inplace models/exp_B.ipynb                  # Exp B -> exps/exp_B/
python -m nbconvert --to notebook --execute --inplace models/exp_C.ipynb                  # Exp C -> exps/exp_C/
```

Hoặc mở notebook bằng Jupyter / VS Code rồi Run All.

## Cấu hình baseline

| Tham số | Giá trị |
|---|---|
| Seed dữ liệu / mô hình | 42 / 0, 1, 2 |
| Chuẩn hoá input | x1/2, x2/4 |
| Mạng | 1 tầng ẩn 10 nơ-ron, tanh, tầng ra tuyến tính |
| Loss, optimizer | MSELoss, Adam lr = 1e-3 |
| Batch, epoch | 32, tối đa 1000 epoch, early stopping patience 100 theo val loss |
| A cho Exp B, C | 1000 |

Để tham khảo: nếu chỉ đoán y bằng một hằng số (trung bình y của train) thì MSE khoảng 3.4e-3 trên train, 3.8e-3 trên val, 2.7e-3 trên test (`eda/constant_baseline.csv`).

## Kết quả

Mỗi lần chạy ghi một dòng vào `exps/exp_*/runs.csv`:

```
exp,value,seed,train_mse,val_mse,test_mse,test_mae,test_rmse,best_epoch,train_time_s,n_params
```

`summary.csv` là trung bình và độ lệch chuẩn theo `value`.
