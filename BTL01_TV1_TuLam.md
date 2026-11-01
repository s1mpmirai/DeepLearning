# BTL01 – TV1: Tự làm lại và chuẩn bị bảo vệ

Cách dùng: làm từng bước **không mở code có sẵn**. Mỗi bước có một tiêu chí "tự kiểm" để biết mình làm đúng chưa.
Phần câu hỏi ở cuối: tự trả lời thành tiếng trước, rồi mới mở mục "Ý chính" để so.

---

## Phần A. Làm lại từng bước

### A0. Đọc đề (15 phút)
- [ ] Đọc `BTL/document/MLP_Exercise - Yeu Cau.pdf` mục 3.1, 5, 6, 9.
- [ ] Tự trả lời: phần của TV1 chiếm bao nhiêu điểm rubric? Những gì "không có minh chứng thì 0 điểm"?
- [ ] Đọc lướt `Sample_Report.pdf` và tự tìm **ít nhất 3 lỗi** (gợi ý: công thức, ma trận C, tập dùng làm validation).

### A1. Tính tay trên giấy (20 phút)
- [ ] Tính det C, C⁻¹, trị riêng của C, hệ số tương quan ρ.
- [ ] Tính f(0, 0) bằng máy tính bỏ túi.
- **Tự kiểm:** det C = 0.35; C⁻¹ ≈ [[5.714, 1.429], [1.429, 0.857]]; ρ ≈ −0.645; f(0,0) ≈ 0.269021.

### A2. Viết lại hàm Gaussian (30 phút)
- [ ] Tạo file nháp mới, viết `gaussian_2d(x)` bằng NumPy theo đúng công thức, nhận x có shape (n, 2).
- [ ] So với `scipy.stats.multivariate_normal(mu, C).pdf(x)` trên vài nghìn điểm ngẫu nhiên.
- [ ] Dùng `scipy.integrate.dblquad` tính tích phân trên miền rộng (≈ 1) và trên miền đề bài.
- **Tự kiểm:** sai lệch với scipy cỡ 1e-16; tích phân trên miền đề ≈ 0.995.

### A3. Sinh lại dữ liệu và khớp MD5 (30 phút)
- [ ] Dùng `rng = np.random.default_rng(42)`. Với từng tập theo thứ tự train_pool (2000) → val (200) → test (100):
  rút **toàn bộ x1 trước** bằng `rng.uniform(-2, 2, n)`, rồi **toàn bộ x2** bằng `rng.uniform(-4, 4, n)`, rồi tính y.
- [ ] Lưu CSV cột `x1,x2,y`, `index=False`, `float_format="%.17g"`, `lineterminator="\n"`.
- [ ] Tính MD5 file của bạn, so với `BTL/data/metadata.json`.
- **Tự kiểm:** MD5 khớp nghĩa là bạn đã hiểu đúng 100% quy trình. Không khớp → tìm xem khác ở đâu (thứ tự rút? định dạng số? xuống dòng?). Đây là bài tập hay nhất để hiểu "tái lập".

### A4. Kiểm tra dữ liệu (20 phút)
- [ ] Tự viết kiểm tra: không NaN, mọi điểm nằm trong miền, y khớp f(x) tính lại, không có điểm trùng trong và giữa các tập.
- [ ] Tự giải thích: vì sao ba tập rút từ **cùng một** rng vẫn là độc lập?

### A5. EDA (1–1.5 giờ)
- [ ] Vẽ lại 6 hình: scatter 3D ba tập; bề mặt thật + contour; mẫu trên nền contour; histogram x1, x2, y; histogram log10(y) + ECDF; tập con lồng nhau.
- [ ] Tính bảng thống kê, bảng tỷ lệ y vượt ngưỡng, KS test, bảng tập con `pool[:A]`.
- [ ] **Viết nhận xét của chính bạn trước**, rồi mới so với mục 9 trong `BTL/eda/eda.ipynb`.
- **Tự kiểm:** std của x1 ≈ 4/√12 ≈ 1.155, của x2 ≈ 8/√12 ≈ 2.309 (bạn phải giải thích được vì sao).

### A6. Mốc dự đoán hằng số (15 phút)
- [ ] Chứng minh trên giấy: nếu luôn dự đoán ŷ = ȳ thì MSE = phương sai của y.
- [ ] Tính lại MSE trên train/val/test. **Tự kiểm:** ≈ 3.38e-3 / 3.80e-3 / 2.74e-3.

