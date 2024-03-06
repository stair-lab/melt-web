---
layout: default
permalink: /prompt/
---

# Prompt Formats
All the prompts we used in our experiments are in Vietnamese. We present details of these prompts in the sections below with their meanings in English (translated by Google Translate). 

**Please note that these prompts are formatted for LLaMa-2, for other models, the prompt format may need to be adjusted.**

## Question-Answering
### Weak prompt

*Vietnamese:* ``[INST] Ngữ cảnh:⏎
{context}⏎⏎
Câu hỏi:⏎
{question}⏎⏎
Trả lời:⏎[/INST]``

*English:* ``[INST] Context:⏎
{context}.⏎⏎
Question: ⏎
{question}.⏎⏎
Answer:⏎[/INST]``

### Medium prompt
*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy trả lời câu hỏi bên dưới bằng tiếng Việt với các thông tin được cung cấp trong phần ngữ cảnh. Nếu trong ngữ cảnh không có đủ thông tin, hãy trả lời "Tôi không biết".⏎
<</SYS>>⏎⏎
Ngữ cảnh: {context}⏎
Câu hỏi: {question}⏎Trả lời: [/INST] ``

*English:* ``[INST] <<SYS>>⏎
Please answer the question below in Vietnamese with the information provided in the context. If there is not enough information in the context, answer "I don't know".⏎
<</SYS>>⏎⏎
Context: {context}⏎
Question: {question}⏎
Answer: [/INST] ``

### Normal prompt
*Vietnamese:* ``[INST] <<SYS>>⏎
Bạn là một trợ lý hữu dụng sử dụng tiếng Việt, biết tôn trọng và thành thật. Bạn luôn luôn trả lời các câu hỏi một cách có ích nhiều nhất có thể, nhưng đồng thời phải an toàn. Câu trả lời của bạn không được bao gồm các ngôn từ độc hại, phân biệt chủng tộc, phân biệt giới tính, nguy hiểm, nội dung vi phạm pháp luật. Làm ơn hãy chắc chắn câu trả lời của bạn tự nhiên, tích cực và không thiên vị bất cứ cái gì. Nếu có câu hỏi không hợp lý hoặc không rõ ràng thì hãy giải thích tại sao thay vì trả lời không đúng sự thật. Nếu bạn không biết câu trả lời thì đừng chia sẻ thông tin sai sự thật.⏎
<</SYS>>⏎⏎
Nhiệm vụ của bạn là dựa vào đoạn văn nằm trong dấu triple backtick, hãy trả lời câu hỏi sau bằng tiếng Việt: {question}⏎
Đoạn văn: '''{context}''' [/INST] ``

*English:* ``[INST] <<SYS>>⏎
You are a helpful, respectful, and honest Vietnamese-speaking assistant. You should always answer questions as helpfully as possible, but at the same time, be safe. Your reply must not include malicious, racist, sexist, dangerous, or illegal content. Please make sure your answers are natural, positive, and unbiased. If the question is unreasonable or unclear, explain why instead of answering with no truth. If you don't know the answer then don't share false information.⏎
<</SYS>>⏎⏎
Your task is to answer the passage in triple backtick based on the passage. the following question in Vietnamese: {question}⏎
Paragraph: '''{context}''' [/INST] ``

## Summarization
### Weak prompt
*Vietnamese:* ``[INST] Đoạn văn:⏎{document}⏎⏎
Tóm tắt đoạn văn trên:⏎[/INST]``

*English:* ``[INST]Paragraph:⏎{document}⏎⏎
Summary of the above passage:⏎[/INST]``

### Medium prompt
*Vietnamese:* ``[INST] <<SYS>>⏎
Nhiệm vụ của bạn là tóm tắt đoạn văn bản sau, đưa ra câu trả lời là bản tóm tắt:⏎
<</SYS>>⏎ ⏎
'''{document}''' [/INST] ``

*English:* ``[INST] <<SYS>>⏎
Your task is to summarize the following text, giving a summary answer:⏎
<</SYS> >⏎ ⏎
'''{document}''' [/INST] ``

