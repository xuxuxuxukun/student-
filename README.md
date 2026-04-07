# 📊 在线学生练习数据查询系统

一个基于 Streamlit 的学生数据查询网站，支持学生通过手机号或学号查询自己的练习数据。

## ✨ 功能特点

- 🔍 **简单查询**：输入手机号或学号即可查询
- 📈 **数据展示**：美观的分数展示、进度条、成绩评价
- 🔒 **数据安全**：学生只能查看自己的数据
- 📱 **响应式设计**：支持手机、平板、电脑访问
- 🚀 **免费部署**：可部署到 Streamlit Cloud，获得在线网址

## 📦 项目文件

```
在线学生查询/
├── app.py              # Streamlit 应用主文件
├── requirements.txt    # Python 依赖列表
├── data.xlsx          # 学生数据文件
└── README.md          # 本说明文档
```

## 🚀 部署到 Streamlit Cloud

### 步骤一：注册 GitHub 账号

1. 访问 [GitHub 官网](https://github.com/)
2. 点击右上角 "Sign up" 注册账号
3. 完成邮箱验证

### 步骤二：创建 GitHub 仓库

1. 登录 GitHub，点击右上角 "+" → "New repository"
2. 填写仓库信息：
   - Repository name: `student-query-app` (或其他名称)
   - 选择 "Public" (公开仓库)
   - ✅ 勾选 "Add a README file"
3. 点击 "Create repository" 创建仓库

### 步骤三：上传项目文件到 GitHub

**方法一：使用 GitHub 网页上传（推荐新手）**

1. 进入刚创建的仓库页面
2. 点击 "Add file" → "Upload files"
3. 拖拽以下文件到上传区域：
   - `app.py`
   - `requirements.txt`
   - `data.xlsx`
4. 在底部填写 Commit 信息，点击 "Commit changes"

**方法二：使用 Git 命令行**

```bash
# 克隆仓库
git clone https://github.com/你的用户名/student-query-app.git
cd student-query-app

# 复制项目文件到此目录
# 然后执行以下命令
git add .
git commit -m "添加学生查询系统"
git push origin main
```

### 步骤四：注册 Streamlit Cloud

1. 访问 [Streamlit Cloud](https://streamlit.io/cloud)
2. 点击 "Sign up" 或 "Start for free"
3. 选择 "Continue with GitHub" 使用 GitHub 账号登录
4. 授权 Streamlit 访问你的 GitHub

### 步骤五：部署应用

1. 登录 Streamlit Cloud 后，点击右上角 "New app"
2. 填写部署信息：
   - **Repository**: 选择你刚才创建的 `student-query-app` 仓库
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL** (可选): 自定义应用名称，如 `student-query-2026`
3. 点击 "Deploy!" 开始部署
4. 等待 1-3 分钟，部署完成后会自动跳转到应用页面

### 步骤六：获取在线网址

部署成功后，你会获得一个在线网址，格式如：

```
https://student-query-2026.streamlit.app
```

或者：

```
https://你的用户名-student-query-app-app-xxx.streamlit.app
```

这个网址可以直接分享给学生使用！

## 🎯 使用方法

### 学生端使用

1. 访问部署后的在线网址
2. 在输入框中输入自己的手机号（11位数字）或学号
3. 点击"查询"按钮
4. 查看个人练习数据和成绩评价

### 管理员更新数据

1. 准备新的数据文件（Excel格式），确保包含以下列：
   - 用户ID
   - 手机号
   - 用户昵称
   - 用户标签
   - 练习时长
   - 练习次数
   - 最高分数
   - 最低分数
   - 平均分数

2. 替换 `data.xlsx` 文件
3. 上传到 GitHub 仓库
4. Streamlit Cloud 会自动重新部署（或手动刷新）

## ⚙️ 本地运行

如果你想先在本地测试：

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行应用
streamlit run app.py

# 3. 浏览器会自动打开 http://localhost:8501
```

## 📊 数据格式要求

Excel 文件必须包含以下列名（首行为列名）：

| 列名 | 数据类型 | 说明 |
|------|---------|------|
| 用户ID | 文本 | 学生的唯一标识 |
| 手机号 | 数字 | 11位手机号 |
| 用户昵称 | 文本 | 学生姓名 |
| 用户标签 | 文本 | 班级、年级等信息 |
| 练习时长 | 文本 | 格式如"57时38分19秒" |
| 练习次数 | 数字 | 练习总次数 |
| 最高分数 | 数字 | 0-100 |
| 最低分数 | 数字 | 0-100 |
| 平均分数 | 数字 | 0-100 |

## 💡 常见问题

### Q1: 部署后显示 "FileNotFoundError: data.xlsx"

**解决方案**：确保 `data.xlsx` 文件已上传到 GitHub 仓库，并且文件名完全一致。

### Q2: 查询时显示"未找到相关记录"

**可能原因**：
- 手机号输入错误
- 数据文件中没有该学生的记录

**解决方案**：检查输入是否正确，或联系老师确认数据是否已录入。

### Q3: 如何修改应用名称和图标？

编辑 `app.py` 中的 `st.set_page_config` 部分：

```python
st.set_page_config(
    page_title="你的应用名称",
    page_icon="🎯",  # 可以用 emoji 或图片 URL
    layout="centered"
)
```

### Q4: 如何隐藏 Streamlit 的默认菜单和页脚？

在 `app.py` 顶部添加：

```python
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
```

### Q5: 部署后更新代码，如何刷新？

Streamlit Cloud 会自动检测 GitHub 仓库的更新并自动重新部署。如果没有自动更新：
1. 进入 Streamlit Cloud 控制台
2. 找到你的应用
3. 点击右上角 "Reboot" 重启应用

## 🔧 高级设置

### 自定义域名

Streamlit Cloud 支持自定义域名（需付费套餐）。免费版使用 `xxx.streamlit.app` 域名即可。

### 设置访问密码

如果需要密码保护，可以在 `app.py` 中添加密码验证：

```python
import streamlit as st

def check_password():
    def password_entered():
        if st.session_state["password"] == "你的密码":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("密码", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("密码", type="password", on_change=password_entered, key="password")
        st.error("😕 密码错误")
        return False
    else:
        return True

if check_password():
    # 主应用代码
    main()
```

## 📞 技术支持

如有问题，请联系老师或管理员。

---

**祝学习进步！📚✨**
