
# Basic Capstone Design : BELIEVE
___

<div align="center">
<img width="450" alt="image" src="https://github.com/user00144/basic_capstone_BELIEVE_ai_server/assets/120700820/68cf2f8a-386a-4591-811f-c34aa73c27c6">
</div>


## Vision Based Edge Intelligence System for Safety Management on Industrial Environment 
> **Team AASC(Anywhere Anytime Security with CCTV)** , **Mar. 2024 ~ Jun. 2024**

---

##  Team members
| **Name** | **Role** | **Email** |
|----------|----------|---------|
| **Seungeun Kang** | **Team Leader, AI engineer** | haun620@kyonggi.ac.kr |
| Jiyeon Park | Backend programmer | 202212971@kyonggi.ac.kr |
| Yubin Moon | Backend programmer | mubw00@kyonggi.ac.kr |
| Eunbyeol Park | Backend programmer | si1verstar99@kyonggi.ac.kr |
| Kibum Park | Hardware Engineer | rlqja530@kyonggi.ac.kr |
| Gunwoo Park | Frontend programmer | dbel56@kyonggi.ac.kr |


## Software Stacks
![](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


---

## Project Motivation

### 1. Rasing awareness of safety management
- Serious Accidents Punishment Act, Korean Law ( from 2021 )
<img width="450" alt="스크린샷 2024-06-09 오후 3 17 56" src="https://github.com/user00144/basic_capstone_BELIEVE_ai_server/assets/120700820/b2c422eb-d47a-4d53-84d1-d4812ff9d111">
</br>
- Accidents at industrial sites, construction sites, etc. cause significant loss of life and property damage.

### 2. Problems with existing AI-based safety management systems
- AI inference is executed on “Server”
- Requires high traffic and high performance GPU servers
- We focused on “edge intelligence” technologies

|  | **Warn notification** | **Portable**  | **Using Sensor data** | **Real time inference** | **Edge inference** | **Physical Volume** |
|---|---|---|---|---|---|---|
|Existing tech| yes | yes | yes | yes | **no** | **big** |
| **BELIEVE** | yes | yes | yes | yes | **yes** | **small** |
---

## Implementation

### 1. Overall System
![그림1](https://github.com/user00144/basic_capstone_BELIEVE_ai_server/assets/120700820/239b4676-5706-460e-8993-4a2c4155628e)


### 2. Object Detection Model (Safety Helmet Detection)

- Dataset : Kaggle - Safety Helmet Detection Dataset ([link](https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection))
- Model : Yolo v7 Tiny ([link](https://github.com/WongKinYiu/yolov7))
- Detection From Test dataset
<img width="246" alt="image" src="https://github.com/user00144/basic_capstone_BELIEVE_ai_server/assets/120700820/fc8d76dc-1a29-4fab-9451-22825f1d70ef">

---

## Outputs

### 1. Conference Paper  

- **Publication conference paper** in Korean Institute of Information Technology Summer Conference (May. 2024)
- 🏆 **Best Paper Award(Gold prize)** in Korean Institute of Information Technology Summer Conference (May. 2024)
<img width="450" alt="스크린샷 2024-06-09 오후 3 47 29" src="https://github.com/user00144/basic_capstone_BELIEVE_ai_server/assets/120700820/c3f72c7f-d5a0-49f2-8791-0546d58cc102">
<img width="450" alt="스크린샷 2024-06-09 오후 3 46 46" src="https://github.com/user00144/basic_capstone_BELIEVE_ai_server/assets/120700820/38891db7-c595-4ce6-9c0b-8f2532847739">


### 2. Poster 

- **Poster presentation** in Basic Capstone Design competition, Kyonggi University (Jun. 2024)
- 🏆 **Excellence Award(Gold prize)** in Basic Capstone Design competition, Kyonggi University (Jun. 2024)
<img width="450" alt="poster" src = "https://github.com/user00144/basic_capstone_BELIEVE_ai_server/assets/120700820/a0f11522-3f3f-4535-9a0b-dd56a9ca5459">
