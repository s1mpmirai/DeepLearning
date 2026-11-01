import os
import math
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def create_document():
    doc = docx.Document()

    # Set page margins
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
        p_space = doc.add_paragraph()
        p_space.paragraph_format.space_before = Pt(0)
        p_space.paragraph_format.space_after = Pt(10)

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
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
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
    add_title("BÀI TẬP: HUẤN LUYỆN MẠNG NEURON BẰNG BATCH GRADIENT DESCENT")
    add_student_info([
        "Môn học: Học sâu (Deep Learning)",
        "Họ và tên: Nguyễn Hoàng Tín - MSSV: 3123411299",
        "Lớp: DCT123C3 - Khoa: Công nghệ Thông tin - Trường Đại học Sài Gòn"
    ])

    # ==================== PHẦN A ====================
    add_part_heading("PHẦN A. NEURON KHÔNG HÀM KÍCH HOẠT")

    add_question_heading("Câu A1. Lan truyền xuôi (Forward pass)")
    add_body("Mô hình tuyến tính không sử dụng hàm kích hoạt:")
    add_body("ŷi = w * xi + b")
    add_body("Sai số dự đoán của từng mẫu dữ liệu:")
    add_body("ei = ŷi - yi")
    add_body("Với các tham số khởi tạo ban đầu w = 0, b = 0, kết quả tính toán chi tiết cho epoch 0:")
    add_body("- Mẫu 1: x1 = 1, y1 = 3 -> ŷ1 = 0 * 1 + 0 = 0 -> e1 = 0 - 3 = -3 -> e1^2 = (-3)^2 = 9")
    add_body("- Mẫu 2: x2 = 2, y2 = 5 -> ŷ2 = 0 * 2 + 0 = 0 -> e2 = 0 - 5 = -5 -> e2^2 = (-5)^2 = 25")
    add_body("- Mẫu 3: x3 = 3, y3 = 7 -> ŷ3 = 0 * 3 + 0 = 0 -> e3 = 0 - 7 = -7 -> e3^2 = (-7)^2 = 49")
    add_body("Bảng kết quả lan truyền xuôi epoch 0:")
    add_custom_table(
        ["i", "xi", "yi", "w", "b", "ŷi", "ei", "ei^2"],
        [
            ["1", "1", "3", "0", "0", "0", "-3", "9"],
            ["2", "2", "5", "0", "0", "0", "-5", "25"],
            ["3", "3", "7", "0", "0", "0", "-7", "49"]
        ],
        col_widths=[0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.9, 0.9]
    )

    add_question_heading("Câu A2. Tính hàm mất mát MSE")
    add_body("Công thức hàm mất mát trung bình bình phương sai số (Mean Squared Error):")
    add_body("MSE = (1 / 3) * ∑ (ei^2) = (1 / 3) * (e1^2 + e2^2 + e3^2)")
    add_body("Tổng bình phương sai số trên toàn bộ tập dữ liệu huấn luyện:")
    add_body("∑ (ei^2) = 9 + 25 + 49 = 83")
    add_body("Giá trị hàm mất mát MSE:")
    add_body("MSE = 83 / 3 ≈ 27.666667")
    add_body("Bảng kết quả tính hàm mất mát:")
    add_custom_table(
        ["∑ (ei^2)", "MSE"],
        [
            ["83", "27.666667"]
        ],
        col_widths=[3.0, 3.0]
    )

    add_question_heading("Câu A3. Tính gradient theo Batch Gradient Descent")
    add_body("Công thức đạo hàm riêng của hàm mất mát MSE theo trọng số w và bias b:")
    add_body("∂L/∂w = (2 / 3) * ∑ (ei * xi)")
    add_body("∂L/∂b = (2 / 3) * ∑ (ei)")
    add_body("Tính các thành phần cho từng mẫu:")
    add_body("- Mẫu 1: e1 = -3, x1 = 1 -> e1 * x1 = -3 * 1 = -3")
    add_body("- Mẫu 2: e2 = -5, x2 = 2 -> e2 * x2 = -5 * 2 = -10")
    add_body("- Mẫu 3: e3 = -7, x3 = 3 -> e3 * x3 = -7 * 3 = -21")
    add_body("Tổng sai số và tổng tích sai số với đầu vào:")
    add_body("∑ (ei) = (-3) + (-5) + (-7) = -15")
    add_body("∑ (ei * xi) = (-3) + (-10) + (-21) = -34")
    add_body("Bảng tổng hợp tính gradient:")
    add_custom_table(
        ["i", "ei", "xi", "ei * xi"],
        [
            ["1", "-3", "1", "-3"],
            ["2", "-5", "2", "-10"],
            ["3", "-7", "3", "-21"],
            ["Tổng", "-15", "-", "-34"]
        ],
        col_widths=[1.2, 1.6, 1.6, 1.8]
    )
    add_body("Giá trị gradient của các tham số theo toàn bộ batch:")
    add_body("∂L/∂w = (2 / 3) * (-34) = -68 / 3 ≈ -22.666667")
    add_body("∂L/∂b = (2 / 3) * (-15) = -30 / 3 = -10.000000")

    add_question_heading("Câu A4. Cập nhật tham số")
    add_body("Công thức cập nhật tham số với tốc độ học η = 0.01:")
    add_body("w^(1) = w^(0) - η * (∂L/∂w)")
    add_body("b^(1) = b^(0) - η * (∂L/∂b)")
    add_body("Thay số tính giá trị mới:")
    add_body("w^(1) = 0 - 0.01 * (-22.666667) = 0 + 0.226667 = 0.226667")
    add_body("b^(1) = 0 - 0.01 * (-10.000000) = 0 + 0.100000 = 0.100000")
    add_body("Bảng kết quả cập nhật tham số sau epoch 0:")
    add_custom_table(
        ["Tham số", "Giá trị cũ", "Gradient", "η", "Giá trị mới"],
        [
            ["w", "0", "-22.666667", "0.01", "0.226667"],
            ["b", "0", "-10.000000", "0.01", "0.100000"]
        ],
        col_widths=[1.2, 1.2, 1.6, 1.0, 1.4]
    )

    # ==================== PHẦN B ====================
    add_part_heading("PHẦN B. NEURON CÓ HÀM KÍCH HOẠT SIGMOID")

    add_question_heading("Câu B1. Lan truyền xuôi (Forward pass)")
    add_body("Mô hình nơ-ron có hàm kích hoạt Sigmoid:")
    add_body("zi = w * xi + b")
    add_body("ŷi = σ(zi) = 1 / (1 + e^(-zi))")
    add_body("ei = ŷi - yi")
    add_body("Với tham số khởi tạo ban đầu w = 0, b = 0:")
    add_body("- Mẫu 1: x1 = 1, y1 = 3 -> z1 = 0 * 1 + 0 = 0 -> ŷ1 = σ(0) = 1 / (1 + e^0) = 0.5 -> e1 = 0.5 - 3 = -2.5")
    add_body("- Mẫu 2: x2 = 2, y2 = 5 -> z2 = 0 * 2 + 0 = 0 -> ŷ2 = σ(0) = 1 / (1 + e^0) = 0.5 -> e2 = 0.5 - 5 = -4.5")
    add_body("- Mẫu 3: x3 = 3, y3 = 7 -> z3 = 0 * 3 + 0 = 0 -> ŷ3 = σ(0) = 1 / (1 + e^0) = 0.5 -> e3 = 0.5 - 7 = -6.5")
    add_body("Bảng kết quả lan truyền xuôi:")
    add_custom_table(
        ["i", "xi", "yi", "zi", "ŷi", "ei"],
        [
            ["1", "1", "3", "0", "0.5", "-2.5"],
            ["2", "2", "5", "0", "0.5", "-4.5"],
            ["3", "3", "7", "0", "0.5", "-6.5"]
        ],
        col_widths=[0.8, 1.0, 1.0, 1.0, 1.1, 1.1]
    )

    add_question_heading("Câu B2. Đạo hàm của hàm Sigmoid")
    add_body("Công thức đạo hàm của hàm kích hoạt Sigmoid:")
    add_body("σ'(z) = σ(z) * (1 - σ(z))")
    add_body("Với ŷ = σ(z), biểu thức đạo hàm viết gọn theo đầu ra kích hoạt:")
    add_body("∂ŷ/∂z = ŷ * (1 - ŷ)")

    add_question_heading("Câu B3. Tính gradient bằng quy tắc chuỗi (Chain Rule)")
    add_body("Áp dụng quy tắc chuỗi đạo hàm:")
    add_body("∂L/∂w = (2 / 3) * ∑ (ŷi - yi) * ŷi * (1 - ŷi) * xi")
    add_body("∂L/∂b = (2 / 3) * ∑ (ŷi - yi) * ŷi * (1 - ŷi)")
    add_body("Vì tại epoch 0, zi = 0 dẫn đến ŷi = 0.5 với mọi mẫu, ta có:")
    add_body("ŷi * (1 - ŷi) = 0.5 * (1 - 0.5) = 0.25")
    add_body("Tính các thành phần cho từng mẫu:")
    add_body("- Mẫu 1: e1 = -2.5 -> e1 * ŷ1 * (1 - ŷ1) = -2.5 * 0.25 = -0.625 -> nhân x1: -0.625 * 1 = -0.625")
    add_body("- Mẫu 2: e2 = -4.5 -> e2 * ŷ2 * (1 - ŷ2) = -4.5 * 0.25 = -1.125 -> nhân x2: -1.125 * 2 = -2.250")
    add_body("- Mẫu 3: e3 = -6.5 -> e3 * ŷ3 * (1 - ŷ3) = -6.5 * 0.25 = -1.625 -> nhân x3: -1.625 * 3 = -4.875")
    add_body("Tổng các đại lượng:")
    add_body("∑ [ei * ŷi * (1 - ŷi)] = (-0.625) + (-1.125) + (-1.625) = -3.375")
    add_body("∑ [ei * ŷi * (1 - ŷi) * xi] = (-0.625) + (-2.250) + (-4.875) = -7.750")
    add_body("Bảng tổng hợp chi tiết tính gradient:")
    add_custom_table(
        ["i", "ei", "ŷi * (1 - ŷi)", "ei * ŷi * (1 - ŷi)", "ei * ŷi * (1 - ŷi) * xi"],
        [
            ["1", "-2.5", "0.25", "-0.625", "-0.625"],
            ["2", "-4.5", "0.25", "-1.125", "-2.250"],
            ["3", "-6.5", "0.25", "-1.625", "-4.875"],
            ["Tổng", "-", "-", "-3.375", "-7.750"]
        ],
        col_widths=[0.8, 1.2, 1.4, 1.6, 1.6]
    )
    add_body("Giá trị gradient của các tham số:")
    add_body("∂L/∂w = (2 / 3) * (-7.75) = -15.5 / 3 ≈ -5.166667")
    add_body("∂L/∂b = (2 / 3) * (-3.375) = -6.75 / 3 = -2.250000")

    add_question_heading("Câu B4. Cập nhật tham số")
    add_body("Công thức cập nhật tham số với tốc độ học η = 0.01:")
    add_body("w^(1) = w^(0) - η * (∂L/∂w)")
    add_body("b^(1) = b^(0) - η * (∂L/∂b)")
    add_body("Thay số tính giá trị mới:")
    add_body("w^(1) = 0 - 0.01 * (-5.166667) = 0 + 0.051667 = 0.051667")
    add_body("b^(1) = 0 - 0.01 * (-2.250000) = 0 + 0.022500 = 0.022500")
    add_body("Bảng kết quả cập nhật tham số sau epoch 0:")
    add_custom_table(
        ["Tham số", "Giá trị cũ", "Gradient", "η", "Giá trị mới"],
        [
            ["w", "0", "-5.166667", "0.01", "0.051667"],
            ["b", "0", "-2.250000", "0.01", "0.022500"]
        ],
        col_widths=[1.2, 1.2, 1.6, 1.0, 1.4]
    )

    # ==================== PHẦN C ====================
    add_part_heading("PHẦN C. CÂU HỎI NHẬN XÉT")

    add_question_heading("Câu C1. So sánh biểu thức gradient của hai trường hợp")
    add_body("1. Biểu thức gradient trường hợp neuron tuyến tính (không dùng hàm kích hoạt):")
    add_body("∂L/∂w = (2 / 3) * ∑ (ei * xi)")
    add_body("∂L/∂b = (2 / 3) * ∑ (ei)")
    add_body("2. Biểu thức gradient trường hợp neuron sử dụng hàm kích hoạt Sigmoid:")
    add_body("∂L/∂w = (2 / 3) * ∑ [ei * σ'(zi) * xi] = (2 / 3) * ∑ [ei * ŷi * (1 - ŷi) * xi]")
    add_body("∂L/∂b = (2 / 3) * ∑ [ei * σ'(zi)] = (2 / 3) * ∑ [ei * ŷi * (1 - ŷi)]")
    add_body("So sánh:")
    add_body("- Điểm tương đồng: Cả hai biểu thức đều tỷ lệ thuận với sai số ei = ŷi - yi và đầu vào xi.")
    add_body("- Điểm khác biệt cốt lõi: Ở trường hợp Sigmoid, trong biểu thức gradient xuất hiện thêm thừa số đạo hàm của hàm kích hoạt σ'(zi) = ŷi * (1 - ŷi) được nhân trực tiếp với sai số ei.")

    add_question_heading("Câu C2. Vì sao gradient trong trường hợp sigmoid nhỏ hơn?")
    add_body("Lưu ý về mặt khái niệm trong Học sâu: Khi nói gradient 'lớn hơn' hay 'nhỏ hơn', thuật ngữ này luôn đề cập đến ĐỘ LỚN (độ dài vector / giá trị tuyệt đối |∂L/∂w|), đại diện cho cường độ dốc và biên độ bước nhảy cập nhật tham số (dấu âm chỉ thể hiện hướng dốc).")
    add_body("Về giá trị tuyệt đối:")
    add_body("- Trường hợp tuyến tính: |∂L/∂w| = |-22.666667| = 22.666667; |∂L/∂b| = |-10.0| = 10.0.")
    add_body("- Trường hợp Sigmoid: |∂L/∂w| = |-5.166667| = 5.166667; |∂L/∂b| = |-2.25| = 2.25.")
    add_body("Rõ ràng độ lớn gradient ở trường hợp Sigmoid nhỏ hơn trường hợp tuyến tính đúng 4 lần. Nguyên nhân toán học:")
    add_body("1. Giới hạn giá trị của đạo hàm Sigmoid:")
    add_body("Hàm đạo hàm σ'(z) = σ(z) * (1 - σ(z)) luôn bị chặn trên bởi 0.25 (đạt cực đại tại z = 0 khi σ(0) = 0.5, suy ra 0.5 * 0.5 = 0.25). Với mọi z ≠ 0, giá trị đạo hàm luôn nhỏ hơn 0.25 và nhanh chóng tiệm cận về 0 khi |z| lớn.")
    add_body("2. Tác động làm suy giảm biên độ bước cập nhật (Vanishing Gradient):")
    add_body("Do luôn nhân thêm thừa số σ'(zi) ≤ 0.25 vào sai số, độ lớn gradient bị co hẹp ít nhất 4 lần. Hệ quả là bước nhảy cập nhật tham số Δw = -η * (∂L/∂w) của Sigmoid chỉ đạt +0.051667, nhỏ hơn rất nhiều so với +0.226667 ở mô hình tuyến tính.")

    add_question_heading("Câu C3. Trường hợp nào hội tụ nhanh hơn? Giải thích")
    add_body("1. Kết luận:")
    add_body("Trường hợp neuron không có hàm kích hoạt (tuyến tính) sẽ hội tụ nhanh hơn vượt trội và tìm được nghiệm tối ưu chính xác.")
    add_body("2. Giải thích chi tiết:")
    add_body("- Bản chất quan hệ dữ liệu: Dữ liệu huấn luyện tuân theo quy luật tuyến tính hoàn hảo y = 2 * x + 1 (với x = 1 -> y = 3; x = 2 -> y = 5; x = 3 -> y = 7). Mô hình tuyến tính ŷ = w * x + b hoàn toàn trùng khớp với không gian hàm của bài toán.")
    add_body("- Bề mặt hàm mất mát: Với mô hình tuyến tính kết hợp hàm mất mát MSE, bề mặt mất mát là một paraboloid lồi (convex) duy nhất, đảm bảo gradient luôn dẫn thẳng trực tiếp về điểm cực tiểu toàn cục duy nhất tại w = 2, b = 1 mà không bị mắc kẹt hay suy giảm bước học.")
    add_body("- Trong khi đó, với mô hình Sigmoid, hàm mất mát trở thành phi lồi, gradient bị co hẹp liên tục do hiện tượng bão hòa, khiến tốc độ cập nhật cực kỳ chậm chạp.")

    add_question_heading("Câu C4. Dữ liệu bài toán này có phù hợp với sigmoid không? Vì sao?")
    add_body("1. Kết luận:")
    add_body("Dữ liệu của bài toán này HOÀN TOÀN KHÔNG PHÙ HỢP với hàm kích hoạt Sigmoid.")
    add_body("2. Vì sao:")
    add_body("- Miền giá trị của hàm Sigmoid: Hàm Sigmoid có miền giá trị bị chặn ngặt trong khoảng mở (0, 1), tức là 0 < ŷ < 1 với mọi giá trị đầu vào z.")
    add_body("- Miền giá trị của nhãn dữ liệu thực tế: Tập nhãn y = {3, 5, 7} đều là các số thực dương lớn hơn 1 rất nhiều (y > 1).")
    add_body("- Hậu quả khi huấn luyện:")
    add_body("Mô hình sử dụng Sigmoid không bao giờ có thể tạo ra đầu ra đạt đến 3, 5 hoặc 7. Trong quá trình tối ưu để cố gắng đạt tới giá trị lớn, thuật toán sẽ đẩy trọng số w và bias b lên giá trị dương rất lớn để z -> +∞ nhằm đạt ŷ -> 1. Khi z rất lớn, đạo hàm σ'(z) -> 0, gradient bị triệt tiêu hoàn toàn (bão hòa nơ-ron). Mạng bị tê liệt không thể tiếp tục học và luôn tồn tại sai số mất mát không thể khử bỏ.")
    add_body("- Khuyến nghị: Hàm Sigmoid chỉ phù hợp làm tầng đầu ra cho bài toán phân loại nhị phân (Binary Classification) có nhãn thuộc {0, 1} hoặc xác suất thuộc [0, 1], hoàn toàn không dùng được cho bài toán hồi quy liên tục có miền giá trị vượt ra ngoài khoảng (0, 1). Với bài toán này, nơ-ron tuyến tính (Identity) là mô hình chuẩn xác.")

    # Save file
    output_dir = r"d:\it_sgu\4\1\DeepLearning\Tuan 8"
    filename1 = "BT08_BatchGD_Regression_NguyenHoangTin_3123411299.docx"
    filename2 = "M01_BatchGD_Regression_NguyenHoangTin_3123411299.docx"
    path1 = os.path.join(output_dir, filename1)
    path2 = os.path.join(output_dir, filename2)
    doc.save(path1)
    try:
        doc.save(path2)
        print(f"File created successfully at:\n  {path1}\n  {path2}")
    except PermissionError:
        print(f"File created successfully at: {path1} (path2 currently open/locked in Word)")

if __name__ == "__main__":
    create_document()
