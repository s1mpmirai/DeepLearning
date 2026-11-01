import os
import math
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_document():
    doc = docx.Document()

    # Set page margins (1 inch around)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Base style
    style_normal = doc.styles['Normal']
    font = style_normal.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0, 0, 0)

    def set_black(run):
        run.font.name = 'Times New Roman'
        run.font.color.rgb = RGBColor(0, 0, 0)

    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        set_black(run)
        run.font.size = Pt(16)
        run.bold = True
        return p

    def add_student_info(lines):
        for line in lines:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(line)
            set_black(run)
            run.font.size = Pt(12)
        # Add spacing after info
        p_space = doc.add_paragraph()
        p_space.paragraph_format.space_before = Pt(0)
        p_space.paragraph_format.space_after = Pt(12)

    def add_part_heading(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        set_black(run)
        run.font.size = Pt(14)
        run.bold = True
        return p

    def add_question_heading(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        set_black(run)
        run.font.size = Pt(13)
        run.bold = True
        return p

    def add_sub_heading(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        set_black(run)
        run.font.size = Pt(12)
        run.bold = True
        return p

    def add_body(text, space_after=4):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        set_black(run)
        run.font.size = Pt(12)
        run.bold = False
        return p

    def set_table_borders(table):
        tblPr = table._tbl.tblPr
        borders_xml = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>\n'
            f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
            f'  <w:left w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
            f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
            f'  <w:right w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
            f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
            f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
            f'</w:tblBorders>'
        )
        tblPr.append(borders_xml)

    def add_custom_table(headers, data, col_widths=None):
        table = doc.add_table(rows=len(data) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(table)

        # Header row
        hdr_cells = table.rows[0].cells
        for i, header_text in enumerate(headers):
            hdr_cells[i].text = header_text
            p = hdr_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            for r in p.runs:
                set_black(r)
                r.font.size = Pt(11)
                r.bold = True

        # Data rows
        for r_idx, row_data in enumerate(data):
            row_cells = table.rows[r_idx + 1].cells
            for c_idx, cell_value in enumerate(row_data):
                row_cells[c_idx].text = str(cell_value)
                p = row_cells[c_idx].paragraphs[0]
                p.paragraph_format.space_before = Pt(3)
                p.paragraph_format.space_after = Pt(3)
                # align center for numbers/short codes, left for text
                if len(str(cell_value)) < 15 and not any(k in str(cell_value) for k in ['Duyệt', 'Gom', 'Chậm', 'Tận', 'Thao', 'Tối', 'Cồng', 'Tự', 'Dài', 'Ngắn']):
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in p.runs:
                    set_black(r)
                    r.font.size = Pt(11)
                    r.bold = False

        if col_widths:
            for row in table.rows:
                for idx, width in enumerate(col_widths):
                    row.cells[idx].width = Inches(width)

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # ------------------ DOCUMENT CONTENT ------------------

    # Header & Student Info
    add_title("BÀI TẬP TUẦN 8: MẠNG NƠ-RON NHIỀU TẦNG (MLP)")
    add_student_info([
        "Môn học: Học sâu (Deep Learning)",
        "Họ và tên: Nguyễn Hoàng Tín - MSSV: 3123411299",
        "Lớp: DCT123C3 - Khoa: Công nghệ Thông tin - Trường Đại học Sài Gòn"
    ])

    # ==================== PHẦN 1 ====================
    add_part_heading("PHẦN 1. LAN TRUYỀN XUÔI VÀ CẬP NHẬT TRỌNG SỐ CỦA MỘT NƠ-RON")

    add_question_heading("Câu 1. Tính tổng có trọng số z")
    add_body("Công thức tổng có trọng số:")
    add_body("z = w1 * x1 + w2 * x2 + wbias * b")
    add_body("Thay các giá trị số ban đầu w1 = 0.25, w2 = 0.25, wbias = 0.25, x1 = 0.1, x2 = 0.2, b = 1:")
    add_body("z = 0.25 * 0.1 + 0.25 * 0.2 + 0.25 * 1")
    add_body("z = 0.025 + 0.050 + 0.250 = 0.325")

    add_question_heading("Câu 2. Tính đầu ra dự đoán ŷ")
    add_body("Công thức hàm kích hoạt Sigmoid:")
    add_body("ŷ = σ(z) = 1 / (1 + e^(-z))")
    add_body("Thay giá trị z = 0.325:")
    add_body("ŷ = 1 / (1 + e^(-0.325)) = 1 / (1 + 0.722530) = 1 / 1.722530 ≈ 0.580542")

    add_question_heading("Câu 3. Tính giá trị hàm mất mát Cross-Entropy")
    add_body("Công thức hàm mất mát Binary Cross-Entropy:")
    add_body("L = -[y * ln(ŷ) + (1 - y) * ln(1 - ŷ)]")
    add_body("Với nhãn thực tế y = 1, thành phần thứ hai (1 - y) * ln(1 - ŷ) bằng 0. Biểu thức rút gọn:")
    add_body("L = -ln(ŷ)")
    add_body("Thay ŷ = 0.580542:")
    add_body("L = -ln(0.580542) ≈ 0.543793")

    add_question_heading("Câu 4. Tính các đạo hàm ∂L/∂w1, ∂L/∂w2, ∂L/∂wbias theo quy tắc dây chuyền")
    add_body("Áp dụng quy tắc dây chuyền phân rã đạo hàm qua các biến trung gian:")
    add_body("∂L/∂w = (∂L/∂ŷ) * (∂ŷ/∂z) * (∂z/∂w)")
    add_body("Đạo hàm của hàm mất mát L theo đầu ra dự đoán ŷ (với y = 1):")
    add_body("∂L/∂ŷ = -y / ŷ + (1 - y) / (1 - ŷ) = -1 / ŷ")
    add_body("Đạo hàm của hàm Sigmoid theo z:")
    add_body("∂ŷ/∂z = σ'(z) = ŷ * (1 - ŷ)")
    add_body("Nhân hai đạo hàm trung gian để thu được sai số gradient tại z:")
    add_body("∂L/∂z = (∂L/∂ŷ) * (∂ŷ/∂z) = (-1 / ŷ) * [ŷ * (1 - ŷ)] = -(1 - ŷ) = ŷ - 1")
    add_body("Thay số tính giá trị ∂L/∂z:")
    add_body("∂L/∂z = 0.580542 - 1 = -0.419458")
    add_body("Đạo hàm của z theo từng trọng số:")
    add_body("∂z/∂w1 = x1 = 0.1")
    add_body("∂z/∂w2 = x2 = 0.2")
    add_body("∂z/∂wbias = b = 1.0")
    add_body("Giá trị gradient của từng tham số:")
    add_body("∂L/∂w1 = (∂L/∂z) * x1 = -0.419458 * 0.1 = -0.041946")
    add_body("∂L/∂w2 = (∂L/∂z) * x2 = -0.419458 * 0.2 = -0.083892")
    add_body("∂L/∂wbias = (∂L/∂z) * b = -0.419458 * 1.0 = -0.419458")

    add_question_heading("Câu 5. Cập nhật các trọng số bằng Gradient Descent với α = 0.1")
    add_body("Công thức cập nhật tổng quát của thuật toán Gradient Descent:")
    add_body("w_mới = w_cũ - α * (∂L/∂w)")
    add_body("Cập nhật cho từng tham số với α = 0.1:")
    add_body("w1_mới = 0.25 - 0.1 * (-0.041946) = 0.25 + 0.004195 = 0.254195")
    add_body("w2_mới = 0.25 - 0.1 * (-0.083892) = 0.25 + 0.008389 = 0.258389")
    add_body("wbias_mới = 0.25 - 0.1 * (-0.419458) = 0.25 + 0.041946 = 0.291946")

    add_question_heading("Câu 6. Tính lại đầu ra và hàm mất mát sau một lần cập nhật, nhận xét sự thay đổi")
    add_body("Tính tổng có trọng số mới:")
    add_body("z_mới = w1_mới * x1 + w2_mới * x2 + wbias_mới * b")
    add_body("z_mới = 0.254195 * 0.1 + 0.258389 * 0.2 + 0.291946 * 1.0")
    add_body("z_mới = 0.025420 + 0.051678 + 0.291946 = 0.369044")
    add_body("Tính đầu ra dự đoán mới:")
    add_body("ŷ_mới = 1 / (1 + e^(-0.369044)) = 1 / (1 + 0.691396) ≈ 0.591228")
    add_body("Tính giá trị hàm mất mát mới:")
    add_body("L_mới = -ln(ŷ_mới) = -ln(0.591228) ≈ 0.525554")
    add_body("Bảng tổng hợp trước và sau khi cập nhật trọng số:")
    add_custom_table(
        ["Đại lượng", "Trước cập nhật", "Sau cập nhật (1 bước)", "Mức độ thay đổi"],
        [
            ["Trọng số w1", "0.250000", "0.254195", "+0.004195"],
            ["Trọng số w2", "0.250000", "0.258389", "+0.008389"],
            ["Trọng số bias wbias", "0.250000", "0.291946", "+0.041946"],
            ["Tổng có trọng số z", "0.325000", "0.369044", "+0.044044"],
            ["Đầu ra dự đoán ŷ", "0.580542", "0.591228", "+0.010686"],
            ["Hàm mất mát L", "0.543793", "0.525554", "-0.018239"]
        ],
        col_widths=[1.8, 1.4, 1.8, 1.4]
    )
    add_body("Nhận xét sự thay đổi:")
    add_body("- Đầu ra dự đoán ŷ tăng từ 0.580542 lên 0.591228, dịch chuyển gần hơn về phía nhãn mục tiêu y = 1.")
    add_body("- Hàm mất mát L giảm từ 0.543793 xuống 0.525554 (giảm 0.018239 đơn vị sai số).")
    add_body("- Điều này chứng minh thuật toán Gradient Descent đã hoạt động chính xác theo lý thuyết: các trọng số được điều chỉnh ngược chiều gradient âm, đưa mô hình tiến gần hơn đến nghiệm tối ưu.")

    # ==================== PHẦN 2 ====================
    add_part_heading("PHẦN 2. BIỂU DIỄN MẠNG NƠ-RON BẰNG VECTOR VÀ MA TRẬN")

    add_question_heading("Câu 1. Xác định vector đầu vào, ma trận trọng số và vector bias của mạng")
    add_body("Vector đầu vào x (kích thước 2 * 1):")
    add_body("x = [x1, x2]^T = [0.1, 0.2]^T")
    add_body("Ma trận trọng số W (kích thước 2 * 2), trong đó hàng 1 chứa trọng số liên kết đến nơ-ron 1 và hàng 2 chứa trọng số liên kết đến nơ-ron 2:")
    add_body("W = [[w11, w21], [w12, w22]] = [[0.5, 0.5], [0.5, 0.5]]")
    add_body("Vector trọng số bias b (kích thước 2 * 1):")
    add_body("b = [wbias,1, wbias,2]^T = [0.5, 0.5]^T")

    add_question_heading("Câu 2. Viết phương trình lan truyền xuôi dưới dạng vector và ma trận")
    add_body("Phương trình tính vector tổng có trọng số z:")
    add_body("z = W * x + b")
    add_body("Phương trình tính vector đầu ra dự đoán ŷ:")
    add_body("ŷ = f(z) = [f(z1), f(z2)]^T")
    add_body("Trong đó hàm kích hoạt f(z) được áp dụng đồng thời trên từng phần tử của vector z.")

    add_question_heading("Câu 3. Tính vector tổng có trọng số z")
    add_body("Thực hiện phép nhân ma trận và cộng vector:")
    add_body("z = [[0.5, 0.5], [0.5, 0.5]] * [0.1, 0.2]^T + [0.5, 0.5]^T")
    add_body("z = [0.5 * 0.1 + 0.5 * 0.2, 0.5 * 0.1 + 0.5 * 0.2]^T + [0.5, 0.5]^T")
    add_body("z = [0.05 + 0.10, 0.05 + 0.10]^T + [0.5, 0.5]^T")
    add_body("z = [0.15, 0.15]^T + [0.5, 0.5]^T = [0.65, 0.65]^T")

    add_question_heading("Câu 4. Biểu diễn vector đầu ra dưới dạng ŷ = f(z)")
    add_body("Giả định lựa chọn hàm kích hoạt Sigmoid theo gợi ý của đề bài: f(z) = σ(z) = 1 / (1 + e^(-z)).")
    add_body("ŷ = [σ(z1), σ(z2)]^T = [σ(0.65), σ(0.65)]^T")
    add_body("Tính giá trị cụ thể:")
    add_body("σ(0.65) = 1 / (1 + e^(-0.65)) = 1 / (1 + 0.522046) ≈ 0.657010")
    add_body("Vector đầu ra dự đoán:")
    add_body("ŷ = [0.657010, 0.657010]^T")

    add_question_heading("Câu 5. Thực hiện phép tính lan truyền xuôi bằng phương pháp vectorized")
    add_body("Quy trình tính toán theo phương pháp Vectorized gồm 3 bước đại số tuyến tính liên tục:")
    add_body("Bước 1: Tích vô hướng ma trận trọng số và vector đầu vào:")
    add_body("u = W * x = [[0.5, 0.5], [0.5, 0.5]] * [[0.1], [0.2]] = [[0.5 * 0.1 + 0.5 * 0.2], [0.5 * 0.1 + 0.5 * 0.2]] = [[0.15], [0.15]]")
    add_body("Bước 2: Cộng vector bias theo cơ chế vector addition:")
    add_body("z = u + b = [[0.15], [0.15]] + [[0.5], [0.5]] = [[0.65], [0.65]]")
    add_body("Bước 3: Áp dụng hàm phi tuyến Sigmoid trên toàn bộ vector z:")
    add_body("ŷ = 1 / (1 + exp(-z)) = [[1 / (1 + exp(-0.65))], [1 / (1 + exp(-0.65))]] = [[0.657010], [0.657010]]")

    add_question_heading("Câu 6. So sánh cách tính bằng từng nơ-ron với cách tính bằng phép nhân ma trận; giải thích lợi ích của vectorization")
    add_body("Bảng so sánh hai phương pháp tính toán:")
    add_custom_table(
        ["Tiêu chí", "Tính bằng từng nơ-ron (Vòng lặp tuần tự)", "Tính bằng ma trận (Vectorization)"],
        [
            ["Cơ chế thực thi", "Duyệt vòng lặp for tính riêng từng zj = ∑ wij * xi + bj rồi tính ŷj.", "Gom toàn bộ trọng số và đầu vào vào ma trận để tính z = W * x + b."],
            ["Tốc độ tính toán", "Chậm, tốn chi phí điều khiển vòng lặp và truy xuất bộ nhớ rời rạc.", "Rất nhanh, xử lý song song toàn bộ các phép tính trong một chu kỳ lệnh."],
            ["Tận dụng phần cứng", "Chỉ tận dụng được năng lực xử lý tuần tự cơ bản của CPU.", "Khai thác tối đa các chỉ lệnh SIMD trên CPU và hàng nghìn lõi song song trên GPU."],
            ["Khả năng mở rộng", "Cồng kềnh khi mạng tăng số lớp và dữ liệu có batch size lớn.", "Dễ dàng mở rộng sang ma trận batch X với công thức Z = X * W^T + b^T."],
            ["Cú pháp mã nguồn", "Dài dòng, nhiều vòng lặp lồng nhau, dễ xảy ra lỗi lập trình.", "Ngắn gọn, rõ nghĩa toán học, đồng bộ chuẩn xác với biểu thức lý thuyết."]
        ],
        col_widths=[1.5, 2.5, 2.5]
    )
    add_body("Giải thích lợi ích của Vectorization:")
    add_body("- Tăng tốc độ huấn luyện mô hình Học sâu từ hàng chục đến hàng trăm lần nhờ các thư viện đại số tuyến tính tối ưu cao (như BLAS, LAPACK, cuBLAS trong PyTorch).")
    add_body("- Cho phép xử lý đồng thời cả lô dữ liệu (mini-batch) thay vì từng mẫu đơn lẻ, giúp gradient cập nhật ổn định hơn và hội tụ nhanh hơn.")
    add_body("- Mã nguồn ngắn gọn, trực tiếp, hạn chế lỗi chỉ số trong các vòng lặp lồng nhau.")

    # ==================== PHẦN 3 ====================
    add_part_heading("PHẦN 3. LAN TRUYỀN NGƯỢC VỚI CÁC HÀM KÍCH HOẠT KHÁC NHAU")

    add_question_heading("Câu 1. Viết biểu thức tính tổng có trọng số tại hai nơ-ron đầu ra")
    add_body("Biểu thức tính tổng có trọng số tại nơ-ron đầu ra 1:")
    add_body("z1 = w11 * x1 + w21 * x2 + wbias,1 * b = 0.5 * 0.1 + 0.5 * 0.2 + 0.5 * 1.0 = 0.65")
    add_body("Biểu thức tính tổng có trọng số tại nơ-ron đầu ra 2:")
    add_body("z2 = w12 * x1 + w22 * x2 + wbias,2 * b = 0.5 * 0.1 + 0.5 * 0.2 + 0.5 * 1.0 = 0.65")

    add_question_heading("Câu 2. Tính đầu ra của mạng cho từng trường hợp")
    add_sub_heading("Trường hợp 1: Tanh tại nơ-ron 1 và Sigmoid tại nơ-ron 2")
    add_body("Đầu ra nơ-ron 1: ŷ1 = tanh(z1) = (e^0.65 - e^(-0.65)) / (e^0.65 + e^(-0.65)) = (1.915541 - 0.522046) / (1.915541 + 0.522046) = 1.393495 / 2.437587 ≈ 0.571670")
    add_body("Đầu ra nơ-ron 2: ŷ2 = σ(z2) = 1 / (1 + e^(-0.65)) ≈ 0.657010")

    add_sub_heading("Trường hợp 2: ReLU tại nơ-ron 1 và Sigmoid tại nơ-ron 2")
    add_body("Đầu ra nơ-ron 1: ŷ1 = ReLU(z1) = max(0, 0.65) = 0.650000")
    add_body("Đầu ra nơ-ron 2: ŷ2 = σ(z2) = 1 / (1 + e^(-0.65)) ≈ 0.657010")

    add_question_heading("Câu 3. Tính giá trị hàm mất mát theo cách định nghĩa phù hợp")
    add_body("Nhận diện vấn đề lý thuyết:")
    add_body("Hàm Binary Cross-Entropy đòi hỏi đầu ra dự đoán phải thuộc khoảng xác suất (0, 1). Tuy nhiên hàm Tanh có miền giá trị (-1, 1) và hàm ReLU có miền giá trị [0, +∞).")
    add_body("Giải pháp xử lý:")
    add_body("Tại điểm đầu vào khảo sát cụ thể, z1 = 0.65 dẫn đến ŷ1(Tanh) ≈ 0.571670 ∈ (0, 1) và ŷ1(ReLU) = 0.650000 ∈ (0, 1). Cả hai giá trị này đều nằm trong miền xác suất hợp lệ, cho phép áp dụng trực tiếp hàm Binary Cross-Entropy trên từng đầu ra để đo lường sai số với nhãn mục tiêu y1 = 0 và y2 = 1:")
    add_body("L = L1 + L2")
    add_body("Thành phần hàm mất mát tại nơ-ron 2 (với y2 = 1):")
    add_body("L2 = -[1 * ln(ŷ2) + 0 * ln(1 - ŷ2)] = -ln(ŷ2) = -ln(0.657010) ≈ 0.420055")
    add_body("Thành phần hàm mất mát tại nơ-ron 1 (với y1 = 0):")
    add_body("L1 = -[0 * ln(ŷ1) + 1 * ln(1 - ŷ1)] = -ln(1 - ŷ1)")
    add_body("Tính toán cụ thể cho hai trường hợp:")
    add_body("- Trường hợp 1 (Tanh & Sigmoid):")
    add_body("L1 = -ln(1 - 0.571670) = -ln(0.428330) ≈ 0.847861")
    add_body("L_TH1 = L1 + L2 = 0.847861 + 0.420055 = 1.267916")
    add_body("- Trường hợp 2 (ReLU & Sigmoid):")
    add_body("L1 = -ln(1 - 0.650000) = -ln(0.350000) ≈ 1.049822")
    add_body("L_TH2 = L1 + L2 = 1.049822 + 0.420055 = 1.469877")

    add_question_heading("Câu 4. Áp dụng quy tắc dây chuyền để tính gradient của các trọng số và bias")
    add_body("Quy tắc dây chuyền tổng quát cho nơ-ron j:")
    add_body("∂L/∂wij = (∂L/∂ŷj) * (∂ŷj/∂zj) * (∂zj/∂wij) = (∂L/∂zj) * xi")
    add_body("∂L/∂wbias,j = (∂L/∂zj) * b")

    add_sub_heading("1. Gradient tại nơ-ron 2 (Hàm kích hoạt Sigmoid, y2 = 1 - dùng chung cho cả 2 trường hợp)")
    add_body("∂L/∂ŷ2 = -1 / ŷ2")
    add_body("∂ŷ2/∂z2 = ŷ2 * (1 - ŷ2)")
    add_body("∂L/∂z2 = (∂L/∂ŷ2) * (∂ŷ2/∂z2) = ŷ2 - 1 = 0.657010 - 1 = -0.342990")
    add_body("Gradient theo các trọng số của nơ-ron 2:")
    add_body("∂L/∂w12 = (∂L/∂z2) * x1 = -0.342990 * 0.1 = -0.034299")
    add_body("∂L/∂w22 = (∂L/∂z2) * x2 = -0.342990 * 0.2 = -0.068598")
    add_body("∂L/∂wbias,2 = (∂L/∂z2) * b = -0.342990 * 1.0 = -0.342990")

    add_sub_heading("2. Gradient tại nơ-ron 1 trong Trường hợp 1 (Hàm kích hoạt Tanh, y1 = 0)")
    add_body("∂L1/∂ŷ1 = 1 / (1 - ŷ1)")
    add_body("∂ŷ1/∂z1 = 1 - tanh^2(z1) = (1 - ŷ1) * (1 + ŷ1)")
    add_body("∂L/∂z1 = (∂L1/∂ŷ1) * (∂ŷ1/∂z1) = [1 / (1 - ŷ1)] * [(1 - ŷ1) * (1 + ŷ1)] = 1 + ŷ1 = 1 + 0.571670 = 1.571670")
    add_body("Gradient theo các trọng số của nơ-ron 1 (TH1):")
    add_body("∂L/∂w11 = (∂L/∂z1) * x1 = 1.571670 * 0.1 = 0.157167")
    add_body("∂L/∂w21 = (∂L/∂z1) * x2 = 1.571670 * 0.2 = 0.314334")
    add_body("∂L/∂wbias,1 = (∂L/∂z1) * b = 1.571670 * 1.0 = 1.571670")

    add_sub_heading("3. Gradient tại nơ-ron 1 trong Trường hợp 2 (Hàm kích hoạt ReLU, y1 = 0)")
    add_body("∂L1/∂ŷ1 = 1 / (1 - ŷ1) = 1 / (1 - 0.65) = 1 / 0.35 ≈ 2.857143")
    add_body("∂ŷ1/∂z1 = 1 (do z1 = 0.65 > 0)")
    add_body("∂L/∂z1 = (∂L1/∂ŷ1) * (∂ŷ1/∂z1) = 2.857143 * 1 = 2.857143")
    add_body("Gradient theo các trọng số của nơ-ron 1 (TH2):")
    add_body("∂L/∂w11 = (∂L/∂z1) * x1 = 2.857143 * 0.1 = 0.285714")
    add_body("∂L/∂w21 = (∂L/∂z1) * x2 = 2.857143 * 0.2 = 0.571429")
    add_body("∂L/∂wbias,1 = (∂L/∂z1) * b = 2.857143 * 1.0 = 2.857143")

    add_question_heading("Câu 5. Cập nhật toàn bộ trọng số và bias sau một bước Gradient Descent với α = 0.1")
    add_body("Công thức cập nhật: w_mới = w_cũ - α * (∂L/∂w)")

    add_sub_heading("Cập nhật tham số nơ-ron 2 (chung cho cả hai trường hợp):")
    add_body("w12_mới = 0.5 - 0.1 * (-0.034299) = 0.5 + 0.003430 = 0.503430")
    add_body("w22_mới = 0.5 - 0.1 * (-0.068598) = 0.5 + 0.006860 = 0.506860")
    add_body("wbias,2_mới = 0.5 - 0.1 * (-0.342990) = 0.5 + 0.034299 = 0.534299")

    add_sub_heading("Cập nhật tham số nơ-ron 1 trong Trường hợp 1 (Tanh):")
    add_body("w11_mới = 0.5 - 0.1 * 0.157167 = 0.5 - 0.015717 = 0.484283")
    add_body("w21_mới = 0.5 - 0.1 * 0.314334 = 0.5 - 0.031433 = 0.468567")
    add_body("wbias,1_mới = 0.5 - 0.1 * 1.571670 = 0.5 - 0.157167 = 0.342833")

    add_sub_heading("Cập nhật tham số nơ-ron 1 trong Trường hợp 2 (ReLU):")
    add_body("w11_mới = 0.5 - 0.1 * 0.285714 = 0.5 - 0.028571 = 0.471429")
    add_body("w21_mới = 0.5 - 0.1 * 0.571429 = 0.5 - 0.057143 = 0.442857")
    add_body("wbias,1_mới = 0.5 - 0.1 * 2.857143 = 0.5 - 0.285714 = 0.214286")

    add_question_heading("Câu 6. Tính lại kết quả dự đoán sau cập nhật")
    add_sub_heading("1. Kết quả dự đoán tại nơ-ron 2 (Sigmoid):")
    add_body("z2_mới = 0.503430 * 0.1 + 0.506860 * 0.2 + 0.534299 * 1.0 = 0.050343 + 0.101372 + 0.534299 = 0.686014")
    add_body("ŷ2_mới = 1 / (1 + e^(-0.686014)) ≈ 0.665080")
    add_body("L2_mới = -ln(0.665080) ≈ 0.407849 (giảm từ 0.420055)")

    add_sub_heading("2. Kết quả dự đoán tại nơ-ron 1 trong Trường hợp 1 (Tanh):")
    add_body("z1_mới = 0.484283 * 0.1 + 0.468567 * 0.2 + 0.342833 * 1.0 = 0.048428 + 0.093713 + 0.342833 = 0.484974")
    add_body("ŷ1_mới = tanh(0.484974) ≈ 0.450219 (giảm từ 0.571670 về phía y1 = 0)")
    add_body("L1_mới = -ln(1 - 0.450219) = -ln(0.549781) ≈ 0.598235 (giảm từ 0.847861)")
    add_body("Tổng mất mát TH1 sau cập nhật: L_TH1_mới = 0.598235 + 0.407849 = 1.006084 (giảm 0.261832)")

    add_sub_heading("3. Kết quả dự đoán tại nơ-ron 1 trong Trường hợp 2 (ReLU):")
    add_body("z1_mới = 0.471429 * 0.1 + 0.442857 * 0.2 + 0.214286 * 1.0 = 0.047143 + 0.088571 + 0.214286 = 0.350000")
    add_body("ŷ1_mới = ReLU(0.350000) = 0.350000 (giảm từ 0.650000 về phía y1 = 0)")
    add_body("L1_mới = -ln(1 - 0.350000) = -ln(0.650000) ≈ 0.430783 (giảm từ 1.049822)")
    add_body("Tổng mất mát TH2 sau cập nhật: L_TH2_mới = 0.430783 + 0.407849 = 0.838632 (giảm 0.631245)")

    add_body("Bảng tổng hợp so sánh các thông số trước và sau cập nhật ở cả hai trường hợp:")
    add_custom_table(
        ["Đại lượng", "Ban đầu", "Sau cập nhật TH1 (Tanh)", "Sau cập nhật TH2 (ReLU)"],
        [
            ["Trọng số w11", "0.500000", "0.484283", "0.471429"],
            ["Trọng số w21", "0.500000", "0.468567", "0.442857"],
            ["Trọng số wbias,1", "0.500000", "0.342833", "0.214286"],
            ["Tổng trọng số z1", "0.650000", "0.484974", "0.350000"],
            ["Đầu ra dự đoán ŷ1 (đích: 0)", "0.571670 / 0.650000", "0.450219", "0.350000"],
            ["Mất mát nơ-ron 1 (L1)", "0.847861 / 1.049822", "0.598235", "0.430783"],
            ["Đầu ra dự đoán ŷ2 (đích: 1)", "0.657010", "0.665080", "0.665080"],
            ["Mất mát nơ-ron 2 (L2)", "0.420055", "0.407849", "0.407849"],
            ["Tổng hàm mất mát L", "1.267916 / 1.469877", "1.006084", "0.838632"]
        ],
        col_widths=[1.8, 1.4, 1.9, 1.9]
    )

    add_question_heading("Câu 7. So sánh kết quả hai trường hợp, phân tích ảnh hưởng của Tanh, ReLU và Sigmoid đến gradient và quá trình cập nhật trọng số")
    add_body("1. Phân tích ảnh hưởng của từng hàm kích hoạt:")
    add_body("- Hàm Sigmoid (áp dụng tại nơ-ron 2):")
    add_body("  + Đặc tính gradient: Đạo hàm riêng σ'(z) = σ(z) * (1 - σ(z)) đạt giá trị cực đại bằng 0.25 tại z = 0 và tiến dần về 0 khi |z| lớn. Khi kết hợp với hàm mất mát Cross-Entropy, mẫu số triệt tiêu nhau cho gradient ∂L/∂z = ŷ - y rất đẹp và tuyến tính theo sai số.")
    add_body("  + Quá trình cập nhật: Trọng số thay đổi vừa phải (∂L/∂z2 = -0.342990), đảm bảo sự hội tụ mượt mà và an toàn, hạn chế dao động quá mức quanh cực tiểu.")
    add_body("- Hàm Tanh (áp dụng tại nơ-ron 1 ở TH1):")
    add_body("  + Đặc tính gradient: Đạo hàm riêng tanh'(z) = 1 - tanh^2(z) có giá trị cực đại bằng 1.0 tại z = 0, gấp 4 lần cực đại của Sigmoid. Hàm có tính chất đối xứng quanh gốc tọa độ (zero-centered), giúp dòng gradient truyền xuôi và ngược cân bằng hơn.")
    add_body("  + Quá trình cập nhật: Độ lớn gradient tại z1 đạt 1.571670, đưa giá trị ŷ1 giảm tương đối nhanh từ 0.571670 xuống 0.450219.")
    add_body("- Hàm ReLU (áp dụng tại nơ-ron 1 ở TH2):")
    add_body("  + Đặc tính gradient: Đạo hàm riêng bằng 1 với mọi z > 0 và bằng 0 với z < 0. Gradient không bị suy giảm (không bị hiện tượng Vanishing Gradient) trong miền dương.")
    add_body("  + Quá trình cập nhật: Do không có hệ số triệt tiêu của đạo hàm kích hoạt, gradient tại z1 đạt giá trị lớn nhất là 2.857143. Trọng số bias wbias,1 giảm mạnh từ 0.5 xuống 0.214286, làm cho đầu ra ŷ1 rơi nhanh nhất từ 0.650000 xuống 0.350000, tổng mất mát giảm mạnh nhất từ 1.469877 xuống 0.838632.")
    add_body("2. Kết luận và khuyến nghị thiết kế mạng nơ-ron theo lý thuyết Học sâu:")
    add_body("- Tầng ẩn (Hidden Layers): ReLU là lựa chọn chuẩn mực hàng đầu nhờ tốc độ tính toán nhanh, gradient bằng 1 khi z > 0 giúp mô hình học rất nhanh và chống triệt tiêu gradient ở mạng sâu. Tanh là lựa chọn tốt thứ hai khi dữ liệu cần duy trì tính chuẩn hóa đối xứng quanh 0.")
    add_body("- Tầng đầu ra (Output Layer): Sigmoid và Softmax là lựa chọn bắt buộc cho các bài toán phân loại xác suất (Classification) vì chúng đảm bảo giá trị đầu ra luôn nằm trong [0, 1] và tổng bằng 1. Không nên dùng trực tiếp Tanh hay ReLU ở tầng đầu ra kết hợp với Cross-Entropy vì chúng không thỏa mãn tiên đề xác suất và dễ gây mất ổn định số học.")

    # Save file
    output_dir = r"d:\it_sgu\4\1\DeepLearning\Tuan 8"
    output_filename = "BT07_MLP_NguyenHoangTin_3123411299.docx"
    output_path = os.path.join(output_dir, output_filename)
    doc.save(output_path)
    print(f"File created successfully at: {output_path}")

if __name__ == "__main__":
    create_document()
