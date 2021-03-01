# encoding=utf8
import tkinter as tk

TOTAL_SECONDS = 5


def central_location(tkobject, w, h):
	# 获取屏幕 宽、高
	ws = tkobject.winfo_screenwidth()
	hs = tkobject.winfo_screenheight()
	# 计算 x, y 位置
	x = str(int((ws / 2) - (w / 2)))
	y = str(int((hs / 2) - (h / 2)))
	s_geometry = str(w) + "x" + str(h) + "+" + x + "+" + y
	return s_geometry


class App:

	m_now_time = TOTAL_SECONDS
	m_pause = False
	m_record_list = []

	def __init__(self):
		self.m_root = tk.Tk()
		self.m_root.title("结构化面试计时器")
		# 设置root窗口大小与位置
		new_geometry = central_location(self.m_root, 600, 250)
		# 禁止修改窗口大小
		self.m_root.resizable(0, 0)
		self.m_root.geometry(new_geometry)

		# 初始化所有控件
		self.m_time_label = None
		self.m_dy_time_label = None
		self.m_start_btn = None
		self.m_pause_btn = None
		self.m_record_btn = None
		self.m_stop_btn = None
		self.m_record_entry = None
		self.m_copy_btn = None
		self.m_seconds = tk.StringVar(value=self.m_now_time)

		# 布局
		self.layout()

		# 启动
		self.start()

	# 这里使用place来布局
	def layout(self):
		self.row1()
		self.row2()
		self.row3()

	def row1(self):
		self.m_time_label = tk.Label(self.m_root, text="倒计时:")
		self.m_time_label.place(x=70, y=50, anchor='nw')
		self.m_dy_time_label = tk.Label(self.m_root, textvariable=self.m_seconds)
		self.m_dy_time_label.place(x=120, y=50, anchor='nw')

	def row2(self):
		self.m_start_btn = tk.Button(self.m_root, text="开始", command=self.start_btn)
		self.m_start_btn.place(x=70, y=100, anchor='nw')
		self.m_record_btn = tk.Button(self.m_root, text="记录", command=self.record_timer)
		self.m_record_btn.place(x=140, y=100, anchor='nw')
		self.m_stop_btn = tk.Button(self.m_root, text="停止", command=self.stop_timer, state="disabled")
		self.m_stop_btn.place(x=210, y=100, anchor='nw')

	def row3(self):
		self.m_record_entry = tk.Entry(self.m_root, width=20)
		self.m_record_entry.place(x=70, y=150, anchor='nw')
		self.m_copy_btn = tk.Button(self.m_root, text="复制", command=self.copy_record)
		self.m_copy_btn.place(x=280, y=150, anchor='nw')

	def start(self):
		self.m_root.mainloop()

	def start_btn(self):
		self.m_stop_btn.config(state="active")
		self.m_start_btn.config(state="disabled")
		self.m_dy_time_label.after(1000, self.start_timer)

	def pause_timer(self):
		if not self.m_pause:
			self.m_pause = True
			self.m_pause_btn.config(text="继续")
		else:
			self.m_pause = False
			self.m_pause_btn.config(text="暂停")
			self.start_timer()

	def record_timer(self):
		if self.m_now_time > 0:
			self.m_record_list.append(self.m_now_time)
		record_list = list(map(str, self.m_record_list))		# 把列表中的元素转为字符串
		self.m_record_entry.delete(0, "end")
		self.m_record_entry.insert(0, "  ".join(record_list))

	def stop_timer(self):
		self.m_pause = True
		self.m_seconds.set(TOTAL_SECONDS)
		self.m_start_btn.config(state="active")
		self.m_stop_btn.config(state="disabled")

	def start_timer(self):
		if not self.m_pause:
			self.m_now_time -= 1
			if self.m_now_time < 0:
				self.m_record_list.append(0)
				self.record_timer()
				return
			self.m_seconds.set(self.m_now_time)
			self.m_dy_time_label.after(1000, self.start_timer)

	def copy_record(self):
		records = "第一题开始秒数：" + str(self.m_record_list[0]) + "    第一题思考秒数:" + str(TOTAL_SECONDS - self.m_record_list[0])
		records += "\n第一题结束秒数：" + str(self.m_record_list[1]) + "    第一题花费秒数:" + str(self.m_record_list[0] - self.m_record_list[1])
		records += "\n第二题开始秒数：" + str(self.m_record_list[2]) + "    第二题思考秒数:" + str(self.m_record_list[1] - self.m_record_list[2])
		records += "\n第二题结束秒数：" + str(self.m_record_list[3]) + "    第二题花费秒数:" + str(self.m_record_list[2] - self.m_record_list[3])

		self.m_root.clipboard_clear()
		self.m_root.clipboard_append(records)


if __name__ == '__main__':
	App()
