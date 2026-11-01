# TRI THỨC CỐT LÕI HỌC SÂU (DEEP LEARNING) — TỔNG HỢP 7 TUẦN

> **Kho tri thức tổng hợp toàn diện (Comprehensive Knowledge Base)**  
> **Chương trình:** Học sâu (Deep Learning) — Đại học Sài Gòn (SGU)  
> **Mục tiêu:** Hệ thống hóa toàn bộ lý thuyết, công thức toán học, thuật toán, kiến trúc mô hình, phương pháp tối ưu và thực hành từ Tuần 1 đến Tuần 7 thành tri thức nền tảng chuẩn mực.

---

## MỤC LỤC TỔNG QUAN

1. [TUẦN 1: NỀN TẢNG AI, HỌC MÁY (ML) & CUỘC CÁCH MẠNG HỌC SÂU (DEEP LEARNING)](#tuần-1-nền-tảng-ai-học-máy-ml--cuộc-cách-mạng-học-sâu-deep-learning)
   - 1.1. Khái niệm nền tảng AI – ML – DL
   - 1.2. Lý thuyết Tác tử thông minh (Intelligent Agent) & Bài toán Tìm kiếm
   - 1.3. Bản chất của Học sâu: Học biểu diễn (Representation Learning)
   - 1.4. Cột mốc lịch sử & Đột phá Nobel Vật lý 2024 (Hopfield Network & Boltzmann Machine)
2. [TUẦN 2: QUY TRÌNH XÂY DỰNG MÔ HÌNH (MODELING) & HỆ SINH THÁI SCIKIT-LEARN / PYTORCH](#tuần-2-quy-trình-xây-dựng-mô-hình-modeling--hệ-sinh-thái-scikit-learn--pytorch)
   - 2.1. Vòng đời dự án Học máy (Machine Learning Lifecycle)
   - 2.2. Thiết kế Hướng đối tượng trong Scikit-Learn
   - 2.3. Quy chuẩn thi đấu Kaggle & Kiểm soát Hiện tượng Rò rỉ Dữ liệu (Data Leakage)
   - 2.4. Kiến trúc Nền tảng PyTorch & Cơ chế Tensor / Autograd
3. [TUẦN 3: THẤU HIỂU DỮ LIỆU & TIỀN XỬ LÝ ĐẶC TRƯNG (DATA UNDERSTANDING & PREPROCESSING)](#tuần-3-thấu-hiểu-dữ-liệu--tiền-xử-lý-đặc-trưng-data-understanding--preprocessing)
   - 3.1. Thang đo dữ liệu (Scales of Measurement)
   - 3.2. Thống kê mô tả (Descriptive Statistics) & Phân tích Khám phá (EDA)
   - 3.3. Xử lý Dữ liệu khuyết thiếu (Missing Data Imputation)
   - 3.4. Xử lý Ngoại lai (Outlier Detection & Handling)
   - 3.5. Biến đổi đặc trưng & Chuẩn hóa (Feature Scaling & Transformation)
   - 3.6. Mã hóa Biến phân loại (Categorical Encoding)
4. [TUẦN 4: ĐÁNH GIÁ MÔ HÌNH, LỰA CHỌN MÔ HÌNH & LÝ THUYẾT HỌC (EVALUATION, SELECTION & LEARNING THEORY)](#tuần-4-đánh-giá-mô-hình-lựa-chọn-mô-hình--lý-thuyết-học-evaluation-selection--learning-theory)
   - 4.1. Chiến lược phân chia dữ liệu & Kiểm định chéo (Cross-Validation)
   - 4.2. Hệ thống Đánh giá Mô hình Phân loại (Classification Metrics)
   - 4.3. Hệ thống Đánh giá Mô hình Hồi quy (Regression Metrics)
   - 4.4. Đánh đổi Độ chệch – Phương sai (Bias - Variance Tradeoff)
   - 4.5. Các thuật toán học có giám sát cơ sở (KNN, Decision Trees)
5. [TUẦN 5: MÔ HÌNH HỒI QUY TUYẾN TÍNH (LINEAR REGRESSION) & NỀN TẢNG TỐI ƯU HÓA](#tuần-5-mô-hình-hồi-quy-tuyến-tính-linear-regression--nền-tảng-tối-ưu-hóa)
   - 5.1. Mô hình Hồi quy Tuyến tính Đơn biến & Đa biến
   - 5.2. Hàm mất mát Bình phương Tối thiểu (Ordinary Least Squares - OLS)
   - 5.3. Nghiệm giải tích chính xác (Normal Equation)
   - 5.4. Thuật toán Gradient Descent cho Hồi quy Tuyến tính
   - 5.5. Phân tích Residual và Hệ số Xác định $R^2$
   - 5.6. Triển khai Hồi quy Tuyến tính với PyTorch
6. [TUẦN 6: HỒI QUY LOGISTIC, ĐỒ THỊ TÍNH TOÁN & THUẬT TOÁN TỐI ƯU GRADIENT DESCENT NÂNG CAO](#tuần-6-hồi-quy-logistic-đồ-thị-tính-toán--thuật-toán-tối-ưu-gradient-descent-nâng-cao)
   - 6.1. Hồi quy Logistic (Logistic Regression) & Hàm Sigmoid
   - 6.2. Hàm mất mát Binary Cross-Entropy (BCE Loss) & Dẫn xuất MLE
   - 6.3. Đồ thị Tính toán (Computation Graphs) & Tự động Vi phân (Autograd)
   - 6.4. Các biến thể Gradient Descent: BGD, SGD, Mini-batch GD
   - 6.5. Các bộ tối ưu hóa thích ứng (Momentum, RMSprop, Adam)
7. [TUẦN 7: PERCEPTRON, MẠNG NƠ-RON NHIỀU TẦNG (MLP) & THUẬT TOÁN LAN TRUYỀN NGƯỢC (BACKPROPAGATION)](#tuần-7-perceptron-mạng-nơ-ron-nhiều-tầng-mlp--thuật-toán-lan-truyền-ngược-backpropagation)
   - 7.1. Perceptron Cổ điển (Rosenblatt, 1958) & Giới hạn XOR (Minsky - Papert, 1969)
   - 7.2. Ranh giới quyết định hình học & Miền kích hoạt của Perceptron
   - 7.3. Mạng Nơ-ron Nhiều Tầng (Multilayer Perceptron - MLP)
   - 7.4. Vai trò của Hàm kích hoạt phi tuyến & Định lý Xấp xỉ Phổ quát (Universal Approximation Theorem)
   - 7.5. Khảo sát các hàm kích hoạt (Sigmoid, Tanh, ReLU, Leaky ReLU, Softmax)
   - 7.6. Thuật toán Lan truyền ngược (Backpropagation Algorithm) — Chi tiết Toán học
   - 7.7. Triển khai Mạng MLP với PyTorch `nn.Module`
8. [BẢN ĐỒ LIÊN KẾT TRI THỨC VÀ HỆ THỐNG CÔNG THỨC TOÁN HỌC CỐT LÕI](#bản-đồ-liên-kết-tri-thức-và-hệ-thống-công-thức-toán-học-cốt-lõi)

---

## TUẦN 1: NỀN TẢNG AI, HỌC MÁY (ML) & CUỘC CÁCH MẠNG HỌC SÂU (DEEP LEARNING)

### 1.1. Khái niệm nền tảng AI – ML – DL
- **Trí tuệ nhân tạo (Artificial Intelligence - AI):** Ngành khoa học máy tính hướng tới việc kiến tạo các hệ thống có khả năng mô phỏng hoặc thực thi các hành vi thông minh vốn có của con người (suy luận, học tập, lập kế hoạch, nhận thức, tương tác ngôn ngữ).
- **Học máy (Machine Learning - ML):** Một nhánh cốt lõi của AI. Thay vì lập trình quy tắc tường minh (rule-based / explicit programming), hệ thống tự động học các quy luật ẩn từ dữ liệu kinh nghiệm.
  - *Định nghĩa của Herbert Simon (1983):* "Học tập là bất kỳ quá trình nào mà thông qua đó một hệ thống nâng cao hiệu suất hoạt động của chính mình từ kinh nghiệm."
  - *Định nghĩa hình thức của Tom Mitchell (1997):* "Một chương trình máy tính được xem là học từ kinh nghiệm $E$ đối với một lớp tác vụ $T$ và thước đo hiệu suất $P$, nếu hiệu suất của nó tại các tác vụ trong $T$, được đo bằng $P$, cải thiện theo kinh nghiệm $E$."
- **Học sâu (Deep Learning - DL):** Phân lớp chuyên biệt của ML dựa trên các mạng nơ-ron nhân tạo có nhiều tầng ẩn (multi-layered artificial neural networks), có khả năng tự động học các biểu diễn phân cấp đặc trưng từ dữ liệu thô.

```
+-------------------------------------------------------+
|  Trí tuệ nhân tạo (Artificial Intelligence - AI)     |
|   +-----------------------------------------------+   |
|   |  Học máy (Machine Learning - ML)             |   |
|   |   +---------------------------------------+   |   |
|   |   |  Học sâu (Deep Learning - DL)        |   |   |
|   |   |  (Mạng nơ-ron nhiều tầng, CNN, RNN...) |   |   |
|   |   +---------------------------------------+   |   |
|   +-----------------------------------------------+   |
+-------------------------------------------------------+
```

### 1.2. Lý thuyết Tác tử thông minh (Intelligent Agent) & Bài toán Tìm kiếm
- **Mô hình Tác tử (Agent):** Thực thể nhận thức môi trường thông qua các cảm biến (sensors) và tác động lên môi trường thông qua cơ cấu chấp hành (actuators).
- **Mô hình PEAS:** Tiêu chuẩn định nghĩa môi trường tác vụ gồm:
  - **P**erformance measure (Thước đo hiệu suất).
  - **E**nvironment (Môi trường).
  - **A**ctuators (Cơ cấu tác động).
  - **S**ensors (Cảm biến nhận thức).
- **Giải quyết vấn đề bằng Tìm kiếm (Problem Solving by Searching):**
  - **Không gian trạng thái (State Space):** Trạng thái khởi đầu (Initial state), Tập hành động (Actions), Mô hình chuyển trạng thái (Transition model), Kiểm tra mục tiêu (Goal test), Chi phí đường đi (Path cost).
  - **Tìm kiếm không có thông tin (Uninformed / Blind Search):** BFS (Breadth-First Search - tìm kiếm theo chiều rộng, tìm nghiệm tối ưu khi chi phí các bước bằng nhau), DFS (Depth-First Search - tìm kiếm theo chiều sâu), UCS (Uniform-Cost Search - tìm kiếm với chi phí cực tiểu theo thuật toán Dijkstra).
  - **Tìm kiếm có thông tin (Informed / Heuristic Search):** Thuật toán $A^*$ kết hợp chi phí thực tế $g(n)$ và chi phí ước lượng $h(n)$:
    $$f(n) = g(n) + h(n)$$
    Điều kiện tối ưu của $A^*$: Hàm Heuristic $h(n)$ phải chấp nhận được (admissible: $0 \le h(n) \le h^*(n)$ trên đồ thị cây) và nhất quán (consistent / monotonic: $h(n) \le c(n, a, n') + h(n')$ trên đồ thị tổng quát).
  - **Tìm kiếm cục bộ (Local Search):** Hill-Climbing (leo đồi - dễ kẹt tại cực đại cục bộ, sống trâu hoặc cao nguyên), Simulated Annealing (tôi luyện mô phỏng - cho phép nhảy bước đi xuống với xác suất giảm dần theo nhiệt độ $P = e^{\Delta E / T}$).
  - **Bài toán thỏa mãn ràng buộc (Constraint Satisfaction Problems - CSP):** Tập biến $X$, miền giá trị $D$, tập ràng buộc $C$. Các chiến lược tối ưu giải CSP: MRV (Minimum Remaining Values - biến có ít giá trị khả dụng nhất), LCV (Least Constraining Value - giá trị ít hạn chế các biến khác nhất), Forward Checking và Thuật toán kiểm tra tính nhất quán cung AC-3.

### 1.3. Bản chất của Học sâu: Học biểu diễn (Representation Learning)
*(Theo công trình tổng kết kinh điển của Yann LeCun, Yoshua Bengio & Geoffrey Hinton — Nature 2015)*
- **Hạn chế của ML truyền thống:** Phụ thuộc nặng nề vào quá trình **Trích xuất đặc trưng thủ công (Manual Feature Engineering)** bởi chuyên gia miền ứng dụng (ví dụ: SIFT, HOG cho thị giác máy tính; MFCC cho xử lý âm thanh). Quá trình này thiếu tính linh hoạt, tiêu tốn tài nguyên và không thích ứng khi phân phối dữ liệu thay đổi.
- **Bản chất của Học sâu:** Xây dựng hệ thống học từ đầu đến cuối (**End-to-End Learning**). Mạng nơ-ron tự động biến đổi biểu diễn ở tầng thấp thành các biểu diễn trừu tượng hơn ở tầng cao:
  - *Ảnh thô (Pixels)* $\rightarrow$ Cạnh/Góc (Edges) $\rightarrow$ Họa tiết cục bộ (Textures) $\rightarrow$ Bộ phận (Parts) $\rightarrow$ Thực thể hoàn chỉnh (Objects).
- **Bộ ba đột phá giúp Học sâu bùng nổ:**
  1. **Big Data:** Dữ liệu số hóa khổng lồ (ImageNet, Common Crawl...) cung cấp mẫu huấn luyện phong phú.
  2. **Năng lực tính toán (Compute - GPU/TPU):** Kiến trúc xử lý song song ma trận hàng nghìn nhân rút ngắn thời gian huấn luyện từ hàng tháng xuống hàng giờ.
  3. **Thuật toán & Kiến trúc mới:** Hàm kích hoạt không bão hòa (ReLU), Kỹ thuật điều chuẩn (Dropout, Batch Normalization), Tối ưu hóa vi phân tự động (Backpropagation, SGD, Adam), và các kiến trúc chuyên sâu: CNN (ảnh), RNN/LSTM/Transformer (chuỗi và ngôn ngữ).

### 1.4. Cột mốc lịch sử & Đột phá Nobel Vật lý 2024 (Hopfield Network & Boltzmann Machine)
*(Giải Nobel Vật lý 2024 trao cho John Hopfield và Geoffrey Hinton nhằm tôn vinh các phát minh nền tảng cho mạng nơ-ron nhân tạo)*
- **Mạng Hopfield (John Hopfield, 1982):**
  - Mô hình lấy cảm hứng từ hệ vật lý chất rắn (mô hình spin Ising trong vật lý từ tính).
  - Mạng gồm $N$ nơ-ron nhị phân liên kết hai chiều đối xứng ($w_{ij} = w_{ji}, w_{ii} = 0$).
  - **Hàm năng lượng (Energy Function):**
    $$E = -\frac{1}{2}\sum_{i}\sum_{j} w_{ij} s_i s_j - \sum_{i} b_i s_i$$
  - Khi cập nhật trạng thái nơ-ron theo quy tắc ngưỡng, năng lượng $E$ luôn đơn điệu giảm hoặc giữ nguyên cho tới khi rơi vào điểm cực tiểu cục bộ (attractor / năng lượng tối thiểu).
  - Mạng hoạt động như một **Bộ nhớ liên tưởng (Associative Memory)**: Dù đầu vào bị méo mó hoặc thiếu chi tiết, mạng vẫn có khả năng khôi phục lại mẫu ký ức nguyên bản đã lưu trữ.
- **Cỗ máy Boltzmann (Geoffrey Hinton & Terry Sejnowski, 1985):**
  - Đưa tính xác suất và khái niệm nhiệt động lực học thế kỷ 19 vào mạng nơ-ron.
  - Xác suất một cấu hình trạng thái $s$ tuân theo phân phối Boltzmann:
    $$P(s) = \frac{1}{Z} e^{-\frac{E(s)}{k_B T}}$$
    *(trong đó $Z = \sum_{s} e^{-E(s)/k_B T}$ là hàm phân chia partition function).*
  - **Restricted Boltzmann Machine (RBM, Hinton 2002):** Giới hạn liên kết giữa các nút, chỉ có liên kết giữa tầng hiển thị (visible) và tầng ẩn (hidden), không có liên kết nội tầng. Thuật toán **Contrastive Divergence (CD-k)** giúp học trọng số hiệu quả.
  - **Cuộc hồi sinh năm 2006:** Hinton đề xuất kỹ thuật **Tiền huấn luyện không giám sát từng tầng (Layer-wise Unsupervised Pre-training)** bằng cách xếp chồng các RBM (Deep Belief Networks), giải quyết triệt để bài toán bế tắc tối ưu hóa trong mạng sâu, mở màn cho kỷ nguyên Deep Learning hiện đại.

---

## TUẦN 2: QUY TRÌNH XÂY DỰNG MÔ HÌNH (MODELING) & HỆ SINH THÁI SCIKIT-LEARN / PYTORCH

### 2.1. Vòng đời dự án Học máy (Machine Learning Lifecycle)
Quy trình xây dựng mô hình thực tế tuân theo tiêu chuẩn công nghiệp (như CRISP-DM):
1. **Hiểu bài toán nghiệp vụ (Problem Understanding):** Xác định bài toán thuộc phân lớp nào (Hồi quy, Phân loại nhị phân, Phân loại đa lớp, Gom cụm, v.v.), chỉ số kinh doanh mục tiêu.
2. **Thu thập & Khám phá Dữ liệu (Data Collection & Exploration):** Thu thập dữ liệu nguồn, phân tích thống kê mô tả, trực quan hóa khám phá phân phối và quan hệ.
3. **Tiền xử lý Dữ liệu (Data Preprocessing):** Làm sạch, điền khuyết, xử lý ngoại lai, mã hóa, co giãn thang đo.
4. **Kỹ nghệ Đặc trưng (Feature Engineering):** Tạo đặc trưng mới, trích xuất đặc trưng có giá trị phân loại/dự đoán cao, chọn lọc biến.
5. **Huấn luyện Mô hình (Model Training):** Thử nghiệm đa dạng các thuật toán cơ sở và nâng cao trên tập Train.
6. **Đánh giá & Tinh chỉnh (Evaluation & Hyperparameter Tuning):** Đo lường hiệu suất trên tập Validation bằng các metric chuẩn xác, tối ưu siêu tham số (GridSearchCV, RandomizedSearchCV, Bayesian Optimization).
7. **Kiểm thử & Triển khai (Testing & Deployment):** Kiểm chứng mô hình lần cuối trên tập Test độc lập; đóng gói container và triển khai API serving.

### 2.2. Thiết kế Hướng đối tượng trong Scikit-Learn
Scikit-Learn tuân thủ các quy tắc thiết kế phần mềm mẫu mực thông qua 3 giao diện đối tượng:
- **Estimators (Bộ ước lượng):** Khởi tạo mô hình và học tham số từ dữ liệu qua phương thức `.fit(X, y)`.
- **Transformers (Bộ biến đổi):** Dùng để tiền xử lý đặc trưng. Sở hữu phương thức `.transform(X)` hoặc kết hợp `.fit_transform(X)`.
- **Predictors (Bộ dự đoán):** Thực hiện suy luận dự đoán nhãn hoặc giá trị qua `.predict(X)` và xác suất qua `.predict_proba(X)`.
- **Pipeline & ColumnTransformer:**
  - `Pipeline`: Chuỗi tuần tự các bước Transformer và kết thúc bằng một Estimator/Predictor, giúp tự động hóa toàn bộ quy trình từ dữ liệu thô đến dự đoán, ngăn chặn hoàn toàn việc rò rỉ dữ liệu.
  - `ColumnTransformer`: Cho phép áp dụng các biến đổi độc lập cho từng nhóm cột đặc trưng (ví dụ: chuẩn hóa cho cột số, One-Hot cho cột phân loại).

### 2.3. Quy chuẩn thi đấu Kaggle & Kiểm soát Hiện tượng Rò rỉ Dữ liệu (Data Leakage)
- **Cấu trúc Cuộc thi Kaggle:**
  - **Train Set:** Dữ liệu có nhãn dùng để xây dựng, huấn luyện mô hình và cross-validation.
  - **Test Set:** Dữ liệu không nhãn gửi cho thí sinh. Hệ thống tự động chia làm 2 phần:
    - *Public Leaderboard:* Đánh giá trên một phần nhỏ (ví dụ 30%) của Test set để hiển thị thứ hạng tạm thời trong thời gian thi đấu.
    - *Private Leaderboard:* Đánh giá trên phần còn lại (70%) được giữ bí mật hoàn toàn cho đến khi cuộc thi kết thúc nhằm xác định kết quả chung cuộc.
- **Hiện tượng Quá khớp Leaderboard (Overfitting to Public Leaderboard):** Thí sinh liên tục tinh chỉnh mô hình theo điểm Public LB, dẫn đến mô hình khớp với nhiễu của tập Public và sụp đổ thứ hạng (shake-up) trên Private LB.
- **Nguyên tắc Phòng chống Rò rỉ Dữ liệu (Data Leakage):**
  - Không bao giờ áp dụng các biến đổi thống kê (như tính Mean, Median, Min, Max, hoặc fit Scaler) trên toàn bộ dữ liệu gộp.
  - Quy tắc bất di bất dịch: **Chỉ gọi `.fit()` trên tập huấn luyện (Train set)**, sau đó áp dụng phép biến đổi `.transform()` cho Validation và Test set.

### 2.4. Kiến trúc Nền tảng PyTorch & Cơ chế Tensor / Autograd
- **PyTorch Tensor:** Cấu trúc dữ liệu mảng đa chiều tương tự NumPy ndarray nhưng được tối ưu hóa cho phần cứng GPU/TPU:
  - Thuộc tính cốt lõi: `shape` (kích thước các chiều), `dtype` (kiểu dữ liệu số như `float32`, `int64`), `device` (nơi lưu trữ trên bộ nhớ `cpu` hoặc `cuda:0`).
- **Autograd Engine (Cơ chế Đạo hàm Tự động):**
  - Cờ `requires_grad=True`: Bật cơ chế theo dõi tất cả các phép toán thực hiện trên Tensor để xây dựng đồ thị tính toán động (dynamic computational graph).
  - Phương thức `.backward()`: Kích hoạt lan truyền ngược, tự động áp dụng quy tắc chuỗi để tính gradient của hàm mục tiêu (Loss) đối với tensor tham số.
  - Thuộc tính `.grad`: Chứa giá trị đạo hàm riêng $\frac{\partial \text{Loss}}{\partial w}$ sau khi gọi backward.
  - Phương thức `.detach()` hoặc khối lệnh `with torch.no_grad():`: Tắt việc tính toán và lưu đồ thị đạo hàm, giúp tiết kiệm bộ nhớ khi đánh giá hoặc suy luận.

---

## TUẦN 3: THẤU HIỂU DỮ LIỆU & TIỀN XỬ LÝ ĐẶC TRƯNG (DATA UNDERSTANDING & PREPROCESSING)

### 3.1. Thang đo dữ liệu (Scales of Measurement)
Stanley Smith Stevens (1946) phân loại dữ liệu thành 4 thang đo cơ bản:
1. **Nominal (Định danh):** Các nhãn phân loại không có thứ tự hay quan hệ hơn kém (Ví dụ: Giới tính {Nam, Nữ}, Mã sinh viên, Màu sắc {Đỏ, Xanh, Vàng}). Các phép toán hợp lệ: Tần số (Frequency), Mode, So sánh bằng ($=$ hoặc $\neq$).
2. **Ordinal (Thứ bậc):** Các giá trị có thứ bậc, xếp hạng rõ ràng nhưng khoảng cách giữa các bậc không bằng nhau hoặc không lượng hóa chính xác được (Ví dụ: Trình độ học vấn {Tiểu học, THCS, THPT, Đại học}, Mức độ hài lòng {Kém, Trung bình, Tốt}). Phép toán hợp lệ: Trung vị (Median), Phân vị (Percentiles), Xếp hạng.
3. **Interval (Khoảng):** Dữ liệu số có khoảng cách đều nhau, nhưng **không có điểm 0 tuyệt đối** (điểm 0 chỉ mang tính quy ước) (Ví dụ: Nhiệt độ Celsius/Fahrenheit, Năm lịch sử). Không thể thực hiện phép nhân/chia tỉ lệ ($20^\circ\text{C}$ không phải nóng gấp đôi $10^\circ\text{C}$). Phép toán hợp lệ: Phép cộng, trừ, Trung bình cộng (Mean), Độ lệch chuẩn.
4. **Ratio (Tỉ lệ):** Thang đo hoàn chỉnh nhất, là dữ liệu số có khoảng cách đều và **có điểm 0 tuyệt đối** (tại 0 đại lượng hoàn toàn không tồn tại) (Ví dụ: Thu nhập, Chiều cao, Cân nặng, Tuổi tác, Tốc độ). Thực hiện được mọi phép toán số học gồm nhân và chia tỉ lệ.

### 3.2. Thống kê mô tả (Descriptive Statistics) & Phân tích Khám phá (EDA)
- **Độ tập trung (Central Tendency):**
  - **Mean (Trung bình cộng):** $\bar{x} = \frac{1}{N}\sum_{i=1}^{N} x_i$. Nhạy cảm mạnh với giá trị ngoại lai (outliers).
  - **Median (Trung vị):** Giá trị nằm chính giữa tập dữ liệu đã sắp xếp. Miễn nhiễm (robust) trước các ngoại lai cực trị.
  - **Mode (Yếu vị):** Giá trị xuất hiện với tần suất lớn nhất. Áp dụng được cho cả dữ liệu định danh và định lượng.
  - **Mối quan hệ hình dạng phân phối (Skewness):**
    - Phân phối đối xứng (Chuẩn): $\text{Mean} \approx \text{Median} \approx \text{Mode}$.
    - Lệch phải (Right-skewed / Positive skew): Đuôi kéo dài về bên phải $\rightarrow \text{Mode} < \text{Median} < \text{Mean}$.
    - Lệch trái (Left-skewed / Negative skew): Đuôi kéo dài về bên trái $\rightarrow \text{Mean} < \text{Median} < \text{Mode}$.
- **Độ phân tán (Measures of Dispersion):**
  - **Khoảng biến thiên (Range):** $\text{Range} = x_{max} - x_{min}$.
  - **Phương sai mẫu (Sample Variance):** $s^2 = \frac{1}{N-1}\sum_{i=1}^N (x_i - \bar{x})^2$.
  - **Độ lệch chuẩn (Standard Deviation):** $s = \sqrt{s^2}$.
  - **Khoảng tứ phân vị (Interquartile Range - IQR):** $\text{IQR} = Q_3 - Q_1$, phản ánh mức độ dao động của $50\%$ dữ liệu ở trung tâm.
- **Hệ số tương quan tuyến tính Pearson ($r$):**
  $$r_{xy} = \frac{\sum_{i=1}^N (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^N (x_i - \bar{x})^2}\sqrt{\sum_{i=1}^N (y_i - \bar{y})^2}}$$
  Giá trị $r \in [-1, 1]$. $r > 0$: tương quan thuận; $r < 0$: tương quan nghịch; $r \approx 0$: không có tương quan tuyến tính.

### 3.3. Xử lý Dữ liệu khuyết thiếu (Missing Data Imputation)
- **Cơ chế khuyết thiếu (Rubin, 1976):**
  - **MCAR (Missing Completely at Random):** Dữ liệu bị thiếu hoàn toàn ngẫu nhiên, không phụ thuộc vào bất kỳ biến quan sát hay biến tiềm ẩn nào.
  - **MAR (Missing at Random):** Xác suất thiếu phụ thuộc vào các biến quan sát khác nhưng không phụ thuộc vào chính giá trị bị thiếu đó (Ví dụ: Nam giới ít khi khai báo thu nhập hơn Nữ, nhưng không phụ thuộc mức thu nhập cao hay thấp).
  - **MNAR (Missing Not at Random):** Xác suất thiếu phụ thuộc trực tiếp vào chính giá trị tiềm ẩn của nó (Ví dụ: Những người có thu nhập cực cao thường từ chối khai báo thu nhập).
- **Phương pháp Xử lý:**
  - *Xóa bỏ (Deletion):* Xóa mẫu (Listwise / Row deletion) hoặc xóa thuộc tính (Feature dropping - khi tỷ lệ khuyết quá cao, ví dụ $> 60\%$). Gây mất mát thông tin nếu tập dữ liệu nhỏ.
  - *Điền giá trị thống kê (Simple Imputation):* Điền bằng Mean (nếu phân phối chuẩn), Median (nếu dữ liệu lệch hoặc có ngoại lai) cho biến số; điền bằng Mode hoặc nhãn đặc biệt `"Unknown"` cho biến phân loại.
  - *Phương pháp nội suy mô hình (Advanced Imputation):* KNN Imputer (tìm $K$ mẫu láng giềng gần nhất để lấy giá trị trung bình có trọng số), Iterative Imputer / MICE (xem biến thiếu là biến mục tiêu và huấn luyện mô hình hồi quy dựa trên các biến còn lại).

### 3.4. Xử lý Ngoại lai (Outlier Detection & Handling)
1. **Phương pháp Z-Score (Dành cho phân phối xấp xỉ chuẩn):**
   $$z_i = \frac{x_i - \mu}{\sigma}$$
   Ngưỡng phát hiện ngoại lai kinh điển: $|z_i| > 3$ (chiếm khoảng $0.27\%$ tổng số mẫu theo nguyên tắc thực nghiệm $3\sigma$).
2. **Quy tắc Hàng rào Tukey (Dựa trên IQR - Không phụ thuộc giả định phân phối chuẩn):**
   - Hàng rào dưới (Lower Bound): $LB = Q_1 - 1.5 \times \text{IQR}$.
   - Hàng rào trên (Upper Bound): $UB = Q_3 + 1.5 \times \text{IQR}$.
   - Mẫu $x_i$ bị coi là ngoại lai nếu $x_i < LB$ hoặc $x_i > UB$.
3. **Chiến lược xử lý ngoại lai:** Loại bỏ (trimming), Cắt biên (Winsorization / Capping - ép giá trị ngoài biên về bằng $LB$ hoặc $UB$), hoặc biến đổi dữ liệu (Log transform).

### 3.5. Biến đổi đặc trưng & Chuẩn hóa (Feature Scaling & Transformation)
- **Co giãn Min-Max (Min-Max Normalization):**
  $$x' = \frac{x - x_{min}}{x_{max} - x_{min}} \in [0, 1]$$
  Áp dụng khi dữ liệu có chặn trên/dưới xác định và không có ngoại lai cực trị.
- **Tiêu chuẩn hóa Z-Score (Standardization):**
  $$x' = \frac{x - \mu}{\sigma}$$
  Dữ liệu sau biến đổi có kỳ vọng bằng 0 ($\mu' = 0$) và độ lệch chuẩn bằng 1 ($\sigma' = 1$). Bắt buộc đối với các thuật toán dựa trên khoảng cách (KNN, SVM, K-Means) và tối ưu hóa bằng Gradient Descent nhằm giúp mặt cong hàm mất mát có dạng tròn đều, tăng tốc độ hội tụ.
- **Biến đổi Phi tuyến (Log Transformation):**
  $$x' = \ln(x + 1) \quad (\text{Log1p})$$
  Làm giảm độ lệch phải, biến đổi phân phối lũy thừa (heavy-tailed) hoặc phân phối log-normal về phân phối xấp xỉ chuẩn, giúp các mô hình tuyến tính hoạt động hiệu quả hơn.

### 3.6. Mã hóa Biến phân loại (Categorical Encoding)
- **Ordinal / Label Encoding:** Ánh xạ các giá trị hạng thành số nguyên liên tiếp ($0, 1, 2, \dots$). Chỉ áp dụng cho biến có thứ bậc rõ ràng (ví dụ: Kém $\rightarrow 0$, Trung bình $\rightarrow 1$, Tốt $\rightarrow 2$). Tránh dùng cho biến định danh vì sẽ vô tình áp đặt quan hệ thứ tự sai lệch.
- **One-Hot Encoding:** Tạo $k$ cột nhị phân mới tương ứng với $k$ giá trị phân loại.
  - *Bẫy biến giả (Dummy Variable Trap):* $k$ cột nhị phân có tổng luôn bằng 1, gây ra hiện tượng cộng tuyến hoàn hảo (multicollinearity) trong hồi quy tuyến tính. Giải pháp: Bỏ bớt 1 cột quy chiếu (drop one category $\rightarrow k-1$ cột).
  - *Hạn chế:* Gây bùng nổ số chiều khi biến có độ biến thiên phân loại cao (high cardinality).

---

## TUẦN 4: ĐÁNH GIÁ MÔ HÌNH, LỰA CHỌN MÔ HÌNH & LÝ THUYẾT HỌC (EVALUATION, SELECTION & LEARNING THEORY)

### 4.1. Chiến lược phân chia dữ liệu & Kiểm định chéo (Cross-Validation)
- **Hold-out Split:** Phân chia tập dữ liệu thành Train (huấn luyện tham số), Validation (đánh giá và chỉnh siêu tham số), và Test (kiểm chứng độc lập cuối cùng), thường với tỷ lệ $70/15/15$ hoặc $80/10/10$.
- **$K$-Fold Cross-Validation:** Chia dữ liệu thành $K$ phần bằng nhau. Mô hình được huấn luyện $K$ lần; mỗi lần chọn 1 phần làm Validation và $K-1$ phần còn lại làm Train. Điểm số cuối cùng là trung bình cộng của $K$ lần đánh giá:
  $$\text{CV}_{score} = \frac{1}{K}\sum_{k=1}^K \text{Score}_k$$
- **Stratified $K$-Fold Cross-Validation:** Phân chia $K$-Fold sao cho tỷ lệ phân bổ của các lớp nhãn mục tiêu trong mỗi Fold luôn đồng nhất với tỷ lệ trong toàn bộ tập dữ liệu gốc. Đây là tiêu chuẩn bắt buộc khi làm việc với tập dữ liệu mất cân bằng (imbalanced datasets).
- **Leave-One-Out Cross-Validation (LOOCV):** Trường hợp đặc biệt khi $K = N$ (mỗi lần chỉ giữ đúng 1 mẫu làm validation). Ước lượng không chệch nhưng chi phí tính toán cực cao khi $N$ lớn.

### 4.2. Hệ thống Đánh giá Mô hình Phân loại (Classification Metrics)
#### Ma trận nhầm lẫn (Confusion Matrix)
| | Dự đoán Dương (Predicted Positive - $\hat{y}=1$) | Dự đoán Âm (Predicted Negative - $\hat{y}=0$) |
|:---:|:---:|:---:|
| **Thực tế Dương (Actual Positive - $y=1$)** | **TP** (True Positive) | **FN** (False Negative - Bỏ sót / Sai lầm loại II) |
| **Thực tế Âm (Actual Negative - $y=0$)** | **FP** (False Positive - Báo động giả / Sai lầm loại I) | **TN** (True Negative) |

#### Các thước đo đơn lẻ cốt lõi
- **Accuracy (Độ chính xác tổng thể):**
  $$\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}} = \frac{\sum \text{Đường chéo chính}}{N}$$
  *Hạn chế cốt tử:* Đánh lừa hiệu suất khi dữ liệu mất cân bằng nghiêm trọng (ví dụ: $99\%$ mẫu âm tính, mô hình dự đoán toàn bộ là âm tính vẫn đạt Accuracy $99\%$).
- **Precision (Độ chuẩn xác / Dương tính chuẩn xác):**
  $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$
  Trả lời câu hỏi: *Trong số các mẫu mô hình dự đoán là Dương tính, có bao nhiêu phần trăm là thực sự chính xác?* Cần tối đa hóa Precision trong các bài toán mà chi phí của FP rất đắt (như bộ lọc Spam, phát hiện giao dịch lừa đảo).
- **Recall / Sensitivity / Hit Rate (Độ nhạy / Tỷ lệ phát hiện thực tế):**
  $$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
  Trả lời câu hỏi: *Trong số tất cả các ca thực tế là Dương tính, mô hình đã dò tìm được bao nhiêu phần trăm?* Cần tối đa hóa Recall trong các bài toán mà chi phí của FN cực kỳ nguy hiểm (như chẩn đoán y tế ung thư, phát hiện mã độc).
- **Specificity (Độ đặc hiệu / Tỷ lệ âm tính thực sự):**
  $$\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}$$
- **$F_1$-Score (Trung bình điều hòa giữa Precision và Recall):**
  $$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2\text{TP}}{2\text{TP} + \text{FP} + \text{FN}}$$
  Sử dụng Harmonic Mean đảm bảo $F_1$ chỉ đạt giá trị cao khi cả Precision và Recall đều đồng thời cao (nếu một trong hai chỉ số tiến gần về 0, $F_1$ sẽ bị kéo sụt giảm mạnh).
- **Tổng quát $F_\beta$-Score:**
  $$F_\beta = (1 + \beta^2) \frac{\text{Precision} \times \text{Recall}}{\beta^2 \text{Precision} + \text{Recall}}$$
  - Khi $\beta = 2$: Coi trọng Recall gấp đôi Precision ($F_2$-Score).
  - Khi $\beta = 0.5$: Coi trọng Precision gấp đôi Recall ($F_{0.5}$-Score).

#### Chiến lược đánh giá Bài toán Đa lớp (Multiclass Evaluation)
Với ma trận nhầm lẫn kích thước $C \times C$:
- **Macro-average:** Tính metric độc lập cho từng lớp rồi lấy trung bình số học:
  $$\text{Macro-Metric} = \frac{1}{C}\sum_{c=1}^C \text{Metric}_c$$
  Đánh giá bình đẳng mọi lớp, giúp làm nổi bật hiệu suất trên các lớp hiếm (minority classes).
- **Micro-average:** Tổng gộp toàn bộ $\text{TP}, \text{FP}, \text{FN}$ trên mọi lớp lại trước khi tính toán:
  $$\text{Micro-Precision} = \frac{\sum_{c=1}^C \text{TP}_c}{\sum_{c=1}^C \text{TP}_c + \sum_{c=1}^C \text{FP}_c}$$
  Bị chi phối mạnh bởi các lớp chiếm số lượng áp đảo (majority classes).
- **Weighted-average:** Tính trung bình có trọng số theo kích thước hỗ trợ (support $N_c$) của từng lớp:
  $$\text{Weighted-Metric} = \sum_{c=1}^C \left(\frac{N_c}{N}\right) \text{Metric}_c$$

#### Đường cong ROC và PR-AUC
- **ROC (Receiver Operating Characteristic):** Biểu diễn mối quan hệ đánh đổi giữa $\text{TPR}$ (Recall) trên trục tung và $\text{FPR} = 1 - \text{Specificity}$ trên trục hoành khi thay đổi ngưỡng phân loại threshold từ 1 về 0.
- **AUC-ROC:** Diện tích dưới đường cong ROC ($\in [0.5, 1.0]$). Thể hiện xác suất mà mô hình xếp hạng một mẫu dương tính ngẫu nhiên cao hơn một mẫu âm tính ngẫu nhiên.
- **PR-AUC (Precision-Recall Curve):** Đường cong biểu diễn quan hệ giữa Precision và Recall. Được ưu tiên hàng đầu khi phân tích dữ liệu có tỷ lệ mất cân bằng cực lớn vì không bị nhiễu bởi số lượng khổng lồ của TN.

### 4.3. Hệ thống Đánh giá Mô hình Hồi quy (Regression Metrics)
Cho $y_i$ là giá trị thực tế, $\hat{y}_i$ là giá trị dự đoán, $\bar{y}$ là giá trị trung bình thực tế:
- **Mean Squared Error (MSE):**
  $$\text{MSE} = \frac{1}{N}\sum_{i=1}^N (y_i - \hat{y}_i)^2$$
  Trừng phạt rất nặng các sai số lớn do có phép bình phương; có đạo hàm trơn liên tục, là hàm mục tiêu tối ưu chuẩn mực.
- **Root Mean Squared Error (RMSE):**
  $$\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{N}\sum_{i=1}^N (y_i - \hat{y}_i)^2}$$
  Đưa sai số về cùng đơn vị đo lường gốc của biến mục tiêu, dễ diễn giải thực tế.
- **Mean Absolute Error (MAE):**
  $$\text{MAE} = \frac{1}{N}\sum_{i=1}^N |y_i - \hat{y}_i|$$
  Phản ánh độ lớn sai số tuyệt đối trung bình, ít bị ảnh hưởng bởi các ngoại lai cực trị hơn MSE.
- **Hệ số xác định $R^2$ (Coefficient of Determination):**
  $$R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - \bar{y})^2}$$
  Đo lường tỷ lệ phần trăm phương sai của biến mục tiêu được giải thích bởi các đặc trưng trong mô hình ($R^2 = 1$: mô hình khớp hoàn hảo; $R^2 = 0$: mô hình tương đương việc luôn dự đoán giá trị trung bình $\bar{y}$; $R^2 < 0$: mô hình dự đoán tệ hơn cả việc đoán trung bình).
- **Adjusted $R^2$ (Hệ số $R^2$ hiệu chỉnh):**
  $$R^2_{adj} = 1 - \left[\frac{(1 - R^2)(N - 1)}{N - p - 1}\right]$$
  *(với $N$ là số mẫu, $p$ là số lượng biến dự báo).* Trừng phạt việc thêm các biến đặc trưng vô bổ vào mô hình hồi quy đa biến.

### 4.4. Đánh đổi Độ chệch – Phương sai (Bias - Variance Tradeoff)
Sai số dự đoán kỳ vọng trên tập dữ liệu kiểm tra phân rã thành ba thành phần toán học độc lập:
$$\mathbb{E}\left[(y - \hat{f}(x))^2\right] = \underbrace{\left(\text{Bias}\left[\hat{f}(x)\right]\right)^2}_{\text{Độ chệch bình phương}} + \underbrace{\text{Var}\left[\hat{f}(x)\right]}_{\text{Phương sai mô hình}} + \underbrace{\sigma^2}_{\text{Nhiễu không thể giảm (Irreducible Error)}}$$

```
    Sai số
      ^
      |        \                        /  Sai số kiểm thử (Test Error)
      |         \    Vùng tối ưu       /
      |          \      |             /   Phương sai (Variance)
      |           \     v            /    /
      |            \   ---          /    /
      |             \ /   \        /    /
      |--------------X-----------------/------------------
      |             / \     \         /
      |            /   \     -------/
      |           /     \          /
      |          /       ---------/------ Độ chệch (Bias^2)
      +---------------------------------------------------->
          Mô hình đơn giản              Mô hình phức tạp
          (Underfitting)                (Overfitting)
```

- **Underfitting (Khớp dưới - High Bias):** Mô hình quá đơn giản, không học được quy luật thực sự của dữ liệu. Biểu hiện: Lỗi trên cả tập Train và Validation đều cao. Giải pháp: Tăng độ phức tạp của mô hình, bổ sung thêm đặc trưng, giảm mức độ điều chuẩn (regularization).
- **Overfitting (Quá khớp - High Variance):** Mô hình quá phức tạp, ghi nhớ luôn cả nhiễu ngẫu nhiên của tập Train. Biểu hiện: Lỗi tập Train rất thấp nhưng lỗi tập Validation lại rất cao (khoảng cách sai số phân kỳ). Giải pháp: Thu thập thêm dữ liệu huấn luyện, giảm bớt đặc trưng, áp dụng kỹ thuật điều chuẩn ($L_1$ Lasso, $L_2$ Ridge, Dropout), áp dụng Early Stopping.

### 4.5. Các thuật toán học có giám sát cơ sở (KNN, Decision Trees)
- **K-Nearest Neighbors (KNN):**
  - Thuộc loại giải thuật học lười (**Lazy Learning** / Instance-based learning) do không có pha huấn luyện tường minh; toàn bộ tính toán diễn ra tại thời điểm suy luận.
  - Dự đoán nhãn cho mẫu mới bằng cách tính khoảng cách (Euclidean: $d(x, z) = \sqrt{\sum (x_j - z_j)^2}$, Manhattan: $d(x, z) = \sum |x_j - z_j|$) đến toàn bộ các điểm dữ liệu và bỏ phiếu theo đa số trong $K$ láng giềng gần nhất.
  - $K$ nhỏ: Ranh giới quyết định gấp khúc, dễ Overfitting (phương sai cao). $K$ lớn: Ranh giới mượt mà, dễ Underfitting (độ chệch cao).
- **Cây quyết định (Decision Tree):**
  - Xây dựng mô hình cây phân cấp bằng cách liên tục phân chia tập dữ liệu tại mỗi nút dựa trên đặc trưng và ngưỡng tối ưu.
  - **Độ tinh khiết Gini (Gini Impurity - dùng trong thuật toán CART):**
    $$Gini(D) = 1 - \sum_{i=1}^C p_i^2$$
  - **Độ hỗn loạn Entropy (Entropy - dùng trong thuật toán ID3 / C4.5):**
    $$\text{Entropy}(D) = -\sum_{i=1}^C p_i \log_2(p_i)$$
  - **Độ lợi thông tin (Information Gain):** Mức độ suy giảm Entropy sau khi phân chia theo thuộc tính $A$:
    $$\text{Gain}(D, A) = \text{Entropy}(D) - \sum_{v \in \text{Values}(A)} \frac{|D_v|}{|D|} \text{Entropy}(D_v)$$
  - Cắt tỉa cây (Pruning - Pre-pruning như `max_depth`, `min_samples_split` và Post-pruning) là kỹ thuật sống còn để ngăn chặn cây quyết định bị quá khớp.

---

## TUẦN 5: MÔ HÌNH HỒI QUY TUYẾN TÍNH (LINEAR REGRESSION) & NỀN TẢNG TỐI ƯU HÓA

### 5.1. Mô hình Hồi quy Tuyến tính Đơn biến & Đa biến
- **Phương trình Hồi quy Tuyến tính Đơn biến:**
  $$\hat{y} = w x + b$$
- **Phương trình Hồi quy Tuyến tính Đa biến ($d$ đặc trưng):**
  $$\hat{y} = w_1 x_1 + w_2 x_2 + \dots + w_d x_d + b = \mathbf{w}^T \mathbf{x} + b$$
- **Dạng Ma trận hóa cho toàn bộ tập dữ liệu gồm $N$ mẫu:**
  Bằng cách bổ sung cột số 1 vào ma trận thiết kế $\mathbf{X}$ để gộp hệ số chệch $b$ vào vector trọng số $\mathbf{w} = [b, w_1, w_2, \dots, w_d]^T$:
  $$\hat{\mathbf{y}} = \mathbf{X}\mathbf{w} \quad \text{với } \mathbf{X} \in \mathbb{R}^{N \times (d+1)}, \; \mathbf{w} \in \mathbb{R}^{(d+1) \times 1}, \; \hat{\mathbf{y}} \in \mathbb{R}^{N \times 1}$$

### 5.2. Hàm mất mát Bình phương Tối thiểu (Ordinary Least Squares - OLS)
Hàm mục tiêu đo lường độ lệch giữa giá trị dự đoán và nhãn thực tế:
$$J(\mathbf{w}) = \frac{1}{2N} \sum_{i=1}^N \left(\hat{y}^{(i)} - y^{(i)}\right)^2 = \frac{1}{2N} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 = \frac{1}{2N} (\mathbf{X}\mathbf{w} - \mathbf{y})^T (\mathbf{X}\mathbf{w} - \mathbf{y})$$
*(Hệ số $\frac{1}{2}$ nhằm triệt tiêu số mũ 2 khi lấy đạo hàm).*

### 5.3. Nghiệm giải tích chính xác (Normal Equation)
Khai triển hàm mất mát dưới dạng ma trận:
$$J(\mathbf{w}) = \frac{1}{2N} \left(\mathbf{w}^T \mathbf{X}^T \mathbf{X} \mathbf{w} - 2\mathbf{y}^T \mathbf{X}\mathbf{w} + \mathbf{y}^T \mathbf{y}\right)$$
Tính đạo hàm riêng (gradient) theo vector trọng số $\mathbf{w}$ và cho bằng vector 0:
$$\nabla_{\mathbf{w}} J(\mathbf{w}) = \frac{1}{N} \left(\mathbf{X}^T \mathbf{X} \mathbf{w} - \mathbf{X}^T \mathbf{y}\right) = \mathbf{0}$$
$$\iff \mathbf{X}^T \mathbf{X} \mathbf{w} = \mathbf{X}^T \mathbf{y}$$
Khi ma trận vuông $\mathbf{X}^T \mathbf{X}$ khả nghịch (full-rank), nghiệm giải tích tối ưu duy nhất là:
$$\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$

- **Trường hợp đơn biến rút gọn:**
  $$w = \frac{\sum_{i=1}^N (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^N (x_i - \bar{x})^2} = \frac{SS_{xy}}{SS_{xx}}, \qquad b = \bar{y} - w \bar{x}$$
- **So sánh Nghiệm giải tích và Thuật toán Lặp:**
  - *Nghiệm giải tích (Normal Equation):* Cho nghiệm chính xác tuyệt đối sau một bước tính, không cần chọn learning rate. Tuy nhiên, phép nghịch đảo ma trận có độ phức tạp tính toán $O(d^3)$, không khả thi khi số lượng đặc trưng $d$ lớn ($d > 10^4$).
  - *Gradient Descent:* Có độ phức tạp tính toán mỗi vòng lặp $O(N \cdot d)$, mở rộng tốt với dữ liệu quy mô lớn hàng triệu mẫu và hàng triệu chiều.

### 5.4. Thuật toán Gradient Descent cho Hồi quy Tuyến tính
- Thuật toán tối ưu lặp bắt đầu từ một điểm khởi tạo ngẫu nhiên $\mathbf{w}^{(0)}$ và di chuyển ngược hướng gradient của hàm mất mát:
  $$\mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \alpha \nabla_{\mathbf{w}} J\left(\mathbf{w}^{(t)}\right)$$
  *(trong đó $\alpha > 0$ là tốc độ học - learning rate).*
- **Quy tắc cập nhật tường minh cho từng trọng số:**
  $$\frac{\partial J}{\partial w_j} = \frac{1}{N} \sum_{i=1}^N \left(\hat{y}^{(i)} - y^{(i)}\right) x_j^{(i)}$$
  $$\frac{\partial J}{\partial b} = \frac{1}{N} \sum_{i=1}^N \left(\hat{y}^{(i)} - y^{(i)}\right)$$
  $$w_j \leftarrow w_j - \alpha \left[\frac{1}{N} \sum_{i=1}^N \left(\hat{y}^{(i)} - y^{(i)}\right) x_j^{(i)}\right]$$
  $$b \leftarrow b - \alpha \left[\frac{1}{N} \sum_{i=1}^N \left(\hat{y}^{(i)} - y^{(i)}\right)\right]$$

### 5.5. Phân tích Residual và Hệ số Xác định $R^2$
- **Phần dư (Residual):** $e_i = y_i - \hat{y}_i$.
- **Đẳng thức Phân rã Tổng bình phương (Sum of Squares Decomposition):**
  $$\underbrace{\sum_{i=1}^N (y_i - \bar{y})^2}_{SS_{tot} \text{ (Tổng biến thiên toàn phần)}} = \underbrace{\sum_{i=1}^N (\hat{y}_i - \bar{y})^2}_{SS_{reg} \text{ (Biến thiên giải thích bởi mô hình)}} + \underbrace{\sum_{i=1}^N (y_i - \hat{y}_i)^2}_{SS_{res} \text{ (Biến thiên phần dư không giải thích được)}}$$
- **Mối quan hệ định lượng:**
  $$R^2 = \frac{SS_{reg}}{SS_{tot}} = 1 - \frac{SS_{res}}{SS_{tot}}$$

### 5.6. Triển khai Hồi quy Tuyến tính với PyTorch
Chu trình huấn luyện (training loop) chuẩn mực gồm 5 bước cốt lõi:
```python
import torch
import torch.nn as nn
import torch.optim as optim

# 1. Định nghĩa mô hình hồi quy tuyến tính
model = nn.Linear(in_features=d, out_features=1)

# 2. Khởi tạo hàm mất mát và bộ tối ưu hóa
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 3. Vòng lặp huấn luyện chuẩn
for epoch in range(num_epochs):
    # Bước a: Lan truyền xuôi (Forward pass)
    predictions = model(X_train)
    loss = criterion(predictions, y_train)
    
    # Bước b: Xóa sạch gradient tích lũy từ bước trước
    optimizer.zero_grad()
    
    # Bước c: Lan truyền ngược (Backward pass) tính toán gradient
    loss.backward()
    
    # Bước d: Cập nhật trọng số mô hình
    optimizer.step()
```

---

## TUẦN 6: HỒI QUY LOGISTIC, ĐỒ THỊ TÍNH TOÁN & THUẬT TOÁN TỐI ƯU GRADIENT DESCENT NÂNG CAO

### 6.1. Hồi quy Logistic (Logistic Regression) & Hàm Sigmoid
Hồi quy Logistic là mô hình phân loại xác suất nhị phân ($y \in \{0, 1\}$).
- **Hàm Logistic / Sigmoid:**
  $$\sigma(z) = \frac{1}{1 + e^{-z}} = \frac{e^z}{1 + e^z}$$
- **Đặc tính giải tích cốt lõi của hàm Sigmoid:**
  1. Miền giá trị: $\sigma(z) \in (0, 1)$, cho phép ánh xạ mọi giá trị thực $z \in (-\infty, +\infty)$ thành xác suất.
  2. Tính đối xứng: $\sigma(-z) = 1 - \sigma(z)$.
  3. **Đạo hàm trơn tuyệt đẹp:**
     $$\sigma'(z) = \frac{d}{dz}\left(\frac{1}{1 + e^{-z}}\right) = \frac{e^{-z}}{(1 + e^{-z})^2} = \left(\frac{1}{1 + e^{-z}}\right) \left(\frac{e^{-z}}{1 + e^{-z}}\right) = \sigma(z)(1 - \sigma(z))$$
- **Mô hình hóa Xác suất Dự đoán:**
  $$z = \mathbf{w}^T \mathbf{x} + b$$
  $$P(y = 1 \mid \mathbf{x}) = \hat{y} = \sigma(z) = \frac{1}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}$$
  $$P(y = 0 \mid \mathbf{x}) = 1 - \hat{y} = 1 - \sigma(z)$$
- **Tỉ số Chênh (Odds) và Log-Odds (Logit):**
  $$\text{Odds} = \frac{P(y=1\mid\mathbf{x})}{1 - P(y=1\mid\mathbf{x})} = \frac{\hat{y}}{1 - \hat{y}} = e^{\mathbf{w}^T \mathbf{x} + b}$$
  $$\ln\left(\frac{\hat{y}}{1 - \hat{y}}\right) = \mathbf{w}^T \mathbf{x} + b = z$$
  *Ranh giới quyết định (Decision Boundary):* Khi phân loại theo ngưỡng chuẩn $P \ge 0.5 \iff z \ge 0 \iff \mathbf{w}^T \mathbf{x} + b = 0$, tạo ra một siêu phẳng ranh giới tuyến tính trong không gian đặc trưng.

### 6.2. Hàm mất mát Binary Cross-Entropy (BCE Loss) & Dẫn xuất MLE
Vì bài toán phân loại có nhãn nhị phân, phân phối xác suất của nhãn $y \in \{0, 1\}$ có điều kiện theo đầu vào là phân phối Bernoulli:
$$P(y \mid \mathbf{x}) = \hat{y}^y (1 - \hat{y})^{1-y}$$
Với tập dữ liệu huấn luyện gồm $m$ mẫu độc lập cùng phân phối (i.i.d.), hàm hợp lý (Likelihood Function) là:
$$L(\mathbf{w}, b) = \prod_{i=1}^m P(y^{(i)} \mid \mathbf{x}^{(i)}) = \prod_{i=1}^m \left(\hat{y}^{(i)}\right)^{y^{(i)}} \left(1 - \hat{y}^{(i)}\right)^{1 - y^{(i)}}$$
Lấy logarit tự nhiên để chuyển tích thành tổng (Log-Likelihood):
$$\ln L(\mathbf{w}, b) = \sum_{i=1}^m \left[ y^{(i)} \ln \hat{y}^{(i)} + (1 - y^{(i)}) \ln \left(1 - \hat{y}^{(i)}\right) \right]$$
Áp dụng nguyên lý ước lượng hợp lý cực đại (MLE - Maximum Likelihood Estimation), ta cực đại hóa $\ln L$, tương đương với cực tiểu hóa hàm **Negative Log-Likelihood / Binary Cross-Entropy Loss**:
$$J(\mathbf{w}, b) = -\frac{1}{m} \sum_{i=1}^m \left[ y^{(i)} \ln \hat{y}^{(i)} + (1 - y^{(i)}) \ln \left(1 - \hat{y}^{(i)}\right) \right]$$

- **Đạo hàm của hàm mất mát BCE (Chi tiết từng bước qua Quy tắc Chuỗi):**
  Xét một mẫu dữ liệu với $L = - [y \ln \hat{y} + (1 - y) \ln (1 - \hat{y})]$, trong đó $\hat{y} = \sigma(z)$ và $z = \mathbf{w}^T \mathbf{x} + b$:
  1. Đạo hàm của $L$ theo $\hat{y}$:
     $$\frac{\partial L}{\partial \hat{y}} = -\left(\frac{y}{\hat{y}} - \frac{1 - y}{1 - \hat{y}}\right) = -\frac{y(1 - \hat{y}) - (1 - y)\hat{y}}{\hat{y}(1 - \hat{y})} = \frac{\hat{y} - y}{\hat{y}(1 - \hat{y})}$$
  2. Đạo hàm của $\hat{y}$ theo $z$:
     $$\frac{\partial \hat{y}}{\partial z} = \sigma'(z) = \hat{y}(1 - \hat{y})$$
  3. Áp dụng quy tắc chuỗi cho $\frac{\partial L}{\partial z}$:
     $$\frac{\partial L}{\partial z} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} = \left(\frac{\hat{y} - y}{\hat{y}(1 - \hat{y})}\right) \cdot \left(\hat{y}(1 - \hat{y})\right) = \hat{y} - y$$
  4. Đạo hàm theo tham số trọng số và bias:
     $$\frac{\partial L}{\partial w_j} = \frac{\partial L}{\partial z} \frac{\partial z}{\partial w_j} = (\hat{y} - y) x_j, \qquad \frac{\partial L}{\partial b} = \frac{\partial L}{\partial z} \frac{\partial z}{\partial b} = (\hat{y} - y)$$
  5. Gradient trung bình trên toàn bộ $m$ mẫu:
     $$\frac{\partial J}{\partial w_j} = \frac{1}{m}\sum_{i=1}^m \left(\hat{y}^{(i)} - y^{(i)}\right) x_j^{(i)}, \qquad \frac{\partial J}{\partial b} = \frac{1}{m}\sum_{i=1}^m \left(\hat{y}^{(i)} - y^{(i)}\right)$$
  *(Nhận xét then chốt: Dạng biểu thức gradient của BCE trong Logistic Regression giống hệt MSE trong Linear Regression, nhưng bản chất $\hat{y}$ ở đây là hàm phi tuyến Sigmoid chứ không phải hàm tuyến tính).*

