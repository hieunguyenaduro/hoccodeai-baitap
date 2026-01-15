- Prompt 1

I am providing a document containing lesson material on a prompt engineering. Please act as an educational consultant and generate a review worksheet for many level students.

Please include the following:

5 Multiple Choice Questions focusing on key definitions and facts. 

3 Short Answer Questions that require students to explain a concept in their own words.

2 Critical Thinking Questions that ask students to apply the knowledge to a real-world scenario or 'what if' situation.

An Answer Key at the very bottom for my reference. 
Generate multiple-choice questions on this topic with Format: Question on its own line. Each option (A, B, C, D) on a new line.

Ensure the language is appropriate for their age and that all answers can be found or inferred from the text provided. Here is the document in double qoute """Prompt Engineering nâng cao
Ở bài trước, chúng ta đã học cách viết prompt cơ bản. Trong bài này, mình sẽ hướng dẫn một số kĩ thuật nâng cao khác nha!

Chain of Thought - Hướng dẫn từng bước
Sau khi sử dụng LLM một thời gian, các bạn sẽ thấy mặc dù nó khá thông minh, nhưng với những vấn đề phức tạp, đôi khi nó sẽ khá là... chuối.

Điểm này cũng khá giống con người, nếu bắt các bạn đọc đề bài và đưa ra đáp án, đa phân chúng ta sẽ không làm ngay được, mà cần phải suy nghĩ, phân tích từng bước.

Sau khi tính toán từng bước giải, chúng ta mới tính ra kết quả. LLM cũng như vậy.

Thay vì đòi kết quả ngay, các bạn có thể hướng dẫn nó suy nghĩ từng bước, từng khâu để giải quyết vấn đề, rồi mới tính ra kết quả.

Kĩ thuật này gọi là CoT (Chain of Thought).

Ví dụ như bạn code một AI chấm bài thi. Đây là đề bài và đáp án của thí sinh.

Problem Statement: I'm building a solar power installation and I need help working out the financials.
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost me a flat $100k per year, and an additional $10 / square foot
What is the total cost for the first year of operations as a function of the number of square feet.

Student's Solution: Let x be the size of the installation in square feet.
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
Nếu bạn chỉ dùng prompt đơn giản, đôi khi chat GPT sẽ kêu kết quả là đúng (mặc dù kết quả sai bét).

❌ Determine if the student's solution is correct or not.
4-ex

Nhưng nếu bạn hướng dẫn nó từng bước, nó sẽ giúp bạn kiểm tra kết quả của học sinh có đúng hay không.

✅ First work out your own solution to the problem. Then compare your solution to the student's solution and evaluate if the student's solution is correct or not. Don't decide if the student's solution is correct until you have done the problem yourself.
4-ex

Các bạn thấy đấy, với các tác vụ phức tạp, việc hướng dẫn từng bước sẽ giúp LLM cho kết quả tốt hơn.

Bạn có thể áp dụng cách này cho các bài toán phức tạp khác như viết code, giải toán, phân tích dữ liệu...v.v.

Nếu bạn lười suy nghĩ các bước giải quyết vấn đề, bạn cũng có thể dùng thần chú Take a deep breath and think step by step để LLM tự suy nghĩ các bước giải quyết nhé.

❌ How to add 2 big big big numbers in C??

✅ How to add 2 big big big numbers in C?? Take a deep breath and think step by step.
(Cách này cũng sẽ khiến bạn kiểm lỗi dễ hơn, biết model sai ở đâu!)
4-ex4-ex

Sử dụng khẳng định thay vì phủ định
Do LLM hoạt động theo cơ chế... dự đoán từ xuất hiện kế tiếp, LLM khá ngu và nhiều khi không hiểu khái niệm KHÔNG.

Do vậy, để tránh nhầm lẫn, bạn nên sử dụng khẳng định thay vì phủ định.

Ví dụ thay vì prompt bảo model ĐỪNG LÀM, KHÔNG LÀM GÌ ĐÓ... bạn nên hướng dẫn nó làm gì. (Ví dụ này chỉ là tương đối, vì các LLM đời mới đã được train dựa trên lệnh có phủ định nhiều nên có khôn ra chút!)

Ví dụ
Thay vì nói AI đừng hỏi password, hay bảo model chỉ tới những trang khác.

❌ The following is a conversation between an Agent and a Customer. DO NOT ASK USERNAME OR PASSWORD. DO NOT REPEAT.

✅ The following is a conversation between an Agent and a Customer. The agent will attempt to diagnose the problem and suggest a solution, whilst refraining from asking any questions related to PII. Instead of asking for PII, such as username or password, refer the user to the help article www.samplewebsite.com/help/faq
Thay vì bảo AI đừng viết comment, hay nói nó đưa code không cho bạn.

❌ Write a program to add two numbers without using the '+' operator. DO NOT WRITE ANY COMMENT.

✅ Ưrite a program to add two numbers without using the '+' operator. GIVE ME ONLY THE CODE.
Zero-shot, One-shot, Few-shot - đưa ví dụ
Hướng dẫn cho AI cũng giống như hướng dẫn cho học sinh hoặc trẻ nhỏ vậy, bạn cần phải đưa ví dụ để nó hiểu rõ hơn.

Do đặc tính của LLM là dự đoán những từ tiếp theo, bạn đưa càng nhiều ví dụ thì nó sẽ càng hiểu rõ và cho kết quả chính xác hơn.

Với một số task, ta chỉ cần yêu cầu AI làm, không cần đưa ví dụ, kĩ thuật này gọi là Zero-shot.

Zero-shot Prompt
Đoạn văn: "Bộ phim này thật tuyệt vời! Tôi rất thích cốt truyện và diễn xuất của các diễn viên."
Hãy phân loại sắc thái của đoạn văn trên thành tích cực, tiêu cực hoặc trung tính.

Kết quả: Tích cực
Nếu bạn cần AI làm một số task cụ thể, bạn cần đưa ví dụ, kĩ thuật này gọi là One-shot hoặc Few-shot. One-shot tức là đưa một ví dụ, còn few-shot là nhiều ví dụ.

One-shot
- Đoạn văn 1: "Bộ phim này thật tuyệt vời! Tôi rất thích cốt truyện và diễn xuất của các diễn viên." - Tích cực
- Đoạn văn 2: "Món ăn này có vị khá tẻ nhạt. Tôi đã kỳ vọng nhiều hơn từ nhà hàng này."
Hãy phân loại sắc thái của đoạn văn 2 thành tích cực, tiêu cực hoặc trung tính.

Few-shots
- Đoạn văn 1: "Bộ phim này thật tuyệt vời! Tôi rất thích cốt truyện và diễn xuất của các diễn viên." - Tích cực
- Đoạn văn 2: "Món ăn này có vị khá tẻ nhạt. Tôi đã kỳ vọng nhiều hơn từ nhà hàng này." - Tiêu cực
- Đoạn văn 3: "Cuốn sách này không xuất sắc, nhưng cũng không tệ. Nó có vài điểm thú vị." - Trung tính
- Đoạn văn 4: "Dịch vụ khách hàng của công ty này thật tồi tệ. Tôi sẽ không bao giờ mua hàng từ họ nữa."
Hãy phân loại sắc thái của đoạn văn 4 thành tích cực, tiêu cực hoặc trung tính.
Cá nhân mình thấy, với những model yếu, chưa thông minh như GPT-4o-mini, Claude Haiku, Mistral 7B... việc đưa nhiều ví dụ với few-shot sẽ giúp các model trả lời chuẩn và chính xác ngang với các model thông minh hơn như GPT-4, với giá cả và tốc độ nhanh hơn nhiều!

Yêu cầu model xuất kết quả đầu ra theo một format cụ thể
Bạn có thể yêu cầu model đưa kết quả dưới các format sau, để bạn có thể đọc và xử lý bằng code.

JSON
XML
HTML
Markdown
CSV
Tất nhiên, bạn vẫn phải ghi rõ JSON hoặc XML bạn muốn có những field nào, giá trị các field đó là gì v...v.

Ví dụ như ở bài trước, chúng ta có prompt này để phân tích CV.

Extract the information about this CV. I need the name, years of experience, and the list of skills and certifications.

Format:
Name: [Candidate's name]
Years of experience: [Number of years]
Skills: [List of skills]
Certifications: [List of certifications]

"""CV: [CV cần extract]"""
(Có kết quả và format, format cụ thể.)
Nếu muốn tích hợp vào hệ thống đọc CV, ta có thể yêu cầu nó trả kết quả về dưới dạng JSON.

Extract the information about this CV. I need the name, years of experience, and the list of skills and certifications.

Return the JSON ONLY.
JSON Format
{
  "name": "Candidate's name",
  "year_of_exprience": "Number of years",
  "skill": "[List of skills]",
  "certifications": "[List of certifications]"
}
Các bạn thấy đó, LLM đã đọc CV của mình và tự parse thành 1 chuối JSON, dễ tích hợp vào hệ thống code hơn.4-json

Nếu muốn tích hợp LLM vào hệ thống, đôi khi chỉ dùng prompt và đọc kết quả dạng text là không đủ. (Như chỗ số 3 ở trên mình muốn nó là 1 số thay vì 3 years).

Để làm được điều này, bọn mình sẽ chia sẻ thêm ở bài function calling trong phần nâng cao nha!"""

