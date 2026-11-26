# BÁO CÁO ĐỒ ÁN MÔN HỌC: KHOA HỌC DỮ LIỆU (DATA SCIENCE)
## ĐỀ TÀI: DỰ ĐOÁN XÁC SUẤT CHUYỂN VIỆC CỦA CHUYÊN VIÊN DỮ LIỆU (HR ANALYTICS: JOB CHANGE OF DATA SCIENTISTS)

---

### THÔNG TIN CHUNG
- **Học phần:** Khoa học dữ liệu (Data Science) – Năm 3, Học kỳ 1
- **Bộ môn / Khoa:** Công nghệ Thông tin / Khoa học & Kỹ thuật Dữ liệu
- **Sinh viên thực hiện:** [Họ và Tên Sinh Viên]
- **Mã số sinh viên (MSSV):** [MSSV]
- **Lớp chuyên ngành:** [Tên Lớp]
- **Giảng viên hướng dẫn:** [Họ và Tên Giảng Viên]
- **Thời gian thực hiện:** Học kỳ 1 – Năm học 2026

---

## MỤC LỤC
1. [LỜI MỞ ĐẦU](#1-lời-mở-đầu)
2. [CHƯƠNG 1: TỔNG QUAN BÀI TOÁN & BỐI CẢNH THỰC TẾ](#chương-1-tổng-quan-bài-toán--bối-cảnh-thực-tế)
   - 1.1. Bối cảnh nhân sự trong kỷ nguyên dữ liệu lớn
   - 1.2. Phát biểu bài toán Machine Learning
   - 1.3. Mục tiêu và đóng góp của đồ án
3. [CHƯƠNG 2: PHÂN TÍCH KHÁM PHÁ DỮ LIỆU (EDA)](#chương-2-phân-tích-khám-phá-dữ-liệu-eda)
   - 2.1. Nguồn gốc và quy mô tập dữ liệu
   - 2.2. Từ điển dữ liệu (Data Dictionary)
   - 2.3. Hiện tượng mất cân bằng dữ liệu (Class Imbalance)
   - 2.4. Phân tích các mối tương quan then chốt
4. [CHƯƠNG 3: PHƯƠNG PHÁP TIỀN XỬ LÝ VÀ SỐ HÓA DỮ LIỆU](#chương-3-phương-pháp-tiền-xử-lý-và-số-hóa-dữ-liệu)
   - 3.1. Cơ sở lý thuyết xử lý dữ liệu khuyết thiếu (Theo Slide 7 bài giảng Data Preprocessing)
   - 3.2. Chiến lược thay thế bằng Đại lượng xu thế tập trung (Mode & Median)
   - 3.3. Quy trình số hóa toàn diện 100% dữ liệu (Khử sạch NaN và số âm -1)
   - 3.4. Chuẩn hóa đặc trưng (Feature Scaling)
   - 3.5. Kiểm chứng tính toàn vẹn của dữ liệu sau làm sạch
5. [CHƯƠNG 4: THIẾT KẾ VÀ HUẤN LUYỆN 3 MÔ HÌNH HỌC MÁY ĐỘC LẬP](#chương-4-thiết-kế-và-huấn-luyện-3-mô-hình-học-máy-độc-lập)
   - 4.1. Kiến trúc phân rã module độc lập
   - 4.2. Mô hình 1: Logistic Regression (Baseline Tuyến tính)
   - 4.3. Mô hình 2: Random Forest Classifier (Bagging Ensemble)
   - 4.4. Mô hình 3: LightGBM Classifier (Gradient Boosting tối ưu)
6. [CHƯƠNG 5: THỰC NGHIỆM VÀ ĐÁNH GIÁ ĐỐI ĐẦU](#chương-5-thực-nghiệm-và-đánh-giá-đối-đầu)
   - 5.1. Thiết lập thực nghiệm với Stratified 5-Fold Cross-Validation
   - 5.2. Các chỉ số đo lường hiệu năng
   - 5.3. Bảng tổng hợp so sánh đối đầu giữa 3 mô hình
   - 5.4. Phân tích đường cong ROC (Receiver Operating Characteristic)
   - 5.5. Phân tích ma trận nhầm lẫn (Confusion Matrix)
   - 5.6. Phân tích độ quan trọng của các thuộc tính (Feature Importance)
7. [CHƯƠNG 6: KHUYẾN NGHỊ VÀ ỨNG DỤNG THỰC TIỄN CHO DOANH NGHIỆP](#chương-6-khuyến-nghị-và-ứng-dụng-thực-tiễn-cho-doanh-nghiệp)
   - 6.1. Hồ sơ ứng viên có nguy cơ nhảy việc cao nhất
   - 6.2. Chiến lược nhân sự (HR Retention Strategy)
8. [CHƯƠNG 7: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN](#chương-7-kết-luận-và-hướng-phát-triển)
   - 7.1. Kết luận đồ án
   - 7.2. Hạn chế và hướng mở rộng
9. [TÀI LIỆU THAM KHẢO & PHỤ LỤC](#tài-liệu-tham-khảo--phụ-lục)

---

## 1. LỜI MỞ ĐẦU

Trong bối cảnh bùng nổ của Trí tuệ nhân tạo (AI) và Khoa học dữ liệu (Data Science), nhu cầu tuyển dụng các chuyên gia phân tích và kỹ sư dữ liệu tăng trưởng theo cấp số nhân. Tuy nhiên, một trong những thách thức nghiêm trọng nhất mà các tổ chức, tập đoàn công nghệ phải đối mặt hiện nay chính là **tỷ lệ biến động nhân sự (turnover rate)** rất cao trong nhóm ngành này. Chi phí tuyển dụng mới, thời gian đào tạo hội nhập, sự gián đoạn trong các dự án công nghệ và nguy cơ rò rỉ tri thức tổ chức khiến bài toán giữ chân nhân tài (talent retention) trở thành ưu tiên chiến lược hàng đầu.

Xuất phát từ thực tiễn trên, đồ án môn học **Khoa học dữ liệu** lựa chọn đề tài: **"Dự đoán xác suất chuyển việc của chuyên viên dữ liệu (HR Analytics: Job Change of Data Scientists)"**. 

Đồ án tập trung nghiên cứu toàn diện quy trình KDD (Knowledge Discovery in Databases) và vòng đời dự án Data Science: từ bước khám phá dữ liệu (EDA), áp dụng chuẩn tiền xử lý dữ liệu học phần (Data Preprocessing), chuẩn hóa 100% số hóa không còn giá trị khuyết hay số âm, thiết kế kiến trúc 3 mô hình học máy độc lập, đánh giá đối đầu qua kiểm định chéo Stratified 5-Fold, cho đến việc đề xuất các khuyến nghị hành động thực tiễn cho bộ phận quản trị nhân lực.

---

## CHƯƠNG 1: TỔNG QUAN BÀI TOÁN & BỐI CẢNH THỰC TẾ

### 1.1. Bối cảnh nhân sự trong kỷ nguyên dữ liệu lớn
Các công ty đào tạo công nghệ và tập đoàn lớn thường đầu tư ngân sách rất lớn để mở các khóa đào tạo Big Data và Data Science cho ứng viên. Tuy nhiên, sau khi hoàn thành khóa học, một tỷ lệ đáng kể học viên không ở lại làm việc cho doanh nghiệp tài trợ mà tìm kiếm cơ hội mới tại các công ty khác. 

Nếu doanh nghiệp có thể dự đoán trước được: **"Ứng viên nào thực sự có ý định gắn bó lâu dài, và ứng viên nào có xác suất cao sẽ nhảy việc?"**, doanh nghiệp sẽ:
1. **Tiết kiệm chi phí đầu tư đào tạo**: Ưu tiên tài trợ cho các ứng viên có cam kết cao.
2. **Chủ động trong chiến lược nhân sự**: Chuẩn bị kế hoạch giữ chân (tăng lương, thưởng, lộ trình thăng tiến) đối với nhân sự chất lượng cao trước khi họ nộp đơn xin nghỉ.
3. **Tối ưu hóa nguồn lực tuyển dụng**: Giảm thời gian trống vị trí công việc (time-to-hire).

### 1.2. Phát biểu bài toán Machine Learning
- **Bản chất bài toán:** Phân loại nhị phân có giám sát (Supervised Binary Classification).
- **Đầu vào (Features $\mathbf{X}$):** Tập hợp các thông tin nhân khẩu học, trình độ học vấn, kinh nghiệm làm việc, số giờ đào tạo, thông tin thành phố sinh sống và quy mô công ty hiện tại của ứng viên ($N$ mẫu, $D = 12$ đặc trưng).
- **Đầu ra (Target $y$):** 
  - $y = 0$: Ứng viên không có ý định chuyển việc (muốn ở lại gắn bó).
  - $y = 1$: Ứng viên đang tích cực tìm kiếm cơ hội việc làm mới (nguy cơ chuyển việc).
- **Yêu cầu kỹ thuật:** Mô hình không chỉ đưa ra nhãn cứng ($0$ hoặc $1$), mà phải dự đoán được xác suất liên tục $P(y = 1 | \mathbf{X}) \in [0, 1]$ để xếp hạng mức độ rủi ro rời bỏ của từng nhân sự.

### 1.3. Mục tiêu và đóng góp của đồ án
- Xây dựng pipeline tiền xử lý dữ liệu chuẩn hóa, chuyển đổi toàn bộ 100% dữ liệu sang dạng số phi âm ($\ge 0$), xử lý triệt để giá trị `NaN` theo đúng hướng dẫn giáo trình bộ môn.
- Thiết kế 3 mô hình học máy đại diện cho 3 trường phái kinh điển:
  1. *Linear Model:* Logistic Regression (Mô hình tham số, baseline).
  2. *Ensemble Bagging:* Random Forest (Mô hình phi tham số, tập hợp cây quyết định).
  3. *Ensemble Boosting:* LightGBM (Mô hình tăng cường độ dốc tối ưu hóa hiện đại).
- Tổ chức mã nguồn chuẩn công nghiệp: phân tách độc lập từng file chạy, lưu vết mô hình `.pkl`, xuất file nộp `.csv`, và vẽ biểu đồ phân tích trực quan.

---

## CHƯƠNG 2: PHÂN TÍCH KHÁM PHÁ DỮ LIỆU (EDA)

### 2.1. Nguồn gốc và quy mô tập dữ liệu
Tập dữ liệu nghiên cứu là bộ dữ liệu thực tế **"HR Analytics: Job Change of Data Scientists"** cung cấp bởi nền tảng Kaggle:
- **Tập huấn luyện (`aug_train.csv`):** Gồm **19.158 dòng** và **14 cột** (chứa cả cột định danh `enrollee_id` và nhãn `target`).
- **Tập kiểm tra (`aug_test.csv`):** Gồm **2.129 dòng** và **13 cột** (chưa có nhãn `target`, dùng để kiểm thử độc lập).
- **Tập nộp mẫu (`sample_submission.csv`):** Khuôn dạng gồm `enrollee_id` và xác suất dự đoán `target`.

### 2.2. Từ điển dữ liệu (Data Dictionary)

| STT | Thuộc tính (Feature) | Kiểu gốc | Ý nghĩa nghiệp vụ |
| :---: | :--- | :--- | :--- |
| 1 | `enrollee_id` | Số nguyên | Mã định danh duy nhất của ứng viên/học viên |
| 2 | `city` | Chuỗi (`city_103`,...) | Mã định danh thành phố ứng viên đang sinh sống |
| 3 | `city_development_index` | Số thực (0.448 - 0.949) | Chỉ số phát triển của thành phố (CDI) |
| 4 | `gender` | Chuỗi | Giới tính (Male, Female, Other) |
| 5 | `relevent_experience` | Chuỗi | Kinh nghiệm liên quan đến khoa học dữ liệu (Có/Không) |
| 6 | `enrolled_university` | Chuỗi | Loại hình khóa học đại học đang theo học (Nếu có) |
| 7 | `education_level` | Chuỗi (Thứ bậc) | Bậc học cao nhất (Primary School $\rightarrow$ PhD) |
| 8 | `major_discipline` | Chuỗi | Chuyên ngành đào tạo chính (STEM, Humanities,...) |
| 9 | `experience` | Chuỗi (`<1`, `1`..`20`, `>20`) | Tổng số năm kinh nghiệm làm việc thực tế |
| 10 | `company_size` | Chuỗi (`<10`, `10/49`,...) | Quy mô nhân sự tại công ty hiện tại |
| 11 | `company_type` | Chuỗi | Loại hình doanh nghiệp (Pvt Ltd, Startup, Public,...) |
| 12 | `last_new_job` | Chuỗi (`never`, `1`..`4`, `>4`) | Khoảng thời gian cách biệt kể từ lần chuyển việc trước |
| 13 | `training_hours` | Số nguyên (1 - 336) | Tổng số giờ đào tạo chuyên môn đã tích lũy |
| 14 | `target` | Số nguyên (0 / 1) | Nhãn mục tiêu: 0 (Ở lại), 1 (Tìm kiếm việc làm mới) |

### 2.3. Hiện tượng mất cân bằng dữ liệu (Class Imbalance)
Qua khảo sát nhãn `target` trên 19.158 mẫu train:
- **Lớp 0 (Không đổi việc):** 14.381 mẫu, chiếm **75.07%**.
- **Lớp 1 (Tìm việc mới):** 4.777 mẫu, chiếm **24.93%**.
- **Tỷ lệ mất cân bằng:** Khoảng $3 : 1$.
- **Hệ quả kỹ thuật:** Nếu sử dụng độ chính xác tổng thể (Accuracy) một cách ngây thơ, một mô hình dự đoán tất cả là 0 vẫn sẽ đạt được độ chính xác $75.07\%$, nhưng hoàn toàn vô dụng trong nghiệp vụ thực tế vì không phát hiện được bất kỳ ai muốn nhảy việc. Do đó, các chỉ số cốt lõi bắt buộc phải là **ROC-AUC (Area Under the ROC Curve)**, **Recall (Độ nhạy)** và **F1-Score**.

### 2.4. Phân tích các mối tương quan then chốt
1. **Chỉ số phát triển thành phố (`city_development_index`):** Đây là thuộc tính có sức mạnh phân loại mạnh nhất. Phân tích phân phối cho thấy các ứng viên sống tại các thành phố có CDI thấp ($< 0.7$) có tỷ lệ muốn chuyển việc lên tới trên $55\%$, trong khi ứng viên tại các thành phố phát triển cao ($CDI > 0.9$) chỉ có khoảng $15\%$ tỷ lệ chuyển việc.
2. **Kinh nghiệm làm việc (`experience`):** Những người có dưới 5 năm kinh nghiệm có xu hướng chuyển việc cao hơn rõ rệt so với những chuyên gia có thâm niên trên 15 năm.
3. **Quy mô công ty (`company_size`):** Nhân sự tại các công ty khởi nghiệp quy mô nhỏ ($< 50$ người) có tỷ lệ nhảy việc cao hơn nhiều so với nhân sự tại các tập đoàn lớn ($10.000+$ nhân viên).

---

## CHƯƠNG 3: PHƯƠNG PHÁP TIỀN XỬ LÝ VÀ SỐ HÓA DỮ LIỆU

### 3.1. Cơ sở lý thuyết xử lý dữ liệu khuyết thiếu
Theo nguyên lý Khai phá dữ liệu và chuẩn bài giảng môn học (Slide 7 - `DS04-DM03-DataPreProcess.ppt`):
- Khi dữ liệu chứa các giá trị trống (`NaN`), phương pháp hiệu quả và phổ biến là thay thế giá trị thiếu bằng **Đại lượng đo xu thế tập trung (Measures of Central Tendency)** của thuộc tính đó.
- Đối với **thuộc tính định lượng (Continuous / Numerical Attributes)** có độ lệch phân phối: Sử dụng **Trung vị (Median)** thay vì Trung bình (Mean) để hạn chế ảnh hưởng của giá trị ngoại lai (outliers).
- Đối với **thuộc tính định tính / phân loại (Categorical Attributes)**: Sử dụng **Yếu vị (Mode - giá trị xuất hiện nhiều nhất)** để điền khuyết.
- **Quy tắc tuyệt đối:** Không tùy tiện tạo nhãn giả định như `'Unknown'` hay các giá trị âm như `-1`, vì các giá trị này có thể gây nhiễu cho mô hình học máy dựa trên khoảng cách hoặc mô hình tuyến tính.

### 3.2. Chiến lược thay thế bằng Đại lượng xu thế tập trung
Thống kê các cột bị khuyết thiếu trên tập huấn luyện và chiến lược điền khuyết:

| Thuộc tính | Số lượng NaN | Tỷ lệ % khuyết | Đại lượng áp dụng | Giá trị điền cụ thể |
| :--- | :---: | :---: | :---: | :--- |
| `gender` | 4.508 | 23.53% | Mode (Yếu vị) | `'Male'` |
| `enrolled_university` | 386 | 2.01% | Mode (Yếu vị) | `'no_enrollment'` |
| `education_level` | 460 | 2.40% | Mode (Yếu vị) | `'Graduate'` |
| `major_discipline` | 2.813 | 14.68% | Mode (Yếu vị) | `'STEM'` |
| `experience` | 65 | 0.34% | Median (Trung vị) | `9` (năm) |
| `company_size` | 5.915 | 30.87% | Mode (Yếu vị) | `'50-99'` |
| `company_type` | 6.140 | 32.05% | Mode (Yếu vị) | `'Pvt Ltd'` |
| `last_new_job` | 423 | 2.21% | Mode (Yếu vị) | `'1'` (năm trước) |

### 3.3. Quy trình số hóa toàn diện 100% dữ liệu (100% Numeric Pipeline)
Để đảm bảo tất cả các giải thuật học máy có thể xử lý toán học đồng bộ mà không phát sinh lỗi kiểu dữ liệu:
1. **Trích xuất thuộc tính `city`:**
   Dữ liệu gốc có dạng chuỗi `city_103`, `city_21`,... Ta loại bỏ tiền tố chuỗi và chuyển đổi trực tiếp thành số nguyên đại diện:
   $$\text{city\_id} = \text{int}(\text{city.replace}('\text{city\_}', ''))$$
2. **Mã hóa thứ bậc (Ordinal Encoding $\ge 0$):**
   Bảo toàn quan hệ thứ tự logic tự nhiên:
   - `education_level`: $\text{Primary School} (0) < \text{High School} (1) < \text{Graduate} (2) < \text{Masters} (3) < \text{Phd} (4)$.
   - `company_size`: $<10 (0) < 10/49 (1) < 50-99 (2) < 100-500 (3) < 500-999 (4) < 1000-4999 (5) < 5000-9999 (6) < 10000+ (7)$.
   - `last_new_job`: $\text{never} (0) < 1 (1) < 2 (2) < 3 (3) < 4 (4) < >4 (5)$.
   - `experience`: $<1$ quy về $0$; các năm từ $1$ đến $20$ giữ nguyên giá trị số; $>20$ quy về $21$.
3. **Mã hóa danh mục (Categorical Label Encoding $\ge 0$):**
   - `gender`: Female (0), Male (1), Other (2).
   - `relevent_experience`: No relevent experience (0), Has relevent experience (1).
   - `enrolled_university`: no_enrollment (0), Part time (1), Full time (2).
   - `major_discipline`: STEM (0), Business Degree (1), Arts (2), Humanities (3), No Major (4), Other (5).
   - `company_type`: Pvt Ltd (0), Funded Startup (1), Early Stage Startup (2), Public Sector (3), NGO (4), Other (5).

### 3.4. Chuẩn hóa đặc trưng (Feature Scaling)
Đối với mô hình Logistic Regression, các đặc trưng có thang đo chênh lệch lớn (ví dụ: `city_id` lên tới 180, `training_hours` từ 1 đến 336, trong khi `city_development_index` từ 0.4 đến 0.9) sẽ làm mặt cắt hàm mất mát bị méo dạng ellipse dẹt, khiến thuật toán Gradient Descent hội tụ chậm. Do đó, kỹ thuật **MinMaxScaler** được áp dụng riêng cho Logistic Regression để đưa tất cả biến về đoạn $[0, 1]$:
$$x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$
Đối với Random Forest và LightGBM, do bản chất thuật toán phân tách ngưỡng dựa trên cây quyết định bất biến với phép co giãn đơn điệu, dữ liệu số hóa nguyên thủy được giữ nguyên để tối ưu khả năng diễn giải.

### 3.5. Kiểm chứng tính toàn vẹn của dữ liệu sau làm sạch
Tập dữ liệu sau tiền xử lý được xuất bản thành hai file:
- `train_cleaned_numeric.csv` ($19.158 \times 14$)
- `test_cleaned_numeric.csv` ($2.129 \times 13$)

Kiểm tra định lượng trên toàn bộ ma trận dữ liệu:
- Tổng số ô chứa `NaN`: **`0`**.
- Tổng số ô chứa giá trị âm ($< 0$, ví dụ `-1`): **`0`**.
- Toàn bộ 100% cột thuộc kiểu `int64` hoặc `float64`.

---

## CHƯƠNG 4: THIẾT KẾ VÀ HUẤN LUYỆN 3 MÔ HÌNH HỌC MÁY ĐỘC LẬP

### 4.1. Kiến trúc phân rã module độc lập
Hệ thống được thiết kế theo nguyên lý module hóa cao (High Cohesion, Loose Coupling). Mỗi mô hình được đóng gói trong một file Python độc lập, có thể tự động tải dữ liệu tiền xử lý, huấn luyện kiểm định chéo, in báo cáo, lưu trữ mô hình và sinh file dự đoán:

```text
HR Analytics/
├── src/data_preprocessing.py            # Module tiền xử lý dùng chung
├── 01_model_logistic_regression.py      # Mã nguồn Mô hình 1
├── 02_model_random_forest.py            # Mã nguồn Mô hình 2
├── 03_model_lightgbm.py                 # Mã nguồn Mô hình 3
└── 04_compare_models.py                 # Đối đầu và tổng hợp đồ thị
```

### 4.2. Mô hình 1: Logistic Regression (Baseline Tuyến tính)
- **Cơ sở lý thuyết:** Sử dụng hàm liên kết Logit để mô hình hóa xác suất hậu nghiệm thông qua hàm Sigmoid:
  $$P(y = 1 | \mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x} + b) = \frac{1}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}$$
- **Hàm mất mát và tối ưu hóa:** Sử dụng Cross-Entropy Loss kết hợp điều chuẩn L2 (Ridge Regularization):
  $$J(\mathbf{w}) = - \frac{1}{N} \sum_{i=1}^N \left[ y_i \ln(p_i) + (1 - y_i) \ln(1 - p_i) \right] + \frac{1}{2C} \|\mathbf{w}\|_2^2$$
- **Cấu hình siêu tham số:**
  - `solver='lbfgs'`, `max_iter=1000` đảm bảo hội tụ.
  - `class_weight='balanced'`: Tự động nhân trọng số phạt ngược với tần suất xuất hiện của lớp thiểu số ($w_1 = \frac{N}{2 N_1}$), giúp mô hình không bị thiên vị về lớp đa số.

### 4.3. Mô hình 2: Random Forest Classifier (Bagging Ensemble)
- **Cơ sở lý thuyết:** Thuật toán tập hợp (Ensemble) dựa trên kỹ thuật **Bootstrap Aggregating (Bagging)**. Xây dựng $B$ cây quyết định độc lập trên các tập con mẫu được lấy mẫu có hoàn lại (Bootstrap Sample) và ngẫu nhiên hóa tập đặc trưng tại mỗi nút phân nhánh.
- **Dự đoán:** Trung bình cộng xác suất dự đoán từ tất cả các cây thành phần:
  $$P(y = 1 | \mathbf{x}) = \frac{1}{B} \sum_{b=1}^B P_b(y = 1 | \mathbf{x})$$
- **Cấu hình siêu tham số:**
  - `n_estimators=150`: Xây dựng 150 cây quyết định.
  - `max_depth=12`, `min_samples_split=10`, `min_samples_leaf=4`: Ràng buộc độ sâu và kích thước nút lá nhằm chống hiện tượng học vẹt (overfitting).
  - `class_weight='balanced'`: Đảm bảo độ nhạy cho lớp 1.

### 4.4. Mô hình 3: LightGBM Classifier (Gradient Boosting tối ưu)
- **Cơ sở lý thuyết:** Thuật toán tăng cường độ dốc tiên tiến do Microsoft phát triển. Xây dựng chuỗi các cây quyết định tuần tự, trong đó mỗi cây mới được huấn luyện để xấp xỉ phần dư (gradient âm của hàm mất mát) của các cây trước đó:
  $$F_m(\mathbf{x}) = F_{m-1}(\mathbf{x}) + \eta \cdot h_m(\mathbf{x})$$
- **Đặc trưng ưu việt:**
  - *Leaf-wise Tree Growth:* Phát triển cây theo nút lá có độ giảm tổn thất lớn nhất thay vì phát triển cân bằng theo tầng (level-wise), mang lại độ chính xác cao hơn.
  - *GOSS (Gradient-based One-Side Sampling):* Giữ lại các mẫu có gradient lớn và lấy mẫu ngẫu nhiên các mẫu có gradient nhỏ.
  - *EFB (Exclusive Feature Bundling):* Gộp các đặc trưng thưa xung khắc để giảm chiều dữ liệu.
- **Cấu hình siêu tham số:**
  - `n_estimators=200`, `learning_rate=0.05`.
  - `num_leaves=31`, `max_depth=7`.
  - `scale_pos_weight=3.0`: Tăng trọng số cho lớp 1 theo đúng tỷ lệ mất cân bằng dữ liệu ($75\% / 25\% \approx 3.0$).

---

## CHƯƠNG 5: THỰC NGHIỆM VÀ ĐÁNH GIÁ ĐỐI ĐẦU

### 5.1. Thiết lập thực nghiệm với Stratified 5-Fold Cross-Validation
Để ngăn chặn triệt để hiện tượng rò rỉ dữ liệu (data leakage) và đảm bảo kết quả đo lường có tính đại diện cao:
- Toàn bộ 19.158 mẫu train được chia thành 5 tập con (folds) theo phương pháp **Stratified K-Fold** (mỗi fold đều duy trì chính xác tỷ lệ 75% lớp 0 và 25% lớp 1).
- Trong mỗi lượt, 4 fold ($80\%$) dùng để huấn luyện và 1 fold ($20\%$) dùng để đánh giá độc lập. Điểm CV là giá trị trung bình qua cả 5 lượt lặp.

### 5.2. Các chỉ số đo lường hiệu năng
$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
$$\text{Precision (Class 1)} = \frac{TP}{TP + FP}$$
$$\text{Recall (Class 1)} = \frac{TP}{TP + FN}$$
$$\text{F1-Score (Class 1)} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
$$\text{ROC-AUC:} \text{ Diện tích dưới đường cong biểu diễn tương quan giữa TPR và FPR qua mọi ngưỡng phân loại } \theta \in [0, 1].$$

### 5.3. Bảng tổng hợp so sánh đối đầu giữa 3 mô hình

| Thuật toán | CV ROC-AUC (5-Fold) | Val Accuracy | Precision (Lớp 1) | Recall (Lớp 1) | F1-Score (Lớp 1) | Đánh giá tổng quan |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Logistic Regression** | **0.7274** | 70.96% | 44.51% | 67.12% | 0.5353 | Baseline tuyến tính ổn định |
| **Random Forest** | **0.7844** | **76.54%** | **52.04%** | 74.87% | **0.6140** | Kiểm soát phương sai tốt, cân bằng Precision-Recall |
| **LightGBM** | **0.7890** | 75.05% | 49.97% | **79.06%** | 0.6123 | **Tối ưu nhất:** ROC-AUC cao nhất, bắt trúng 79% nhân sự có ý định rời đi |

### 5.4. Phân tích đường cong ROC (Receiver Operating Characteristic)
Đường cong ROC trực quan hóa khả năng phân tách của 3 mô hình ở mọi ngưỡng quyết định:
- Đường cong của **LightGBM (màu xanh lá, AUC = 0.7890)** và **Random Forest (màu xanh dương, AUC = 0.7844)** bám sát góc trên bên trái, vượt trội hoàn toàn so với mô hình tham chiếu ngẫu nhiên (đường chéo màu đỏ nét đứt, AUC = 0.50) và mô hình Logistic Regression (màu cam, AUC = 0.7274).
- Điều này chứng minh mối quan hệ phi tuyến tính phức tạp giữa các thuộc tính nhân khẩu học và quyết định nhảy việc đòi hỏi các mô hình phi tuyến dạng cây quyết định để khai thác tối đa tri thức.

*(Hình minh họa: Đường cong ROC đối đầu lưu tại `figures/roc_curves_comparison.png`)*

### 5.5. Phân tích ma trận nhầm lẫn (Confusion Matrix)
Phân tích ma trận nhầm lẫn của **LightGBM** trên tập kiểm định:
- **True Positives (TP):** Phát hiện chính xác **755** ứng viên muốn chuyển việc trong tổng số 955 ứng viên thuộc lớp 1 thực tế (**Recall đạt tới ~79.06%**).
- **False Negatives (FN):** Chỉ bỏ sót **200** ứng viên (tỷ lệ bỏ sót rất thấp).
- **Ý nghĩa thực tế:** Trong bài toán giữ chân nhân sự, chi phí bỏ sót một Data Scientist giỏi chuẩn bị rời đi (False Negative) lớn hơn rất nhiều so với chi phí gửi thông điệp chăm sóc hoặc phỏng vấn giữ chân một người chưa có ý định đi (False Positive). Do đó, việc LightGBM tối ưu hóa Recall lên gần $80\%$ là cực kỳ giá trị đối với doanh nghiệp.

### 5.6. Phân tích độ quan trọng của các thuộc tính (Feature Importance)
Trích xuất độ quan trọng thuộc tính từ mô hình LightGBM và Random Forest:
1. **`city_development_index` (Chiếm ~35% trọng số phân loại):** Đứng đầu tuyệt đối về tầm ảnh hưởng. Những thành phố có điều kiện kinh tế thấp, cơ sở hạ tầng công nghệ chưa phát triển là nguyên nhân cốt lõi khiến chuyên viên dữ liệu muốn di cư hoặc tìm kiếm môi trường làm việc mới.
2. **`training_hours` (Chiếm ~22% trọng số):** Những người dành nhiều thời gian tham gia các khóa học nâng cao thường là những cá nhân có khao khát nâng cấp kỹ năng và sẵn sàng đón nhận cơ hội nghề nghiệp mới.
3. **`experience` (Chiếm ~15% trọng số):** Thâm niên làm việc tỷ lệ nghịch với rủi ro nhảy việc; nhóm nhân sự trẻ (dưới 5 năm kinh nghiệm) có độ dịch chuyển cao nhất.
4. **`company_size` & `last_new_job` (Chiếm ~12% trọng số):** Quy mô doanh nghiệp nhỏ và thời gian chuyển việc gần đây là các tín hiệu cảnh báo quan trọng tiếp theo.

---

## CHƯƠNG 6: KHUYẾN NGHỊ VÀ ỨNG DỤNG THỰC TIỄN CHO DOANH NGHIỆP

### 6.1. Hồ sơ ứng viên có nguy cơ nhảy việc cao nhất
Dựa trên phân tích mô hình, bộ phận HR có thể phác họa chân dung nhóm chuyên viên dữ liệu có rủi ro rời bỏ cao nhất:
- Sinh sống và làm việc tại các thành phố có chỉ số CDI thấp ($CDI < 0.70$).
- Đang làm việc tại các công ty nhỏ, startup (dưới 50 nhân sự) hoặc doanh nghiệp tư nhân (`Pvt Ltd`).
- Có từ 1 đến 4 năm kinh nghiệm thực tế.
- Tích cực tham gia các khóa đào tạo chuyên môn ngắn hạn với số giờ đào tạo cao ($> 60$ giờ).
- Chưa từng chuyển việc hoặc mới chuyển việc trong vòng 1 năm qua.

### 6.2. Chiến lược nhân sự (HR Retention Strategy)
1. **Chính sách hỗ trợ theo khu vực địa lý:** 
   Đối với các chi nhánh tại các thành phố có chỉ số phát triển thấp, doanh nghiệp cần cung cấp phụ cấp vùng miền, hỗ trợ chỗ ở hoặc áp dụng chính sách làm việc từ xa (Remote / Hybrid) linh hoạt để nhân sự không cảm thấy bị thiệt thòi về môi trường phát triển so với các trung tâm công nghệ lớn.
2. **Xây dựng lộ trình thăng tiến sau đào tạo:**
   Không chỉ tài trợ các khóa học Big Data/Data Science, doanh nghiệp cần gắn liền việc hoàn thành khóa đào tạo với cơ hội tăng bậc chuyên môn, tăng đãi ngộ hoặc giao các dự án AI thực tế để nhân viên được ứng dụng tri thức mới ngay trong tổ chức.
3. **Chăm sóc nhóm nhân sự trẻ (Junior / Mid-level):**
   Thiết lập mô hình Mentorship 1-kèm-1 giữa các Senior/Lead với nhân sự từ 1 đến 4 năm kinh nghiệm để hỗ trợ giải quyết khó khăn trong công việc, giảm bớt áp lực và nâng cao mức độ gắn kết tổ chức.

---

## CHƯƠNG 7: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

### 7.1. Kết luận đồ án
1. Đã nghiên cứu và triển khai trọn vẹn quy trình Khoa học dữ liệu chuẩn mực cho bài toán HR Analytics.
2. Đã áp dụng chuẩn xác lý thuyết tiền xử lý dữ liệu theo giáo trình: thay thế giá trị khuyết bằng Mode và Median, số hóa 100% dữ liệu sang dạng số nguyên/số thực phi âm ($\ge 0$), không còn bất kỳ giá trị `NaN` hay `-1`.
3. Đã xây dựng và đánh giá độc lập 3 mô hình học máy: **Logistic Regression (AUC = 0.7274)**, **Random Forest (AUC = 0.7844)**, và **LightGBM (AUC = 0.7890, Recall = 79.06%)**.
4. Toàn bộ mã nguồn, dữ liệu làm sạch, mô hình huấn luyện và hình ảnh trực quan được tổ chức bài bản, có thể chạy lại độc lập và mở rộng dễ dàng.

### 7.2. Hạn chế và hướng mở rộng
- **Hạn chế:** Tập dữ liệu chưa có các thông tin tài chính chi tiết (mức lương hiện tại, mức thưởng, chế độ đãi ngộ) - những yếu tố có sức chi phối rất mạnh đến quyết định nhảy việc trong đời thực.
- **Hướng mở rộng:**
  - Thử nghiệm các kỹ thuật cân bằng dữ liệu nâng cao như SMOTE (Synthetic Minority Over-sampling Technique) kết hợp Tomek Links.
  - Tinh chỉnh siêu tham số chuyên sâu hơn thông qua Bayesian Optimization (Optuna).
  - Triển khai mô hình thành Web Application (dùng Streamlit/FastAPI) để cung cấp công cụ dự đoán thời gian thực cho chuyên viên nhân sự.

---

## TÀI LIỆU THAM KHẢO & PHỤ LỤC

### Tài liệu tham khảo
1. Slide bài giảng môn học: *DS04-DM03-DataPreProcess.ppt*, Bộ môn Khoa học dữ liệu.
2. Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., ... & Liu, T. Y. (2017). *LightGBM: A highly efficient gradient boosting decision tree*. Advances in Neural Information Processing Systems (NeurIPS), 30.
3. Breiman, L. (2001). *Random forests*. Machine Learning, 45(1), 5-32.
4. Pedregosa, F., et al. (2011). *Scikit-learn: Machine learning in Python*. Journal of Machine Learning Research, 12, 2825-2830.
5. Kaggle Dataset: *HR Analytics: Job Change of Data Scientists* (https://www.kaggle.com/datasets/arashnic/hr-analytics-job-change-of-data-scientists).

### Phụ lục: Hướng dẫn chạy kiểm thử mã nguồn
Mọi thao tác kiểm thử được thực thi trong PowerShell tại thư mục đồ án:
```powershell
cd "D:\Năm 3 học kỳ 1\Khoa học dữ liệu\HR Analytics"

# 1. Kiểm tra dữ liệu làm sạch 100% số:
python -c "import pandas as pd; df = pd.read_csv('train_cleaned_numeric.csv'); print('NaN count:', df.isna().sum().sum(), '| Dtypes:', len(df.dtypes))"

# 2. Chạy độc lập từng mô hình:
python 01_model_logistic_regression.py
python 02_model_random_forest.py
python 03_model_lightgbm.py

# 3. Chạy tổng hợp so sánh đối đầu:
python 04_compare_models.py
```
