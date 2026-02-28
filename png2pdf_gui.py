import tkinter as tk
from tkinter import filedialog, messagebox
import img2pdf
import os

class PngToPdfApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PNG to PDF Converter")
        self.root.geometry("400x200")

        self.file_paths = []

        # UI要素
        self.label = tk.Label(root, text="PNGファイルを選択してください", pady=20)
        self.label.pack()

        self.select_btn = tk.Button(root, text="ファイルを選択", command=self.select_files)
        self.select_btn.pack(pady=5)

        self.convert_btn = tk.Button(root, text="PDFに変換して保存", command=self.convert_to_pdf, state=tk.DISABLED)
        self.convert_btn.pack(pady=5)

    def select_files(self):
        # 複数ファイル選択
        files = filedialog.askopenfilenames(
            title="PNGファイルを選択",
            filetypes=[("PNG files", "*.png")]
        )
        if files:
            self.file_paths = list(files)
            # ファイル名順にソート（結合順序のため）
            self.file_paths.sort()
            self.label.config(text=f"{len(self.file_paths)} 個のファイルが選択されました")
            self.convert_btn.config(state=tk.NORMAL)

    def convert_to_pdf(self):
        if not self.file_paths:
            return

        # 保存先を指定
        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="保存先を選択"
        )

        if save_path:
            try:
                with open(save_path, "wb") as f:
                    f.write(img2pdf.convert(self.file_paths))
                messagebox.showinfo("完了", "PDFの作成に成功しました！")
            except Exception as e:
                messagebox.showerror("エラー", f"変換に失敗しました:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PngToPdfApp(root)
    root.mainloop()