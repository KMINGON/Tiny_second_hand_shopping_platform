# Tiny_second_hand_shopping_platform
WHS 시큐어 코딩 과제

# 🛍️ Tiny Second-hand Shopping Platform

Django 기반의 시큐어코딩 실습형 중고거래 플랫폼입니다.  
기능별 앱 분리 및 보안 요소 반영을 통해 실제 서비스 수준의 구조를 갖춘 웹 애플리케이션을 목표로 합니다.

---

# 🧱 프로젝트 폴더 구조 (Tree)

```

tiny_second_hand_shopping_platform/
├── accounts/        사용자 인증 (회원가입, 로그인, 마이페이지 등)
├── products/        상품 등록, 조회, 상세보기 기능
├── chat/            전체 채팅, 1:1 채팅 기능
├── reports/         사용자 및 상품 신고 기능
├── core/            메인 홈, 공통 페이지
├── market/          Django 프로젝트 설정 (settings, urls 등)
├── templates/       HTML 템플릿
│   ├── index.html
│   ├── accounts/
│   ├── products/
│   ├── chat/
│   ├── reports/ 
├── static/          CSS, JS 등 정적 파일
├── media/           업로드 이미지 저장소
├── db.sqlite3       SQLite 데이터베이스
├── manage.py        Django 명령어 실행 파일
└── venv/            가상환경 디렉토리 (보통 .gitignore 대상)

```
---

## 🔗 URL → View → Template 매핑

| URL 경로 | View 함수 | 템플릿 파일 | 설명 |
|----------|-----------|--------------|------|
| `/` | `core.views.index_view` | `templates/index.html` | 메인 홈화면 |
| `/accounts/signup/` | `accounts.views.signup_view` | `accounts/signup.html` | 회원가입 |
| `/accounts/login/` | `accounts.views.login_view` | `accounts/login.html` | 로그인 |
| `/accounts/logout/` | `accounts.views.logout_view` | `accounts/logout.html` | 로그아웃 |
| `/accounts/mypage/` | `accounts.views.mypage_view` | `accounts/mypage.html` | 마이페이지 |
| `/products/` | `products.views.product_list_view` | `products/list.html` | 상품 목록 |
| `/products/new/` | `products.views.product_create_view` | `products/create.html` | 상품 등록 |
| `/products/<id>/` | `products.views.product_detail_view` | `products/detail.html` | 상품 상세 |
| `/chat/global/` | `chat.views.global_chat_view` | `chat/global.html` | 전체 채팅방 |
| `/chat/user/<id>/` | `chat.views.private_chat_view` | `chat/private.html` | 1:1 채팅 |
| `/reports/` | `reports.views.report_create_view` | `reports/create.html` | 신고 페이지 |

---

## 🧩 앱별 역할 및 의존성

| 앱 | 기능 | 주요 역할 |
|----|------|-----------|
| `accounts` | 사용자 인증 | 회원가입, 로그인, 마이페이지, 세션 |
| `products` | 상품 관리 | DB 모델, 업로드 이미지, 상태관리 |
| `chat` | 실시간 채팅 | 전체 채팅방, 1:1 채팅 구조 |
| `reports` | 신고 시스템 | 유저/상품 신고 처리, 제재 로직 |
| `core` | 공용 뷰 | 홈페이지(index), 관리자 화면 등 |
| `market` | 프로젝트 설정 | `settings.py`, `urls.py`, 앱 등록 등 |

---

## ✅ 개발 체크포인트

- [x] Django 프로젝트 및 앱 구조 설정
- [x] URL 라우팅 및 템플릿 연결
- [x] `index.html` 연결 성공
- [ ] 기능별 View/Model/Template 구성
- [ ] 보안 요소 반영 (CSRF, XSS, 인증, 파일 업로드 제한 등)
- [ ] 관리자 페이지 설정

---

## 📌 실행 방법

```bash
# 1. 가상환경 실행
source venv/bin/activate

# 2. 서버 실행
python manage.py runserver
접속 주소: http://127.0.0.1:8000
