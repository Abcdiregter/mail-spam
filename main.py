import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    # Tạo đối tượng email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Thêm nội dung email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Thiết lập kết nối với SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() # Sử dụng TLS
        server.login(smtp_user, smtp_password)

        # Gửi email
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)

        # Đóng kết nối
        server.quit()

        print("Email đã được gửi thành công!")
    except Exception as e:
        print(f"Không thể gửi email: {e}")

# Cấu hình
smtp_server = "smtp.example.com"  # Thay đổi thành SMTP server của bạn
smtp_port = 587  # SMTP port (587 cho TLS)
smtp_user = "your_email@example.com"  # Thay đổi thành email của bạn
smtp_password = "your_password"  # Mật khẩu email của bạn

# Thông tin email
subject = "Tiêu đề email"
body = "Nội dung email"
to_email = "receiver@example.com"  # Địa chỉ email người nhận
from_email = smtp_user  # Địa chỉ email người gửi

send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password)
