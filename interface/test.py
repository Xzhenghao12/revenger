import flet as ft
import os
import certifi

# 解决网络请求图标/字体时的 SSL 证书报错
os.environ['SSL_CERT_FILE'] = certifi.where()

class ModernWorkbench:
    def __init__(self, page: ft.Page):
        """
        初始化应用，接收 page 对象作为核心驱动
        """
        self.page = page

        # 1. 执行页面基础配置
        self.setup_page()   

        # 2. 实例化所有 UI 组件
        self.init_components()

        # 3. 将组件拼装并渲染到页面
        self.build()

    def setup_page(self):
        """页面全局属性设置"""
        self.page.title = "Flet 1.0 现代 UI (面向对象版)"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.window_width = 450
        self.page.window_height = 700
        self.page.padding = 30
        self.page.spacing = 20
        self.page.scroll = ft.ScrollMode.ADAPTIVE

    def init_components(self):
        """初始化 UI 控件（将它们作为类的属性保存，方便在其他方法中调用）"""

        # 顶部主题切换按钮
        self.theme_icon = ft.IconButton(
            icon=ft.Icons.DARK_MODE,
            icon_color=ft.Colors.BLUE_GREY_700,
            on_click=self.toggle_theme,
            tooltip="切换主题"
        )

        # 顶部标题栏
        self.header = ft.Row(
            [
                ft.Text("我的工作台", size=32, weight=ft.FontWeight.BOLD),
                self.theme_icon,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        # 输入框
        self.name_input = ft.TextField(
            label="项目名称",
            hint_text="例如：学习 Python GUI",
            border_radius=12,
            prefix_icon=ft.Icons.EDIT_NOTE,
            focused_border_color=ft.Colors.BLUE_400,
        )

        # 提交按钮 (Flet 0.80.0+ 规范：使用 ft.Button 和 content)
        self.submit_btn = ft.Button(
            content="新建任务",
            icon=ft.Icons.ADD,
            on_click=self.add_task,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_600,
            ),
            height=50,
        )

    def create_card(self, title, subtitle, color):
        """生成独立卡片的工厂方法"""
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(subtitle, size=13, color=ft.Colors.WHITE70),
            ], alignment=ft.MainAxisAlignment.CENTER),
            width=190,
            height=130,
            bgcolor=color,
            border_radius=20,
            padding=20,
            animate_scale=300,
            on_hover=lambda e: setattr(e.control, 'scale', 1.05 if e.data == "true" else 1) or e.control.update(),
        )

    # --- 交互事件处理方法 ---

    def toggle_theme(self, e):
        """切换深色/浅色模式的逻辑"""
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.theme_icon.icon = ft.Icons.LIGHT_MODE
            self.theme_icon.icon_color = ft.Colors.AMBER_400
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.theme_icon.icon = ft.Icons.DARK_MODE
            self.theme_icon.icon_color = ft.Colors.BLUE_GREY_700
        self.page.update()

    def add_task(self, e):
        """点击按钮后的逻辑"""
        if not self.name_input.value:
            self.name_input.error_text = "项目名称不能为空"
        else:
            self.name_input.error_text = None
            print(f"终端打印 -> 成功提交项目: {self.name_input.value}")
            self.name_input.value = ""
        self.page.update()

    # --- 渲染方法 ---

    def build(self):
        """将所有实例化好的组件添加到页面"""
        self.page.add(
            self.header,
            ft.Text("你好！准备好开始新的一天了吗？", color=ft.Colors.GREY_600),
            ft.Column([
                self.name_input,
                self.submit_btn,
            ], spacing=15),
            ft.Divider(height=40, thickness=1, color=ft.Colors.GREY_200),
            ft.Text("活跃中的项目", size=20, weight=ft.FontWeight.W_600),
            ft.Row(
                [
                    self.create_card("AI 模型训练", "进行中 75%", ft.Colors.BLUE_ACCENT_700),
                    self.create_card("UI 设计系统", "已完成", ft.Colors.INDIGO_400),
                    self.create_card("后端接口开发", "待处理", ft.Colors.ORANGE_800),
                ],
                scroll=ft.ScrollMode.ALWAYS,
            )
        )


# --- 启动入口 ---
def main(page: ft.Page):
    # 只需要在这里实例化我们的 App 类，将 page 传进去即可
    app = ModernWorkbench(page)


if __name__ == "__main__":
    ft.run(main=main)