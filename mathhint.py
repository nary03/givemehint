pip install pillow pytesseract openai
from PIL import Image
import pytesseract
import openai

# Tesseract OCR 경로 설정 (시스템에 따라 경로가 다를 수 있음)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# OpenAI API 키 설정
openai.api_key = 'YOUR_OPENAI_API_KEY'

def extract_text_from_image(image_path):
    # 이미지 열기
    img = Image.open(image_path)

    # 이미지에서 텍스트 추출
    text = pytesseract.image_to_string(img)
    return text

def get_indirect_hint_from_text(text):
    # GPT-3를 사용하여 간접적인 힌트 생성
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"다음 수학 문제를 기반으로 간접적인 힌트를 생성해줘: {text}",
        max_tokens=50
    )

    # 응답에서 텍스트 추출
    indirect_hint = response.choices[0].text.strip()
    return indirect_hint

def get_direct_hint_from_text(text):
    # GPT-3를 사용하여 직접적인 힌트 생성
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"다음 수학 문제를 기반으로 직접적인 힌트를 생성해줘: {text}",
        max_tokens=50
    )

    # 응답에서 텍스트 추출
    direct_hint = response.choices[0].text.strip()
    return direct_hint

# 메인 함수
def main(image_path):
    extracted_text = extract_text_from_image(image_path)
    indirect_hint = get_indirect_hint_from_text(extracted_text)
    direct_hint = get_direct_hint_from_text(extracted_text)
    print(f"추출된 텍스트: {extracted_text}")
    print(f"간접적인 힌트: {indirect_hint}")
    print(f"직접적인 힌트: {direct_hint}")

# 예시 이미지 경로
image_path = 'example.png'
main(image_path)
