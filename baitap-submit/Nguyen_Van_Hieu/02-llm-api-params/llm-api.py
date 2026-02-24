1. Viết một ứng dụng console đơn giản, người dùng gõ câu hỏi vào console, bot trả lời và in ra. Có thể dùng `stream` hoặc `non-stream`.
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.openai.com/v1",
    api_key='sk-learn-open-ai...',  # Thay key thật của bạn vào đây
)

print("--- Chào mừng bạn đến với AI Console Bot ---")
print("(Gõ 'exit' hoặc 'quit' để thoát chương trình)")

while True:
    # 1. Lấy dữ liệu nhập từ bàn phím
    user_input = input("\nBạn: ")

    # Kiểm tra điều kiện thoát
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Tạm biệt bạn nhé!")
        break

    # 2. Gửi yêu cầu đến OpenAI API (Sử dụng Stream)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Hoặc gpt-4o tùy tài khoản của bạn
            messages=[
                {"role": "system", "content": "Bạn là một trợ lý ảo hữu ích và lịch sự."},
                {"role": "user", "content": user_input}
            ],
            stream=True  # Kích hoạt chế độ stream
        )

        print("Bot: ", end="", flush=True)

        # 3. Duyệt qua từng "mảnh" (chunk) dữ liệu trả về
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)

        print()  # Xuống dòng khi kết thúc câu trả lời

    except Exception as e:
        print(f"\nCó lỗi xảy ra: {e}")

2. Cải tiến ứng dụng chat: Sau mỗi câu hỏi và trả lời, ta lưu vào array `messages` và tiếp tục gửi lên API để bot nhớ nội dung trò chuyện.

import os
from openai import OpenAI
from dotenv import load_dotenv

# client = OpenAI(
#     base_url="https://api.openai.com/v1",
#     api_key='sk-learn-open-ai...', # Thay key thật của bạn vào đây
# )

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

print("--- Chào mừng bạn đến với AI Console Bot ---")
print("(Gõ 'exit' hoặc 'quit' để thoát chương trình)")

list_messages = []
while True:
    # 1. Lấy dữ liệu nhập từ bàn phím
    user_input = input("\nBạn: ")

    # Kiểm tra điều kiện thoát
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Tạm biệt bạn nhé!")
        break

    # 2. Gửi yêu cầu đến OpenAI API (Sử dụng Stream)
    try:
        if len(list_messages) == 0:
            list_messages = [
                {"role": "system", "content": "Bạn là một trợ lý ảo hữu ích và lịch sự."},
                {"role": "user", "content": user_input}
            ]
        else:
            list_messages.append({
                "role": "user",
                "content": user_input,
            })
        response = client.chat.completions.create(
            model="gpt-5",  # Hoặc gpt-4o tùy tài khoản của bạn
            messages=list_messages,
            reasoning_effort="low",
            stream=True  # Kích hoạt chế độ stream
        )

        print("Bot: ", end="", flush=True)

        # 3. Duyệt qua từng "mảnh" (chunk) dữ liệu trả về
        full_response = ""
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)
                full_response += content

        print()  # Xuống dòng khi kết thúc câu trả lời

        list_messages.append(
            {"role": "assistant",
             "content": full_response
             })

    except Exception as e:
        print(f"\nCó lỗi xảy ra: {e}")

3. Tóm tắt website. Dán link website vào console, bot sẽ tóm tắt lại nội dung của website đó.

import os
from openai import OpenAI
import requests
from bs4 import BeautifulSoup

client = OpenAI(
    base_url="https://api.openai.com/v1",
    api_key='sk-learn-open-ai...',  # Thay key thật của bạn vào đây
)

user_input = input("\nBạn: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
url = user_input

try:
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        main_detail = soup.find('div', id='main-detail')

        if main_detail:

            content = main_detail.get_text(separator='\n', strip=True)

            prompt = ('Act as an information analyst. '
                      'Your task is to read and summarize the content from a text using the following structure: '
                      'Core Theme: One sentence summarizing the main purpose of the content. '
                      'Significant Details: Mention any key data, names, or notable events (if applicable). '
                      'Conclusion/Call to Action: What is the author’s final message or recommended next step? '
                      'Requirements: Use concise, objective language and translate and provide all the structures and your responses in Vietnamese only. '
                      'Ensure the summary is easy to read and well-organized. here is the text : ' + '""" ' + content + ' """')

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                # sử dụng model 4o-mini cho rẻ và nhanh nhé
                model="gpt-4o-mini"
            )
            print("--- NỘI DUNG CHÍNH TRONG BÀI VIẾT ---")
            print(chat_completion.choices[0].message.content)

        else:
            print("Không tìm thấy thẻ div có id='main-detail'.")
    else:
        print(f"Lỗi khi truy cập website. Mã lỗi: {response.status_code}")

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

5. Dùng bot để... giải bài tập lập trình. Viết ứng dụng console cho phép bạn đưa câu hỏi vào, bot sẽ viết code Python/JavaScript. Sau đó, viết code lưu đáp án vào file `final.py` và chạy thử. (Dùng Python sẽ dễ hơn JavaScript nhé!)

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.openai.com/v1",
    api_key='sk-learn-open-ai...',  # Thay key thật của bạn vào đây
)

print("--- Chào mừng bạn đến với AI Console Bot ---")
print("(Gõ 'exit' hoặc 'quit' để thoát chương trình)")

while True:
    # 1. Lấy dữ liệu nhập từ bàn phím
    user_input = input("\nBạn: ")

    # Kiểm tra điều kiện thoát
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Tạm biệt bạn nhé!")
        break

    # 2. Gửi yêu cầu đến OpenAI API (Sử dụng Stream)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Hoặc gpt-4o tùy tài khoản của bạn
            messages=[
                {"role": "system",
                 "content": "Act as a programming instructor. Write a program for the following request. Return only the python code"},
                {"role": "user", "content": user_input}
            ],
            stream=True  # Kích hoạt chế độ stream
        )

        print("Bot: ", end="", flush=True)

        # 3. Duyệt qua từng "mảnh" (chunk) dữ liệu trả về
        full_response = ""
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)
                full_response += content

        print()  # Xuống dòng khi kết thúc câu trả lời

        # 4. lưu cách giải vào file final.py
        full_response = full_response.replace('```python', '')
        full_response = full_response.replace('```', '')
        with open("final.py", "w", encoding="utf-8") as file:
            file.write(full_response)


    except Exception as e:
        print(f"\nCó lỗi xảy ra: {e}")