### A7. Chạy lại như người ngoài (20 phút)
- [ ] Clone repo ra thư mục khác (hoặc máy khác), `pip install -r requirements.txt`, chạy hai lệnh trong README.
- [ ] Ghi lại mọi chỗ bị vướng, sửa README cho rõ.

### A8. Viết lại báo cáo mục 1–2 bằng lời của bạn (1–2 giờ)
- [ ] Mở `BTL/Report.docx`, viết lại từng đoạn mục 1 và 2 theo cách bạn hiểu. Giữ nguyên số liệu (chúng lấy từ CSV).
- [ ] Mỗi con số trong báo cáo phải chỉ ra được nó nằm ở file CSV nào (rubric "số liệu truy vết được").
- [ ] Điền bìa: tên giảng viên, số nhóm, họ tên/MSSV các thành viên.

### A9. Việc TV1 còn lại (sau khi có kết quả A, B, C)
- [ ] `experiments.xlsx`: gộp `exps/exp_*/summary.csv` thành các sheet A, B, C + sheet tổng hợp.
- [ ] Gửi TV4 nội dung 2–3 slide (xem Phần C).
- [ ] Ghép báo cáo: dán mục 3–6 của các bạn, đánh lại số Hình/Bảng, cập nhật mục lục (chuột phải → Update Field), điền tỷ lệ đóng góp (tổng 100%).
- [ ] Xuất `Report.pdf`; nén `BTL01_Nhom_HoTen_MSSV.zip`.
- [ ] Merge nhánh `btl01-tv1` vào `main`, đẩy `data/` lên repo chung của nhóm (chỉ một lần).
- [ ] Đóng Word rồi chuyển file "Phân công BTL01…docx" vào `BTL/document/`.

---

## Phần B. Câu hỏi thầy có thể hỏi

### B1. Hàm Gaussian

**1. Vì sao hệ số chuẩn hoá là 1/(2π√det C)? Báo cáo mẫu ghi (2π)^(1/2) đúng không?**
<details><summary>Ý chính</summary>
Công thức tổng quát là 1/((2π)^(d/2)·√det C). Với d = 2 thì (2π)^(2/2) = 2π. Báo cáo mẫu sai. Kiểm chứng: tích phân trên R² ra đúng 1.
</details>

**2. Làm sao biết C là ma trận hiệp phương sai hợp lệ?**
<details><summary>Ý chính</summary>
C đối xứng và xác định dương: hai trị riêng 0.164 và 2.136 đều dương (hoặc C₁₁ = 0.3 > 0 và det C = 0.35 > 0).
</details>

**3. Vì sao đường đồng mức là elip nghiêng? Nghiêng theo hướng nào?**
<details><summary>Ý chính</summary>
Hiệp phương sai −0.5 ≠ 0 nên x1, x2 tương quan, ρ ≈ −0.65 < 0. Vì vậy khi x1 tăng, vùng giá trị cao dịch về x2 âm (elip nghiêng từ trên-trái xuống dưới-phải). Hẹp theo x1 (σ ≈ 0.55), rộng theo x2 (σ ≈ 1.41).
</details>

**4. Giá trị lớn nhất của f là bao nhiêu, ở đâu? Vì sao y_max trong dữ liệu nhỏ hơn?**
<details><summary>Ý chính</summary>
0.269 tại μ = (0, 0). Mẫu lấy ngẫu nhiên nên gần như không rơi đúng vào (0, 0); y_max của train là 0.2675.
</details>

**5. Em tự cài hàm hay dùng thư viện? Kiểm tra đúng bằng cách nào?**
<details><summary>Ý chính</summary>
Tự cài theo công thức. Kiểm tra bằng 3 cách: f(0,0) khớp lý thuyết, so với scipy (sai lệch 1e-16), tích phân bằng 1.
</details>

### B2. Sinh và chia dữ liệu

**6. Vì sao lấy mẫu đều mà không lấy theo phân phối Gaussian?**
<details><summary>Ý chính</summary>
Đề yêu cầu sinh ngẫu nhiên trong miền. Đây là bài toán xấp xỉ hàm, nên mạng phải đúng ở mọi vị trí, kể cả vùng f ≈ 0. Đánh đổi: chỉ khoảng 19% mẫu nằm ở vùng đỉnh (y > 0.05).
</details>

