# FaceConnect

##### Never lose a connection again! Connect with anyone, any wallet, and send transactions through an image of one's face!

## Inspiration

Have you ever met someone and instantly connected with them, only to realize you forgot to exchange contact information? Or, even worse, you have someone's contact but they are outdated and you have no way of contacting them? I certainly have.

This past week, I was going through some old photos and stumbled upon one from a Grade 5 Summer Camp. It was my first summer camp experience, I was super nervous going in but I had an incredible time with a friend I met there. We did everything together and it was one of my favorite memories from childhood. But there was a catch – I never got their contact, and I'd completely forgotten their name since it's been so long. All I had was a physical photo of us laughing together, and it felt like I'd lost a precious connection forever.

This dilemma got me thinking. The problem of losing touch with people we've shared fantastic moments with is all too common, whether it's at a hackathon, a party, a networking event, or a summer camp. So, I set out to tackle this issue at Hack The Valley.

## What it does

That's why I created FaceConnect, a Discord bot that rekindles these connections using facial recognition. With FaceConnect, you can stay in touch with people as long as you have a picture of their face. But that's not all. FaceConnect also allows you to view account information and send transactions if you have a friend's face in your database.

If you owe your friend money and have their face in your database, you can simply use the "transaction" command to complete the payment.

Imagine a world where you never lose contact with your favorite people again.

Join me in a future where no connections are lost. Welcome to FaceConnect!

## Demos

Mobile Registration and Connection Flow (Registering and Detecting my own face!):


https://github.com/WilliamUW/HackTheValley/assets/25058545/eb8501ad-1c4c-4795-a1a4-91ff7385d281


Desktop Connection Flow (Obama + Trump + Me as examples):


https://github.com/WilliamUW/HackTheValley/assets/25058545/5e8f7c74-dd3a-4742-a5a3-e309cfd9d2e8



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
