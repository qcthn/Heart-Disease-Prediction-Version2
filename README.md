﻿# Heart-Disease-Prediction-Version2
# DecisionSupportSystem-V2

Repository này chứa một Hệ thống Hỗ trợ Quyết định cho dự đoán bệnh tim được phát triển bằng Python. Hệ thống bao gồm tiền xử lý dữ liệu, phân tích dữ liệu khám phá (EDA), xếp hạng đặc trưng, phân tích thành phần chính (PCA), và các mô hình học máy khác nhau cho phân loại.

## Dữ liệu

Bộ dữ liệu được sử dụng trong dự án này có tựa đề "Bệnh tim" và có sẵn dưới định dạng Excel. Nó chứa thông tin về các thuộc tính khác nhau liên quan đến sức khỏe của trái tim, như BMI, thói quen hút thuốc, tiêu thụ rượu bia, tiền sử đột quỵ, tình trạng sức khỏe vật lý và tinh thần, thông tin dân số học, tiền sử y tế (ví dụ: tiểu đường, hen suyễn, bệnh thận, ung thư da), v.v.

## Yêu cầu

- Python 3.x
- Thư viện: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Imbalanced-learn, XGBoost, Plotly, Gradio

## Cài đặt

Để chạy Hệ thống Hỗ trợ Quyết định, làm theo các bước sau:

1. Sao chép kho này vào máy cục bộ của bạn:

```
git clone <repository_url>
```

2. Cài đặt các thư viện cần thiết bằng pip:

```
pip install -r requirements.txt
```

## Sử dụng

1. Chạy tập tin Jupyter Notebook `Chuandoanbenhtim-DataMining.ipynb` để thực thi Hệ thống Hỗ trợ Quyết định.

2. Tuân theo các hướng dẫn được cung cấp trong notebook để thực hiện tiền xử lý dữ liệu, phân tích dữ liệu khám phá, xếp hạng đặc trưng, PCA và huấn luyện mô hình.

3. Sau khi chạy notebook, bạn có thể sử dụng các mô hình đã huấn luyện để dự đoán bệnh tim.

## Đánh giá mô hình

Các mô hình học máy sau được huấn luyện và đánh giá cho việc phân loại bệnh tim:

- Hồi quy Logistic
- Bộ phân loại cây quyết định
- Bộ phân loại XGBoost
- Bộ phân loại AdaBoost
- Bộ phân loại K Nearest Neighbour
- Bộ phân loại Máy vector hỗ trợ
- Bộ phân loại Rừng ngẫu nhiên

Độ chính xác và hiệu suất của mỗi mô hình được đánh giá bằng các chỉ số như điểm chính xác, ma trận nhầm lẫn, độ chính xác, độ nhớ, và F1-score.

## Giao diện người dùng đồ họa (GUI)

Một giao diện người dùng đồ họa (GUI) được cung cấp bằng Gradio, cho phép người dùng nhập các thuộc tính sức khỏe của họ và nhận dự đoán về khả năng mắc bệnh tim.

## Lưu ý

Hệ thống Hỗ trợ Quyết định này chỉ dành cho mục đích giáo dục và thông tin. Không nên sử dụng làm thay thế cho tư vấn y tế chuyên nghiệp, chẩn đoán hoặc điều trị. Luôn tìm kiếm ý kiến ​​tư vấn y tế từ một chuyên gia y tế đủ năng lực cho bất kỳ vấn đề y tế nào.