**7. Seed để làm gì? Ba tập rút từ cùng một rng thì có độc lập không?**
<details><summary>Ý chính</summary>
Seed giúp tái lập: chạy lại ra đúng dữ liệu cũ (kiểm bằng MD5). Ba tập là ba đoạn liên tiếp, không chồng nhau, trong cùng một dãy giả ngẫu nhiên, nên độc lập với nhau. Đổi thứ tự sinh sẽ ra dữ liệu khác.
</details>

**8. Vì sao phải có tập validation riêng? Dùng test để chọn mô hình thì sao?**
<details><summary>Ý chính</summary>
Nếu chọn cấu hình theo test thì test đã "tham gia" vào quá trình chọn, nên kết quả trên test lạc quan hơn thực tế (rò rỉ dữ liệu). Val dùng cho early stopping, checkpoint và chọn mô hình; test chỉ chạy một lần ở cuối. Code mẫu mắc đúng lỗi này.
</details>

**9. Tập con lồng nhau `pool[:A]` là gì, sao không rút ngẫu nhiên lại cho mỗi A?**
<details><summary>Ý chính</summary>
pool[:200] ⊂ pool[:400] ⊂ … Khi A tăng chỉ thêm mẫu mới, giữ mẫu cũ, nên khác biệt giữa các A đến từ số lượng mẫu, ít nhiễu do lần rút. Bảng tập con cho thấy tỷ lệ y > 0.05 ổn định 18.5–20%.
</details>

**10. Vì sao lưu CSV mà không sinh lại mỗi lần chạy? MD5 để làm gì?**
<details><summary>Ý chính</summary>
Để mọi thí nghiệm dùng đúng cùng dữ liệu (so sánh công bằng). MD5 phát hiện file bị sửa. CSV ghi với LF để MD5 giống nhau trên Windows/Mac/Linux.
</details>

### B3. Phân tích dữ liệu

**11. Phân bố của y thế nào? Ảnh hưởng gì tới việc đánh giá?**
<details><summary>Ý chính</summary>
Lệch phải mạnh (skew ≈ 2.3): trung bình 0.031, trung vị 0.0036; 63% mẫu y < 0.01. MSE bị chi phối bởi vùng đỉnh, nên cần xem thêm MAE, hình y–ŷ, heatmap lỗi theo vị trí.
</details>

**12. KS test là gì? p-value lớn có chứng minh ba tập giống nhau không?**
<details><summary>Ý chính</summary>
So hai hàm phân phối thực nghiệm; thống kê KS là khoảng cách lớn nhất giữa hai ECDF. p-value lớn chỉ có nghĩa là **không đủ bằng chứng** nói chúng khác, không chứng minh giống nhau.
</details>

**13. Vì sao MSE trên test có thể thấp hơn trên val?**
<details><summary>Ý chính</summary>
Test chỉ có 100 mẫu và tình cờ ít điểm ở đỉnh (8% y > 0.1 so với 11.7% ở train), nên "dễ" hơn. Không có nghĩa mô hình tốt hơn.
</details>

**14. Mốc dự đoán hằng số là gì? Vì sao MSE của nó bằng phương sai?**
<details><summary>Ý chính</summary>
ŷ = ȳ thì MSE = (1/n)Σ(yᵢ − ȳ)² = phương sai. Khoảng 3.8e-3 trên val. MLP nào không thấp hơn hẳn mức này là chưa học được hình dạng hàm.
</details>

**15. Chuẩn hoá x1/2, x2/4 hay z-score? Có rò rỉ không? Có nên chuẩn hoá y?**
<details><summary>Ý chính</summary>
Chia theo miền đã biết, không ước lượng từ dữ liệu nên không rò rỉ. Đưa input về [−1, 1], hợp với tanh (không bão hoà). Nếu dùng z-score thì mean/std phải tính trên train rồi áp dụng cho val/test. Về y: giữ nguyên để MSE cùng đơn vị với f; chuẩn hoá y cũng được nhưng phải đổi ngược trước khi báo cáo.
</details>