- Prompt 2

Act as a professional content editor and literary analyst. I will provide a text below. Your mission is to perform the following two steps:

Step 1: Text Analysis

Theme & Message: Identify the main idea and the core message.

Tone: Analyze the nuance (e.g., formal, intimate, humorous, melancholic, etc.).

Linguistic Style: Comment on word choice, sentence structure, and rhetorical devices (if any).

Step 2: Creative Continuation

Based on the analysis in Step 1, write an additional [Number of sentences/words] to complete or expand the ideas in the text.

Requirements: Ensure seamless coherence, maintaining the original author's tone and style so that the transition is indistinguishable.

Constraint: The total response must be under 500 words and transate the output into vietnamese

Text to process """ Con sông Thái Bình là một con sông lớn và chảy dài qua nhiều tỉnh thành. Em chỉ nghe bà kể chứ chưa được tường tận quan sát hết cả con sông đó. Em chỉ được biết về một khúc sông đi qua sau nhà bà em mà thôi. Khúc sông ấy rộng bằng bề ngang của đường mòn Hồ Chí Minh, không quá sâu. Điểm sâu nhất là lòng sông, thì cũng phải hơn 2m. Còn hai bên bờ thì khi lội cũng chỉ qua đầu gối mà thôi. Nước sông không trong mà hơi đục, bởi nước sông chứa nhiều phù sa. Nhờ có sông, mà cây cối sau vườn của các gia đình ở đây đều vô cùng tươi tốt. Vạt rau nào cũng tươi xanh vô cùng. Lòng sông có cua, trai và ốc khá nhiều. Thỉnh thoảng, bà con lại kéo nhau ra sông mò, ấy thế mà cũng có một bữa no. Cá dưới sông cũng nhiều lắm, từ to đến nhỏ. Cứ cách vài ngày ra giăng lưới, thì sẽ được cả một cái thuyền con đầy ăm ắp. Chiều chiều, nước sông sẽ dâng cao lên, cao hơn ban ngày chừng một gang tay. Nước sông về đêm lạnh hơn và tối sẫm, chảy nhanh hơn hẳn. Bởi vậy, cứ chiều tà, thì đám bèo trên mặt sông lại nô nức trôi theo dòng nước, đi khám phá những vùng đất khác."""

