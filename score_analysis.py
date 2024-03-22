import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def analyze_and_output_subject(data, subject):
    """
    分析并输出指定科目的统计数据
    :param data:
    :param subject:
    :return:
    """
    df = pd.DataFrame(data)
    subject_stats = df[subject].describe()
    _save_csv(subject_stats, f'{subject}_stats.csv')


def correlation_analysis(data):
    """
    相关性分析
    :param data:
    :return:
    """
    df = pd.DataFrame(data)
    correlation_matrix = df.corr()
    _chinese_font_config()
    # 绘制热力图
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Analysis')
    plt.savefig('correlation_analysis.png')

    _save_csv(correlation_matrix, 'correlation_matrix.csv')


def plot_subject(data, subject):
    """
    绘制指定科目的直方图
    :param data:
    :param subject:
    :return:
    """
    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=subject, kde=True)

    _chinese_font_config()

    plt.title(f'{subject}成绩分布')
    plt.xlabel('成绩')
    plt.ylabel('频数')
    plt.savefig(f'{subject}_histogram.png')


def compare_and_output_groups(data):
    """
    高分组与低分组对比
    :param data:
    :return:
    """
    df = pd.DataFrame(data)
    median_score = df["总分"].median()
    high_group = df[df["总分"] >= median_score]
    low_group = df[df["总分"] < median_score]
    high_group_means = high_group[["政治", "英语", "专业课667", "专业课972"]].mean()
    low_group_means = low_group[["政治", "英语", "专业课667", "专业课972"]].mean()

    _save_csv(high_group_means, 'high_group_means.csv')
    _save_csv(low_group_means, 'low_group_means.csv')
    _chinese_font_config()

    plt.figure(figsize=(10, 6))
    x = np.arange(len(high_group_means))
    width = 0.25
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, high_group_means, width, label='高分组')
    rects2 = ax.bar(x + width/2, low_group_means, width, label='低分组')
    ax.set_ylabel('成绩')
    ax.set_title('高分组与低分组的对比')
    ax.set_xticks(x)
    ax.set_xticklabels(["政治", "英语", "专业课667", "专业课972"])
    ax.legend()
    fig.tight_layout()
    plt.show()


def _chinese_font_config():
    """
    中文显示配置
    :return:
    """
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False


def _save_csv(data, file_name):
    """
    保存数据到csv文件
    :param data:
    :param file_name:
    :return:
    """
    df = pd.DataFrame(data)
    df.to_csv(file_name)


def load_data(file_path):
    """
    从Excel文件加载数据
    :param file_path: Excel文件的路径
    :return: 数据集，pandas DataFrame格式
    """
    return pd.read_excel(file_path)


if __name__ == '__main__':
    """
    主函数
    """
    # 从Excel文件加载数据
    data = load_data('[你的excle文件路径]')

    # 示例数据
    # data = {
    #     "政治": [69, 73, 67, 73, 71, 64, 66, 73, 75, 73, 68, 73, 76, 71, 79, 76, 75, 77, 78, 66, 69, 76, 73, 71],
    #     "英语": [86, 75, 83, 88, 79, 87, 73, 79, 75, 71, 80, 80, 74, 83, 69, 85, 84, 77, 82, 73, 79, 71, 80, 79],
    #     "专业课667": [126, 126, 124, 126, 121, 126, 125, 125, 124, 121, 124, 125, 125, 113, 124, 110, 123, 108, 123,
    #                   128, 128, 112, 125, 124],
    #     "专业课972": [100, 102, 124, 108, 112, 99, 102, 124, 104, 99, 116, 116, 106, 96, 113, 96, 119, 101, 92, 113,
    #                   112, 110, 95, 116],
    #     "总分": [381, 376, 398, 395, 383, 376, 366, 401, 378, 364, 388, 394, 381, 363, 385, 367, 401, 363, 375, 380,
    #              388, 369, 373, 390]
    # }

    # 总分分析
    analyze_and_output_subject(data, "总分")
    plot_subject(data, "总分")

    # 英语成绩分析
    analyze_and_output_subject(data, "英语")
    plot_subject(data, "英语")

    # 政治成绩分析
    analyze_and_output_subject(data, "政治")
    plot_subject(data, "政治")

    # 专业课667成绩分析
    analyze_and_output_subject(data, "专业课667")
    plot_subject(data, "专业课667")

    # 专业课972成绩分析
    analyze_and_output_subject(data, "专业课972")
    plot_subject(data, "专业课972")

    # 高分组与低分组对比
    compare_and_output_groups(data)

    # 相关性分析
    correlation_analysis(data)