**16. Dữ liệu không có nhiễu thì có quá khớp được không?**
<details><summary>Ý chính</summary>
Vẫn có thể: khi ít mẫu (A nhỏ) mà mô hình nhiều tham số, mạng có thể đi qua đúng các điểm train nhưng dao động giữa các điểm. Nhưng không nhiễu thì khó quá khớp hơn nhiều. Đây là lý do có phần mở rộng B lớn / A nhỏ.
</details>

### B4. Vòng train (ai cũng phải trả lời được, chiếm 3 điểm hỏi đáp)

**17. Giải thích một bước train: forward → loss → zero_grad → backward → step. Quên zero_grad thì sao?**
<details><summary>Ý chính</summary>
PyTorch **cộng dồn** gradient vào .grad. Không zero_grad thì gradient các batch cộng lại, bước cập nhật sai và càng lúc càng lớn.
</details>

**18. model.train() / model.eval() khác gì? MLP không có dropout/BatchNorm thì có cần không?**
<details><summary>Ý chính</summary>
Hai hàm này đổi chế độ của các lớp như Dropout, BatchNorm. Với MLP thuần thì kết quả không đổi, nhưng vẫn gọi đúng chỗ vì đó là quy trình chuẩn và rubric chấm.
</details>

**19. torch.no_grad() để làm gì?**
<details><summary>Ý chính</summary>
Không xây đồ thị tính gradient khi validation/test, nên nhanh hơn, tốn ít bộ nhớ hơn, và không vô tình ảnh hưởng tới quá trình train.
</details>

**20. Early stopping và checkpoint hoạt động thế nào?**
<details><summary>Ý chính</summary>
Theo dõi val loss mỗi epoch; khi val loss tốt hơn mức tốt nhất trước đó thì lưu .pth. Sau `patience` epoch không cải thiện thì dừng, rồi nạp lại checkpoint tốt nhất.
</details>

**21. Vì sao tầng ra tuyến tính mà không dùng sigmoid như code mẫu?**
<details><summary>Ý chính</summary>
Đây là bài hồi quy. Sigmoid ép output vào (0, 1) và bão hoà, làm gradient nhỏ. Tầng tuyến tính là lựa chọn chuẩn cho hồi quy.
</details>

**22. MLP 2 → 10 → 1 có bao nhiêu tham số? Với C tầng 10 nơ-ron?**
<details><summary>Ý chính</summary>
Mỗi tầng có (n_vào + 1) × n_ra tham số. 2-10-1: 30 + 11 = 41. C tầng: 41 + 110 × (C − 1).
</details>

**23. MSE, MAE, RMSE khác nhau thế nào?**
<details><summary>Ý chính</summary>
MSE phạt nặng lỗi lớn và có đơn vị là bình phương đơn vị y. RMSE = √MSE, cùng đơn vị với y. MAE ít nhạy với vài điểm lỗi lớn. Với y lệch như bài này, nên báo cáo cả ba.
</details>

---

## Phần C. Nội dung 2–3 slide gửi TV4 (tự soạn, mỗi slide nói khoảng 1 phút)

1. **Bài toán:** công thức f, μ, C, miền; hình bề mặt + contour. Câu chốt: "đỉnh là elip hẹp, nghiêng do ρ ≈ −0.65".
2. **Dữ liệu:** bảng 3 tập (2000 / 200 / 100, seed 42, rút đều); hình mẫu trên contour; 1 dòng về kiểm tra rò rỉ và MD5.
3. **Điều cần lưu ý khi đọc kết quả:** y lệch (63% < 0.01), mốc hằng số MSE ≈ 3.8e-3, test nhỏ nên chọn theo val.

---

## Phần D. Những chỗ AI đã làm mà bạn phải tự quyết hoặc kiểm lại

- [ ] Cách sinh (rút hết x1 rồi đến x2, một rng cho ba tập): bạn có đồng ý không? Nếu nhóm muốn đổi thì phải đổi **trước khi** đẩy `data/` lên repo chung.
- [ ] Hệ quả số 3 ở mục 2.7 (giữ nguyên thang đo y) chỉ là đề xuất; cần TV2 chốt.
- [ ] Danh sách tài liệu tham khảo: mở từng tài liệu xác nhận lại thông tin trước khi nộp.
- [ ] Ghi trung thực trong báo cáo/README nếu khoa yêu cầu khai báo việc dùng công cụ AI.