### 6.3. Đồ thị Tính toán (Computation Graphs) & Tự động Vi phân (Autograd)
- **Cấu trúc Đồ thị Tính toán:** Là một đồ thị có hướng không chu trình (Directed Acyclic Graph - DAG), trong đó:
  - *Nút lá (Leaf Nodes):* Chứa dữ liệu đầu vào ($x$) và tham số mô hình ($w, b$).
  - *Nút phép toán (Operation Nodes):* Đại diện cho các phép toán cơ bản ($+, \times, \exp, \ln, \dots$).
  - *Nút gốc (Root Node):* Biểu diễn giá trị hàm mất mát vô hướng cuối cùng (Loss $L$).
- **Quy trình Tính toán Hai Pha:**
  1. **Lan truyền xuôi (Forward Pass):** Tính tuần tự giá trị của từng nút trung gian từ các nút lá hướng về nút gốc theo thứ tự topo.
  2. **Lan truyền ngược (Backward Pass):** Bắt đầu từ nút gốc với $\frac{\partial L}{\partial L} = 1$. Tại mỗi nút trung gian $u$, áp dụng quy tắc chuỗi để tính gradient hạ nguồn:
     $$\frac{\partial L}{\partial u} = \sum_{v \in \text{Children}(u)} \frac{\partial L}{\partial v} \cdot \frac{\partial v}{\partial u}$$
     *(Gradient tích lũy = Gradient thượng nguồn $\times$ Gradient cục bộ).*

