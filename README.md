# FaceConnect

##### Never lose a connection again! Connect with anyone, any wallet, and send transactions through an image of one's face!

## Inspiration

Have you ever met someone and felt an instant connection, only to realize you never exchanged contact information? Or perhaps you've faced the frustration of having someone's contact but struggling to remember who they are later on. Now, imagine a solution that helps you bridge these gaps using the power of facial recognition. FaceConnect was inspired by the question: "What if you could reconnect with those you've met simply by sharing a photo?"

This common scenario, whether at a hackathon, a social event, or even a casual get-together, often leaves us longing to stay in touch with the amazing people we've crossed paths with. The inspiration for FaceConnect also came from a personal experience when I attended a summer camp and forged a remarkable bond with a friend. However, I never got their contact information and only have a photo as a memory. The desire to reconnect with that friend was a driving force behind the creation of FaceConnect.

FaceConnect seeks to answer the question by enabling connections through the simplicity of a photograph, ensuring that you never lose contact with those you've shared incredible moments with.

## What it does

FaceConnect is a Discord bot designed to help you reconnect with people using facial recognition. It allows users to upload a selfie, and the bot generates a unique facial encoding. Users can then upload a photo of someone they want to connect with, and the bot matches it to the encoding. Once a match is found, users can send a message to initiate contact.

Additionally, FaceConnect also includes a transaction feature that allows users to send transactions based on facial recognition. If you owe your friend money and have their face in your database, you can simply use the "transaction" command to complete the payment.

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
