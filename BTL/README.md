# BTL01 – Xấp xỉ hàm Gaussian 2 chiều bằng MLP (PyTorch)

Huấn luyện mạng perceptron đa tầng (MLP) viết bằng PyTorch để xấp xỉ hàm mật độ Gaussian 2 chiều

$$f(\mathbf{x}) = \frac{1}{2\pi\sqrt{\det C}} \exp\left(-\tfrac{1}{2}(\mathbf{x}-\boldsymbol\mu)^T C^{-1}(\mathbf{x}-\boldsymbol\mu)\right),
\quad \boldsymbol\mu = (0, 0),\ C = \begin{bmatrix}0.3 & -0.5\\ -0.5 & 2\end{bmatrix}$$

trên miền $-2 \le x_1 \le 2$, $-4 \le x_2 \le 4$, rồi khảo sát ảnh hưởng của số mẫu train (A), số nơ-ron tầng ẩn (B) và số tầng ẩn (C).

## Cài đặt

Yêu cầu Python ≥ 3.10. Chạy được trên CPU, GPU là tuỳ chọn.

```bash
pip install -r requirements.txt
```

Đã chạy thử với Python 3.13.2, numpy 2.4.3, pandas 3.0.1, scipy 1.17.1, matplotlib 3.10.8, torch 2.14.0+cpu.

## Cấu trúc thư mục

```
BTL/
├── data/              train_pool.csv, val.csv, test.csv, metadata.json   (TV1)
├── document/          đề bài, yêu cầu, code và báo cáo mẫu
├── preprocessing/     gaussian.py, generate_data.ipynb                   (TV1)
├── eda/               eda.ipynb, bảng thống kê *.csv, figures/           (TV1)
├── models/            mlp.py, train.py, exp_C.ipynb                      (TV2)
│                      plots.py, exp_A.ipynb                              (TV3)
│                      experiment.py, exp_B.ipynb                         (TV4)
├── exps/              exp_A/, exp_B/, exp_C/: log CSV, runs.csv, summary.csv, .pth, hình
├── experiments.xlsx   tổng hợp kết quả A, B, C                           (TV1)
├── Report.docx, Report.pdf                                               (TV1)
└── Slides.pptx, Slides.pdf                                               (TV4)
```

Mọi notebook tự tìm thư mục gốc `BTL/` nên chạy được từ thư mục gốc hoặc từ chính thư mục chứa notebook. Không dùng đường dẫn tuyệt đối.

## Dữ liệu

| Tập | Số mẫu | Dùng cho |
|---|---|---|
| `data/train_pool.csv` | 2000 | Huấn luyện. Exp A lấy tập con lồng nhau `train_pool[:A]`; Exp B, C dùng `train_pool[:1000]` |
| `data/val.csv` | 200 | Early stopping, lưu checkpoint, chọn mô hình |
| `data/test.csv` | 100 | **Chỉ** đánh giá mô hình cuối, không dùng để chọn cấu hình |

- Mỗi file có 3 cột `x1, x2, y`, với `y = f(x1, x2)` không nhiễu.
- `x1`, `x2` lấy đều trên miền. Ba tập là ba lần rút liên tiếp (train_pool → val → test) từ `numpy.random.default_rng(42)`. Không có điểm trùng giữa các tập.
- `data/metadata.json` ghi seed, kích thước và mã MD5 của từng file CSV. Notebook sinh dữ liệu sẽ báo lỗi nếu CSV bị sửa.
- Dữ liệu đã sinh **một lần** và commit. Không ai sinh lại; chạy lại `generate_data.ipynb` chỉ kiểm tra tính tái lập, không ghi đè.

Đọc dữ liệu từ code khác:

```python
from preprocessing.gaussian import load_split, gaussian_2d
X_train, y_train = load_split("data/train_pool.csv")   # X: (n, 2), y: (n,)
```

`gaussian_2d(X)` trả về giá trị thật của hàm, dùng để vẽ bề mặt thật hoặc heatmap lỗi.

## Cách chạy

Chạy từ thư mục gốc `BTL/`. Nếu lệnh `jupyter` không có trong PATH thì dùng `python -m nbconvert` như dưới đây.

| Bước | Lệnh | Kết quả |
|---|---|---|
| 1. Sinh / kiểm tra dữ liệu | `python -m nbconvert --to notebook --execute --inplace preprocessing/generate_data.ipynb` | `data/*.csv`, `data/metadata.json` |
| 2. EDA | `python -m nbconvert --to notebook --execute --inplace eda/eda.ipynb` | `eda/figures/*.png`, `eda/*.csv` |
| 3. Exp A – số mẫu | `python -m nbconvert --to notebook --execute --inplace models/exp_A.ipynb` | `exps/exp_A/` |
| 4. Exp B – số nơ-ron | `python -m nbconvert --to notebook --execute --inplace models/exp_B.ipynb` | `exps/exp_B/` |
| 5. Exp C – số tầng | `python -m nbconvert --to notebook --execute --inplace models/exp_C.ipynb` | `exps/exp_C/` |

Bước 3–5 cần `models/mlp.py`, `models/train.py`, `models/experiment.py`. Tên notebook và thư mục kết quả theo phân công; người phụ trách cập nhật lại bảng này nếu đổi.

## Cấu hình baseline

| Tham số | Giá trị |
|---|---|
| Seed dữ liệu | 42 |
| Seed mô hình | 0, 1, 2 |
| Chuẩn hoá input | `x1/2`, `x2/4` (đưa về [−1, 1]) |
| Kiến trúc baseline | 1 tầng ẩn × 10 nơ-ron, tanh; tầng ra tuyến tính |
| Loss, optimizer | `nn.MSELoss`, Adam, lr = 1e-3 |
| Batch, epoch | 32; tối đa 1000 epoch, early stopping patience 100 theo val loss |
| A baseline cho Exp B, C | 1000 |

## Mốc so sánh

Dự đoán hằng số $\hat y = \bar y_{train}$ cho MSE ≈ 3.4e-3 trên train_pool, 3.8e-3 trên val và 2.7e-3 trên test (`eda/constant_baseline.csv`). Mọi cấu hình MLP phải có MSE thấp hơn hẳn mốc này.

## Định dạng kết quả

Mỗi lần chạy ghi một dòng vào `exps/exp_*/runs.csv`:

```
exp,value,seed,train_mse,val_mse,test_mse,test_mae,test_rmse,best_epoch,train_time_s,n_params
```

`summary.csv` là trung bình ± độ lệch chuẩn theo `value`. Kết quả nào không có log CSV đi kèm thì không đưa vào báo cáo.
