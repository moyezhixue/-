import tkinter as tk
from tkinter import messagebox, filedialog
import csv


def calculate_average():
    # 获取用户输入的数字
    numbers = entry.get().split('.')

    # 将字符串转换为整数列表
    try:
        numbers = [int(num) for num in numbers]
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字")
        return

        # 计算平均值、求和、最大值、最小值
    if len(numbers) > 0:
        average = sum(numbers) / len(numbers)
        max_value = max(numbers)
        min_value = min(numbers)
        sum_result.set(f"总和为：{sum(numbers)}")
        max_result.set(f"最大值为：{max_value}")
        min_result.set(f"最小值为：{min_value}")
        result.set(f"平均分为：{average}")
    else:
        messagebox.showinfo("提示", "请输入至少一个数字")


def export_data():
    # 获取用户输入的数字列表
    user_numbers = entry.get().split(',')
    try:
        user_numbers = [int(num) for num in user_numbers]
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字")
        return

        # 将数字列表写入CSV文件
    filename = filedialog.asksaveasfilename(defaultextension=".csv")
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Number'])
        for number in user_numbers:
            writer.writerow([number])
    messagebox.showinfo("导出成功", "数据已成功导出到" + filename)


# 创建主窗口
root = tk.Tk()
root.title("平均分计算器")

# 创建标签和输入框
label = tk.Label(root, text="请输入数字，用逗号分隔：")
label.pack()
entry = tk.Entry(root)
entry.pack()

# 创建结果显示框和按钮
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()
sum_result = tk.StringVar()
sum_label = tk.Label(root, textvariable=sum_result)
sum_label.pack()
max_result = tk.StringVar()
max_label = tk.Label(root, textvariable=max_result)
max_label.pack()
min_result = tk.StringVar()
min_label = tk.Label(root, textvariable=min_result)
min_label.pack()
button = tk.Button(root, text="计算平均分", command=calculate_average)
button.pack()

# 创建导出按钮和结果显示框
export_button = tk.Button(root, text="导出数据", command=export_data)
export_button.pack()
export_result = tk.StringVar()
export_label = tk.Label(root, textvariable=export_result)
export_label.pack()

# 运行主循环
root.mainloop()