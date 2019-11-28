import matplotlib.pyplot as plt

# 图形输入值
input_values = [1, 2, 3, 4, 9]
# 图形输出值
squares = [1, 4, 9, 16, 25]

# plot根据列表绘制出有意义的图形，linewidth是图形线宽，可省略
plt.plot(input_values, squares, linewidth=1)
# 绘制散点图(传如一对x和y坐标，在指定位置绘制一个点)
plt.scatter(2, 4)
# 设置输出样式
plt.scatter(3, 5, s=200)
# 设置图标标题
plt.title("Square Numbers", fontsize=24)
# 设置坐标轴标签
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
# 打开matplotlib查看器，并显示绘制图形
plt.show()
