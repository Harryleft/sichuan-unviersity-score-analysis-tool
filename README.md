# 脚本说明

这是一个用于成绩分析和可视化的Python脚本。它可以分析指定科目的统计数据，进行相关性分析，绘制成绩分布图，以及比较高分组和低分组的平均成绩。

## 安装

首先，你需要安装以下Python库：
> `pip install -r requirements.txt`

## 运行

你可以通过运行`python score_analysis.py`命令来运行这个脚本。

## 功能和使用方法

这个脚本包含以下函数：

- `analyze_and_output_subject(data, subject)`: 分析并输出指定科目的统计数据，默认支持政治、英语、专业课667、专业课972。
- `correlation_analysis(data)`: 进行相关性分析，显示相关性矩阵的热力图。
- `plot_subject(data, subject)`: 绘制指定科目的成绩分布图。
- `compare_and_output_groups(data)`: 比较高分组和低分组的平均成绩。
