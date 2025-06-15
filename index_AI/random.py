import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random

def show(image):
    image_folder = 'images'

    # 이미지 파일 목록 가져오기
    image_list = [f for f in os.listdir(image_folder)
                  if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    if not image_list:
        messagebox.showerror("오류", "이미지가 없습니다.")
        return

    # 랜덤 이미지 선택
    selected_image = random.choice(image_list)
    image_path = os.path.join(image_folder, selected_image)

    # 이미지 열기 및 크기 조정
    img = Image.open(image_path)
    img = img.resize((600, 400), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)

    # 이미지 업데이트
    image_label.config(image=photo)
    image_label.image = photo  # 참조 저장 (가비지 컬렉션 방지)

# 메인 윈도우 설정
root = tk.Tk()
root.title("랜덤 포트폴리오 이미지")
root.geometry("800x600")

# 이미지 라벨
image_label = tk.Label(root)
image_label.pack(pady=20)

# 버튼
change_button = tk.Button(root, text="이미지 변경", font=("Arial", 14),
                          bg="#4CAF50", fg="white", padx=10, pady=5, command=show)
change_button.pack()

# 처음에 이미지 한 장 표시
show()

# GUI 루프 실행
root.mainloop()