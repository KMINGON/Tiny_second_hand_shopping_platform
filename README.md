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

## 주요 기능 설명

### 상품 관리
- 상품 등록, 수정, 삭제 기능
- 상품 이미지 업로드
- 상품 상태 관리 (판매중, 예약중, 판매완료)
- 상품 검색 및 필터링

### 실시간 채팅
- 판매자와 구매자 간의 실시간 채팅
- 채팅방 목록 관리
- 읽지 않은 메시지 알림

### 사용자 관리
- 회원가입 및 로그인
- 프로필 관리
- 권한에 따른 기능 제한

### 신고 시스템
- 부적절한 상품 신고
- 부적절한 사용자 신고
- 신고 처리 상태 관리

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
