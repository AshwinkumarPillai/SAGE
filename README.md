# TEAM MEMBERS (SOLO)

- Ashwin Pillai (ap22943@uga.edu)

# PROJECT PURPOSE

In today's fast-paced world, individuals often struggle to find accurate and relevant answers to their queries amidst the abundance of information available online. Traditional methods involve scouring through multiple websites, which can be time-consuming and overwhelming. To address this challenge, I have developed a solution called SAGE (Search Augmented Generation Engine) - using RAG: Retrieval Augmented Generation.

SAGE harnesses the power of Retrieval-Augmented Generation (RAG), a cutting-edge natural language processing (NLP) model architecture. By integrating information retrieval from the web with generative capabilities, SAGE delivers responses that are not only accurate but also grounded in relevant context.

One of the primary objectives of SAGE is to streamline the information-seeking process for users across various domains. For instance, an international student seeking updates on OPT or EAD filing procedures can rely on SAGE to fetch and present the latest information from relevant sources in a coherent manner.

Key features of SAGE include:

- Generating code snippets in a readable format.
- Providing accurate responses to user queries, surpassing the limitations of traditional search engines.
- Crafting email responses tailored to specific topics.
- And much more.

Basically, anything that ChatGPT does but more.

Here are a few examples on how this is better than ChatGPT:

1. When asked who the president of India is, ChatGPT answered Ram Nath Kovind, which is actually the former president but SAGE gave the current president's name
2. You can ask SAGE about the Union budget that was released last week and it will get you the information but GPT fails since the training data is limited to 2022 (last update)
3. When asked about the current Director of School of Computing at UGA, SAGE gave the correct response and GPT did not.

### WHAT IS RAG

"Retrieval-Augmented Generation" (RAG) is a natural language processing (NLP) model architecture that combines retrieval-based methods with generative methods. It aims to improve the quality and relevance of generated text by incorporating information retrieved from a large corpus of text during the generation process.

In RAG, the model consists of two main components:

Retriever: This component is responsible for retrieving relevant information from a large text corpus based on the input query or prompt. It uses techniques such as information retrieval (IR) or pre-trained language models to find relevant passages or documents.

Generator: After retrieving relevant information, the generator component generates text based on both the input query/prompt and the retrieved information. It typically utilizes a pre-trained language model (such as GPT, BERT, or T5) to generate coherent and contextually relevant text.

# TOOLS UTILIZED

1. React: Frontend development.
2. Flask: Backend development.
3. Tailwind CSS: Styling for the user interface.
4. LangChain: Leveraged for its powerful language model capabilities.
5. SERPAPI: Integrated to access the Google Search API efficiently.

## PROBLEMS THAT OCCURED WHILE DEVELOPING THIS SYSTEM AND HOW THEY WERE OVERCOME

Since my ML experience was limited, I had some issues in figuring out how to create context after querying from the web using API (SERP). The way I overcame this is by googling around and looking at articles and then finally coming up with creating an in-memory vector search using the loaded data which means basically vectorizing the documents retrieved.

There were other small issues that popped up but I finessed my way through them :)

# APIs USED

- [OPEN AI API](https://platform.openai.com/docs/overview)
- [SERP API](https://serpapi.com/)

# USAGE

Note: Since I am using private API keys, I had to put config, env and API-gateway files in git-ignore, hence you wont be able to run the backend. But you can run the front-end to see how it looks

1. The front-end it present in the chat-bot-frontend folder
2. Navigate to that folder and in the terminal run `npm install` to install all dependencies and `npm start` to start the frontend on http://localhost:3000

3. The backend is present in the folder rag_pip
4. Navigate to that folder and in the terminal run
   `pip install requirements.txt`
   to install dependencies
   `python3 index.p`
   to start the backend on http://localhost:5000

   Although the backend won't start since I have removed some files due to privacy and security concerns.