```
  [x] ---> (*) ---> [z] ---> [Sigmoid] ---> [y_hat] ---> [BCE Loss] ---> (L)
            ^        ^
  [w] ------+        |
  [b] ---------------+
```

### 6.4. Các biến thể Gradient Descent: BGD, SGD, Mini-batch GD
| Tiêu chí | Batch Gradient Descent (BGD) | Stochastic Gradient Descent (SGD) | Mini-batch Gradient Descent |
|:---|:---|:---|:---|
| **Kích thước Batch ($B$)** | Toàn bộ tập dữ liệu ($B = N$) | Đúng 1 mẫu ($B = 1$) | Một nhóm nhỏ ($B \in [32, 512]$) |
| **Tính chất Gradient** | Gradient chính xác tuyệt đối của toàn bộ tập dữ liệu | Gradient có tính xấp xỉ nhiễu cao (noisy / stochastic) | Gradient xấp xỉ tốt, cân bằng hoàn hảo |
| **Đường đi hội tụ** | Đi thẳng, mượt mà về cực tiểu | Dao động mạnh (zig-zag), nhảy qua lại | Mượt mà tương đối, có độ rung vừa đủ |
| **Khả năng thoát cực tiểu địa phương** | Kém, dễ mắc kẹt tại điểm yên ngựa hoặc cực tiểu địa phương nông | Rất tốt nhờ nhiễu ngẫu nhiên hỗ trợ nhảy khỏi vùng phẳng | Tốt, khai thác được các đặc tính tối ưu của bề mặt phi lồi |
| **Tận dụng phần cứng** | Kém hiệu quả nếu bộ nhớ RAM/VRAM không chứa hết dữ liệu | Kém, không tận dụng được sức mạnh tính toán song song ma trận của GPU | Tối ưu hóa tối đa năng lực xử lý SIMD/Tensor Cores của GPU |

