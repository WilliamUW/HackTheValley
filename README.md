# FaceConnect

##### Never lose a connection again! Connect with anyone, any wallet, and send transactions through an image of one's face!

## Inspiration

The inspiration for FaceConnect came from a common problem many of us have experienced - the difficulty of staying in touch with people I meet at various events, whether it's a hackathon, a party, or a networking event. It's frustrating when I hit it off with someone, but either forget to exchange contact information or struggle to remember who they are later on. FaceConnect was born out of a desire to solve this problem by using facial recognition technology to connect people through their photos!

## What it does

FaceConnect is a Discord bot designed to help you reconnect with people using facial recognition. It allows users to upload a selfie, and the bot generates a unique facial encoding. Users can then upload a photo of someone they want to connect with, and the bot matches it to the encoding. Once a match is found, users can send a message to initiate contact.

Additionally, FaceConnect also includes a transaction feature that allows users to send transactions based on facial recognition. If you owe your friend money and have their face in your database, you can simply use the "transaction" command to complete the payment.

## Demos

Mobile Registration and Connection Flow (Registering and Detecting my own face!):


https://github.com/WilliamUW/HackTheValley/assets/25058545/eb8501ad-1c4c-4795-a1a4-91ff7385d281


Desktop Connection Flow (Obama + Trump + Me as examples):


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

- **Biometric Encoding:** Implementing facial biometric encoding and recognition, although cool, required finding the right tools to convert a face to a biometric hash and then compare these hashes accurately.

## Accomplishments that I're proud of

I're proud of several accomplishments:

- **Facial Recognition:** Successfully implementing facial recognition technology, allowing users to connect based on photos.

- **Blockchain Integration:** Integrating Hedera and Flow to enable seamless transactions based on facial recognition.

- **Custom LLMs:** Building custom Language Models trained on sponsor documentation, which significantly aided the learning process for new technologies.

- **Inclusivity:** Aligning the project with the Diversity theme, promoting inclusivity and connection across barriers such as language and disabilities.

- **Real-World Application:** Developing a solution that addresses a common real-world problem - staying in touch with people.

## What I learned

Throughout this hackathon, I learned a great deal:

- **Technology Stacks:** I gained experience with a wide range of technologies, including computer vision, blockchain, and biometric encoding.

- **Solo Coding:** The experience of solo coding, while initially challenging, allowed for greater freedom and experimentation.

- **Documentation:** Building custom LLMs for various technologies, based on sponsor documentation, proved invaluable for rapid learning.

## What's next for FaceConnect

The future of FaceConnect looks promising:

- **Multiple Faces:** Supporting multiple people in a single photo to enhance the ability to reconnect with groups of friends or acquaintances.

- **Improved Transactions:** Expanding the transaction feature to enable users to pay or transfer funds to multiple people at once.

- **Additional Technologies:** Exploring and integrating new technologies to enhance the platform's capabilities and reach.
