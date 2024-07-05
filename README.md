Overview
<br>
Welcome, AI enthusiasts! We're excited to present a challenge that pushes the boundaries of computer vision and artificial intelligence. This is the first challenge in a three-part series aimed at developing an advanced AI system for image analysis and manipulation. The ultimate goal is to create a comprehensive solution capable of object detection, scene interpretation, placement scoring for object insertion, and seamless object integration within various scenes.In this phase, we are initially focusing on the Food and Beverage industry, with plans to expand to the Clothing industry in the future.
<br>
 #1: Image Classification
 <br>
The first task focuses on image classification, where your AI model will analyze an uploaded image and extract valuable information. <br>

Object Detection <br>
Your model will identify and categorize individual objects present within the image. This might include common objects like people, animals, furniture, or natural elements like trees, water bodies, and terrain.<br>
Scene Interpretation <br>
Go beyond simply identifying objects; aim to understand the overall scene depicted in the image. This involves generating a concise description that captures the essence of the picture. For example, an image containing a group of people gathered around a table with food might be interpreted as "a family enjoying a dinner together.<br>
#2: Placement Scoring (Future scope) <br>
The second task delves into the realm of object placement scoring. Here, your model will analyze an image and identify optimal locations for inserting or replacing objects within the scene.

Placement Zones
Instead of a single placement suggestion, your model should identify multiple suitable zones within the image where an object could be realistically and aesthetically inserted. These zones should be visually distinct and well-defined.
Zone Scoring
Don't just identify zones; rank them based on a set of criteria. This might include factors like:
Realism: How seamlessly would the inserted object blend into the existing scene?
Aesthetics: Does the placement enhance the visual appeal of the image, or create an awkward composition?
Object Occlusion: Would the placement partially or entirely obscure other important elements within the image?<br>
#3: Object Integration (Compositing - Future scope) <br>
The final task takes the concept of object placement a step further. Your model will be responsible for inserting or replacing an object within a provided base image, creating a realistic and cohesive final product:<br>

Object Integration <br>
Given an image and a separate image of the object to be inserted, your model should seamlessly integrate the object into the base image. This involves tasks like background removal, perspective adjustment, and lighting correction to ensure the inserted object appears naturally within the scene.<br>
Post-Processing <br>
This step involves any additional adjustments desired for the final image. This might include color correction to ensure consistency between the inserted object and the base image, or minor lighting adjustments for a more natural look. <br>
#1 - Image Classification <br>
The objective is to create an AI model that analyzes an uploaded image and extracts valuable information through the following functionalities: <br>

Object Detection: <br> Identify and categorize individual objects within the image, such as people, animals, furniture, or natural elements like trees and water bodies.
Scene Interpretation: Generate a concise description that captures the essence of the image (e.g., "a family enjoying dinner together").
Requirements
Create an API endpoint that processes images and identifies objects within them. The service should return the object names and bounding box coordinates, along with a detailed description of the image.<br>

Input <br>
The service should accept a JSON object: <br>

{<br>
  "url": "/path/to/image" <br>
} <br>
The service should take into account the following considerations when receiving the input: <br>

The url property is a direct path to the image.<br>
The image can be of any resolution.<br>
Output<br>
The service should return a JSON object:<br>

{<br>
  "objects": [ <br>
    { <br>
      "name": "table",<br>
      "bb": {<br>
        "topLeft": {<br>
          "x": "XXpx",<br>
          "y": "XXpx"<br>
        },<br>
        "size": {<br>
          "width": "XXpx",<br>
          "height": "XXpx"<br>
        }<br>
      }<br>
    }<br>
  ],<br>
  "description": "..."<br>
}<br>
an example like this :<br>

{
  "objects": [
    {
      "bb": {
        "topLeft": {
          "x": 256.82,
          "y": 37.01
        },
        "size": {
          "width": 257.64,
          "height": 269.31
        }
      },
      "name": "person"
    },
    {
      "bb": {
        "topLeft": {
          "x": 270.16,
          "y": 250.29
        },
        "size": {
          "width": 236.65,
          "height": 97.18
        }
      },
      "name": "skateboard"
    }
  ],
  "description": "A man on a long exposure picture riding an electric skateboard."
} <br>
The final JSON output object should take into account the following considerations:<br>

Bounding Box (bb): Contains the top-left x,y coordinates and the dimensions of the box for the object.<br>
Name: Common noun name of the object.<br>
Description: An accurate explanation of the image (e.g., "a bottle on a table" or "a man sitting on a chair by the beach drinking a soft drink").
Technology Stack<br>
API Options:<br>
REST API or GRAPHQL<br>

Programming Language:<br>
Javascript or Python