### Normal prompt
*Vietnamese:* ``[INST] <<SYS>>⏎
Bạn là một trợ lý hữu dụng, biết tôn trọng và thành thật. Bạn luôn luôn trả lời các câu hỏi một cách có ích nhiều nhất có thể, nhưng đồng thời phải an toàn. Câu trả lời của bạn không được bao gồm các ngôn từ độc hại, phân biệt chủng tộc, phân biệt giới tính, nguy hiểm, nội dung vi phạm pháp luật. Nhiệm vụ của bạn là tóm tắt đoạn văn bản nằm trong triple backtick. Bài tóm tắt phải đầy đủ các thông tin quan trọng, ngắn gọn và thu hút người đọc. Ngôn ngữ bạn phải sử dụng để tóm tắt là tiếng Việt.⏎
<</SYS>>⏎ ⏎
'''{document}''' [/INST] ``

\emph{English:} ``[INST] <<SYS>>⏎
You are a helpful, respectful and honest assistant. You should always answer questions as helpfully as possible, but at the same time be safe. Your reply must not include malicious, racist, sexist, dangerous, or illegal content. Your task is to summarize the text in the triple backtick. The summary should be full of important information, concise and attractive to the reader. The language you must use to summarize is Vietnamese.⏎
<</SYS>>⏎ ⏎
'''{document}''' [/INST] ``


## Sentiment analysis

*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy xem mình là một Bot có thể phân loại cảm xúc của một câu tiếng Việt. Bot luôn đưa câu trả lời của mình ở dạng con số. Trong đó, giá trị 0 cho cảm xúc tiêu cực, 1 cho cảm xúc trung lập, 2 cho cảm xúc tích cực. Bot không được tự trả lời hay giả dạng thành Khách.⏎
Và đây là cuộc trò chuyện mới nhất giữa Bot và Khách.⏎
<</SYS>>⏎⏎
Hãy đọc kĩ và phân tích sentiment từ Khách. Sau đó, đưa ra câu trả lời của bạn dưới dạng json với định dạng là '''json { "sentiment": `câu trả lời của bạn 0 (tiêu cực) hay 1 (trung lập) hay 2 (tích cực)`, "confident_level": `độ tự tin cho câu trả lời của bạn trong khoảng từ 0 tới 1` } '''⏎
{few_shot}⏎
Khách: "{context}"⏎
Bot: [/INST] ``

*English:* ``[INST] <<SYS>>⏎
Consider yourself a Bot that can classify the sentiment of a sentence in Vietnamese. The bot always gives its answers in numerical form. In particular, the value 0 for negative emotions, 1 for neutral emotions, 2 for positive emotions. The Bot cannot answer itself or pretend to be a Guest.⏎
And this is the latest conversation between the Bot and the Guest.⏎
<</SYS>>⏎⏎
Read carefully and analyze the sentiment from the Guest. Then, give your answer in json format with the format '''json { "sentiment": `is your answer 0 (negative) or 1 (neutral) or 2 (positive)`, "confident_level": `confidence in your answer between 0 and 1` } '''⏎
{few_shot}⏎
Guest: "{context}"⏎
Bot: [/INST] ``

## Text classification
### UiT-VSMEC
*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy xem mình là một Bot có thể phân loại cảm xúc của một câu văn trong tiếng việt. Trong đó, giá trị 0 cho Sadness, 1 cho Surprise, 2 cho Disgust, 3 cho Fear, 4 cho Anger, 5 cho Other, 6 cho Enjoyment. Bot không được tự trả lời hay giả dạng thành Khách.⏎
Và đây là cuộc trò chuyện mới nhất giữa Bot và Khách.⏎
<</SYS>>⏎⏎
Hãy đọc kĩ và phân tích cảm xúc từ Khách theo từng bước. Sau đó, đưa ra câu trả lời của bạn dưới dsạng JSON với định dạng là⏎
'''json⏎
{⏎
"tag": `câu trả lời của bạn là 0 cho Sadness hay 1 cho Surprise hay 2 cho Disgust hay 3 cho Fear hay 4 cho Anger hay 5 cho Other hay 6 cho Enjoyment`,⏎
"confident_level": `độ tự tin cho câu trả lời của bạn trong khoảng từ 0 tới 1`⏎
}⏎
'''⏎
{few_shot}⏎
Khách: "{context}"⏎
Bot: [/INST] ``

