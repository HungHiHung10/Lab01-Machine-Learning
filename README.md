# Lab 01 - Machine Learning: Geometric Machine Learning Animations

Repository này chứa mã nguồn (dưới dạng các file Jupyter Notebook) để tạo ra các video hoạt hình minh họa cho bài thuyết trình chủ đề **"Recent developments in geometric machine learning"** (Những phát triển gần đây trong học máy hình học). Dự án sử dụng thư viện **Manim** kết hợp với **Manim Voiceover** để tự động tạo hình ảnh chuyển động và lồng tiếng (Text-to-Speech).

**Xem video hoàn chỉnh trên YouTube:** [tại đây](https://youtu.be/ksszAB2-QRA)

## Cấu trúc Repository

Toàn bộ bài thuyết trình (126 slide) được chia nhỏ thành 3 file Jupyter Notebook chính:

-  **`notebooks/Slide1-30.ipynb`** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tPiaZYiOyjZUOnz_IoYTQwLe0pAy6PcK?usp=sharing)
  - Chứa các bước hướng dẫn chi tiết để thiết lập môi trường (cài đặt Manim, các gói hệ thống, Manim Voiceover).
  - Code render hoạt hình và lồng tiếng cho các Slide từ 1 đến 30.

-  **`notebooks/Slide31-80.ipynb`** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1oYVkuz3NUtoHXBQdslGyfrk1ycVkjUSe?usp=sharing)
  - Tiếp tục tạo hoạt hình cho phần giữa của bài thuyết trình (Slide 31 đến 80).
  - Tập trung giải thích các khái niệm phức tạp hơn như *Representation theory* (Lý thuyết biểu diễn).

-  **`notebooks/Slide81_126.ipynb`** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1v3pUnrULWDSmM1cA0_SoQhmmnIl1KPOl?usp=sharing)
  - Phần cuối của bài thuyết trình (Slide 81 đến 126).
  - Các đoạn code được tổ chức theo quy trình `Generative` (Tạo dữ liệu/hiệu ứng) và `Display` (Hiển thị) trước khi xuất ra video hoàn chỉnh cuối cùng (Final).

## 🛠 Yêu cầu hệ thống và cài đặt

Dự án yêu cầu các công cụ và thư viện sau:
- **Python 3.7+**
- **[Manim Community](https://www.manim.community/)**: Thư viện Python để lập trình video hoạt hình toán học.
- **[Manim Voiceover](https://voiceover.manim.community/)**: Plugin hỗ trợ lồng tiếng tự động vào video Manim.
- Các công cụ hệ thống cần thiết cho Manim như `FFmpeg`, `LaTeX`, v.v.

*(Lưu ý: Môi trường tốt nhất để chạy thử nhanh là Google Colab, hướng dẫn cài đặt cụ thể đã có ở những block code đầu tiên trong file `Slide1-30.ipynb`).*

##  Cách sử dụng

1. Clone repository này về máy hoặc tải trực tiếp lên Google Colab.
2. Mở file `notebooks/Slide1-30.ipynb` và chạy các cell đầu tiên (Bước 1, 2, 3) để cài đặt các package hệ thống và thư viện Python cần thiết.
3. Chạy các cell tiếp theo theo thứ tự để render video cho từng slide. Cú pháp cơ bản của Manim thường được sử dụng dưới dạng `%%manim` magic command.
4. Chuyển sang chạy file `notebooks/Slide31-80.ipynb` và `notebooks/Slide81_126.ipynb` để kết xuất các phần còn lại của video.
