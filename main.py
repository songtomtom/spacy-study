import sys
import spacy

# 커맨드 라인 인자를 확인하여 문장 입력 여부를 검사
if len(sys.argv) < 2:
    print("Usage: python script_name.py <sentence>")
    exit()

# spaCy의 영어 모델을 로드
nlp = spacy.load("en_core_web_sm")

# 커맨드 라인에서 입력받은 문장
sentence = sys.argv[1]

# 문장을 처리
doc = nlp(sentence)

# 출력을 위한 헤더
print(f"{'Token':<15} {'POS':<10}")

# 구분선 출력
print(f"{'-'*15} {'-'*10}")

# 토큰과 품사 태그를 테이블 형태로 출력
for token in doc:
    # SPACE 품사 태그를 가진 토큰은 건너뛰기
    if token.pos_ != "SPACE":
        print(f"{token.text:<15} {token.pos_:<10}")