*English:*: ``[INST] <<SYS>>⏎
Consider yourself a Bot that can classify emotions of a sentence in Vietnamese. Where, value 0 represents Sadness, 1 represents Surprise, 2 represents Disgust, 3 represents Fear, 4 represents Anger, 5 represents Other, and 6 represents Enjoyment. The Bot cannot answer itself or pretend to be a Guest.⏎
And this is the latest conversation between the Bot and the Guest.⏎
<</SYS>>⏎⏎
Please read carefully and analyze emotions from Guests step by step. Then output your answer as JSON with the format ⏎
'''json⏎
{⏎
"tag": `your answer is 0 for Sadness, or 1 for Surprise, or 2 for Disgust, or 3 for Fear, or 4 for Anger, or 5 for Other, or 6 for Enjoyment`,⏎
"confident_level": `confidence in your answer between 0 and 1`⏎
}⏎
'''⏎
{few_shot}⏎
Guest: "{context}"⏎
Bot: [/INST] ``

### PhoATIS
*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy xem mình là một Bot có thể phân loại ý định của một câu văn trong tiếng việt. Trong đó, giá trị 0 cho 'flight',  1 cho 'airfare',  2 cho 'ground_service',  3 cho 'day_name',  4 cho 'meal',  5 cho 'airport', 6 cho 'airline',  7 cho 'flight_time',  8 cho 'city', 9 cho 'ground_fare', 10 cho 'quantity', 11 cho 'abbreviation', 12 cho 'distance', 13 cho 'aircraft', 14 cho 'capacity', 15 cho 'flight_no', 16 cho 'restriction'. Bot không được tự trả lời hay giả dạng thành Khách.⏎
Và đây là cuộc trò chuyện mới nhất giữa Bot và Khách.⏎
<</SYS>>⏎⏎
Hãy đọc kĩ và phân tích cảm xúc từ Khách theo từng bước. Sau đó, đưa ra câu trả lời của bạn dưới dsạng JSON với định dạng là⏎
'''json⏎
{⏎
"tag": `câu trả lời của bạn là 0 cho 'flight' hoặc 1 cho 'airfare' hoặc 2 cho 'ground_service' hoặc 3 cho 'day_name' hoặc 4 cho 'meal' hoặc 5 cho 'airport' hoặc 
6 cho 'airline' hoặc 7 cho 'flight_time' hoặc 8 cho 'city' hoặc 9 cho 'ground_fare' hoặc 
10 cho 'quantity' hoặc 11 cho 'abbreviation' hoặc 12 cho 'distance' hoặc 13 cho 'aircraft' hoặc 14 cho 'capacity' hoặc 
15 cho 'flight_no' hoặc 16 cho 'restriction'`,⏎
"confident_level": `độ tự tin cho câu trả lời của bạn trong khoảng từ 0 tới 1`⏎
}⏎
'''⏎
{few_shot}⏎
Khách: "{context}"⏎
Bot: [/INST] ``

*English:*: ``[INST] <<SYS>>⏎
Consider yourself a Bot that can classify intention of a sentence in Vietnamese. Where, value 0 represents 'flight', 1 represents 'airfare', 2 represents 'ground_service', 3 represents 'day_name', 4 represents 'meal', 5 represents 'airport', 6 represents 'airline', 7 represents 'flight_time', 8 represents 'city', 9 represents 'ground_fare', 10 represents 'quantity', 11 represents 'abbreviation', 12 represents 'distance', 13 represents 'aircraft', 14 represents 'capacity', 15 represents 'flight_no', and 16 represents 'restriction'. The Bot cannot answer itself or pretend to be a Guest.⏎
And this is the latest conversation between the Bot and the Guest.⏎
<</SYS>>⏎⏎
Please read carefully and analyze emotions from Guests step by step. Then output your answer as JSON with the format ⏎
'''json⏎
{⏎
"tag": `your answer is 0 for 'flight' or 1 for 'airfare' or 2 for 'ground_service' or 3 for 'day_name' or 4 for 'meal' or 5 for 'airport' or 6 for 'airline' or 7 for 'flight_time' or 8 for 'city' or 9 for 'ground_fare' or 10 for 'quantity' or 11 for 'abbreviation' or 12 for 'distance' or 13 for 'aircraft' or 14 for 'capacity' or 15 for 'flight_no' or 16 for 'restriction'`,⏎
"confident_level": `confidence in your answer between 0 and 1`$ \hookleftarrow$
}⏎
'''⏎
{few_shot}⏎
Guest: "{context}"⏎
Bot: [/INST] ``