### 6.5. Các bộ tối ưu hóa thích ứng (Momentum, RMSprop, Adam)
- **Momentum (Khắc phục dao động hẻm vực):** Mô phỏng quán tính của hòn bi lăn xuống dốc, tích lũy vận tốc $v$ từ các gradient quá khứ:
  $$v^{(t+1)} = \beta v^{(t)} + (1 - \beta) \nabla J(\mathbf{w}^{(t)})$$
  $$\mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \alpha v^{(t+1)}$$
  *(với $\beta \approx 0.9$). Giúp triệt tiêu dao động ở các chiều dốc đứng và gia tốc di chuyển dọc theo đáy thung lũng.*
- **RMSprop (Root Mean Square Propagation - Hinton, 2012):** Tự động điều chỉnh tốc độ học cho từng tham số dựa trên trung bình động cấp số nhân của bình phương các gradient:
  $$s^{(t+1)} = \gamma s^{(t)} + (1 - \gamma) \left(\nabla J(\mathbf{w}^{(t)})\right)^{\odot 2}$$
  $$\mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \frac{\alpha}{\sqrt{s^{(t+1)} + \epsilon}} \odot \nabla J(\mathbf{w}^{(t)})$$
  *(với $\gamma \approx 0.99, \epsilon = 10^{-8}$). Giảm learning rate ở các tham số có gradient quá lớn và tăng learning rate cho các tham số có gradient thưa thớt.*
