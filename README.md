# Text-To-Art
The art work based on the given prompts:

1.Given Prompt :  an illustration of a baby daikon radish in a tutu walking a dog.
Detailed description of the given prompt : Please create an adorable illustration of a baby daikon radish wearing a cute tutu and confidently walking a dog. The daikon radish should have a cheerful expression on its face, and the dog should be a friendly and lovable companion. The illustration should capture the playful nature of the scene and evoke a sense of joy and innocence.
Art Work : ![Daikon](https://github.com/adityak1905/Text-To-Art/assets/152466219/0685f7e2-a7aa-4209-972f-382e7704db68)

2.Given Prompt :  an armchair in the shape of an avocado.
Detailed description of the given prompt : Please create an illustration of an armchair in the shape of an avocado. The armchair should resemble an avocado, with a green exterior and a brown pit in the center.The illustration should capture the uniqueness and whimsical nature of the avocado armchair.
Art Work : ![avacado](https://github.com/adityak1905/Text-To-Art/assets/152466219/928f0acb-3d45-4057-9446-50edaf60360b)

3.Given Prompt : a store front that has the word ‘Slash Mark’ written on it.
Detailed description of the given prompt :Please create an illustration of a store front with the word "Slash Mark" prominently displayed.  Use creative elements such as bold colors and interesting typography to make the word "Slash Mark" stand out. Feel free to add additional details like signage or surrounding scenery to enhance the overall composition.
Art Work : ![Slashmark](https://github.com/adityak1905/Text-To-Art/assets/152466219/24672cf9-6e53-41f6-a5ef-ffa95606de5d)





# Text-T0-3D Models
3D Models based on the given prompts:

1.Given prompt : Beautiful and colorful spanish tile.
Detailed Description of the prompt : Please create a 3D model of the text "Beautiful and colorful Spanish tile." The model should showcase the text in an artistic and visually appealing way, highlighting the beauty and vibrant colors of Spanish tiles. Use your cretivity to bring the text to life in a three-dimensional space.
3D Model : ![Spanish tile 3d model](https://github.com/adityak1905/SlashMark-Tasks/assets/152466219/5798a7c7-4c21-4e0d-afba-f7db04633fc5)

2.Given Prompt : Macro photograph of a green leaf.
Detailed Description of the prompt :Please create a detailed 3D model of the text "macro photograph of a green leaf". The model should accurately depict a close-up shot of a green leaf, capturing the intricate details and texture. Pay special attention to the lighting and shading to create a realistic effect.
3D Model : ![leaf 3d model](https://github.com/adityak1905/SlashMark-Tasks/assets/152466219/e8bdcc11-a8e3-4880-b324-c17c43a9bdf1)

3.Given prompt : pink flowers petals on a wood floor.
Detailed Description of the prompt :Please create a 3D model of pink flower petals scattered on a wooden floor. The model should accurately capture the shape, color, and texture of the petals and the wood. Pay attention to the lighting and shadows to create a realistic and visually appealing scene.
3D Model : ![petals 3d model](https://github.com/adityak1905/SlashMark-Tasks/assets/152466219/543c3f5c-5f74-4373-8003-344c931f7640)






# Creating a chat bot using faq's given in the task.
Hello SlashMark! thanks for assigning me the task of creating a chatbot according to the given faq's i gave my bets and im still in a process of learning.

Here is the my code of teh chatbot:

<!DOCTYPE html>
<html lang="en">
    <title>CHATBOT</title>
    <h1>Chat Bot,Based On Faq's given By The Slash Mark team !</h1>
    <h2>Special Faq (Type "SlashMark")</h2>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAQ Chatbot</title>
    <style>
        #chatbox {
            display: flex;
            flex-direction: column;
            align-items: leftcorner;
            justify-content: leftcorner;
            height: 300vh;
            height: 300px;
            overflow-y: scroll;
            border: 1px solid #ccc;
            padding: 50px;
        }
    
    </style>
</head>
<body>
    <div id="chatbox"></div>
    <input type="text" id="messageInput" />
    <button onclick="sendMessage()">Send</button>
  

    <script>
        const faqs = {
            
            "what is chatgpt?":"ChatGPT is a language model developed by OpenAI that is designed for natural language conversation. It can answer questions, generate 
            text, and have interactive discussions with users.",
            "how does chatgpt work?": "ChatGPT is powered by a deep learning model called GPT (Generative Pre-trained Transformer). It's trained on a large corpus of 
            text from the internet and uses that knowledge to generate human-like text based on input.",
            "what can i do with chatgpt?": "You can use ChatGPT for a variety of tasks, such as answering questions, generating text, creating content, providing 
            recommendations, and much more.",
            "is chatgpt free to use?": "OpenAI offers both free and paid access to ChatGPT. There may be usage limitations on the free tier, and you can check 
            OpenAI's pricing for more details.",
            "what is prompt engineering?": "Prompt engineering is the process of designing specific instructions or questions to obtain desired responses from a 
            language model like ChatGPT. It involves crafting prompts to be clear and effective in conveying your intent.",
            "hello": ["Hi there!", "Hello!", "How can I help you today?"],
            "how are you": ["I'm just a computer program, so I don't have feelings, but thanks for asking! How can I assist you?", "I'm here to help. What can I do 
            for you?"],
            "bye": ["Goodbye!", "Have a great day!", "See you later!"],
            "help": ["You can ask me questions or say hello. If you want to exit, just type 'bye'."],
            "hi": ["Hi! I'm your friendly chatbot. You can start a conversation with me or type 'bye' to exit."],
            "slashmark":"I would like to take this opportunity to express my sincere thanks to Slashmark. I am genuinely grateful for the 
            [opportunity/experience/partnership] with your company. Your support and [mentorship/leadership/collaboration] have been invaluable, and I appreciate the 
            chance to [contribute/learn/grow] within the Slashmark community. Thank you for making a positive impact on my journey, and I look forward to continuing 
            to [contribute/engage/work] together in the future. Cheers to the Slashmark team for creating an environment that fosters 
            [innovation/creativity/success]."
            };
 
            const chatbox = document.getElementById('chatbox');
            const messageInput = document.getElementById('messageInput');

            function sendMessage() {
            const userMessage = messageInput.value;
            appendMessage('User', userMessage);

            const response = faqs[userMessage] || "I'm not sure I understand. Can you please rephrase your question or greeting?";
            appendMessage('Chatbot', response);

            // Clear the input field
            messageInput.value = '';
        }

        function appendMessage(sender, message) {
            const newMessage = document.createElement('div');
            newMessage.innerText = `${sender}: ${message}`;
            chatbox.appendChild(newMessage);
        }
        
    </script>
</body>
</html>

