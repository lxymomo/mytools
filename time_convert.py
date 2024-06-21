import pandas as pd
import os

# 文件路径列表
file_paths = [
    r'C:\Users\45372\Downloads\SSE_DLY_000300.csv',
    r'C:\Users\45372\Downloads\BATS_QQQ.csv',
]

# 输出目录
output_dir = r'C:\Users\45372\Downloads\converted_files'

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 处理每个文件
for file_path in file_paths:
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 将时间列从时间戳转换为UTC的年月日时格式
    df['time'] = pd.to_datetime(df['time'], unit='s', utc=True)

    # 生成输出文件路径
    base_name = os.path.basename(file_path)
    output_path = os.path.join(output_dir, f'converted_{base_name}')

    # 保存转换后的结果到新的CSV文件
    df.to_csv(output_path, index=False)

    print(f"时间格式转换完成，已保存到 {output_path}")

print("所有文件的时间格式转换完成。")
