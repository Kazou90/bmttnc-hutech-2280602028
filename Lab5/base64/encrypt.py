import base64

def main():
    # Nhận chuỗi đầu vào từ người dùng
    input_string = input("Nhập thông tin cần mã hóa: ")

    # Mã hóa chuỗi sang bytes UTF-8, sau đó mã hóa Base64
    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
    # Giải mã bytes Base64 thành chuỗi để ghi vào tệp
    encoded_string = encoded_bytes.decode("utf-8")

    # Mở tệp data.txt ở chế độ ghi và ghi chuỗi đã mã hóa
    with open("data.txt", "w") as file:
        file.write(encoded_string)

    # In thông báo xác nhận
    print("Đã mã hóa và ghi vào tệp data.txt")

# Chạy hàm main nếu script được thực thi trực tiếp
if __name__ == "__main__":
    main()