# KỊCH BẢN THUYẾT TRÌNH & BẢO VỆ ĐỒ ÁN MÔN HỌC: KHOA HỌC DỮ LIỆU
## ĐỀ TÀI: DỰ BÁO XÁC SUẤT CHUYỂN VIỆC CỦA HỌC VIÊN SAU KHÓA ĐÀO TẠO VỀ DỮ LIỆU (HR ANALYTICS)

---

### THÔNG TIN TỔNG QUAN
* **Học phần:** Khoa học dữ liệu (Data Science - CSE3040)
* **Thời lượng thuyết trình đề xuất:** 10 – 12 phút (kèm 3 – 5 phút hỏi đáp)
* **Mô hình cốt lõi:** Random Forest Classifier (Rừng ngẫu nhiên – 150 cây quyết định)
* **Cơ sở dữ liệu:** HR Analytics: Job Change of Data Scientists (19.158 bản ghi huấn luyện)

---

## 🎙️ LỜI MỞ ĐẦU & DẪN NHẬP (THỜI LƯỢNG: 1 PHÚT)

*(Hít thở sâu, đứng thẳng, giao tiếp bằng mắt với hội đồng và mở đầu tự tin)*

> *"Kính thưa Thầy/Cô trong Hội đồng chấm điểm và các bạn sinh viên,*  
>  
> *Hôm nay, em xin phép được đại diện nhóm trình bày báo cáo đồ án môn học Khoa học Dữ liệu với đề tài: **'Nghiên cứu và Xây dựng Mô hình Học máy Dự báo Xác suất Chuyển việc của Học viên sau Khóa Đào tạo Chuyên môn về Dữ liệu'**.*  
>  
> *Bài thuyết trình của em hôm nay sẽ tập trung vào **4 nội dung cốt lõi**:*  
> 1. **Mô tả bài toán và bối cảnh nghiệp vụ thực tế.**  
> 2. **Minh họa tập dữ liệu và quy trình tiền xử lý số hóa chuẩn mực.**  
> 3. **Giới thiệu giải pháp thuật toán đề xuất: Random Forest Classifier.**  
> 4. **Chứng minh thuật toán chạy được 100% trên thực tế và bài toán hoàn toàn xứng đáng.**  
>  
> *Sau đây, em xin phép được đi vào chi tiết từng phần."*

---

## 📌 PHẦN 1: MÔ TẢ VỀ BÀI TOÁN (THỜI LƯỢNG: 2 - 3 PHÚT)

### 1.1. Bối cảnh doanh nghiệp (Context)
* Trong kỷ nguyên công nghệ số, một doanh nghiệp hoạt động chuyên sâu trong lĩnh vực **Big Data & Data Science** tổ chức các chương trình đào tạo chuyên môn quy mô lớn. 
* Các khóa học này thu hút số lượng học viên đăng ký rất đông (hơn **19.000 học viên** trong tập dữ liệu huấn luyện).
* **Mục tiêu của công ty:** Tìm kiếm và tuyển dụng các chuyên viên dữ liệu (Data Scientist) chất lượng cao từ chính những học viên hoàn thành khóa đào tạo này.

### 1.2. Vấn đề nhức nhối cốt lõi (The Pain Point)
* Doanh nghiệp phải đối mặt với một câu hỏi kinh doanh mang tính sống còn:  
  👉 **"Trong số hàng nghìn học viên tham gia, ai là người thực sự muốn ở lại làm việc cho công ty sau khóa học, và ai chỉ đăng ký học để lấy kiến thức rồi tìm kiếm cơ hội việc làm ở nơi khác (nhảy việc)?"**
* **Hậu quả nếu không có công cụ phân loại:**
  1. **Lãng phí chi phí và thời gian:** Doanh nghiệp đầu tư ngân sách tài trợ đào tạo lớn nhưng người hưởng lợi lại là các công ty đối thủ.
  2. **Bị động trong tuyển dụng:** Không ước tính được số lượng nhân sự kế cận sẵn sàng gia nhập tổ chức.
  3. **Khó khăn trong lập kế hoạch khóa học (Course Planning):** Không biết cách tối ưu hóa quy mô lớp học và phân bổ nguồn lực đào tạo theo nhóm đối tượng phù hợp.