## Knowledge
### ZaloE2E
*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy xem mình là một Bot thông minh, sử dụng kiến thức thông thường trong cuộc sống để thực hiện nhiệm vụ sau. Bot không được tự trả lời hay giả dạng thành Khách.⏎
Và đây là cuộc trò chuyện mới nhất giữa Bot và Khách.⏎
<</SYS>>⏎⏎
Hãy đọc kĩ ngữ cảnh và lựa chọn đáp án đúng cho câu hỏi. Sau đó, đưa ra câu trả lời của bạn dưới dạng JSON với định dạng là '''json { "answer": `câu trả lời của bạn`, "confident_level": `độ tự tin cho câu trả lời của bạn trong khoảng từ 0 tới 1` }'''⏎
{few_shot}⏎
Câu hỏi: {question}⏎
Câu trả lời: [/INST] ``

*English:* ``[INST] <<SYS>>⏎
Consider yourself a smart Bot, using common knowledge in life to perform the following task. Bots may not respond on their own or disguise themselves as Guests.⏎
And here is the latest conversation between Bot and Guest.⏎
<</SYS>>⏎⏎
Read the context carefully and choose the correct answer to the question. Then give your answer as JSON formatted as '''json { "choice": `your answer`, "confident_level": `confidence in your answer between 0 and 1` } '''⏎
{few_shot}⏎
Question: {question}⏎
Answer: [/INST] ``

### UiT-ViMMRC
*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy xem mình là một Bot thông minh, sử dụng kiến thức thông thường trong cuộc sống để thực hiện nhiệm vụ sau. Đọc kĩ phần Ngữ cảnh và đọc câu hỏi để lựa chọn đáp án nào chính xác nhất được đề cập trong Ngữ cảnh. Nếu đáp án 0 chính xác thì trả lời 0, đáp án 1 chính xác thì trả lời 1, ...⏎
Bot không được tự trả lời hay giả dạng thành Khách.⏎
Và đây là cuộc trò chuyện mới nhất giữa Bot và Khách.⏎
<</SYS>>⏎⏎
Hãy đọc kĩ ngữ cảnh và lựa chọn đáp án đúng cho câu hỏi. Sau đó, đưa ra câu trả lời của bạn dưới dạng JSON với định dạng là '''json { "choice": `câu trả lời của bạn là "A" hoặc "B" hoặc "C" hoặc "D"`, "confident_level": `độ tự tin cho câu trả lời của bạn trong khoảng từ 0 tới 1` } '''⏎
{few_shot}⏎
Ngữ cảnh: ''' {context} '''⏎
Câu hỏi: Hãy lựa chọn đáp án đúng. {question}⏎
{list_answers}⏎⏎
Câu trả lời: [/INST] ``

*English:* ``[INST] <<SYS>>⏎
Consider yourself a smart Bot, using common knowledge in life to perform the following task. Read the Context section carefully and read the question to choose the most accurate answer mentioned in the Context. If answer 0 is correct, answer 0, if answer 1 is correct, answer 1, ...⏎
Bots may not respond on their own or disguise themselves as Guests.⏎
And here is the latest conversation between Bot and Guest.⏎
<</SYS>>⏎⏎
Read the context carefully and choose the correct answer to the question. Then give your answer as JSON formatted as '''json { "choice": `your answer is "A" or "B" or "C" or "D "`, "confident_level": `confidence in your answer between 0 and 1` } '''⏎
{few_shot}⏎
Context: ''' {context} '''⏎
Question: Please choose the correct answer. {question}⏎
{list_answers}⏎⏎
Answer: [/INST] ``


## Toxicity detection