- Prompt 3

Role: You are an expert in Customer Experience and Data Analysis.

Task: I will provide you with a list of customer reviews. Please perform the following tasks:

Classification: Categorize each review as "Good" (Positive/Satisfied) or "Bad" (Negative/Dissatisfied).

Summarization: Summarize the key points mentioned by customers in both categories (e.g., common praises or recurring complaints).

Statistics: Count the total number of reviews, the number of "Good" reviews, and the number of "Bad" reviews.

Output Format:
1. Detailed Classification Table
2. Key Insights Summary
Pros (Good): [Key strengths mentioned]
Cons (Bad): [Issues that need improvement]
3. Statistical Report
Total Reviews: [Count]
Good Reviews: [Count] ([%])
Bad Reviews: [Count] ([%])

Constraint:  transate the output into vietnamese

Input Data (Reviews) 
""" 
sau đây là những bình luận về iphone 17 prod max.
Màn hình siêu bền: "Màn hình Ceramic Shield 2 thực sự là một bước tiến. Sau vài tháng dùng trần không dán cường lực, máy vẫn không có vết xước dăm nào, tốt hơn hẳn đời 16."

Hệ thống tản nhiệt hiệu quả: "Apple cuối cùng đã trang bị tản nhiệt buồng hơi (Vapor Chamber). Chơi game nặng hay quay video 4K lâu máy chỉ ấm nhẹ, không còn tình trạng bị hạ độ sáng hay giật lag như trước."


Tốc độ sạc cải tiến: "Dù không nhanh như các hãng Trung Quốc, nhưng việc sạc đầy 100% trong khoảng 80 phút (nhanh hơn đời trước 30 phút) là một sự thay đổi rất thực tế và đáng giá."

RAM 12GB mượt mà: "Khả năng đa nhiệm quá đỉnh, mở hàng chục ứng dụng hay dùng các tính năng Apple Intelligence (AI) đều phản hồi tức thì, không bị tải lại app."

Chất liệu khung nhôm bị coi là "cải lùi": "Bỏ khung Titan để quay lại dùng nhôm là một bước lùi. Cảm giác cầm không sang trọng bằng và rất dễ bị trầy xước nếu không dùng ốp."

Cụm camera quá thô: "Thiết kế camera nằm ngang (hoặc dạng plateau mới) nhìn rất lạ lẫm và thô. Máy để trên bàn bị bập bênh cực kỳ khó chịu."

Trọng lượng và kích thước: "Máy vẫn rất nặng (khoảng 233g). Cầm một tay lâu rất mỏi, đặc biệt là với khung viền nhôm có vẻ không 'đầm' bằng Titan nhưng lại vẫn nặng tương đương."

Lỗi phần mềm (iOS 26): "Hệ điều hành mới vẫn còn lỗi, đôi khi xem video trên Netflix bị mờ hoặc kết nối Hotspot chập chờn, cần chờ các bản cập nhật vá lỗi."

Giá thành quá cao: "Mức giá cho bản 1TB hay 2TB thực sự quá xa xỉ, không phù hợp với đại đa số người dùng phổ thông."
"""