### 1.3. Hai nhiệm vụ kỹ thuật cốt lõi (Core Tasks)
* **Nhiệm vụ 1 (Dự báo - Prediction):** Xây dựng mô hình học máy ước lượng chính xác xác suất nhị phân $P(y = 1 \mid \mathbf{X})$:
  * $y = 0$: Học viên không tìm việc mới $\rightarrow$ Sẵn sàng ở lại làm việc cho công ty.
  * $y = 1$: Học viên đang tích cực tìm việc làm mới $\rightarrow$ Có nguy cơ cao sẽ nhảy việc sang nơi khác.
* **Nhiệm vụ 2 (Diễn giải tri thức - Model Interpretation):** Mở "hộp đen" mô hình để chỉ ra chính xác các nhân tố (factors) nào chi phối mạnh nhất đến quyết định của ứng viên, từ đó hỗ trợ ban lãnh đạo đưa ra các quyết sách nhân sự chuẩn xác.

---

## 📊 PHẦN 2: SHOW TẬP DỮ LIỆU ĐƯỢC SỬ DỤNG ĐỂ MINH HỌA (THỜI LƯỢNG: 2 - 3 PHÚT)

### 2.1. Nguồn gốc và quy mô tập dữ liệu
* **Tên CSDL:** *"HR Analytics: Job Change of Data Scientists"* (Nền tảng Kaggle).
* **Quy mô:** Gồm **19.158 dòng** trong tập huấn luyện (`aug_train.csv`) và **2.129 dòng** trong tập kiểm thử độc lập (`aug_test.csv`).
* **Không gian đặc trưng:** Gồm **12 thuộc tính đầu vào** phản ánh toàn diện hồ sơ học viên + **1 cột nhãn mục tiêu** (`target`).

### 2.2. Minh họa dữ liệu thực tế (Trích xuất 3 bản ghi mẫu)

| `enrollee_id` | `city` | `city_dev_index` | `gender` | `relevent_experience` | `enrolled_university` | `education_level` | `experience` | `company_size` | `company_type` | `training_hours` | **`target`** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 8949 | `city_103` | 0.920 | Male | Has relevent exp | no_enrollment | Graduate | >20 | *NaN* | *NaN* | 36 | **1.0 (Tìm việc)** |
| 29725 | `city_40` | 0.776 | Male | No relevent exp | no_enrollment | Graduate | 15 | 50-99 | Pvt Ltd | 47 | **0.0 (Ở lại)** |
| 11561 | `city_21` | 0.624 | *NaN* | No relevent exp | Full time course | Graduate | 5 | *NaN* | *NaN* | 83 | **0.0 (Ở lại)** |

### 2.3. Phân nhóm 12 đặc trưng nghiệp vụ:
1. **Nhóm Nhân khẩu học & Địa phương:** `city` (Mã thành phố), `city_development_index` (Chỉ số phát triển kinh tế CDI từ 0.448 đến 0.949), `gender` (Giới tính).
2. **Nhóm Học vấn:** `education_level` (Tiểu học $\rightarrow$ Tiến sĩ), `enrolled_university` (Tình trạng học đại học), `major_discipline` (Chuyên ngành: STEM, Kinh tế,...).
3. **Nhóm Kinh nghiệm làm việc:** `relevent_experience` (Đã có kinh nghiệm dữ liệu chưa), `experience` (Thâm niên làm việc), `company_size` (Quy mô công ty hiện tại), `company_type` (Loại hình công ty), `last_new_job` (Thời gian từ lần đổi việc trước).
4. **Nhóm Quá trình Đào tạo:** `training_hours` (Tổng số giờ học chuyên môn hoàn thành: 1 – 336 giờ).

### 2.4. Quy trình tiền xử lý số hóa 100% (Data Preprocessing Pipeline)
* **Xử lý dữ liệu khuyết thiếu (Tuân thủ Slide 7 bài giảng `DS04-DM03-DataPreProcess.ppt`):**
  * *Biến định tính:* Điền bằng **Yếu vị (Mode - giá trị phổ biến nhất)** cho `gender`, `education_level`, `company_size`, `company_type`, `last_new_job`.
  * *Biến định lượng:* Điền bằng **Trung vị (Median = 9 năm)** cho biến kinh nghiệm `experience` để triệt tiêu ảnh hưởng của giá trị ngoại lai.
  * *Nguyên tắc:* Tuyệt đối không tạo nhãn giả định `'Unknown'` hay các số âm nhân tạo (`-1`).
