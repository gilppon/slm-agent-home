@echo off
title KODARI SYSTEMS - Local Web Server
echo ==========================================================
echo  [KODARI SYSTEMS] Trinity RAG OS Suite 로컬 서버 구동기
echo ==========================================================
echo   * URL: http://localhost:8080
echo   * 로컬 브라우저 보안 경고(CORS) 방지 및 완벽한 다국어 전환 테스트
echo   * 구동을 종료하려면 이 창에서 Ctrl+C를 누르십시오.
echo ==========================================================
echo.
echo  [INFO] 기본 웹 브라우저로 접속을 시도합니다...
start http://localhost:8080
echo.
echo  [START] 파이썬 내장 웹 서버 기동 중...
python -m http.server 8080
pause
