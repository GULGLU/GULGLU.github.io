class PortfolioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("랜덤 포트폴리오 이미지")
        self.root.geometry("800x600")

        # 이미지 폴더 경로
        self.image_folder = "images"
        self.image_list = [f for f in os.listdir(self.image_folder)
                           if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        if not self.image_list:
            raise FileNotFoundError("이미지가 없습니다. 'images/' 폴더에 이미지를 넣어주세요.")

        # 이미지 라벨
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=20)

        # 버튼
        self.button = tk.Button(self.root, text="이미지 변경", command=self.show_random_image,
                                font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5)
        self.button.pack()

        # 첫 이미지 표시
        self.current_image = None
        self.show_random_image()

    def show_random_image(self):
        selected_image = random.choice(self.image_list)
        image_path = os.path.join(self.image_folder, selected_image)

        # PIL로 이미지 열기 및 크기 조정
        img = Image.open(image_path)
        img = img.resize((600, 400), Image.ANTIALIAS)
        self.current_image = ImageTk.PhotoImage(img)

        self.image_label.config(image=self.current_image)