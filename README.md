# FaceConnect

##### Never lose a connection again! Connect with anyone, any wallet, and send transactions through an image of one's face!

## Inspiration

Have you ever met someone and instantly connected with them, only to realize you forgot to exchange contact information? Or, even worse, you have someone's contact but they are outdated and you have no way of contacting them? I certainly have.

This past week, I was going through some old photos and stumbled upon one from a Grade 5 Summer Camp. It was my first summer camp experience, I was super nervous going in but I had an incredible time with a friend I met there. We did everything together and it was one of my favorite memories from childhood. But there was a catch – I never got their contact, and I'd completely forgotten their name since it's been so long. All I had was a physical photo of us laughing together, and it felt like I'd lost a precious connection forever.

This dilemma got me thinking. The problem of losing touch with people we've shared fantastic moments with is all too common, whether it's at a hackathon, a party, a networking event, or a summer camp. So, I set out to tackle this issue at Hack The Valley.

## What it does

That's why I created FaceConnect, a Discord bot that rekindles these connections using facial recognition. With FaceConnect, you can send connection requests to people as long as you have a picture of their face. 

But that's not all. FaceConnect also allows you to view account information and send transactions if you have a friend's face. If you owe your friend money, you can simply use the "transaction" command to complete the payment.

Or even if you find someone's wallet or driver's license, you can send a reach out to them just with their ID photo!

Imagine a world where you never lose contact with your favorite people again.

Join me in a future where no connections are lost. Welcome to FaceConnect!

## Demos

Mobile Registration and Connection Flow (Registering and Detecting my own face!):




https://github.com/WilliamUW/HackTheValley/assets/25058545/d6fc22ae-b257-4810-a209-12e368128268



Desktop Connection Flow (Obama + Trump + Me as examples):




https://github.com/WilliamUW/HackTheValley/assets/25058545/e27ff4e8-984b-42dd-b836-584bc6e13611




## How I built it

FaceConnect is built on a diverse technology stack:

1. **Computer Vision:** I used OpenCV and the Dlib C++ Library for facial biometric encoding and recognition.

2. **Vector Embeddings:** ChromaDB and Llama Index were used to create vector embeddings of sponsor documentation.

3. **Document Retrieval:** I utilized Langchain to implement document retrieval from VectorDBs.

4. **Language Model:** OpenAI was employed to process user queries.

5. **Messaging:** Twilio API was integrated to enable SMS notifications for contacting connections.

6. **Discord Integration:** The bot was built using the discord.py library to integrate the user flow into Discord.

7. **Blockchain Technologies:** I integrated Hedera to build a decentralized landing page and user authentication. I also interacted with Flow to facilitate seamless transactions.

## Challenges I ran into

Building FaceConnect presented several challenges:

- **Solo Coding:** As some team members had midterm exams, the project was developed solo. This was both challenging and rewarding as it allowed for experimentation with different technologies.

- **New Technologies:** Working with technologies like ICP, Flow, and Hedera for the first time required a significant learning curve. However, this provided an opportunity to develop custom Language Models (LLMs) trained on sponsor documentation to facilitate the learning process.

- **Biometric Encoding:** It was my first time implementing facial biometric encoding and recognition! Although cool, it required some time to find the right tools to convert a face to a biometric hash and then compare these hashes accurately.

## Accomplishments that I'm proud of

I're proud of several accomplishments:

- **Facial Recognition:** Successfully implementing facial recognition technology, allowing users to connect based on photos.

- **Custom LLMs:** Building custom Language Models trained on sponsor documentation, which significantly aided the learning process for new technologies.

- **Real-World Application:** Developing a solution that addresses a common real-world problem - staying in touch with people.

## What I learned

Throughout this hackathon, I learned a great deal:

- **Technology Stacks:** I gained experience with a wide range of technologies, including computer vision, blockchain, and biometric encoding.

- **Solo Coding:** The experience of solo coding, while initially challenging, allowed for greater freedom and experimentation.

- **Documentation:** Building custom LLMs for various technologies, based on sponsor documentation, proved invaluable for rapid learning!

## What's next for FaceConnect

The future of FaceConnect looks promising:

- **Multiple Faces:** Supporting multiple people in a single photo to enhance the ability to reconnect with groups of friends or acquaintances.

- **Improved Transactions:** Expanding the transaction feature to enable users to pay or transfer funds to multiple people at once.

- **Additional Technologies:** Exploring and integrating new technologies to enhance the platform's capabilities and reach beyond Discord!









### Sponsor Information

ICP Challenge:

I leveraged ICP to build a decentralized landing page and implement user authentication so spammers and bots are blocked from accessing our bot.

Built custom LLM trained on ICP documentation to assist me in learning about ICP and building on ICP for the first time!

I really disliked deploying on Netlify and now that I’ve learned to deploy on ICP, I can’t wait to use it for all my web deployments from now on!

Canister ID: be2us-64aaa-aaaaa-qaabq-cai

Link: https://github.com/WilliamUW/HackTheValley/blob/readme/ICP.md


Best Use of Hedera:

With FaceConnect, you are able to see your Hedera account info using your face, no need to memorize your public key or search your phone for it anymore!

Allow people to send transactions to people based on face! (Wasn’t able to get it working but I have all the prerequisites to make it work in the future - sender Hedera address, recipient Hedera address).

In the future, to pay someone or a vendor in Hedera, you can just scan their face to get their wallet address instead of preparing QR codes or copy and pasting!

I also built a custom LLM trained on Hedera documentation to assist me in learning about Hedera and building on Hedera as a beginner!

Link: https://github.com/WilliamUW/HackTheValley/blob/readme/hedera.md

Best Use of Flow

With FaceConnect, to pay someone or a vendor in Flow, you can just scan their face to get their wallet address instead of preparing QR codes or copy and pasting!

I also built a custom LLM trained on Flow documentation to assist me in learning about Flow and building on Flow as a beginner!

Link: https://github.com/WilliamUW/HackTheValley/readme/main/flow.md

Georgian AI Challenge Prize

I was inspired by the data sources listed in the document by scraping LinkedIn profile pictures and their faces for obtaining a dataset to test and verify my face recognition model!

I also built a custom LLM trained on Georgian documentation to learn more about the firm!

Link: https://github.com/WilliamUW/HackTheValley/blob/readme/GeorgianAI.md

Best .Tech Domain Name:

FaceCon.tech

Best AI Hack:

Use of AI include:
1. Used Computer Vision with OpenCV and the Dlib C++ Library to implement AI-based facial biometric encoding and recognition.
2. Leveraged ChromaDB and Llama Index to create vector embeddings of sponsor documentation
3. Utilized Langchain to implement document retrieval from VectorDBs
4. Used OpenAI to process user queries for everything Hack the Valley related!

By leveraging AI, FaceConnect has not only addressed a common real-world problem but has also pushed the boundaries of what's possible in terms of human-computer interaction. Its sophisticated AI algorithms and models enable users to connect based on visuals alone, transcending language and other barriers. This innovative use of AI in fostering human connections sets FaceConnect apart as an exceptional candidate for the "Best AI Hack" award.

Best Diversity Hack:

Our project aligns with the Diversity theme by promoting inclusivity and connection across various barriers, including language and disabilities. By enabling people to connect using facial recognition and images, our solution transcends language barriers and empowers individuals who may face challenges related to memory loss, speech, or hearing impairments. It ensures that everyone, regardless of their linguistic or physical abilities, can stay connected and engage with others, contributing to a more diverse and inclusive community where everyone's unique attributes are celebrated and connections are fostered.

Imagine trying to get someone’s contact in Germany, or Thailand, or Ethiopia? Now you can just take a picture!

Best Financial Hack:

FaceConnect is the ideal candidate for "Best Financial Hack" because it revolutionizes the way financial transactions can be conducted in a social context. By seamlessly integrating facial recognition technology with financial transactions, FaceConnect enables users to send and receive payments simply by recognizing the faces of their friends.

This innovation simplifies financial interactions, making it more convenient and secure for users to settle debts, split bills, or pay for services. With the potential to streamline financial processes, FaceConnect offers a fresh perspective on how we handle money within our social circles. This unique approach not only enhances the user experience but also has the potential to disrupt traditional financial systems, making it a standout candidate for the "Best Financial Hack" category.

