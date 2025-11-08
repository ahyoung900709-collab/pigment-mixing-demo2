# 🎨 Practical Pigment Mixing for Digital Painting – 실행 재현 및 실습 보고서
> 성균관대학교 스마트팩토리융합학과  
> **박아영 / 오픈소스 분석 개인과제**

---

## 📘 1️⃣ 프로젝트 개요
- **논문명:** *Practical Pigment Mixing for Digital Painting* (ACM TOG, 2021)  
- **저자:** Šárka Sochorová, Ondřej Jamriška  
- **공개 저장소:** [scrtwpns/pigment-mixing](https://github.com/scrtwpns/pigment-mixing)  
- **핵심 목표:**  
  기존 RGB 기반 디지털 페인팅의 비현실적인 색 혼합 문제(빛의 가산혼합)를 해결하기 위해  
  **Kubelka–Munk(K–M)** 모델을 **RGB 워크플로우**에 통합한 물리 기반 색 혼합 시스템 구현  

---

## ⚙️ 2️⃣ 실습 환경 구성
| 항목 | 내용 |
|------|------|
| OS | Windows 11 Pro |
| Python | 3.10 (Anaconda 환경) |
| GPU | RTX 3060 Laptop GPU |
| IDE | VSCode / Jupyter Notebook |
| 주요 라이브러리 | `numpy`, `scipy`, `matplotlib`, `PyQt5`, `opencv-python` |

### ▶ 설치 및 실행
```bash
# 1. 오픈소스 클론
git clone https://github.com/scrtwpns/pigment-mixing.git
cd pigment-mixing/core

# 2. 가상환경 생성 및 활성화
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate    # macOS/Linux

# 3. 필수 라이브러리 설치
pip install numpy scipy matplotlib PyQt5 opencv-python

# 4. LUT(룩업테이블) 생성
python lut_builder.py



---

#### 2️⃣ 저장소 설명(About 섹션) 작성
→ GitHub 우측 상단의 ⚙️ **“Edit” 버튼 클릭**  
다음 문장을 입력하세요:



---

#### 3️⃣ (선택) `requirements.txt` 생성
다른 PC에서도 재현 가능하게 하려면 PowerShell에서 아래 실행:
```powershell
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add requirements.txt"
git push
