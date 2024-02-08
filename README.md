이 프로젝트는 spaCy를 활용하여 텍스트의 품사(POS)를 태깅하는 방법을 보여줍니다.

## 시작하기 전에
이 프로젝트를 실행하기 전에 Python이 설치되어 있어야 합니다. Python의 설치 여부는 터미널에서 `python --version` 또는 `python3 --version`을 실행하여 확인할 수 있습니다.

### 필요 조건
이 프로젝트를 실행하기 위해서는 다음이 필요합니다:

- Python 3.6 이상
- pip (Python 패키지 관리자)

### 설치
1. 프로젝트 클론
먼저 GitHub 또는 다른 Git 호스팅 서비스에서 프로젝트를 클론하세요.

```bash
git@github.com:songtomtom/spacy-study.git
cd spacy-study
````
2. 의존성 설치

프로젝트 의존성을 설치하기 위해 다음 단계를 따르세요:


```bash
pip install -r requirements.txt
```

3. 영어 모델 다운로드

spaCy의 기능을 사용하기 위해서는 영어 모델을 다운로드해야 합니다. 다음 명령어를 실행하세요:

```bash
python -m spacy download en_core_web_sm
```

## 사용 방법

이 프로젝트를 사용하여 문장의 품사를 태깅하려면, 커맨드 라인에서 다음과 같이 실행하세요:

```bash
python main.py "여기에 분석할 문장을 입력하세요."
```
예를 들어, "Apple is looking at buying U.K. startup for $1 billion" 문장의 품사를 태깅하려면 다음과 같이 입력합니다:

```bash
python main.py "Apple is looking at buying U.K. startup for $1 billion"
```

