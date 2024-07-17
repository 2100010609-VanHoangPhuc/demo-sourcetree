import tkinter as tk
from tkinter import ttk


# Hàm để thay đổi màu nút khi chuột đưa vào và rời khỏi
def on_enter(e):
    e.widget['background'] = 'yellow'


def on_leave(e):
    e.widget['background'] = 'lime'


# Hàm để tạo cửa sổ chính và các thành phần giao diện
def create_main_window():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("AtarBals Modern Antivirus")
    root.geometry("800x500")
    root.configure(bg="white")

    # Khung thanh bên
    sidebar = tk.Frame(root, width=200, bg="blue")
    sidebar.pack(side="left", fill="y")

    # Các nhãn trong thanh bên
    tk.Label(sidebar, text="AtarBals AntiVirus", bg="blue", fg="white", font=("Helvetica", 16)).pack(pady=10)

    # Nút "Scan Now" với sự kiện đổi màu
    scan_now_btn = tk.Button(sidebar, text="Scan Now", bg="lime", fg="black", font=("Helvetica", 14))
    scan_now_btn.pack(pady=20)
    scan_now_btn.bind("<Enter>", on_enter)
    scan_now_btn.bind("<Leave>", on_leave)

    # Các nhãn khác trong thanh bên
    for item in ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]:
        tk.Label(sidebar, text=item, bg="blue", fg="white", font=("Helvetica", 14)).pack(pady=5)

    # Khu vực nội dung chính
    main_content = tk.Frame(root, bg="white")
    main_content.pack(side="right", expand=True, fill="both")

    # Nhãn tiêu đề và phụ đề
    tk.Label(main_content, text="Scan", bg="white", fg="black", font=("Helvetica", 24)).pack(pady=20)
    tk.Label(main_content, text="Premium will be free forever. You just need to click button.", bg="white", fg="black",
             font=("Helvetica", 12)).pack(pady=10)

    # Các nút chức năng
    btn_texts = ["Quick Scan", "Web Protection", "Quarantine", "Full Scan", "Simple Update"]
    for text in btn_texts:
        tk.Button(main_content, text=text, bg="magenta", fg="black", font=("Helvetica", 14)).pack(pady=10)

    # Nhãn trạng thái
    tk.Label(main_content, text="Get Premium to Enable: {Web Protection}, {Full Scan}, {Simple Update}", bg="white",
             fg="magenta", font=("Helvetica", 12)).pack(pady=20)

    # Khởi động vòng lặp chính của giao diện
    root.mainloop()


# Gọi hàm để tạo cửa sổ
create_main_window()