- **Adam (Adaptive Moment Estimation - Kingma & Ba, 2014):** Kết hợp tinh hoa của cả Momentum (ước lượng mô-men bậc 1 $m_t$) và RMSprop (ước lượng mô-men bậc 2 $v_t$), đồng thời bổ sung **Hiệu chỉnh độ lệch (Bias Correction)** giúp mô hình hoạt động chuẩn xác ngay từ các bước khởi đầu:
  $$m^{(t)} = \beta_1 m^{(t-1)} + (1 - \beta_1) g^{(t)}$$
  $$v^{(t)} = \beta_2 v^{(t-1)} + (1 - \beta_2) \left(g^{(t)}\right)^2$$
  $$\hat{m}^{(t)} = \frac{m^{(t)}}{1 - \beta_1^t}, \qquad \hat{v}^{(t)} = \frac{v^{(t)}}{1 - \beta_2^t}$$
  $$\mathbf{w}^{(t)} = \mathbf{w}^{(t-1)} - \frac{\alpha}{\sqrt{\hat{v}^{(t)}} + \epsilon} \hat{m}^{(t)}$$
  *(Giá trị siêu tham số mặc định chuẩn mực: $\alpha = 0.001, \beta_1 = 0.9, \beta_2 = 0.999, \epsilon = 10^{-8}$).*