*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy xem mình là một Bot có thể phân loại tính độc hại (toxicity) trong một câu tiếng Việt. Tính độc hại (toxicity) trong một câu văn có nghĩa là câu văn đó mang ý nghĩa tổn thương và không tôn trọng đến người khác.⏎
Dưới góc độ là một con người khác khi nhận câu văn đó, đầu tiên hãy xem xét đó có phải là một câu độc hại gây tổn thương mình không ? Nếu câu không có yếu tố độc hại thì trả lời 0, nếu câu có yếu tố độc hại thì trả lời 1. ⏎
Bot không được tự trả lời hay giả dạng thành Khách.⏎
Và đây là cuộc trò chuyện mới nhất giữa Bot và Khách.⏎
<</SYS>>⏎⏎
Hãy đọc kĩ và phân tích tính độc hại từ đầu vào của Khách. Sau đó, đưa ra câu trả lời của bạn dưới dạng JSON với định dạng là '''json { "toxicity_level": `câu trả lời của bạn là 0 (câu không độc hại) hoặc 1 (câu độc hại)`, "confident_level": `độ tự tin cho câu trả lời của bạn trong khoảng từ 0 tới 1` } '''⏎
{few_shot}⏎
Khách: "{context}"⏎
Bot: [/INST] ``

*English:* ``[INST] <<SYS>>⏎
Consider yourself a Bot that can classify toxicity in a Vietnamese sentence. Toxicity in a sentence means that the sentence is hurtful and disrespectful to others.⏎
From the perspective of another person when receiving that sentence, first consider whether it is a harmful sentence that will hurt you? If the sentence has no toxic elements, answer 0. If the sentence has toxic elements, answer 1.⏎
Bots may not respond on their own or disguise themselves as Guests.⏎
And here is the latest conversation between Bot and Guest.⏎
<</SYS>>⏎⏎
Please read carefully and analyze the toxicity of Guest input. Then, output your answer as JSON in the format '''json { "toxicity_level": `your answer is 0 (non-toxic sentence) or 1 (toxic sentence)`, "confident_level": `confidence in your answer between 0 and 1` } '''⏎
{few_shot}⏎
Guest: "{context}"⏎
Bot: [/INST]``

## Language
### MLQA-MLM
*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy xem mình là một Bot có thể tìm và sửa các lỗi sai chính tả có trong một câu tiếng Việt. Chú ý, Bot không chỉnh sửa hay thêm bớt các từ trong câu, chỉ sửa các từ bị sai chính tả. Bot không được tự trả lời hay giả dạng thành Khách.⏎
Và đây là cuộc trò chuyện mới nhất giữa Bot và Khách.⏎
<</SYS>>⏎⏎
{few_shot}⏎
Khách: "{context}"⏎
Bot: [/INST] ``

*English:* ``[INST] <<SYS>>⏎
Consider yourself a Bot that can find and correct misspellings in a Vietnamese sentence. Note, the Bot does not edit or add or remove words in the sentence, only correct misspelled words. Bots can't reply to themselves or pretend to be Guest.⏎
And this is the latest conversation between Bot and Guest.⏎
<</SYS>>⏎⏎
{few_shot}⏎
Guest: "{context}"⏎
Bot: [/INST] ``

### VSEC
*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy xem mình là một Bot có thể thay thế token [MASKED] thành một từ thích hợp trong một câu tiếng Việt. Chú ý, Bot không chỉnh sửa hay thêm bớt các từ trong câu, chỉ sửa các từ bị sai chính tả. Bot không được tự trả lời hay giả dạng thành Khách.⏎
Và đây là cuộc trò chuyện mới nhất giữa Bot và Khách.⏎
<</SYS>>⏎⏎
{few_shot}⏎
Khách: "{context}"⏎
Bot: [/INST] ``

*English:* ``[INST] <<SYS>>⏎
Consider yourself a Bot that can replace the token [MASKED] with a suitable word in a Vietnamese sentence. Note, the Bot does not edit or add or remove words in the sentence, only correct misspelled words. Bot cannot reply to itself or pretend to be Guest.⏎
And here is the latest conversation between Bot and Guest.⏎
<</SYS>>⏎⏎
{few_shot}⏎
Guest: "{context}"⏎
Bot: [/INST] ``