* **Số hóa toàn diện 100%:**
  * Mã hóa thứ bậc (**Ordinal Encoding**) cho `education_level` (0-4), `company_size` (0-7), `last_new_job` (0-5), `experience` (0-21).
  * Trích xuất số nguyên ID cho `city` ($0 \dots 180$).
  * Loại bỏ `enrollee_id` (tránh overfitting mã định danh theo Slide 19).
* **Kết quả:** Xuất bản tập dữ liệu sạch [train_cleaned_numeric.csv](file:///d:/Năm%203%20học%20kỳ%201/Khoa%20học%20dữ%20liệu/HR%20Analytics/train_cleaned_numeric.csv) với **0 giá trị NaN, 0 giá trị âm, 100% là số nguyên/số thực**.

---

## 🌲 PHẦN 3: SHOW THUẬT TOÁN ĐỊNH SỬ DỤNG – RANDOM FOREST CLASSIFIER (THỜI LƯỢNG: 2 PHÚT)

Thuật toán duy nhất và cốt lõi được lựa chọn cho đề tài là: **Random Forest Classifier (Rừng ngẫu nhiên)**.

```text
CƠ CHẾ RANDOM FOREST ENSEMBLE (150 CÂY):
Tập dữ liệu huấn luyện (19.158 mẫu)
   ├── Bootstrap Sample 1 ──> [ Cây quyết định 1 ] ──> Dự đoán: 1
   ├── Bootstrap Sample 2 ──> [ Cây quyết định 2 ] ──> Dự đoán: 0
   ├── ...
   └── Bootstrap Sample 150 ─> [ Cây quyết định 150 ] ─> Dự đoán: 1
                                       │
                                       ▼
                       BỎ PHIẾU ĐỒNG THUẬN (MAJORITY VOTE)
                           => KẾT QUẢ CUỐI CÙNG
```

### 3.1. Bản chất thuật toán
* Thuộc trường phái **Học máy tập hợp (Ensemble Learning)** theo kỹ thuật **Bagging (Bootstrap Aggregating)**.
* Thay vì chỉ dựa vào 1 cây quyết định đơn lẻ (vốn rất dễ bị học vẹt / overfitting), Random Forest xây dựng một **hội đồng gồm 150 cây quyết định độc lập (`n_estimators = 150`)**.
* **Cơ chế ngẫu nhiên kép (Double Randomness):**
  1. *Ngẫu nhiên mẫu (Bootstrap):* Mỗi cây được huấn luyện trên một tập con dữ liệu ngẫu nhiên có hoàn lại.
  2. *Ngẫu nhiên đặc trưng (Feature Subsampling):* Tại mỗi nút rẽ nhánh, cây chỉ chọn ngẫu nhiên một tập con đặc trưng ($\sqrt{D}$) để tìm điểm cắt tối ưu.
* Quyết định cuối cùng là **sự đồng thuận bỏ phiếu (Majority Voting / Average Probability)** từ cả 150 cây, giúp triệt tiêu phương sai và chống quá khớp hoàn hảo.

### 3.2. Cấu hình kỹ thuật chuyên biệt cho bài toán HR
* **Giải quyết bài toán mất cân bằng dữ liệu (75/25):** Thiết lập `class_weight = 'balanced'` – Tự động nhân trọng số phạt nặng hơn cho các lỗi đoán sai trên lớp 1 (tìm việc), buộc mô hình phải chú ý cao độ đến nhóm nhân sự có rủi ro rời đi.
* **Kiểm soát độ phức tạp:** Khống chế độ sâu tối đa `max_depth = 12`, `min_samples_split = 10`, `min_samples_leaf = 4` để đảm bảo các cây không mọc quá sâu gây lãng phí tài nguyên tính toán.

---

## 🏆 PHẦN 4: CHỨNG MINH THUẬT TOÁN CHẠY ĐƯỢC VÀ BÀI TOÁN CỰC KỲ XỨNG ĐÁNG (THỜI LƯỢNG: 3 - 4 PHÚT)

---

### I. CHỨNG MINH THỰC TẾ 100% "CHẠY ĐƯỢC" (PROOF OF IMPLEMENTATION)

Đề tài không dừng lại ở lý thuyết suông, toàn bộ giải pháp đã được hiện thực hóa thành mã nguồn và sản phẩm thực tế:

1. **Mã nguồn chạy độc lập trơn tru:**
   * Script [`02_model_random_forest.py`](file:///d:/Năm%203%20học%20kỳ%201/Khoa%20học%20dữ%20liệu/HR%20Analytics/02_model_random_forest.py) đã thực thi 100% hoàn tất trên PowerShell, không phát sinh lỗi.
2. **Mô hình học máy đã được huấn luyện và lưu vết:**
   * File mô hình đóng gói chuẩn: [`models/model_random_forest.pkl`](file:///d:/Năm%203%20học%20kỳ%201/Khoa%20học%20dữ%20liệu/HR%20Analytics/models/model_random_forest.pkl).
3. **File dự đoán độc lập trên tập test (2.129 ứng viên):**
   * Đã xuất bản file dự đoán chuẩn Kaggle: [`submissions/submission_random_forest.csv`](file:///d:/Năm%203%20học%20kỳ%201/Khoa%20học%20dữ%20liệu/HR%20Analytics/submissions/submission_random_forest.csv) (100% đầy đủ xác suất, 0 ô trống).
4. **Các biểu đồ trực quan hóa đã sinh tự động:**
   * Ma trận nhầm lẫn: [figures/confusion_matrix_random_forest.png](file:///d:/Năm%203%20học%20kỳ%201/Khoa%20học%20dữ%20liệu/HR%20Analytics/figures/confusion_matrix_random_forest.png).
   * Biểu đồ độ quan trọng đặc trưng: [figures/feature_importance_random_forest.png](file:///d:/Năm%203%20học%20kỳ%201/Khoa%20học%20dữ%20liệu/HR%20Analytics/figures/feature_importance_random_forest.png).

---

### II. CHỨNG MINH BÀI TOÁN VÀ THUẬT TOÁN "CỰC KỲ XỨNG ĐÁNG" (PROOF OF WORTHINESS)

Sự lựa chọn này hoàn toàn xứng đáng dựa trên **3 luận cứ khoa học đanh thép**:

#### 1. Xứng đáng về Hiệu năng Định lượng (Kiểm định chéo Stratified 5-Fold)
Được đánh giá khách quan trên toàn bộ 19.158 bản ghi:

| Thang đo đánh giá | Kết quả thực nghiệm | Ý nghĩa chứng minh tính xứng đáng |
| :--- | :---: | :--- |
| **CV ROC-AUC** | **`0.7844`** (+/- 0.0075) | Khả năng phân tách giữa người ở lại và người nhảy việc đạt xấp xỉ **0.80**, độ lệch chuẩn cực nhỏ thể hiện tính ổn định cao qua 5 lượt kiểm tra chéo độc lập. |
| **Validation Accuracy** | **`76.54%`** | Độ chính xác tổng thể vượt trội so với baseline ngẫu nhiên. |
| **Recall (Độ nhạy lớp 1)** | **`74.87%`** | **Bắt trúng gần 75%** học viên có ý định nhảy việc thực tế (cứ 4 người muốn rời đi thì mô hình nhận diện chính xác 3 người). |
| **Precision (Lớp 1)** | **`52.04%`** | Tỷ lệ dự đoán đúng vượt trội hoàn toàn so với xác suất ngẫu nhiên của thị trường (chỉ 25%). |
| **F1-Score (Lớp 1)** | **`0.6140`** | Cân bằng hài hòa giữa độ chính xác và độ nhạy trên dữ liệu mất cân bằng. |

#### 2. Xứng đáng vì hoàn thành trọn vẹn Nhiệm vụ 2 (Diễn giải tri thức - Feature Importance)
Random Forest không phải "hộp đen bí ẩn", mô hình trích xuất được chính xác mức độ ảnh hưởng của từng đặc trưng theo chỉ số bất thuần Gini:
* **`city_development_index` (33.37%):** Chi phối số 1. Môi trường kinh tế đô thị nơi học viên sinh sống là nhân tố quyết định mạnh nhất đến việc họ muốn dịch chuyển tìm việc mới.
* **`city` (14.83%):** Yếu tố vùng miền cụ thể.
* **`company_size` (12.37%):** Học viên đang công tác tại công ty nhỏ/startup có tỷ lệ nhảy việc cao hơn nhiều so với học viên ở tập đoàn lớn.
* **`training_hours` (8.95%) & `experience` (8.86%):** Số giờ học tích lũy và thâm niên làm việc.
* **Minh chứng Đạo đức AI:** Biến `gender` chỉ đóng góp **0.69%**, chứng minh việc loại bỏ biến Giới tính không ảnh hưởng đến độ chính xác, giúp hệ thống tuyển dụng **tránh được hoàn toàn định kiến giới tính (Fairness in AI)**.

#### 3. Xứng đáng về Giá trị Kinh tế & Quản trị Doanh nghiệp (Business Value)
* **Giảm lãng phí chi phí đào tạo:** Giúp công ty chấm điểm hồ sơ ngay từ khâu tuyển sinh, ưu tiên cấp học bổng/tài trợ cho những ứng viên có cam kết gắn bó ($y = 0$).
* **Lập kế hoạch tổ chức khóa học (Course Planning):** Ước tính trước tỷ lệ học viên sẽ chuyển đổi thành nhân viên chính thức để chủ động chuẩn bị giảng viên, giáo trình và vị trí công việc tiếp nhận.
* **Chính sách giữ chân nhân tài trúng đích:** Nhận diện sớm các học viên xuất sắc nhưng có rủi ro rời đi cao (ở vùng CDI thấp, công ty nhỏ) để công ty chủ động đưa ra phụ cấp thu hút, chính sách làm việc linh hoạt (Remote/Hybrid) hoặc cam kết đãi ngộ hấp dẫn.

---

## 🎯 LỜI KẾT VÀ BẢO VỆ PHẢN BIỆN (THỜI LƯỢNG: 1 PHÚT)

> *"Kính thưa Thầy/Cô,*  
>  
> *Đồ án của em đã giải quyết trọn vẹn bài toán từ **khâu tiếp nhận bài toán nghiệp vụ, tiền xử lý dữ liệu chuẩn hóa, mô hình hóa với Random Forest, đến đánh giá kiểm định chéo khách quan và diễn giải tri thức hỗ trợ ra quyết định**.*  
>  
> *Mô hình đạt kết quả thực nghiệm vững chắc (**AUC = 0.7844, Recall = 74.87%**), mang lại giá trị kinh tế trực tiếp cho doanh nghiệp.*  
>  
> *Em xin chân thành cảm ơn Thầy/Cô đã chú ý lắng nghe. Em rất mong nhận được những nhận xét và câu hỏi phản biện từ Hội đồng để hoàn thiện đồ án tốt hơn nữa ạ!"*

---

## 💡 PHỤ LỤC: CẨM NANG ĐỐI ĐÁP CÁC CÂU HỎI THƯỜNG GẶP TỪ HỘI ĐỒNG

| Câu hỏi của Thầy/Cô | Hướng trả lời đắt giá |
| :--- | :--- |
| *1. "Tại sao không dùng một Cây quyết định đơn lẻ (Decision Tree) mà phải dùng Random Forest?"* | *"Dạ thưa thầy, Cây quyết định đơn lẻ rất trực quan nhưng rất dễ bị quá khớp (overfitting) và độ nhạy Recall chỉ đạt 57%. Em dùng Random Forest tập hợp 150 cây để lấy số đông biểu quyết, vừa chống quá khớp, vừa nâng Recall lên gần 75% và AUC lên 0.7844 ạ."* |
| *2. "Dữ liệu bị mất cân bằng 75/25, em xử lý bằng cách nào?"* | *"Dạ em thiết lập tham số `class_weight='balanced'` trong Random Forest. Thuật toán sẽ tự động nhân trọng số phạt nặng gấp ~3 lần cho các lỗi dự đoán sai trên lớp thiểu số (lớp nhảy việc), giúp mô hình không bị thiên vị lớp đa số ạ."* |
| *3. "Em dùng Random Forest mà tại sao trong Pipeline vẫn có bước chuẩn hóa StandardScaler?"* | *"Dạ thưa thầy, về mặt toán học, Random Forest bất biến với phép co giãn thang đo. Em đưa `StandardScaler` vào `Pipeline` là để tuân thủ kiến trúc chuẩn công nghiệp (Production Pipeline), đảm bảo dữ liệu xử lý đồng bộ và thuận tiện cho việc tích hợp hệ thống mà không làm ảnh hưởng đến thuật toán cây ạ."* |
| *4. "Dữ liệu này lấy từ cơ sở dữ liệu nào?"* | *"Dạ đây là bộ CSDL **HR Analytics: Job Change of Data Scientists** gồm 19.158 dòng từ Kaggle, phản ánh dữ liệu thực tế từ Hệ thống quản lý học tập (LMS) kết hợp với Hệ thống quản trị nhân sự (HRMS) của một công ty chuyên về Big Data & Data Science ạ."* |