---

## TUẦN 7: PERCEPTRON, MẠNG NƠ-RON NHIỀU TẦNG (MLP) & THUẬT TOÁN LAN TRUYỀN NGƯỢC (BACKPROPAGATION)

### 7.1. Perceptron Cổ điển (Rosenblatt, 1958) & Giới hạn XOR (Minsky - Papert, 1969)
- **Kiến trúc Perceptron đơn lẻ (Single-Layer Perceptron):**
  - Nhận vector đầu vào $\mathbf{x} = [x_1, x_2, \dots, x_d]^T$.
  - Tính tổng kết hợp tuyến tính có trọng số:
    $$s = \sum_{j=1}^d w_j x_j + b = \mathbf{w}^T \mathbf{x} + b$$
  - Đi qua hàm kích hoạt bước (Heaviside / Step function):
    $$y = \tau(s) = \begin{cases} +1 & \text{nếu } s \ge 0 \\ -1 & \text{nếu } s < 0 \end{cases} \quad \left(\text{hoặc } \{0, 1\}\right)$$
- **Thuật toán Học Perceptron (PLA - Perceptron Learning Algorithm):**
  - Khởi tạo $\mathbf{w} = \mathbf{0}, b = 0$.
  - Lặp qua từng mẫu $(\mathbf{x}^{(k)}, y^{(k)})$. Nếu mẫu bị phân loại sai ($y^{(k)} (\mathbf{w}^T \mathbf{x}^{(k)} + b) \le 0$):
    $$\mathbf{w} \leftarrow \mathbf{w} + \eta y^{(k)} \mathbf{x}^{(k)}$$
    $$b \leftarrow b + \eta y^{(k)}$$
  - *Định lý Hội tụ Novikoff (1962):* Nếu tập dữ liệu phân tách tuyến tính với độ lề (margin) $\gamma > 0$, thuật toán PLA chắc chắn sẽ hội tụ và tìm ra nghiệm siêu phẳng phân chia sau tối đa $\left(\frac{R}{\gamma}\right)^2$ bước cập nhật (với $R = \max \|\mathbf{x}\|_2$).