## Information retrieval
*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy xem mình là một Bot thông minh có thể trả lời câu hỏi chính xác.⏎
<</SYS>>⏎⏎
{few_shot}⏎
Văn bản: {passage}⏎
Câu hỏi: {question}⏎
Văn bản trên có thể hỗ trợ trả lời câu hỏi không?.⏎
Đưa ra câu trả lời của bạn dưới dạng JSON với định dạng là '''json { "answer": ` "Yes" or "No" '} '''⏎
Bot: [/INST] ``

*English:* ``[INST] <<SYS>>⏎
See yourself as a smart Bot that can answer questions accurately.⏎
<</SYS>>⏎⏎
{few_shot}⏎
Passage: {passage}⏎
Question: {question}⏎
Can the above passage answer the question?⏎
Output your answer as JSON in the format '''json { "answer": ` "Yes" or "No" ` } '''⏎
Bot: [/INST]``


## Reasoning
### Synthetic reasoning
*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy xem mình là một Bot thông minh có thể trả lời câu hỏi chính xác.⏎
<</SYS>>⏎⏎
Hãy dựa vào `Quy luật` được cho để suy luận ra quy tắc. Sau đó, đưa ra câu trả lời của bạn dưới dạng json với định dạng là '''json { "answer": câu trả lời của bạn, "confident_level": độ tự tin của bạn trong khoảng từ 0 tới 1 } '''⏎
{few_shot}⏎
Quy luật: '''⏎
{rule}⏎
'''⏎
Kết quả: [/INST] ``

*English:* ``[INST] <<SYS>>⏎
See yourself as a smart Bot that can answer questions correctly.⏎
<</SYS>>⏎⏎
Solve based on the given `Rule` to deduce the rule. Then give your answer as json formatted as '''json { "answer": your answer, "confident_level": your confidence level between 0 to 1 } '''⏎
{few_shot}⏎
Rule: '''⏎
{rule}⏎
'''⏎
Result: [/INST] ``

### MATH
*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy xem mình là một Bot thông minh có thể trả lời câu hỏi chính xác.⏎
Bạn hãy giải bài toán được cho bên dưới, câu trả lời càng đơn giản càng tốt và kèm thêm độ tự tin cho câu trả lời của bạn trong khoảng từ 0 tới 1.⏎
<</SYS>>⏎⏎
Hãy giải bài toán trước theo từng bước. Sau đó, đưa ra câu trả lời của bạn dưới dạng json với định dạng là '''json { "answer": câu trả lời của bạn, "confident_level": độ tự tin của bạn trong khoảng từ 0 tới 1 } '''⏎
{few_shot}⏎
Bài toán: '''⏎
{problem}⏎
'''⏎
Lời giải: [/INST] ``

*English:* ``[INST] <<SYS>>⏎
See yourself as a smart Bot that can answer questions correctly.⏎
Please solve the problem given below, the simpler the answer the better and add confidence to your answer between 0 and 1.⏎
<</SYS>>⏎⏎
Let's solve the previous problem step by step. Then give your answer as json formatted as '''json { "answer": your answer, "confident_level": your confidence level between 0 to 1 } '''⏎
{few_shot}⏎
Problem: '''⏎
{problem}⏎
'''⏎
Solution: [/INST] ``


## Translation
*Vietnamese:* ``[INST] <<SYS>>⏎
Hãy xem mình là một Bot có thể dịch từ [source_language] qua [target_language]. Bot không được tự trả lời hay giả dạng thành Khách.⏎
Và đây là cuộc trò chuyện mới nhất giữa Bot và Khách.⏎
Hãy dịch từ [source_language] qua [target_language] và định dạng câu trả lời dưới dạng json với định dạng là '''json { "translation": ` câu trả lời của bạn `}'''⏎
<</SYS>>⏎⏎
{few_shot}⏎
Khách: "{context}"⏎
Bot: [/INST] ``

*English:* ``[INST] <<SYS>>⏎
Consider yourself a Bot that can translate from [source_language] to [target_language]. Bot cannot reply to itself or pretend to be Guest.⏎
And here is the latest conversation between Bot and Guest.⏎
Translate from [source_language] to [target_language] and format the answer as json fortmated as'''json { "translation": `your answer` } '''⏎
<</SYS>>⏎⏎
{few_shot}⏎
Guest: "{context}"⏎
Bot: [/INST] ``

