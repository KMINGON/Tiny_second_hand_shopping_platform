# Tiny Second-hand Shopping Platform

안전하고 편리한 중고거래를 위한 웹 플랫폼입니다.

## 주요 기능

- 상품 등록 및 관리
- 실시간 채팅 기능
- 사용자 인증 및 권한 관리
- 상품 검색 및 필터링
- 신고 시스템

## 프로젝트 구조

```
tiny_second_hand_shopping_platform/
├── accounts/          # 사용자 인증 및 계정 관리
├── chat/             # 실시간 채팅 기능
├── core/             # 핵심 기능 및 설정
├── market/           # 프로젝트 메인 설정
├── products/         # 상품 관련 기능
├── reports/          # 신고 시스템
├── static/           # 정적 파일 (CSS, JS, 이미지)
├── staticfiles/      # 수집된 정적 파일
├── templates/        # HTML 템플릿
└── media/            # 사용자가 업로드한 파일
```

## 기술 스택

- Python 3.12
- Django 5.0
- SQLite3
- Bootstrap 5
- Font Awesome

## 설치 및 실행 방법

1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
.\venv\Scripts\activate  # Windows
```

2. 의존성 설치
```bash
pip install -r requirements.txt
```

3. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

4. 개발 서버 실행
```bash
python DJANGO_SETTINGS_MODULE=market.settings daphne market.asgi:application
```

## URL 매핑

- 메인 페이지: `/`
- 상품 관련:
  - 상품 목록: `/products/`
  - 상품 상세: `/products/<int:pk>/`
  - 상품 등록: `/products/create/`
  - 상품 수정: `/products/<int:pk>/edit/`
  - 상품 삭제: `/products/<int:pk>/delete/`
- 계정 관련:
  - 로그인: `/accounts/login/`
  - 회원가입: `/accounts/signup/`
  - 로그아웃: `/accounts/logout/`
  - 프로필: `/accounts/profile/`
- 채팅 관련:
  - 채팅 목록: `/chat/`
  - 채팅방: `/chat/<int:room_id>/`
- 신고 관련:
  - 신고하기: `/reports/create/`
  - 신고 목록: `/reports/`

## 📌 프로젝트 주요 기능 (Tiny Second-hand Shopping Platform)

### 🧑‍💼 회원 기능
- **회원가입 / 로그인 / 로그아웃**  
  사용자 인증 및 계정 생성 기능
- **마이페이지**  
  자기소개글 및 비밀번호 변경 가능
- **중복 아이디 방지**  
  중복 아이디 체크 기능 포함

---

### 📦 상품 기능
- **상품 등록**  
  이름, 설명, 가격, 이미지 포함하여 등록 가능
- **상품 조회 및 상세 페이지**  
  전체 상품 목록 확인 및 개별 상품 정보 확인
- **상품 검색 및 필터링**  
  키워드 기반 검색, 가격 범위/카테고리 필터링 기능
- **찜하기 기능**  
  즐겨찾기 등록/해제 가능
- **다중 이미지 업로드**  
  상품별 여러 이미지 업로드 지원
- **상품 거래 상태 표시**  
  예약 중 / 거래 중 / 거래 완료 상태 구분

---

### 💬 실시간 채팅 기능
- **전체 채팅방**  
  모든 사용자 간 실시간 채팅 가능
- **1:1 채팅방**  
  사용자 간 1:1 실시간 채팅 기능
- **채팅 메시지 신고 기능**  
  부적절한 메시지에 대한 신고 기능

---

### 🚨 신고 및 제재 기능
- **신고 기능**  
  사용자 및 상품 신고 가능 (신고 사유 필수)
- **자동 제재 시스템**  
  일정 횟수 이상 신고된 경우:
  - 상품은 자동 삭제
  - 사용자는 자동 휴면 상태 처리

---

### 🔐 관리자 기능
- **관리자 페이지**  
  유저, 상품, 신고 내역 전체 관리 가능  
  (접근 제한 적용)

---

### 🛡 보안 기능
- **입력값 유효성 검증**  
  XSS, SQL Injection 등 방지
- **CSRF 보호**  
  모든 POST 요청에 CSRF 토큰 적용
- **세션/쿠키 보안 강화**  
  HTTPOnly, Secure 속성 적용
- **파일 업로드 제한**  
  허용 확장자 및 용량 제한 설정 (.jpg, .png 등)

---


## 개발 환경 설정

1. `.env` 파일 생성
```bash
cp .env.example .env
```

2. 환경 변수 설정
```
DEBUG=True
SECRET_KEY=your-secret-key
```

## 기여 방법

1. 이슈 생성
2. 브랜치 생성
3. 코드 수정
4. Pull Request 생성

## 라이센스

MIT License
