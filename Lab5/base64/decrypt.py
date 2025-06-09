import base64

def main():
    try:
        # Mở tệp data.txt ở chế độ đọc
        with open("data.txt", "r") as file:
            # Đọc chuỗi đã mã hóa từ tệp và loại bỏ khoảng trắng thừa
            encoded_string = file.read().strip()

        # Giải mã chuỗi Base64 thành bytes
        decoded_bytes = base64.b64decode(encoded_string)
        # Giải mã bytes UTF-8 thành chuỗi gốc
        decoded_string = decoded_bytes.decode("utf-8")

        # In chuỗi đã được giải mã
        print("Chuỗi sau khi giải mã:", decoded_string)
    
    except Exception as e:
        # Bắt và in bất kỳ lỗi nào xảy ra trong quá trình
        print("Lỗi:", e)

# Chạy hàm main nếu script được thực thi trực tiếp
if __name__ == "__main__":
    main()