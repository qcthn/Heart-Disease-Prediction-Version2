# Heart-Disease-Prediction-Version2
# DecisionSupportSystem-V2

Repository này chứa một Hệ thống Hỗ trợ Quyết định cho dự đoán bệnh tim được phát triển bằng Python. Hệ thống bao gồm tiền xử lý dữ liệu, phân tích dữ liệu khám phá (EDA), xếp hạng đặc trưng, phân tích thành phần chính (PCA), và các mô hình học máy khác nhau cho phân loại.
## Người Đóng Góp

- Nguyễn Thị Vân Anh
  - Mã Sinh Viên: 21520578
  - Vai Trò: Lên Ý Tưởng, Viết Báo Cáo, Thuyết Trình

- Lê Quốc Thuận
  - Mã Sinh Viên: 21520473
  - Vai Trò: Triển Khai, Phát Triển Ứng Dụng

## Tập Dữ Liệu

Tập dữ liệu sử dụng trong dự án này có thể tìm thấy tại: https://www.kaggle.com/datasets/abubakarsiddiquemahi/heart-disease-dataset/data

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

# Hệ Thống Dự Đoán Bệnh Tim

Đây là một ứng dụng web để dự đoán nguy cơ mắc bệnh tim dựa trên các chỉ số lâm sàng khác nhau. Ứng dụng sử dụng một mô hình học máy được huấn luyện trên dữ liệu sức khỏe liên quan.

## Cài Đặt

Để chạy ứng dụng này trên máy tính cá nhân, làm theo các bước sau:

1. **Clone Repository**:  
   Sao chép kho lưu trữ này vào máy tính cá nhân của bạn bằng câu lệnh sau:

    ```bash
    git clone https://github.com/qcthn/Heart-Disease-Prediction-Version2.git
    ```

2. **Di Chuyển vào Thư Mục Dự Án**:  
   Di chuyển vào thư mục dự án:

    ```bash
    cd heart-disease-prediction
    ```

3. **Cài Đặt Các Phụ Thuộc**:  
   Sử dụng pip để cài đặt các phụ thuộc Python cần thiết:

    ```bash
    pip install -r requirements.txt
    ```

4. **Chạy Ứng Dụng Flask**:  
   Khởi động ứng dụng Flask:

    ```bash
    python app.py
    ```

5. **Truy Cập Ứng Dụng**:  
   Mở trình duyệt web của bạn và điều hướng đến `http://localhost:5000` để truy cập ứng dụng.

## Sử Dụng

Khi ứng dụng đang chạy, bạn có thể sử dụng như sau:

1. **Nhập Các Chỉ Số Lâm Sàng**:  
   Điền vào biểu mẫu với các chỉ số lâm sàng cần thiết một cách chính xác, sau đó gửi biểu mẫu để nhận kết quả dự đoán.

2. **Xem Kết Quả Dự Đoán**:  
   Ứng dụng sẽ xử lý dữ liệu bằng cách sử dụng mô hình học máy và cung cấp cho bạn kết quả dự đoán về nguy cơ mắc bệnh tim của mình.

## Cấu Trúc Tệp

Các tệp chính trong dự án này được tổ chức như sau:

- `app.py`: Chứa mã ứng dụng Flask bao gồm các tuyến đường để hiển thị trang web và xử lý dự đoán.
- `index.html`: Mẫu HTML cho giao diện người dùng nơi người dùng nhập các chỉ số lâm sàng của mình.
- `result.html`: Mẫu HTML để hiển thị kết quả dự đoán.
- `heart-disease-model.pkl`: Mô hình học máy được huấn luyện để dự đoán nguy cơ mắc bệnh tim.
- `static/PNG/heart-rate_9424143.png`: Hình ảnh được sử dụng trong giao diện ứng dụng.

## Phụ Thuộc

Dự án phụ thuộc vào các phụ thuộc sau:

- Flask: Framework web được sử dụng để phát triển ứng dụng.
- NumPy: Thư viện tính toán số trong Python.
- Pickle: Module để serialize và deserialize các đối tượng Python.
- Bootstrap: Framework front-end để thiết kế trang web đáp ứng.

## Giấy Phép

Dự án này được cấp phép theo Giấy Phép MIT - xem tệp [LICENSE](LICENSE) để biết chi tiết. Hãy thoải mái đóng góp vào dự án hoặc sử dụng nó như một cơ sở cho ứng dụng của riêng bạn!

## Lưu ý

Hệ thống Hỗ trợ Quyết định này chỉ dành cho mục đích giáo dục và thông tin. Không nên sử dụng làm thay thế cho tư vấn y tế chuyên nghiệp, chẩn đoán hoặc điều trị. Luôn tìm kiếm ý kiến ​​tư vấn y tế từ một chuyên gia y tế đủ năng lực cho bất kỳ vấn đề y tế nào.
