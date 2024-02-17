`Django`  
<h2>Django-ninja</h2>

- 장고에서 동작하는 서드파티 패키지
- FAST API와 같은 구문 사용
- 많은 기능을 모두 제공하는 DRF와 달리, 빠르고 간단한 인터페이스를 제공함
- RESTful API 구축에 필요한 필수 기능에 중점을 두어 가볍고 빠르다!
- 성능이 우선시 되는 업무는 Django-ninja 사용, 다만 프로젝트가 커지면 개발해야 할 것들이 많아서 생산성이 내려감

<h3>FastAPI</h3>
파이썬으로 API를 빌드하기 위한 프레임워크

- Node.js, Go와 비슷한 수준으로 빠른 성능
- 개발 속도가 빨라짐
- 코드 버그가 감소
- 쉽게 사용

FastAPI는 web micro framework인 Starletter를 사용 (Flask, Django 등과 비교하면 가볍고 강력한 ASGI 프레임워크/툴킷)
- FastAPI는 Starlettte를 한번 감싸기 때문에 성능이 조금 떨어지지만,FastAPI의 장점은 이 모든 것을 상쇄
- Starlette는 내부적으로 uvicorn을 사용하기 때문에 강력한 성능 보장
  - uvicorn은 uvloops와 httptools를 사용하는 초고속 ASGI 서버, uvloop의 성능 비밀은 libuv과 Cython에 있음