- **Cú sốc Minsky - Papert (1969) và Bài toán XOR:**
  - Marvin Minsky và Seymour Papert xuất bản cuốn sách *"Perceptrons"* chứng minh về mặt toán học rằng Perceptron đơn tầng chỉ có thể phân loại được các mẫu dữ liệu **phân tách tuyến tính (Linearly Separable)**.
  - Các hàm logic phi tuyến kinh điển như **XOR (Exclusive OR)** và **XNOR** hoàn toàn không thể giải quyết bằng một Perceptron đơn lẻ, vì không tồn tại bất kỳ đường thẳng/siêu phẳng nào có thể phân tách 2 điểm nhãn 1 và 2 điểm nhãn 0 trên mặt phẳng hai chiều.
  - Cuốn sách đã làm dập tắt niềm tin vào mạng nơ-ron và đẩy ngành AI vào giai đoạn thoái trào kéo dài hơn một thập kỷ ("Mùa đông AI lần thứ nhất - First AI Winter").

```
  Hàm AND (Tách được bằng 1 đường thẳng)      Hàm XOR (Bất khả thi với 1 đường thẳng)
         x2                                          x2
         ^                                           ^
       1 |      (0)       (1)                      1 |      (1)       (0)
         |         \                                 |
         |          \                                |
       0 |      (0)  \    (0)                      0 |      (0)       (1)
         +-------------\-----> x1                    +--------------------> x1
                       1                                           1
```

### 7.2. Ranh giới quyết định hình học & Miền kích hoạt của Perceptron
- **Phương trình Siêu phẳng ranh giới quyết định:**
  $$\mathbf{w}^T \mathbf{x} + b = 0 \iff w_1 x_1 + w_2 x_2 + \dots + w_d x_d + b = 0$$
- **Ý nghĩa Hình học của Vector trọng số $\mathbf{w}$:**
  1. Vector $\mathbf{w}$ chính là **vector pháp tuyến** vuông góc với siêu phẳng ranh giới quyết định.
  2. Chiều mũi tên của $\mathbf{w}$ luôn chỉ thẳng về phía nửa không gian nhận nhãn dương ($+1$ hay $s \ge 0$).
  3. Khoảng cách hình học vuông góc từ một điểm dữ liệu $\mathbf{x}_0$ bất kỳ đến siêu phẳng ranh giới là:
     $$d(\mathbf{x}_0, \text{Hyperplane}) = \frac{|\mathbf{w}^T \mathbf{x}_0 + b|}{\|\mathbf{w}\|_2}$$
- **Miền kích hoạt của Mạng Nơ-ron Nhiều Tầng:**
  - Mỗi nơ-ron ở tầng ẩn thứ nhất đóng vai trò như một siêu phẳng chia không gian thành hai nửa mặt phẳng.
  - Các nơ-ron ở tầng ẩn tiếp theo thực hiện các phép giao ($\cap$ tương đương hàm logic AND) hoặc hợp ($\cup$ tương đương hàm logic OR) các nửa mặt phẳng đó.
  - *Hệ quả hình học:* Mạng nơ-ron nhiều tầng có khả năng kiến tạo nên các **miền quyết định đa giác lồi hoặc không lồi (non-convex, arbitrary shaped decision regions)**, giải quyết trọn vẹn bài toán XOR và mọi quan hệ phi tuyến phức tạp.

### 7.3. Mạng Nơ-ron Nhiều Tầng (Multilayer Perceptron - MLP)
Mạng truyền thẳng nhiều tầng (Feedforward Neural Network - FNN) tổ chức các nơ-ron theo các lớp phân cấp tuần tự:
- **Tầng đầu vào (Input Layer $l = 0$):** Nhận vector đặc trưng $\mathbf{a}^{[0]} = \mathbf{x} \in \mathbb{R}^{n_0}$.
- **Các tầng ẩn (Hidden Layers $l = 1, \dots, L-1$):** Trích xuất và biến đổi biểu diễn đặc trưng.
- **Tầng đầu ra (Output Layer $l = L$):** Đưa ra dự đoán cuối cùng $\hat{\mathbf{y}} = \mathbf{a}^{[L]} \in \mathbb{R}^{n_L}$.
- **Công thức Biểu diễn Ma trận Tổng quát tại Tầng $l$:**
  $$\mathbf{z}^{[l]} = \mathbf{W}^{[l]} \mathbf{a}^{[l-1]} + \mathbf{b}^{[l]}$$
  $$\mathbf{a}^{[l]} = g^{[l]}\left(\mathbf{z}^{[l]}\right)$$
  *(trong đó $\mathbf{W}^{[l]} \in \mathbb{R}^{n_l \times n_{l-1}}$ là ma trận trọng số, $\mathbf{b}^{[l]} \in \mathbb{R}^{n_l \times 1}$ là vector bias, và $g^{[l]}(\cdot)$ là hàm kích hoạt của tầng $l$).*

### 7.4. Vai trò của Hàm kích hoạt phi tuyến & Định lý Xấp xỉ Phổ quát
- **Tại sao mạng nơ-ron bắt buộc phải có hàm kích hoạt phi tuyến?**
  Nếu tất cả các tầng ẩn đều sử dụng hàm kích hoạt tuyến tính $g(z) = z$, thì toàn bộ mạng nhiều tầng sâu thẳm sẽ suy biến thành một phép biến đổi tuyến tính affine đơn lẻ:
  $$\mathbf{a}^{[1]} = \mathbf{W}^{[1]} \mathbf{x} + \mathbf{b}^{[1]}$$
  $$\mathbf{a}^{[2]} = \mathbf{W}^{[2]} \mathbf{a}^{[1]} + \mathbf{b}^{[2]} = \mathbf{W}^{[2]}\left(\mathbf{W}^{[1]} \mathbf{x} + \mathbf{b}^{[1]}\right) + \mathbf{b}^{[2]} = \underbrace{\left(\mathbf{W}^{[2]} \mathbf{W}^{[1]}\right)}_{\mathbf{W}'} \mathbf{x} + \underbrace{\left(\mathbf{W}^{[2]}\mathbf{b}^{[1]} + \mathbf{b}^{[2]}\right)}_{\mathbf{b}'}$$
  Như vậy, xếp chồng bao nhiêu tầng tuyến tính đi chăng nữa thì năng lực biểu diễn của mạng cũng chỉ tương đương một mô hình tuyến tính một tầng, hoàn toàn bất lực trước dữ liệu phi tuyến.
- **Định lý Xấp xỉ Phổ quát (Universal Approximation Theorem - Cybenko 1989, Hornik 1991):**
  Một mạng nơ-ron truyền thẳng chỉ cần chứa **duy nhất một tầng ẩn** với số lượng nơ-ron hữu hạn đủ lớn và sử dụng hàm kích hoạt phi tuyến liên tục, không phải hằng số (như Sigmoid), có khả năng xấp xỉ bất kỳ hàm số liên tục nào trên một tập compact trong $\mathbb{R}^n$ với độ chính xác tùy ý $\epsilon > 0$.
  *(Lưu ý: Định lý chứng minh sự tồn tại về mặt toán học nhưng không chỉ ra thuật toán tối ưu để tìm ra bộ trọng số đó, đồng thời một tầng ẩn cực rộng đòi hỏi số nơ-ron tăng theo cấp số nhân; do đó cấu trúc mạng sâu - Deep Neural Network với nhiều tầng ẩn hẹp hơn đem lại hiệu quả biểu diễn và khả năng tổng quát hóa vượt trội hơn nhiều).*

### 7.5. Khảo sát các hàm kích hoạt (Activation Functions)
| Hàm Kích hoạt | Công thức Toán học | Miền giá trị | Đạo hàm | Ưu điểm cốt lõi | Nhược điểm chính |
|:---|:---|:---:|:---:|:---|:---|
| **Sigmoid** | $\sigma(z) = \frac{1}{1 + e^{-z}}$ | $(0, 1)$ | $\sigma(z)(1 - \sigma(z))$ | Diễn giải trực tiếp thành xác suất | Triệt tiêu gradient (Vanishing Gradient); Không đối xứng qua 0 (not zero-centered) |
| **Tanh** | $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$ | $(-1, 1)$ | $1 - \tanh^2(z)$ | Đối xứng qua 0, gradient mạnh hơn Sigmoid | Vẫn bị bão hòa và triệt tiêu gradient ở 2 đầu ($|z| \gg 0$) |
| **ReLU** | $f(z) = \max(0, z)$ | $[0, +\infty)$ | $\begin{cases} 1 & z > 0 \\ 0 & z \le 0 \end{cases}$ | Không bị bão hòa vùng dương, giải quyết triệt tiêu gradient, tính toán cực nhanh, tạo tính thưa (sparsity) | Hiện tượng "Chết ReLU" (Dying ReLU): nếu $z \le 0$, nơ-ron không bao giờ kích hoạt lại |
| **Leaky ReLU** | $f(z) = \max(\alpha z, z)$ $(\alpha \approx 0.01)$ | $(-\infty, +\infty)$ | $\begin{cases} 1 & z > 0 \\ \alpha & z \le 0 \end{cases}$ | Khắc phục hoàn toàn Dying ReLU bằng cách duy trì độ dốc nhỏ ở vùng âm | Phải điều chỉnh thêm siêu tham số $\alpha$ |
| **ELU** | $\begin{cases} z & z > 0 \\ \alpha(e^z - 1) & z \le 0 \end{cases}$ | $(-\alpha, +\infty)$ | $\begin{cases} 1 & z > 0 \\ f(z) + \alpha & z \le 0 \end{cases}$ | Giá trị trung bình tiến gần 0, đạo hàm mượt mà tại mọi điểm | Tốn chi phí tính toán hàm mũ $\exp$ |
| **Softmax** | $\frac{e^{z_k}}{\sum_{j=1}^C e^{z_j}}$ | $(0, 1)$, $\sum = 1$ | $\begin{cases} p_i(1 - p_i) & i = k \\ -p_i p_k & i \neq k \end{cases}$ | Chuẩn hóa toàn bộ vector đầu ra thành phân phối xác suất đa lớp | Chỉ dùng cho tầng đầu ra, nhạy cảm với tràn số (cần trừ max) |

