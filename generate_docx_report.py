# -*- coding: utf-8 -*-
"""
Script tao file Bao Cao Do An (.docx) chuan format Dai hoc
Bao gom: Trang bia, bang bieu du lieu, va cac hinh anh bieu do evaluation thuc te.
"""

import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
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

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Dat padding cho o."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_report():
    doc = Document()

    # Thiet lap le trang (Top: 2.0cm, Bottom: 2.0cm, Left: 3.0cm, Right: 2.0cm)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(1.1)
        section.right_margin = Inches(0.8)

    # Dinh nghia mau sac chu dao (Navy & Dark Slate)
    NAVY = RGBColor(26, 54, 93)      # #1A365D
    SLATE = RGBColor(45, 55, 72)     # #2D3748
    MUTED = RGBColor(113, 128, 150)  # #718096

    # ==========================================
    # TRANG BIA (COVER PAGE)
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
    r_star = p_star.add_run("------------------ *** ------------------\n\n\n")
    r_star.font.size = Pt(11)
    r_star.font.color.rgb = MUTED

    p_rep = doc.add_paragraph()
    p_rep.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_rep = p_rep.add_run("BÁO CÁO ĐỒ ÁN MÔN HỌC\n")
    r_rep.font.name = 'Times New Roman'
    r_rep.font.size = Pt(18)
    r_rep.font.bold = True
    r_rep.font.color.rgb = NAVY

    r_sub = p_rep.add_run("HỌC PHẦN: KHOA HỌC DỮ LIỆU (DATA SCIENCE)\n\n\n")
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(14)
    r_sub.font.bold = True
    r_sub.font.color.rgb = SLATE

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t1 = p_title.add_run("ĐỀ TÀI:\n")
    r_t1.font.name = 'Times New Roman'
    r_t1.font.size = Pt(14)
    r_t1.font.bold = True
    r_t1.font.color.rgb = MUTED

    r_t2 = p_title.add_run("DỰ ĐOÁN XÁC SUẤT CHUYỂN VIỆC CỦA CHUYÊN VIÊN DỮ LIỆU\n(HR ANALYTICS: JOB CHANGE OF DATA SCIENTISTS)\n\n\n\n")
    r_t2.font.name = 'Times New Roman'
    r_t2.font.size = Pt(18)
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
        
        # Style
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
    r_yr = p_year.add_run("\n\n\n\nNăm học 2026 - Học kỳ 1")
    r_yr.font.name = 'Times New Roman'
    r_yr.font.size = Pt(12)
    r_yr.font.italic = True
    r_yr.font.color.rgb = MUTED

    doc.add_page_break()

    # ==========================================
    # CAC HAM HELPER CHO NOI DUNG
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
        p.paragraph_format.space_after = Pt(6)
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

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.2
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.font.name = 'Times New Roman'
            rb.font.size = Pt(12)
            rb.font.bold = True
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
    add_h1("LỜI MỞ ĐẦU")
    add_body("Trong thời đại công nghệ số và sự phát triển vượt bậc của Trí tuệ nhân tạo (AI), dữ liệu được xem là nguồn tài nguyên cốt lõi quyết định lợi thế cạnh tranh của mọi doanh nghiệp. Kéo theo đó, nguồn nhân lực trong lĩnh vực Khoa học dữ liệu (Data Science) và Kỹ thuật dữ liệu (Big Data) trở thành mục tiêu săn đón hàng đầu của các tập đoàn công nghệ lớn.")
    add_body("Tuy nhiên, một trong những rào cản lớn nhất mà các tổ chức đang phải đối mặt chính là tỷ lệ biến động nhân sự (turnover rate) rất cao. Chi phí tuyển dụng mới một chuyên viên dữ liệu có thể tốn kém gấp 1.5 - 2 lần lương hàng năm của họ, chưa kể sự gián đoạn nghiêm trọng đối với tiến độ các dự án AI và nguy cơ thất thoát bí mật kinh doanh.")
    add_body("Xuất phát từ nhu cầu thực tiễn đó, đồ án môn học Khoa học dữ liệu lựa chọn đề tài: 'Dự đoán xác suất chuyển việc của chuyên viên dữ liệu (HR Analytics: Job Change of Data Scientists)'. Đồ án ứng dụng trọn vẹn quy trình KDD (Knowledge Discovery in Databases): từ khám phá dữ liệu, áp dụng quy chuẩn tiền xử lý dữ liệu học phần, chuyển đổi 100% dữ liệu sang dạng số không khuyết thiếu, thiết kế và huấn luyện độc lập 3 mô hình học máy kinh điển (Logistic Regression, Random Forest, LightGBM), đến đánh giá kiểm định chéo Stratified 5-Fold và đề xuất các quyết sách nhân sự thiết thực cho doanh nghiệp.")

    add_h1("CHƯƠNG 1: TỔNG QUAN BÀI TOÁN & BỐI CẢNH THỰC TẾ")
    add_h2("1.1. Bối cảnh thực tế trong quản trị nhân lực công nghệ")
    add_body("Các tổ chức tài chính, công ty công nghệ và viện đào tạo thường xuyên tổ chức các khóa học chuyên sâu về Big Data và Data Science nhằm tài trợ và tìm kiếm ứng viên tiềm năng. Tuy nhiên, sau khi kết thúc khóa đào tạo, nhiều ứng viên nhận chứng chỉ và ngay lập tức tìm kiếm cơ hội làm việc tại nơi khác thay vì ở lại cống hiến cho đơn vị tổ chức.")
    add_body("Nếu doanh nghiệp sở hữu một hệ thống Machine Learning có khả năng dự đoán chính xác xác suất rời đi của từng ứng viên, phòng Nhân sự (HR) có thể:", "Giá trị mang lại: ")
    add_bullet(" Tiết kiệm hàng trăm nghìn USD chi phí tài trợ cho những đối tượng có cam kết gắn bó thấp.", "Tối ưu ngân sách đào tạo:")
    add_bullet(" Chủ động tiếp cận, phỏng vấn giữ chân, điều chỉnh lương thưởng và lộ trình thăng tiến cho các nhân tài quan trọng trước khi họ nộp đơn xin nghỉ.", "Chủ động giữ chân nhân tài:")
    add_bullet(" Giảm thiểu thời gian trống vị trí công việc, đảm bảo dòng chảy dự án liên tục.", "Ổn định vận hành:")

    add_h2("1.2. Phát biểu bài toán Machine Learning")
    add_body("Bài toán được mô hình hóa dưới dạng Phân loại nhị phân có giám sát (Supervised Binary Classification):")
    add_bullet(" Tập hợp vector đặc trưng X gồm 12 thuộc tính về nhân khẩu học, trình độ học vấn, kinh nghiệm làm việc, số giờ đào tạo, thông tin thành phố sinh sống và quy mô công ty.", "Đầu vào (Features X):")
    add_bullet(" Biến nhị phân y ∈ {0, 1}. Trong đó y = 0 biểu thị ứng viên không muốn chuyển việc (ở lại gắn bó); y = 1 biểu thị ứng viên đang tích cực tìm kiếm cơ hội việc làm mới.", "Đầu ra (Target y):")
    add_bullet(" Mô hình cần xuất ra xác suất liên tục P(y = 1 | X) ∈ [0, 1] để phân hạng mức độ rủi ro rời bỏ của từng nhân sự.", "Yêu cầu dự đoán:")

    add_h1("CHƯƠNG 2: PHÂN TÍCH KHÁM PHÁ DỮ LIỆU (EDA)")
    add_h2("2.1. Quy mô tập dữ liệu")
    add_body("Nghiên cứu sử dụng tập dữ liệu chuẩn 'HR Analytics: Job Change of Data Scientists' từ nền tảng Kaggle:")
    add_bullet(" Gồm 19.158 dòng và 14 cột (chứa định danh enrollee_id và nhãn target).", "Tập huấn luyện (aug_train.csv):")
    add_bullet(" Gồm 2.129 dòng và 13 cột (được dùng để kiểm thử độc lập).", "Tập kiểm tra (aug_test.csv):")

    add_h2("2.2. Từ điển dữ liệu và ý nghĩa thuộc tính")
    table_dict = doc.add_table(rows=14, cols=4)
    table_dict.alignment = WD_TABLE_ALIGNMENT.CENTER
    dict_headers = ["STT", "Tên thuộc tính", "Kiểu gốc", "Ý nghĩa nghiệp vụ"]
    dict_rows = [
        ("1", "enrollee_id", "int64", "Mã định danh duy nhất của ứng viên"),
        ("2", "city", "object", "Mã thành phố ứng viên đang cư trú (city_103,...)"),
        ("3", "city_development_index", "float64", "Chỉ số phát triển kinh tế - xã hội của thành phố"),
        ("4", "gender", "object", "Giới tính (Male, Female, Other)"),
        ("5", "relevent_experience", "object", "Kinh nghiệm thực tế trong lĩnh vực dữ liệu"),
        ("6", "enrolled_university", "object", "Khóa đào tạo đại học đang theo học (nếu có)"),
        ("7", "education_level", "object", "Trình độ học vấn cao nhất (Primary School -> PhD)"),
        ("8", "major_discipline", "object", "Chuyên ngành đào tạo (STEM, Humanities,...)"),
        ("9", "experience", "object", "Số năm kinh nghiệm làm việc (<1, 1..20, >20)"),
        ("10", "company_size", "object", "Quy mô nhân sự của công ty hiện tại (<10..10000+)"),
        ("11", "company_type", "object", "Loại hình doanh nghiệp (Pvt Ltd, Startup, NGO,...)"),
        ("12", "last_new_job", "object", "Khoảng thời gian kể từ lần đổi việc trước (năm)"),
        ("13", "training_hours", "int64", "Tổng số giờ đào tạo chuyên môn đã hoàn thành")
    ]
    for c_idx, h in enumerate(dict_headers):
        cell = table_dict.cell(0, c_idx)
        cell.text = h
        set_cell_background(cell, "E2E8F0")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.name = 'Times New Roman'
        p.runs[0].font.size = Pt(11)
        p.runs[0].font.bold = True

    for r_idx, row_vals in enumerate(dict_rows):
        for c_idx, val in enumerate(row_vals):
            cell = table_dict.cell(r_idx + 1, c_idx)
            cell.text = val
            p = cell.paragraphs[0]
            if c_idx in [0, 2]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(10.5)
            p.runs[0].font.color.rgb = SLATE
    add_caption("Bảng 2.1: Bảng từ điển dữ liệu HR Analytics")

    add_h2("2.3. Khảo sát hiện tượng mất cân bằng dữ liệu (Class Imbalance)")
    add_body("Khảo sát phân phối nhãn target trên 19.158 mẫu của tập train:")
    add_bullet(" 14.381 mẫu, chiếm tỷ lệ 75.07%.", "Lớp 0 (Ứng viên không chuyển việc):")
    add_bullet(" 4.777 mẫu, chiếm tỷ lệ 24.93%.", "Lớp 1 (Ứng viên tìm kiếm việc mới):")
    add_body("Nhận xét chuyên sâu: Tỷ lệ mất cân bằng giữa hai lớp xấp xỉ 3:1. Nếu một mô hình đơn giản luôn dự đoán lớp 0, mô hình đó vẫn đạt Accuracy 75.07% nhưng hoàn toàn vô giá trị trong thực tế (không phát hiện được bất kỳ ai muốn nhảy việc). Do đó, chỉ số đánh giá trung tâm của đề tài bắt buộc phải là ROC-AUC (Area Under the Curve), Recall của lớp 1 và F1-Score.")

    add_h1("CHƯƠNG 3: PHƯƠNG PHÁP TIỀN XỬ LÝ VÀ SỐ HÓA DỮ LIỆU")
    add_h2("3.1. Cơ sở lý thuyết xử lý dữ liệu khuyết thiếu theo bài giảng")
    add_body("Căn cứ theo giáo trình và tài liệu bài giảng môn Khoa học dữ liệu (Slide 7 - DS04-DM03-DataPreProcess.ppt), các phương pháp xử lý dữ liệu khuyết thiếu (Missing Data) gồm có: bỏ qua mẫu dữ liệu, điền thủ công, sử dụng hằng số toàn cục, hoặc thay thế bằng các đại lượng đo xu thế tập trung (Measures of Central Tendency).")
    add_body("Trong đó, phương pháp chuẩn hóa và hiệu quả nhất đối với bài toán này là:")
    add_bullet(" Sử dụng Trung vị (Median) để hạn chế tối đa sự ảnh hưởng của các giá trị ngoại lai (outliers).", "Đối với thuộc tính định lượng / số:")
    add_bullet(" Sử dụng Yếu vị (Mode - giá trị có tần suất xuất hiện cao nhất) để bảo toàn phân phối tự nhiên.", "Đối với thuộc tính định tính / phân loại:")
    add_body("Đặc biệt, đồ án tuân thủ nghiêm ngặt nguyên tắc: Không tạo ra nhãn giả định như 'Unknown' hay các số âm nhân tạo như -1 vì sẽ làm sai lệch tính liên tục và quan hệ thứ tự trong không gian đặc trưng.")

    add_h2("3.2. Bảng thống kê và chiến lược điền khuyết")
    table_miss = doc.add_table(rows=9, cols=5)
    table_miss.alignment = WD_TABLE_ALIGNMENT.CENTER
    miss_headers = ["Thuộc tính", "Số lượng NaN", "Tỷ lệ khuyết (%)", "Phương pháp", "Giá trị thay thế"]
    miss_rows = [
        ("gender", "4.508", "23.53%", "Yếu vị (Mode)", "Male (1)"),
        ("enrolled_university", "386", "2.01%", "Yếu vị (Mode)", "no_enrollment (0)"),
        ("education_level", "460", "2.40%", "Yếu vị (Mode)", "Graduate (2)"),
        ("major_discipline", "2.813", "14.68%", "Yếu vị (Mode)", "STEM (0)"),
        ("experience", "65", "0.34%", "Trung vị (Median)", "9 năm"),
        ("company_size", "5.915", "30.87%", "Yếu vị (Mode)", "50-99 (2)"),
        ("company_type", "6.140", "32.05%", "Yếu vị (Mode)", "Pvt Ltd (0)"),
        ("last_new_job", "423", "2.21%", "Yếu vị (Mode)", "1 (1)")
    ]
    for c_idx, h in enumerate(miss_headers):
        cell = table_miss.cell(0, c_idx)
        cell.text = h
        set_cell_background(cell, "E2E8F0")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.name = 'Times New Roman'
        p.runs[0].font.size = Pt(11)
        p.runs[0].font.bold = True

    for r_idx, row_vals in enumerate(miss_rows):
        for c_idx, val in enumerate(row_vals):
            cell = table_miss.cell(r_idx + 1, c_idx)
            cell.text = val
            p = cell.paragraphs[0]
            if c_idx in [1, 2, 3]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(10.5)
            p.runs[0].font.color.rgb = SLATE
    add_caption("Bảng 3.1: Chiến lược điền giá trị khuyết thiếu theo chuẩn Slide 7")

    add_h2("3.3. Quy trình số hóa 100% dữ liệu (100% Numeric)")
    add_body("Để đảm bảo không có bất kỳ giá trị phi số nào lọt vào mô hình học máy, pipeline tiền xử lý thực hiện:")
    add_bullet(" Tách chuỗi loại bỏ tiền tố 'city_' và lấy số nguyên ID thành phố (ví dụ: city_103 -> 103).", "Thuộc tính city:")
    add_bullet(" Áp dụng cho các thuộc tính có cấp bậc tự nhiên như education_level (0 -> 4), company_size (0 -> 7), last_new_job (0 -> 5), experience (0 -> 21). Mọi giá trị đều không âm (≥ 0).", "Mã hóa thứ bậc (Ordinal Encoding):")
    add_bullet(" Áp dụng cho gender (0, 1, 2), relevent_experience (0, 1), enrolled_university (0, 1, 2), major_discipline (0 -> 5), company_type (0 -> 5).", "Mã hóa danh mục (Categorical Encoding):")
    add_bullet(" city_development_index (float64) và training_hours (int64) được giữ nguyên giá trị liên tục.", "Thuộc tính định lượng:")

    add_h2("3.4. Kiểm chứng tính toàn vẹn của dữ liệu sạch")
    add_body("Sau quá trình làm sạch, dữ liệu được xuất ra 2 tệp CSV sạch độc lập:")
    add_bullet(" 19.158 dòng × 14 cột; Tổng số ô NaN = 0; Tổng số giá trị âm = 0.", "train_cleaned_numeric.csv:")
    add_bullet(" 2.129 dòng × 13 cột; Tổng số ô NaN = 0; Tổng số giá trị âm = 0.", "test_cleaned_numeric.csv:")
    add_body("Toàn bộ 100% thuộc tính đều thuộc kiểu số int64 hoặc float64, sẵn sàng cho mọi mô hình toán học.")

    add_h1("CHƯƠNG 4: THIẾT KẾ VÀ HUẤN LUYỆN 3 MÔ HÌNH HỌC MÁY ĐỘC LẬP")
    add_body("Để đáp ứng yêu cầu kiến trúc module hóa và bảo trì độc lập, đề tài triển khai 3 mô hình tại 3 file Python tách biệt:")

    add_h2("4.1. Mô hình 1: Hồi quy Logistic (01_model_logistic_regression.py)")
    add_bullet(" Mô hình tham số tuyến tính cơ sở (Baseline). Tính toán tổ hợp tuyến tính các đặc trưng và ánh xạ qua hàm phi tuyến Sigmoid: P(y = 1 | x) = 1 / (1 + e^-(w^T x + b)).", "Nguyên lý:")
    add_bullet(" Áp dụng bộ chuẩn hóa MinMaxScaler đưa tất cả biến số về khoảng [0, 1]; thiết lập class_weight='balanced' nhằm phạt nặng lỗi dự đoán sai trên lớp thiểu số; giải thuật tối ưu hóa L-BFGS với số vòng lặp tối đa max_iter=1000.", "Tối ưu hóa:")

    add_h2("4.2. Mô hình 2: Rừng ngẫu nhiên (02_model_random_forest.py)")
    add_bullet(" Mô hình Ensemble dựa trên nguyên lý Bagging. Xây dựng đồng thời 150 cây quyết định độc lập trên các tập con dữ liệu lấy mẫu ngẫu nhiên có hoàn lại (Bootstrap Sample).", "Nguyên lý:")
    add_bullet(" Thiết lập n_estimators=150, max_depth=12, min_samples_split=10, min_samples_leaf=4 để kiểm soát hiện tượng quá khớp (overfitting); class_weight='balanced'.", "Tối ưu hóa:")

    add_h2("4.3. Mô hình 3: LightGBM (03_model_lightgbm.py)")
    add_bullet(" Thuật toán tăng cường độ dốc (Gradient Boosting) hiện đại. Tối ưu hóa việc phân nhánh cây theo nút lá (Leaf-wise), kết hợp kỹ thuật lấy mẫu đơn phương dựa trên gradient (GOSS) và gom cụm đặc trưng xung khắc (EFB).", "Nguyên lý:")
    add_bullet(" Thiết lập n_estimators=200, learning_rate=0.05, num_leaves=31, max_depth=7; scale_pos_weight=3.0 (tương ứng với tỷ lệ mất cân bằng dữ liệu 75/25).", "Tối ưu hóa:")

    add_h1("CHƯƠNG 5: THỰC NGHIỆM VÀ ĐÁNH GIÁ ĐỐI ĐẦU")
    add_h2("5.1. Thiết lập thực nghiệm kiểm định chéo (Stratified 5-Fold Cross Validation)")
    add_body("Để loại trừ hoàn toàn nguy cơ rò rỉ dữ liệu (data leakage) và đảm bảo tính khách quan của kết quả, toàn bộ 19.158 mẫu huấn luyện được chia thành 5 fold phân tầng (Stratified K-Fold), đảm bảo tỷ lệ lớp 0/1 luôn được giữ nguyên vẹn ở mỗi fold.")

    add_h2("5.2. Bảng tổng hợp đối đầu giữa 3 mô hình")
    table_res = doc.add_table(rows=4, cols=6)
    table_res.alignment = WD_TABLE_ALIGNMENT.CENTER
    res_headers = ["Mô hình", "CV ROC-AUC (5-Fold)", "Val Accuracy", "Precision (Lớp 1)", "Recall (Lớp 1)", "F1-Score (Lớp 1)"]
    res_rows = [
        ("Logistic Regression", "0.7274", "70.96%", "44.51%", "67.12%", "0.5353"),
        ("Random Forest", "0.7844", "76.54%", "52.04%", "74.87%", "0.6140"),
        ("LightGBM (Tối ưu nhất)", "0.7890", "75.05%", "49.97%", "79.06%", "0.6123")
    ]
    for c_idx, h in enumerate(res_headers):
        cell = table_res.cell(0, c_idx)
        cell.text = h
        set_cell_background(cell, "CBD5E1")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.name = 'Times New Roman'
        p.runs[0].font.size = Pt(11)
        p.runs[0].font.bold = True

    for r_idx, row_vals in enumerate(res_rows):
        for c_idx, val in enumerate(row_vals):
            cell = table_res.cell(r_idx + 1, c_idx)
            cell.text = val
            p = cell.paragraphs[0]
            if c_idx > 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(10.5)
            if r_idx == 2:
                p.runs[0].font.bold = True
                set_cell_background(cell, "FEF3C7")
    add_caption("Bảng 5.1: Kết quả đối đầu hiệu năng giữa 3 mô hình học máy")

    add_h2("5.3. Phân tích đường cong ROC (ROC Curves Comparison)")
    add_body("Đường cong ROC trực quan hóa khả năng phân biệt giữa hai lớp tại mọi ngưỡng xác suất cắt:")
    roc_img_path = r"d:\Năm 3 học kỳ 1\Khoa học dữ liệu\HR Analytics\figures\roc_curves_comparison.png"
    if os.path.exists(roc_img_path):
        doc.add_paragraph().alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.paragraphs[-1].paragraph_format.space_after = Pt(2)
        doc.paragraphs[-1].add_run().add_picture(roc_img_path, width=Inches(5.5))
        add_caption("Hình 5.1: Đồ thị so sánh đường cong ROC giữa 3 mô hình (figures/roc_curves_comparison.png)")

    add_body("Nhận xét đồ thị ROC: Cả hai mô hình dạng cây Ensemble (LightGBM và Random Forest) đều vượt trội rõ nét so với đường cơ sở tuyến tính Logistic Regression. Đặc biệt, LightGBM đạt diện tích dưới đường cong lớn nhất (AUC = 0.7890), đường cong bám sát góc trên bên trái, thể hiện khả năng phân tách sắc nét giữa nhóm nhân sự muốn ở lại và nhóm muốn nhảy việc.")

    add_h2("5.4. Phân tích ma trận nhầm lẫn (Confusion Matrix)")
    cm_img_path = r"d:\Năm 3 học kỳ 1\Khoa học dữ liệu\HR Analytics\figures\confusion_matrix_lightgbm.png"
    if os.path.exists(cm_img_path):
        doc.add_paragraph().alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.paragraphs[-1].paragraph_format.space_after = Pt(2)
        doc.paragraphs[-1].add_run().add_picture(cm_img_path, width=Inches(4.5))
        add_caption("Hình 5.2: Ma trận nhầm lẫn của mô hình LightGBM trên tập kiểm định")

    add_body("Phân tích giá trị nghiệp vụ: Trên tập kiểm định độc lập gồm 955 nhân sự có ý định nhảy việc thực tế, LightGBM đã phát hiện chính xác tới 755 trường hợp (True Positives, Recall đạt tới ~79.06%), và chỉ bỏ sót 200 trường hợp. Đối với bài toán nhân sự, chi phí bỏ sót một nhân sự then chốt nghỉ việc (False Negative) đắt đỏ hơn rất nhiều so với việc cảnh báo nhầm một nhân sự có rủi ro (False Positive). Do đó, LightGBM mang lại hiệu quả ứng dụng thực tế cao nhất.")

    add_h2("5.5. Phân tích độ quan trọng của đặc trưng (Feature Importance)")
    fi_img_path = r"d:\Năm 3 học kỳ 1\Khoa học dữ liệu\HR Analytics\figures\feature_importance_lightgbm.png"
    if os.path.exists(fi_img_path):
        doc.add_paragraph().alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.paragraphs[-1].paragraph_format.space_after = Pt(2)
        doc.paragraphs[-1].add_run().add_picture(fi_img_path, width=Inches(5.5))
        add_caption("Hình 5.3: Biểu đồ xếp hạng độ quan trọng đặc trưng trích xuất từ LightGBM")

    add_body("Các nhân tố chi phối quyết định nhảy việc hàng đầu gồm có:")
    add_bullet(" Đóng góp trên 35% sức mạnh phân loại. Những nhân sự làm việc tại các thành phố có điều kiện cơ sở hạ tầng và kinh tế hạn chế có tỷ lệ mong muốn dịch chuyển việc làm cao nhất.", "1. Chỉ số phát triển thành phố (city_development_index):")
    add_bullet(" Chiếm trên 20% mức độ quan trọng. Những cá nhân tích cực đầu tư số giờ học tập chuyên môn lớn là những người có động lực phát triển bản thân mạnh mẽ và sẵn sàng đón nhận thử thách mới.", "2. Số giờ đào tạo hoàn thành (training_hours):")
    add_bullet(" Nhân sự trẻ từ 1 đến 4 năm kinh nghiệm có độ dịch chuyển cao nhất, trong khi nhóm có thâm niên trên 15 năm có xu hướng gắn bó ổn định.", "3. Số năm kinh nghiệm làm việc (experience):")
    add_bullet(" Nhân viên tại các công ty quy mô nhỏ hoặc startup có tỷ lệ nghỉ việc cao hơn các tập đoàn lớn.", "4. Quy mô công ty (company_size):")

    add_h1("CHƯƠNG 6: KHUYẾN NGHỊ VÀ ỨNG DỤNG THỰC TIỄN CHO DOANH NGHIỆP")
    add_h2("6.1. Nhận diện nhóm đối tượng có nguy cơ nhảy việc cao nhất")
    add_body("Từ các phát hiện của mô hình, chân dung nhân sự có nguy cơ chuyển việc cao nhất được phác họa như sau: Chuyên viên dữ liệu trẻ (1-4 năm kinh nghiệm), cư trú tại các thành phố có chỉ số CDI thấp (< 0.70), làm việc tại các công ty nhỏ (< 50 nhân viên), và đã tích lũy số giờ đào tạo chuyên môn cao (> 60 giờ).")

    add_h2("6.2. Chiến lược nhân sự đề xuất cho doanh nghiệp")
    add_bullet(" Cung cấp phụ cấp thu hút vùng miền, hỗ trợ trang thiết bị làm việc hoặc áp dụng chính sách làm việc từ xa (Remote / Hybrid) linh hoạt cho các chuyên viên dữ liệu tại các chi nhánh tỉnh/thành phố nhỏ.", "Chính sách phúc lợi theo vùng:")
    add_bullet(" Gắn liền việc hoàn thành khóa đào tạo Big Data/Data Science với cơ hội thăng tiến, tăng bậc lương hoặc bổ nhiệm tham gia vào các dự án AI trọng điểm của tập đoàn.", "Lộ trình phát triển sau đào tạo:")
    add_bullet(" Thiết lập chương trình Mentoring 1-kèm-1 giữa các Chuyên gia kỳ cựu (Lead / Principal) và các kỹ sư trẻ để đồng hành, gỡ rối kỹ thuật và gia tăng mức độ gắn kết văn hóa doanh nghiệp.", "Đồng hành cùng nhân sự trẻ:")

    add_h1("CHƯƠNG 7: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN")
    add_h2("7.1. Kết luận")
    add_body("Đồ án đã giải quyết trọn vẹn và bài bản bài toán dự đoán xác suất chuyển việc của chuyên viên dữ liệu:")
    add_bullet(" Tiền xử lý dữ liệu chuẩn xác theo giáo trình bộ môn (Mode & Median), số hóa 100% không còn NaN hay số âm.")
    add_bullet(" Xây dựng độc lập 3 mô hình học máy: Logistic Regression (0.7274), Random Forest (0.7844) và LightGBM (0.7890).")
    add_bullet(" Kiểm định chéo Stratified 5-Fold khách quan, trích xuất đầy đủ các biểu đồ đánh giá và phân tích chuyên sâu.")
    add_bullet(" Đóng gói mã nguồn chuẩn công nghiệp, phục vụ tốt cho cả nghiên cứu học thuật và ứng dụng thực tiễn.")

    add_h2("7.2. Hướng mở rộng")
    add_bullet(" Thu thập thêm các biến số tài chính (mức lương, thưởng, cơ chế cổ phần ESOP) để nâng cao độ chính xác.")
    add_bullet(" Thử nghiệm các kỹ thuật cân bằng dữ liệu nâng cao như SMOTE kết hợp Tomek Links.")
    add_bullet(" Triển khai mô hình dưới dạng Web API (FastAPI / Streamlit) để tích hợp trực tiếp vào hệ thống ERP/HRM của doanh nghiệp.")

    add_h1("TÀI LIỆU THAM KHẢO")
    add_bullet(" Slide bài giảng môn học: DS04-DM03-DataPreProcess.ppt, Bộ môn Khoa học dữ liệu.")
    add_bullet(" Ke, G., et al. (2017). 'LightGBM: A highly efficient gradient boosting decision tree.' Advances in Neural Information Processing Systems (NeurIPS), 30.")
    add_bullet(" Breiman, L. (2001). 'Random forests.' Machine Learning, 45(1), 5-32.")
    add_bullet(" Pedregosa, F., et al. (2011). 'Scikit-learn: Machine learning in Python.' JMLR, 12, 2825-2830.")
    add_bullet(" Kaggle Dataset: HR Analytics: Job Change of Data Scientists.")

    output_path = r"d:\Năm 3 học kỳ 1\Khoa học dữ liệu\HR Analytics\Bao_Cao_Do_An_HR_Analytics.docx"
    doc.save(output_path)
    print(f"[OK] Da tao thanh cong file Bao Cao Word tai: {output_path}")

if __name__ == "__main__":
    create_report()