Interface:<br>
Develop a web interface for interacting with the system. This interface should allow users to upload an image and click submit, triggering API calls to process the image and display all detected objects along with the scene description. You can use third-party libraries like Gradio for this interface.

Permitted Tools
The use of closed-source commercial tools like OpenAI and similar alternatives in their entirety is NOT permitted for this challenge.
Here are some options you can consider to tackle this challenge:

Open-Source Frameworks: Utilize open-source deep learning frameworks like TensorFlow, PyTorch, or Keras to build your custom solutions. These frameworks provide the building blocks for creating powerful AI models while offering greater transparency and control over the development process.
Pre-trained Models: Consider leveraging pre-trained models like VGG16 or ResNet for specific tasks like image classification. However, ensure you understand how these models work and fine-tune them on your datasets to achieve optimal performance within the context of this challenge.
Hugging Face Models and Data: You can use models and data available on Hugging Face, provided they are accessible via the free tier.
Provided Data
Training Dataset:
COCO Dataset
Training Images
Annotations
Food and Beverages
Clothing
Provisional Dataset: provisional.zip (This dataset is shared in the forums and used for provisional scoring and leaderboard updates.)
Final Dataset: final.zip (This dataset will be provided 24 hours before the submission deadline in the forums)
Scoring
The scoring for this challenge will be based on two key metrics: Intersection over Union (IoU) and Text Cosine Similarity. These metrics will evaluate the accuracy of object detection and the quality of scene interpretation respectively. The final score for each submission will be the average of the IoU and text cosine similarity scores.
a. Intersection over Union (IoU):

Measure the accuracy of object detection models.
Calculate the overlap between the predicted and ground truth bounding boxes.
b. Text Cosine Similarity:

Measure the similarity between two text descriptions.
Calculate cosine similarity between vector representations of the descriptions.
Generate vector representations of the descriptions using the BERT model.
Evaluation Phrase
Provisional Testing

Dataset: 40 images
Submission File: submission.jsonl (Only the JSONL file will be evaluated, and no code execution will be involved)
Description: In the provisional testing phase, your model will be evaluated using a set of 40 images. These images are provided to help you tune and refine your model. The results should be submitted in a JSONL file format (submission.jsonl). This phase allows for iterative improvements and updates to the leaderboard based on performance.
Final Testing
Submission File: final.jsonl
Description: The final testing phase involves a more extensive evaluation. This dataset will be released 24 hours before the submission deadline to ensure a fair and challenging test of your model's capabilities. The results should be submitted in a JSONL file format (final.jsonl).
Final scores: The final score will be calculated as Score = 0.8*(Final Testing Score based on final.jsonl) + 0.2*(Code Quality and Documentation).
Qualification: To qualify for the prize, participants must achieve a minimum score of 40%.
Submission Instructions.
Submission - 
Code and Software Packages
Main code files implementing the image classification functionality.
Dockerfile for easy deployment (e.g., nvidia/cuda:12.2.0-devel-ubuntu22.04 for GPU computing).
Starter bash script for service bootup from the command line.
Clear inline comments for key steps.
Solution
JSONL format output, with one line per image.
Submission must align with the training and validation dataset structures.
Documentation
README.md: Deployment instructions and a report on your image classification solution, including the chosen pre-trained model.
Cost schedule for expected review costs.
File Structure
The desired file structure is:

submission.zip/
│
├── code/
│   ├── Dockerfile
│   └── (YOUR CODEBASE HERE)
│
├── solution/
│   ├── submission.jsonl
│   └── final.jsonl
│
└── documentation/
    ├── README.md
    │   ├── deployment instruction
    │   └── solution report
    └── (any other relevant documentation)
General Notes
Teaming is not permitted.
Use the match forum to ask general questions or report problems, but please do not post comments and questions that reveal information about the problem itself or possible solution techniques.
In this match you may use allowed programming language and libraries mentioned in the permitted tools section above, provided Topcoder is able to run it free of any charge. You may also use any open-source languages and libraries, with the restrictions listed in the next section below. If your solution requires licenses, you must have these licenses and be able to legally install them in a testing VM etc.
Prior to submission, please make absolutely sure your submission can be run by Topcoder free of cost, and with all necessary licenses pre-installed in your solution. Topcoder is not required to contact submitters.
You may use open source languages and libraries provided they are equally free for your use, use by another competitor, or use by the client.
If your solution includes licensed software (e.g. commercial software, open source software, etc), you must include the full license agreements with your submission. Include your licenses in a folder labeled “Licenses”. Within the same folder, include a text file labeled “README” that explains the purpose of each licensed software package as it is used in your solution.