### 7.6. Thuật toán Lan truyền ngược (Backpropagation Algorithm) — Chi tiết Toán học
Lan truyền ngược (Rumelhart, Hinton & Williams, 1986) là thuật toán áp dụng quy tắc chuỗi vi phân một cách tối ưu để tính đạo hàm riêng của hàm mất mát đối với toàn bộ các trọng số và hệ số chệch trong mạng nơ-ron.

#### Các bước Lan truyền xuôi (Forward Pass)
Với dữ liệu đầu vào $\mathbf{a}^{[0]} = \mathbf{x}$, tính toán lần lượt từ tầng $l = 1$ đến tầng cuối cùng $l = L$:
$$\mathbf{z}^{[l]} = \mathbf{W}^{[l]} \mathbf{a}^{[l-1]} + \mathbf{b}^{[l]}$$
$$\mathbf{a}^{[l]} = g^{[l]}\left(\mathbf{z}^{[l]}\right)$$
Tính hàm mất mát toàn cục $L\left(\mathbf{a}^{[L]}, \mathbf{y}\right)$.

#### 4 Phương trình Vàng của Thuật toán Lan truyền ngược (The 4 Fundamental Equations)
Định nghĩa vector sai số tại tầng $l$ là:
$$\boldsymbol{\delta}^{[l]} \equiv \frac{\partial L}{\partial \mathbf{z}^{[l]}} \in \mathbb{R}^{n_l \times 1}$$

1. **Phương trình 1: Sai số tại Tầng đầu ra ($l = L$):**
   $$\boldsymbol{\delta}^{[L]} = \nabla_{\mathbf{a}^{[L]}} L \odot g'^{[L]}\left(\mathbf{z}^{[L]}\right)$$
   *(trong đó $\odot$ là phép nhân từng phần tử Hadamard product).*
   - *Trường hợp đặc biệt tuyệt đẹp:* Khi kết hợp **Softmax + Cross-Entropy** (hoặc **Sigmoid + Binary Cross-Entropy**), hai số hạng triệt tiêu lẫn nhau, phương trình sai số rút gọn cực kỳ tao nhã:
     $$\boldsymbol{\delta}^{[L]} = \mathbf{a}^{[L]} - \mathbf{y}$$
2. **Phương trình 2: Lan truyền Sai số ngược qua Tầng ẩn ($l \rightarrow l-1$):**
   $$\boldsymbol{\delta}^{[l]} = \left(\left(\mathbf{W}^{[l+1]}\right)^T \boldsymbol{\delta}^{[l+1]}\right) \odot g'^{[l]}\left(\mathbf{z}^{[l]}\right)$$
   *(Sai số của tầng hiện tại bằng chuyển vị của ma trận trọng số tầng kế tiếp nhân với sai số tầng kế tiếp, rồi nhân từng phần tử với đạo hàm kích hoạt của tầng hiện tại).*
3. **Phương trình 3: Gradient theo Vector Bias:**
   $$\frac{\partial L}{\partial \mathbf{b}^{[l]}} = \boldsymbol{\delta}^{[l]}$$
   *(Trên mini-batch gồm $m$ mẫu: $\frac{\partial J}{\partial \mathbf{b}^{[l]}} = \frac{1}{m} \sum_{i=1}^m \boldsymbol{\delta}^{[l](i)}$).*
4. **Phương trình 4: Gradient theo Ma trận Trọng số:**
   $$\frac{\partial L}{\partial \mathbf{W}^{[l]}} = \boldsymbol{\delta}^{[l]} \left(\mathbf{a}^{[l-1]}\right)^T$$
   *(Tích ngoài giữa vector sai số của tầng hiện tại và vector kích hoạt chuyển vị của tầng liền trước. Trên mini-batch: $\frac{\partial J}{\partial \mathbf{W}^{[l]}} = \frac{1}{m} \sum_{i=1}^m \boldsymbol{\delta}^{[l](i)} \left(\mathbf{a}^{[l-1](i)}\right)^T$).*

### 7.7. Triển khai Mạng MLP với PyTorch `nn.Module`
```python
import torch
import torch.nn as nn

class MultilayerPerceptron(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_classes):
        super(MultilayerPerceptron, self).__init__()
        # Khai báo các tầng tuyến tính
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.2)
        self.fc2 = nn.Linear(hidden_dim, num_classes)
        
    def forward(self, x):
        # Định nghĩa luồng tính toán lan truyền xuôi
        out = self.fc1(x)
        out = self.relu(out)
        out = self.dropout(out)
        out = self.fc2(out) # Trả về raw logits (chưa qua Softmax)
        return out

# Khởi tạo mô hình
model = MultilayerPerceptron(input_dim=20, hidden_dim=64, num_classes=3)

# Tiêu chuẩn hàm mất mát phân loại đa lớp
# Lưu ý: nn.CrossEntropyLoss tích hợp sẵn LogSoftmax và NLLLoss
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
```

---

## BẢN ĐỒ LIÊN KẾT TRI THỨC VÀ HỆ THỐNG CÔNG THỨC TOÁN HỌC CỐT LÕI

### 1. Bản đồ Dòng chảy Tri thức (Knowledge Flow: Tuần 1 $\rightarrow$ Tuần 7)

```
[Tuần 1: Nền tảng AI & ML]
       |
       v
[Tuần 2: Modeling Pipeline, Scikit-Learn & PyTorch Tensor]
       |
       v
[Tuần 3: Data Understanding, EDA, Outlier & Transformation]
       |
       v
[Tuần 4: Đánh giá Mô hình, Metrics, Bias-Variance Tradeoff]
       |
       +------------------------------------+
       |                                    |
       v                                    v
[Tuần 5: Hồi quy Tuyến tính]       [Tuần 6: Hồi quy Logistic]
  * Hàm giả thiết: y = w^T x + b     * Hàm giả thiết: y = sigmoid(w^T x + b)
  * Loss: MSE (Bình phương OLS)       * Loss: BCE (Cross-Entropy từ MLE)
  * Tối ưu: Normal Eq & GD           * Tối ưu: Computation Graphs & Autograd
       |                                    |
       +-----------------+------------------+
                         |
                         v
          [Tuần 7: Perceptron & Mạng Nơ-ron Sâu (MLP)]
            * Perceptron cổ điển: y = step(w^T x + b) -> Ranh giới siêu phẳng
            * Bài toán XOR -> Nhu cầu Mạng nhiều tầng (MLP)
            * Hàm kích hoạt phi tuyến (ReLU, Tanh, Softmax) & Xấp xỉ phổ quát
            * Thuật toán Lan truyền ngược (Backpropagation: 4 phương trình vàng)
            * Tối ưu hóa sâu: Momentum, RMSprop, Adam
```

### 2. Bảng Tra cứu Toàn diện Công thức Cốt lõi

| Khái niệm / Mô hình | Công thức Toán học Định nghĩa | Hàm Mất mát / Mục tiêu | Đạo hàm / Gradient Cốt lõi |
|:---|:---|:---|:---|
| **Hồi quy Tuyến tính Đơn** | $\hat{y} = w x + b$ | $MSE = \frac{1}{N}\sum (y_i - \hat{y}_i)^2$ | $w = \frac{SS_{xy}}{SS_{xx}}, \; b = \bar{y} - w\bar{x}$ |
| **Hồi quy Tuyến tính Đa biến** | $\hat{\mathbf{y}} = \mathbf{X}\mathbf{w}$ | $J(\mathbf{w}) = \frac{1}{2N} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2$ | $\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$ |
| **Hồi quy Logistic** | $\hat{y} = \sigma(\mathbf{w}^T \mathbf{x} + b)$ | $J = -\frac{1}{m}\sum [y\ln \hat{y} + (1-y)\ln(1-\hat{y})]$ | $\nabla_{\mathbf{w}} J = \frac{1}{m}\mathbf{X}^T (\hat{\mathbf{y}} - \mathbf{y})$ |
| **Perceptron Cổ điển** | $y = \tau(\mathbf{w}^T \mathbf{x} + b)$ | $L_{PLA} = -\sum_{i \in \mathcal{M}} y^{(i)} (\mathbf{w}^T \mathbf{x}^{(i)} + b)$ | $\mathbf{w} \leftarrow \mathbf{w} + \eta y^{(i)} \mathbf{x}^{(i)}$ |
| **Mạng Nơ-ron Nhiều Tầng** | $\mathbf{a}^{[l]} = g^{[l]}(\mathbf{W}^{[l]}\mathbf{a}^{[l-1]} + \mathbf{b}^{[l]})$ | $L(\mathbf{a}^{[L]}, \mathbf{y})$ (BCE hoặc Cross-Entropy) | $\boldsymbol{\delta}^{[l]} = ((\mathbf{W}^{[l+1]})^T \boldsymbol{\delta}^{[l+1]}) \odot g'^{[l]}(\mathbf{z}^{[l]})$ |
| **Gradient theo Trọng số MLP** | $\frac{\partial L}{\partial \mathbf{W}^{[l]}} = \boldsymbol{\delta}^{[l]} (\mathbf{a}^{[l-1]})^T$ | Phục vụ cập nhật $\mathbf{W}^{[l]} \leftarrow \mathbf{W}^{[l]} - \alpha \frac{\partial L}{\partial \mathbf{W}^{[l]}}$ | $\frac{\partial L}{\partial \mathbf{b}^{[l]}} = \boldsymbol{\delta}^{[l]}$ |
| **Độ chính xác Phân loại** | $F_1 = \frac{2 \cdot P \cdot R}{P + R}$ | Đánh giá phân loại mất cân bằng | $P = \frac{TP}{TP+FP}, \; R = \frac{TP}{TP+FN}$ |
| **Hệ số Xác định** | $R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$ | Đánh giá độ phù hợp của mô hình hồi quy | $SS_{res} = \sum (y_i - \hat{y}_i)^2$ |

---
*Tài liệu này được tạo tự động và đồng bộ trực tiếp vào cơ sở tri thức hệ thống nhằm phục vụ suy luận, giải toán, thiết kế kiến trúc và gỡ lỗi cho toàn bộ các bài toán Học sâu.*