- Prompt 4

SYSTEM You will be provided with a piece of Python code, and your task is to find bugs, explain the code and comment in it
USER
import Random
    a = random.randint(1,12)
    b = random.randint(1,12)
    for i in range(10):
        question = "What is "+a+" x "+b+"? "
        answer = input(question)
        if answer = a*b
            print (Well done!)
        else:
            print("No.")

- Prompt 5

Role: Act as a professional travel consultant and local guide with deep knowledge of global tourism.

Task: I will provide a [Destination]. Please create a comprehensive travel guide including:

Top Attractions: List must-visit landmarks, historical sites, or scenic spots (include a brief description of why they are special).

Must-do Activities: Suggest unique experiences, local tours, or outdoor activities (e.g., trekking, night markets, cultural workshops).

Local Cuisine: Recommend signature dishes, famous street foods, and highly-rated places to eat.

Best Time to Visit: Advise on the ideal season/months to visit and the recommended duration for the trip (how many days).

Formatting: Please use clear headings, bullet points, and bold text for key terms to make it easy to read and then transalte the output into vietnamese

Destination: núi bà đen

- Prompt 6

I am going to provide you with the text of a chapter of Trạng Quỳnh below. Please perform the following tasks:

1. Summary: Provide a concise summary (about 200 words) that captures the key events, main conflicts, and the core message of the text. 
2. Character List: Identify and list all the characters mentioned. For each character, provide a brief description of their personality, traits, or their role in this specific section.

Formatting Requirements: Please use clear headings and bullet points for readability.

Text Content: """Chuyện kể rằng lúc Quỳnh còn nhỏ, mới bảy tám tuổi, Quỳnh đã tỏ ra thông minh đỉnh ngộ nhưng cũng là một đứa trẻ chúa nghịch. Hồi ấy bọn trẻ thường chơi trò xước xách, lấy tàu chuối làm cờ, lá sen làm lọng. Trong trò chơi, Quỳnh bao giờ cũng lấn lướt.

Một đêm mùa thu, trăng tháng tám sáng vằng vặc, đang chơi với đám trẻ ở sân nhà, Quỳnh bảo:

– Chúng bay làm kiệu cho tao ngồi, rồi tao đưa đi xem một người mà cái đầu to bằng cái bồ!

Lũ trẻ tưởng thật, liền tranh nhau làm kiệu rước Quỳnh đi vòng vòng quanh sân, mệt thở muốn đứt hơi. Xong, chúng nhất định bắt Quỳnh phải giữ lời hứa. Lúc ấy trăng đã mờ, Quỳnh bảo:

– Tụi bây đứng đợi cả ở đây, tôi đi đốt lửa soi cho mà xem!

Bọn trẻ nhỏ hơi sợ, không dám ở lại, chỉ những đứa lớn hơn, bạo dạn đứng chờ. Quỳnh lấy lửa thắp đèn xong đâu đấy, rồi thò đầu che ngọn đèn, bảo:

– Kìa, trông trên vách kìa. Ông to đầu đã ra đấy!"""