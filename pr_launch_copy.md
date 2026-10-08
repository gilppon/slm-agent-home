# KODARI Local AI — 검증 단계 평가 자료

> **검증 단계 초안 — 정식 판매·외부 공개 승인 전.** 제품, 보안, 법무, 영업 검토와 실제 문의 경로 확인이 필요합니다. 이 문서는 `E:\진짜배기\slm-agent\docs\b2b_sales\PRODUCT_CURRENT_STATUS.md` (reviewed 2026-10-08).

## 현재 허용 가능한 설명 초안

KODARI is validating a Windows x64 portable local-AI build with Ed25519-signed, device-bound license tokens. Customer hardware compatibility, model workflows, network-egress behavior, and production support are still being tested. Any evaluation must define its hardware, data, network, duration, and acceptance criteria in advance.

## Korean

### A안 — 업무 환경 검증

> 사내 문서 업무에 로컬 AI를 적용할 수 있을까요? KODARI는 Windows x64 포터블 빌드의 장비 호환성과 모델 워크플로를 검증하고 있습니다. 평가를 논의할 때는 대상 장비, 데이터 처리, 네트워크 정책과 합격 기준을 먼저 정합니다.

### B안 — 라이선스와 운영 통제

> 라이선스는 어떻게 특정 장비에 연결되나요? KODARI 검증 빌드는 Ed25519 서명 및 장치 식별값에 바인딩된 라이선스 토큰을 확인합니다. 이는 소프트웨어 라이선스 통제이며 변조 방지 하드웨어 DRM은 아닙니다.

> **CTA:** 제한 평가 범위 협의 — 실제 연락처와 문의 접수 경로가 운영 검증되기 전에는 신청·회신을 약속하지 않습니다.

## 日本語

### A案 — 業務環境での検証

> 社内文書業務にローカルAIを適用できるでしょうか。KODARIはWindows x64ポータブルビルドの機器互換性とモデルのワークフローを検証しています。評価を検討する際は、対象機器、データの取扱い、ネットワーク方針、合格基準を事前に定めます。

### B案 — ライセンスと運用管理

> ライセンスはどのように特定の機器に紐づくのでしょうか。KODARIの検証ビルドは、Ed25519署名とデバイス識別子に紐づいたライセンストークンを検証します。これはソフトウェア上のライセンス制御であり、改変を防ぐハードウェアDRMではありません。

> **CTA:** 限定評価の範囲を相談 — 実際の連絡先と問い合わせ受付経路の運用確認前に、申込みや返信を約束しません。

## English

### A — Validate a real workflow

> Could local AI support your document workflow? KODARI is validating hardware compatibility and model workflows for a Windows x64 portable build. Any evaluation starts by agreeing on the target device, data handling, network policy, and acceptance criteria.

### B — Understand device-bound licensing

> How is a license tied to a device? The KODARI validation build checks Ed25519-signed license tokens bound to a device identifier. This is software licensing control, not tamper-proof hardware DRM.

> **CTA:** Discuss a scoped evaluation — do not promise an application or response until a real contact and intake path are operationally verified.

## 근거와 승인이 생길 때까지 사용하지 않을 주장

- Air-gap certification, zero egress, zero leakage, or absolute security guarantees.
- Fixed prices, free trials, savings, ROI, or break-even periods.
- Customer-ready performance, supported GPU/OS matrix, installation time, or production support SLA.
- PII masking, automatic knowledge deletion, perfect answer quality, or completed audit/test claims.
- Copy-proof or tamper-proof device licensing, automatic online sales, or guaranteed inquiry response time.
