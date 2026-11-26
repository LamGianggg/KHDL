# -*- coding: utf-8 -*-
"""
Script tu dong tao file Word (.docx) cho Kich Ban Thuyet Trinh & Bao Ve Do An HR Analytics.
Bao gom: 4 phan cot loi, bang bieu, loi thoai thuyet trinh va anh bieu do thuc nghiem.
"""

import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    """Dat mau nen cho o trong bang."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def create_script_docx():
    doc = Document()

    # Thiet lap le trang
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(1.1)
        section.right_margin = Inches(0.8)

    NAVY = RGBColor(26, 54, 93)      # #1A365D
    SLATE = RGBColor(45, 55, 72)     # #2D3748
    MUTED = RGBColor(113, 128, 150)  # #718096
    GOLD = RGBColor(180, 83, 9)      # #B45309

    # ==========================================
    # TRANG BIA (COVER)
    # ==========================================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p_inst.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO\nTRƯỜNG ĐẠI HỌC ...\n")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(13)
    r1.font.bold = True
    r1.font.color.rgb = SLATE

    r2 = p_inst.add_run("KHOA CÔNG NGHỆ THÔNG TIN / KHOA HỌC DỮ LIỆU\n")
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(13)
    r2.font.bold = True
    r2.font.color.rgb = NAVY

    p_star = doc.add_paragraph()
    p_star.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_star = p_star.add_run("------------------ *** ------------------\n\n")
    r_star.font.size = Pt(11)
    r_star.font.color.rgb = MUTED

    p_rep = doc.add_paragraph()
    p_rep.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_rep = p_rep.add_run("KỊCH BẢN THUYẾT TRÌNH & BẢO VỆ ĐỒ ÁN\n")
    r_rep.font.name = 'Times New Roman'
    r_rep.font.size = Pt(18)
    r_rep.font.bold = True
    r_rep.font.color.rgb = NAVY

    r_sub = p_rep.add_run("HỌC PHẦN: KHOA HỌC DỮ LIỆU (DATA SCIENCE)\n\n")
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(13)
    r_sub.font.bold = True
    r_sub.font.color.rgb = SLATE

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t1 = p_title.add_run("ĐỀ TÀI:\n")
    r_t1.font.name = 'Times New Roman'
    r_t1.font.size = Pt(13)
    r_t1.font.bold = True
    r_t1.font.color.rgb = MUTED

    r_t2 = p_title.add_run("DỰ BÁO XÁC SUẤT CHUYỂN VIỆC CỦA HỌC VIÊN SAU KHÓA ĐÀO TẠO VỀ DỮ LIỆU\n(HR ANALYTICS: JOB CHANGE OF DATA SCIENTISTS)\n\n\n")
    r_t2.font.name = 'Times New Roman'
    r_t2.font.size = Pt(16)
    r_t2.font.bold = True
    r_t2.font.color.rgb = NAVY

    # Khung thong tin sinh vien
    table_info = doc.add_table(rows=4, cols=2)
    table_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_data = [
        ("Sinh viên thực hiện:", "[Họ và Tên Sinh Viên]"),
        ("Mã số sinh viên (MSSV):", "[MSSV]"),
        ("Lớp chuyên ngành:", "[Tên Lớp Chuyên Ngành]"),
        ("Giảng viên hướng dẫn:", "[Họ và Tên Giảng Viên]")
    ]
    for row_idx, (k, v) in enumerate(info_data):
        cell_k = table_info.cell(row_idx, 0)
        cell_v = table_info.cell(row_idx, 1)
        cell_k.text = k
        cell_v.text = v
        for p in cell_k.paragraphs:
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(12)
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = SLATE
        for p in cell_v.paragraphs:
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(12)
            p.runs[0].font.color.rgb = SLATE

    p_year = doc.add_paragraph()
    p_year.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_yr = p_year.add_run("\n\n\nNăm học 2026 - Học kỳ 1")
    r_yr.font.name = 'Times New Roman'
    r_yr.font.size = Pt(12)
    r_yr.font.italic = True
    r_yr.font.color.rgb = MUTED

    doc.add_page_break()

    # ==========================================
    # CAC HAM HELPER
    # ==========================================
    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(15)
        r.font.bold = True
        r.font.color.rgb = NAVY
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(13)
        r.font.bold = True
        r.font.color.rgb = SLATE
        return p

    def add_body(text, bold_prefix=None, italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.25
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.font.name = 'Times New Roman'
            rb.font.size = Pt(12)
            rb.font.bold = True
            rb.font.color.rgb = SLATE
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.italic = italic
        r.font.color.rgb = SLATE
        return p

    def add_speech(text):
        """Khung loi thoai thuyet trinh."""
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.left_indent = Inches(0.3)
        p.paragraph_format.right_indent = Inches(0.3)
        p.paragraph_format.line_spacing = 1.25
        rb = p.add_run("🎙️ Lời thoại trình bày: ")
        rb.font.name = 'Times New Roman'
        rb.font.size = Pt(11.5)
        rb.font.bold = True
        rb.font.color.rgb = GOLD
        r = p.add_run(f'"{text}"')
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11.5)
        r.font.italic = True
        r.font.color.rgb = SLATE
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.2
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.font.name = 'Times New Roman'
            rb.font.size = Pt(12)
            rb.font.bold = True
            rb.font.color.rgb = SLATE
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.color.rgb = SLATE
        return p

    def add_caption(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(10)
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10.5)
        r.font.italic = True
        r.font.color.rgb = MUTED

    # ==========================================
    # NOI DUNG CHI TIET
    # ==========================================
    add_h1("LỜI MỞ ĐẦU & DẪN NHẬP (THỜI LƯỢNG: 1 PHÚT)")
    add_body("Khi bắt đầu bài bảo vệ trước Hội đồng, việc tạo ấn tượng đầu tiên bằng phong thái đĩnh đạc, rõ ràng và nêu bật cấu trúc bài thuyết trình là yếu tố then chốt để ghi điểm.")
    add_speech("Kính thưa Thầy/Cô trong Hội đồng chấm điểm và các bạn sinh viên, hôm nay em xin phép được đại diện nhóm trình bày báo cáo đồ án môn học Khoa học Dữ liệu với đề tài: 'Nghiên cứu và Xây dựng Mô hình Học máy Dự báo Xác suất Chuyển việc của Học viên sau Khóa Đào tạo Chuyên môn về Dữ liệu'. Bài thuyết trình của em gồm 4 phần cốt lõi: (1) Mô tả bài toán và bối cảnh doanh nghiệp, (2) Show tập dữ liệu minh họa và quy trình tiền xử lý, (3) Show giải pháp thuật toán Random Forest Classifier, và (4) Chứng minh thuật toán chạy được 100% trên thực tế và bài toán cực kỳ xứng đáng. Sau đây em xin phép được đi vào chi tiết.")

    # ------------------------------------------
    # PHAN 1
    # ------------------------------------------
    add_h1("PHẦN 1: MÔ TẢ VỀ BÀI TOÁN (THỜI LƯỢNG: 2 - 3 PHÚT)")
    add_h2("1.1. Bối cảnh xuất phát từ thực tiễn doanh nghiệp")
    add_body("Một doanh nghiệp hoạt động chuyên sâu trong lĩnh vực Big Data & Data Science tổ chức các khóa đào tạo chuyên môn và thu hút lượng lớn người đăng ký tham gia (tập dữ liệu huấn luyện lên tới 19.158 hồ sơ học viên). Mục tiêu của công ty là tìm kiếm và tuyển dụng các chuyên viên dữ liệu (Data Scientist) từ chính những học viên hoàn thành khóa đào tạo này.")

    add_h2("1.2. Vấn đề nhức nhối cốt lõi (The Pain Point)")
    add_body("Doanh nghiệp phải đối mặt với bài toán nan giải: Trong số hàng nghìn học viên tham gia, ai là người thực sự muốn ở lại làm việc cho công ty sau khóa học, và ai chỉ học để lấy kiến thức rồi tìm việc làm ở nơi khác (nhảy việc)?")
    add_body("Nếu không có công cụ phân loại chính xác, công ty sẽ chịu tổn thất lớn về:", "Thiệt hại thực tế: ")
    add_bullet(" Lãng phí ngân sách và nguồn lực đào tạo cho người học xong rồi bỏ sang đối thủ.", "1. Chi phí và thời gian:")
    add_bullet(" Khó khăn trong việc sàng lọc đầu vào và chủ động nguồn nhân sự kế cận.", "2. Bị động trong tuyển dụng:")
    add_bullet(" Bị động trong việc ước tính số lượng học viên sẽ chuyển đổi thành nhân viên để phân bổ giảng viên và giáo trình.", "3. Lập kế hoạch khóa học (Course Planning):")

    add_h2("1.3. Hai nhiệm vụ kỹ thuật cốt lõi")
    add_bullet(" Ước lượng xác suất nhị phân P(y = 1 | X) để phân loại ứng viên: y = 0 là học viên sẵn sàng ở lại làm việc cho công ty; y = 1 là học viên có nguy cơ cao sẽ nhảy việc sang nơi khác.", "Nhiệm vụ 1 (Dự báo):")
    add_bullet(" Chỉ ra chính xác các nhân tố (factors) nào chi phối mạnh nhất đến quyết định của ứng viên để hỗ trợ ban lãnh đạo đưa ra quyết sách nhân sự chuẩn xác.", "Nhiệm vụ 2 (Diễn giải tri thức):")
    add_speech("Thưa Thầy/Cô, bài toán này giải quyết bài toán kinh doanh sống còn của công ty: 'Ai sẽ ở lại làm việc, ai sẽ nhảy việc?'. Việc giải quyết bài toán này không chỉ giúp công ty tiết kiệm hàng nghìn USD chi phí đào tạo lãng phí, mà còn cung cấp công cụ định lượng để lập kế hoạch mở lớp (Course Planning) và phân loại học viên chính xác.")

    # ------------------------------------------
    # PHAN 2
    # ------------------------------------------
    add_h1("PHẦN 2: SHOW TẬP DỮ LIỆU ĐƯỢC SỬ DỤNG ĐỂ MINH HỌA (THỜI LƯỢNG: 2 - 3 PHÚT)")
    add_h2("2.1. Quy mô và cấu trúc tập dữ liệu")
    add_body("Nghiên cứu sử dụng tập dữ liệu chuẩn 'HR Analytics: Job Change of Data Scientists' từ nền tảng Kaggle:")
    add_bullet(" 19.158 dòng bản ghi.", "Tập huấn luyện (aug_train.csv):")
    add_bullet(" 2.129 dòng bản ghi dùng để kiểm thử độc lập.", "Tập kiểm định độc lập (aug_test.csv):")
    add_bullet(" 12 thuộc tính đầu vào (Features) + 1 nhãn mục tiêu nhị phân (target: 0 hoặc 1).", "Không gian đặc trưng:")

    add_h2("2.2. Trích xuất mẫu dữ liệu thực tế (Sample Data)")
    table_sample = doc.add_table(rows=4, cols=6)
    table_sample.alignment = WD_TABLE_ALIGNMENT.CENTER
    s_headers = ["enrollee_id", "city", "CDI", "education_level", "training_hours", "target"]
    s_rows = [
        ("8949", "city_103", "0.920", "Graduate", "36", "1.0 (Tìm việc)"),
        ("29725", "city_40", "0.776", "Graduate", "47", "0.0 (Ở lại)"),
        ("11561", "city_21", "0.624", "Graduate", "83", "0.0 (Ở lại)")
    ]
    for c_idx, h in enumerate(s_headers):
        cell = table_sample.cell(0, c_idx)
        cell.text = h
        set_cell_background(cell, "E2E8F0")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.name = 'Times New Roman'
        p.runs[0].font.size = Pt(11)
        p.runs[0].font.bold = True

    for r_idx, row_vals in enumerate(s_rows):
        for c_idx, val in enumerate(row_vals):
            cell = table_sample.cell(r_idx + 1, c_idx)
            cell.text = val
            p = cell.paragraphs[0]
            if c_idx in [0, 1, 2, 4, 5]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(10.5)
            if c_idx == 5:
                p.runs[0].font.bold = True
    add_caption("Bảng 2.1: Trích xuất các bản ghi mẫu thực tế từ tập dữ liệu HR Analytics")

    add_h2("2.3. Quy trình tiền xử lý số hóa 100% dữ liệu")
    add_body("Dữ liệu được làm sạch và chuyển đổi số hóa theo đúng giáo trình bài giảng (Slide 7 - DS04-DM03-DataPreProcess.ppt):")
    add_bullet(" Dùng Yếu vị (Mode) cho các biến định tính (gender, education_level, company_size...) và Trung vị (Median = 9 năm) cho biến kinh nghiệm để chống ngoại lai. Tuyệt đối không tạo nhãn giả định 'Unknown' hay số âm '-1'.", "Khử dữ liệu khuyết thiếu (Slide 7):")
    add_bullet(" Mã hóa Ordinal cho các biến thứ bậc (education_level, company_size, last_new_job, experience); tách mã số nguyên cho thuộc tính city (0 - 180); loại bỏ enrollee_id để chống overfitting.", "Số hóa 100% (All Numeric):")
    add_bullet(" Xuất ra 2 tệp dữ liệu sạch train_cleaned_numeric.csv (19.158 dòng) và test_cleaned_numeric.csv (2.129 dòng) với 0 NaN, 0 số âm.", "Kết quả kiểm chứng:")
    add_speech("Thưa Thầy/Cô, toàn bộ 19.158 dòng dữ liệu đã được làm sạch theo đúng chuẩn Slide 7 bài giảng của bộ môn: điền Mode và Median, số hóa 100% không còn bất kỳ giá trị NaN hay số âm nào, sẵn sàng đưa vào mô hình học máy mà không phát sinh lỗi.")

    # ------------------------------------------
    # PHAN 3
    # ------------------------------------------
    add_h1("PHẦN 3: SHOW THUẬT TOÁN ĐỊNH SỬ DỤNG – RANDOM FOREST CLASSIFIER (THỜI LƯỢNG: 2 PHÚT)")
    add_body("Thuật toán duy nhất và cốt lõi được lựa chọn để giải quyết bài toán là: Random Forest Classifier (Rừng ngẫu nhiên).")

    add_h2("3.1. Bản chất và cơ chế hoạt động")
    add_bullet(" Thuộc trường phái Học máy tập hợp (Ensemble Learning) theo kỹ thuật Bagging (Bootstrap Aggregating).", "Trường phái:")
    add_bullet(" Thay vì chỉ dựa vào 1 cây quyết định đơn lẻ (rất dễ bị học vẹt / overfitting), Random Forest xây dựng một 'hội đồng gồm 150 cây quyết định độc lập' (n_estimators = 150).", "Quy mô tập hợp:")
    add_bullet(" (1) Ngẫu nhiên hóa mẫu (Bootstrap): Mỗi cây học trên một tập con mẫu ngẫu nhiên có hoàn lại; (2) Ngẫu nhiên hóa đặc trưng: Tại mỗi nút phân nhánh, cây chỉ chọn ngẫu nhiên một tập con đặc trưng để tìm điểm cắt tối ưu.", "Cơ chế ngẫu nhiên kép:")
    add_bullet(" Dự đoán cuối cùng là sự đồng thuận bỏ phiếu (Majority Voting / Average Probability) từ cả 150 cây, giúp triệt tiêu phương sai và chống quá khớp hoàn hảo.", "Đưa ra quyết định:")

    add_h2("3.2. Cấu hình kỹ thuật chuyên biệt cho bài toán HR")
    add_bullet(" Thiết lập class_weight = 'balanced' để tự động nhân trọng số phạt nặng hơn cho các lỗi đoán sai trên lớp 1 (tìm việc), giải quyết bài toán mất cân bằng 75/25.", "Xử lý mất cân bằng lớp:")
    add_bullet(" Giới hạn max_depth = 12, min_samples_split = 10, min_samples_leaf = 4 để kiểm soát chặt chẽ độ phức tạp của cây.", "Kiểm soát quá khớp:")
    add_speech("Thưa Thầy/Cô, chúng em chọn Random Forest gồm 150 cây vì nó là thuật toán Ensemble Bagging xuất sắc: vừa bắt được các quy luật phi tuyến phức tạp của dữ liệu nhân sự, vừa chống hiện tượng quá khớp nhờ cơ chế bỏ phiếu số đông, và đặc biệt giải quyết triệt để vấn đề mất cân bằng dữ liệu 75/25 nhờ tham số class_weight='balanced'.")

    # ------------------------------------------
    # PHAN 4
    # ------------------------------------------
    add_h1("PHẦN 4: CHỨNG MINH THUẬT TOÁN CHẠY ĐƯỢC VÀ BÀI TOÁN CỰC KỲ XỨNG ĐÁNG (THỜI LƯỢNG: 3 - 4 PHÚT)")

    add_h2("4.1. Chứng minh thực tế 100% 'CHẠY ĐƯỢC' (Proof of Implementation)")
    add_body("Toàn bộ giải pháp đã được hiện thực hóa thành mã nguồn và sản phẩm thực tế:")
    add_bullet(" Mã nguồn 02_model_random_forest.py chạy hoàn tất 100% trên PowerShell không lỗi.", "Mã nguồn độc lập:")
    add_bullet(" Đã đóng gói và lưu tại models/model_random_forest.pkl.", "Mô hình lưu trữ:")
    add_bullet(" Đã xuất kết quả dự đoán cho 2.129 học viên tại submissions/submission_random_forest.csv.", "Kết quả dự đoán:")
    add_bullet(" Đã tự động sinh ra ma trận nhầm lẫn và biểu đồ tầm quan trọng đặc trưng trong thư mục figures/.", "Biểu đồ trực quan:")

    add_h2("4.2. Chứng minh hiệu năng định lượng (Kiểm định chéo Stratified 5-Fold)")
    table_metrics = doc.add_table(rows=6, cols=3)
    table_metrics.alignment = WD_TABLE_ALIGNMENT.CENTER
    m_headers = ["Chỉ số đo lường", "Kết quả thực nghiệm", "Ý nghĩa chứng minh tính xứng đáng"]
    m_rows = [
        ("CV ROC-AUC (5-Fold)", "0.7844 (+/- 0.0075)", "Khả năng phân tách xuất sắc, cực kỳ ổn định qua 5 lượt kiểm tra."),
        ("Validation Accuracy", "76.54%", "Độ chính xác tổng thể rất cao trên toàn bộ tập dữ liệu."),
        ("Recall (Độ nhạy Lớp 1)", "74.87%", "Bắt trúng gần 75% học viên có ý định nhảy việc thực tế!"),
        ("Precision (Lớp 1)", "52.04%", "Tỷ lệ dự đoán đúng vượt trội hoàn toàn so với tỷ lệ ngẫu nhiên 25%."),
        ("F1-Score (Lớp 1)", "0.6140", "Cân bằng tối ưu giữa phát hiện mục tiêu và hạn chế cảnh báo nhầm.")
    ]
    for c_idx, h in enumerate(m_headers):
        cell = table_metrics.cell(0, c_idx)
        cell.text = h
        set_cell_background(cell, "CBD5E1")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.name = 'Times New Roman'
        p.runs[0].font.size = Pt(11)
        p.runs[0].font.bold = True

    for r_idx, row_vals in enumerate(m_rows):
        for c_idx, val in enumerate(row_vals):
            cell = table_metrics.cell(r_idx + 1, c_idx)
            cell.text = val
            p = cell.paragraphs[0]
            if c_idx in [0, 1]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(10.5)
            if r_idx in [0, 2]:
                p.runs[0].font.bold = True
                set_cell_background(cell, "FEF3C7")
    add_caption("Bảng 4.1: Kết quả kiểm định chéo Stratified 5-Fold của mô hình Random Forest")

    # Chen hinh anh Confusion Matrix
    cm_path = r"d:\Năm 3 học kỳ 1\Khoa học dữ liệu\HR Analytics\figures\confusion_matrix_random_forest.png"
    if os.path.exists(cm_path):
        p_img1 = doc.add_paragraph()
        p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img1.add_run().add_picture(cm_path, width=Inches(4.5))
        add_caption("Hình 4.1: Ma trận nhầm lẫn của Random Forest trên tập kiểm định độc lập")

    add_h2("4.3. Chứng minh hoàn thành Nhiệm vụ 2 (Diễn giải tri thức - Feature Importance)")
    add_body("Random Forest không phải là hộp đen. Mô hình trích xuất được chính xác mức độ quan trọng Gini của từng đặc trưng:")
    
    # Chen hinh anh Feature Importance
    fi_path = r"d:\Năm 3 học kỳ 1\Khoa học dữ liệu\HR Analytics\figures\feature_importance_random_forest.png"
    if os.path.exists(fi_path):
        p_img2 = doc.add_paragraph()
        p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img2.add_run().add_picture(fi_path, width=Inches(5.2))
        add_caption("Hình 4.2: Biểu đồ xếp hạng độ quan trọng đặc trưng trích xuất từ Random Forest")

    add_body("Các phát hiện then chốt giúp doanh nghiệp ra quyết định:", "Tri thức trích xuất: ")
    add_bullet(" Chi phối số 1. Nơi sống có điều kiện kinh tế thấp là nguyên nhân hàng đầu thúc đẩy học viên tìm việc nơi khác.", "1. city_development_index (33.37%):")
    add_bullet(" Yếu tố vùng miền địa phương cụ thể.", "2. city (14.83%):")
    add_bullet(" Học viên ở công ty nhỏ/startup có tỷ lệ nhảy việc cao hơn nhiều so với tập đoàn lớn.", "3. company_size (12.37%):")
    add_bullet(" Đóng góp ~9% mỗi biến. Số giờ học tích lũy và thâm niên làm việc là các tín hiệu cảnh báo quan trọng.", "4. training_hours & experience:")
    add_bullet(" Biến gender chỉ đóng góp 0.69% (< 1%), chứng minh việc loại bỏ biến Giới tính không làm suy giảm độ chính xác, giúp hệ thống tuyển dụng đảm bảo tính công bằng và đạo đức AI (Fairness in AI).", "5. Minh chứng Đạo đức AI:")

    add_h2("4.4. Chứng minh bài toán cực kỳ xứng đáng về giá trị kinh tế (Business Value)")
    add_bullet(" Giúp công ty chấm điểm hồ sơ ngay từ khâu tuyển sinh, ưu tiên cấp học bổng và tài trợ đào tạo cho ứng viên có cam kết gắn bó (y = 0), tránh lãng phí hàng nghìn USD đào tạo cho người học xong bỏ đi.", "Tối ưu ngân sách đào tạo:")
    add_bullet(" Dự báo trước tỷ lệ học viên sẽ chuyển đổi thành nhân viên chính thức để chủ động quy mô mở lớp và chuẩn bị cơ sở vật chất.", "Lập kế hoạch tổ chức khóa học (Course Planning):")
    add_bullet(" Đối với học viên xuất sắc ở các vùng có chỉ số CDI thấp, công ty chủ động đề xuất phụ cấp vùng miền hoặc chính sách làm việc từ xa (Remote/Hybrid) để thu hút họ gia nhập công ty.", "Chính sách giữ chân nhân tài trúng đích:")
    add_speech("Thưa Thầy/Cô, mô hình Random Forest hoàn toàn xứng đáng được lựa chọn vì nó đạt điểm ROC-AUC 0.7844 rất cao, bắt trúng gần 75% học viên có ý định nhảy việc, giải thích rõ ràng 4 nhân tố cốt lõi chi phối quyết định rời đi, và mang lại giá trị kinh tế trực tiếp cho doanh nghiệp.")

    # ------------------------------------------
    # LOI KET & CAM NANG PHAN BIEN
    # ------------------------------------------
    add_h1("LỜI KẾT VÀ BẢO VỆ PHẢN BIỆN (THỜI LƯỢNG: 1 PHÚT)")
    add_speech("Kính thưa Thầy/Cô, đồ án của em đã giải quyết trọn vẹn bài toán từ khâu tiếp nhận nghiệp vụ, tiền xử lý dữ liệu chuẩn hóa, mô hình hóa với Random Forest, đến đánh giá kiểm định chéo khách quan và trích xuất tri thức hỗ trợ ra quyết định. Em xin chân thành cảm ơn Thầy/Cô đã chú ý lắng nghe và rất mong nhận được những câu hỏi phản biện từ Hội đồng ạ!")

    add_h1("PHỤ LỤC: CẨM NANG ĐỐI ĐÁP CÁC CÂU HỎI THƯỜNG GẶP TỪ HỘI ĐỒNG")
    table_qa = doc.add_table(rows=5, cols=2)
    table_qa.alignment = WD_TABLE_ALIGNMENT.CENTER
    qa_data = [
        ("1. Tại sao không dùng Cây quyết định đơn lẻ mà phải dùng Random Forest?",
         "Cây quyết định đơn lẻ rất trực quan nhưng rất dễ bị quá khớp (overfitting) và độ nhạy Recall chỉ đạt 57%. Em dùng Random Forest gồm 150 cây để lấy số đông biểu quyết, vừa chống quá khớp, vừa nâng Recall lên gần 75% và AUC lên 0.7844."),
        ("2. Dữ liệu bị mất cân bằng 75/25, em xử lý bằng cách nào?",
         "Em thiết lập tham số class_weight='balanced' trong Random Forest. Thuật toán sẽ tự động nhân trọng số phạt nặng gấp ~3 lần cho các lỗi dự đoán sai trên lớp thiểu số (lớp nhảy việc), giúp mô hình không bị thiên vị lớp đa số."),
        ("3. Dùng Random Forest sao trong Pipeline vẫn có bước chuẩn hóa StandardScaler?",
         "Về mặt toán học, Random Forest bất biến với phép co giãn thang đo. Em đưa StandardScaler vào Pipeline là để tuân thủ kiến trúc chuẩn công nghiệp (Production Pipeline), đảm bảo dữ liệu xử lý đồng bộ và thuận tiện cho việc tích hợp hệ thống mà không làm ảnh hưởng đến thuật toán cây."),
        ("4. Dữ liệu này lấy từ cơ sở dữ liệu nào?",
         "Đây là bộ CSDL HR Analytics: Job Change of Data Scientists gồm 19.158 dòng từ Kaggle, phản ánh dữ liệu thực tế từ Hệ thống quản lý học tập (LMS) kết hợp với Hệ thống quản trị nhân sự (HRMS) của một công ty chuyên về Big Data & Data Science.")
    ]
    for r_idx, (q, a) in enumerate(qa_data):
        cell_q = table_qa.cell(r_idx + 1, 0)
        cell_a = table_qa.cell(r_idx + 1, 1)
        cell_q.text = q
        cell_a.text = a
        p_q = cell_q.paragraphs[0]
        p_q.runs[0].font.name = 'Times New Roman'
        p_q.runs[0].font.size = Pt(10.5)
        p_q.runs[0].font.bold = True
        p_q.runs[0].font.color.rgb = SLATE
        set_cell_background(cell_q, "F1F5F9")
        p_a = cell_a.paragraphs[0]
        p_a.runs[0].font.name = 'Times New Roman'
        p_a.runs[0].font.size = Pt(10.5)
        p_a.runs[0].font.color.rgb = SLATE

    # Header QA
    h_q = table_qa.cell(0, 0)
    h_a = table_qa.cell(0, 1)
    h_q.text = "Câu hỏi thường gặp của Thầy/Cô"
    h_a.text = "Câu trả lời đắt giá nhất"
    set_cell_background(h_q, "E2E8F0")
    set_cell_background(h_a, "E2E8F0")
    for h in [h_q, h_a]:
        p = h.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.name = 'Times New Roman'
        p.runs[0].font.size = Pt(11)
        p.runs[0].font.bold = True

    output_path = r"d:\Năm 3 học kỳ 1\Khoa học dữ liệu\HR Analytics\Kich_Ban_Thuyet_Trinh_HR_Analytics.docx"
    doc.save(output_path)
    print(f"[OK] Da tao thanh cong file Word Kich Ban tai: {output_path}")

if __name__ == "__main__":
    create_script_docx()
