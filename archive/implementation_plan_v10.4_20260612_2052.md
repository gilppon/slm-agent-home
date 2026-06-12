# Localization & Content Alignment Plan (v10.4)

| 버전 (Ver.) | 기록 일시 (DateTime) | 작성자 (Author) | 결재 상태 (Status) | 핵심 지시 및 변경 내용 (Key Directives) |
|---|---|---|---|---|
| v10.3 | 2026-06-12 17:40 | 개발부장 코다리 | 🟡 검토 대기 | 기초 1차 시안 작성 및 로컬라이즈 정적 뼈대 설계 |
| v10.4 | 2026-06-12 18:00 | 개발부장 코다리 | 🟢 승인 완료 | grill-me 인터뷰 완료. 단일 통화화, 일본어 블록 내 한글 잔재(500만원 등) 완전 소거, 10단계 검증 파이프라인 일괄 상향 및 var(--primary) 네온 글로우 테마 승인 반영 |

This plan outlines the changes required to localize currency representations across the landing page and all B2B pitch decks, resolve translation inconsistencies, correct version discrepancies (8-stage vs 10-stage), fix a pricing typo, and enhance the visual hover effects with premium glassmorphic/neon glow attributes.

## User Review Required

> [!IMPORTANT]
> **Approved Currency Separation Strategy**: 
> - **Korean (ko)**: Displays ONLY Korean Won (KRW).
> - **Japanese (ja)**: Displays ONLY Japanese Yen (JPY).
> - **English (en)**: Displays ONLY US Dollars (USD).
> - Clean up mixed Korean sentences within `ja` blocks: `500만원` -> `50万円`, `300만원` -> `30万円`, `社내` -> `社내` (should be `社内`), `일본 로컬 특허/특상법 법제 팩` -> `日本ローカル商取引・特許完全対応法制パック`.
>
> **Approved Design Polish**:
> - We will enhance `.card-spec` and `.seal-stamp` with dynamic transitions and neon glowing border effects on hover using `var(--primary)` color.
>
> **Approved Verification Alignment**:
> - Change "8단계" to "10단계" (or "8-stage" to "10-stage") for E2E validation pipeline consistency.

## Proposed Changes

We will systematically update `index.html`, `pr_launch_copy.md`, and all HTML slide decks inside `slides/`.

---

### [Component: slm-landing-web]

#### [MODIFY] [index.html](file:///e:/진짜배기/slm-landing-web/index.html)
- Already modified to separate currencies.

#### [MODIFY] [pr_launch_copy.md](file:///e:/진짜배기/slm-landing-web/pr_launch_copy.md)
- Already modified. Fix Healer OS KRW typo and separate currency descriptions.

---

### [Component: slm-landing-web/slides]

For all 9 slide files:
1. [slides_all_in_one.html](file:///e:/진짜배기/slm-landing-web/slides/slides_all_in_one.html)
2. [slides_all_in_one_tech.html](file:///e:/진짜배기/slm-landing-web/slides/slides_all_in_one_tech.html)
3. [slides_corps1_builder.html](file:///e:/진짜배기/slm-landing-web/slides/slides_corps1_builder.html)
4. [slides_corps1_builder_tech.html](file:///e:/진짜배기/slm-landing-web/slides/slides_corps1_builder_tech.html)
5. [slides_corps2_agent.html](file:///e:/진짜배기/slm-landing-web/slides/slides_corps2_agent.html)
6. [slides_corps2_agent_tech.html](file:///e:/진짜배기/slm-landing-web/slides/slides_corps2_agent_tech.html)
7. [slides_corps3_healer.html](file:///e:/진짜배기/slm-landing-web/slides/slides_corps3_healer.html)
8. [slides_corps3_healer_tech.html](file:///e:/진짜배기/slm-landing-web/slides/slides_corps3_healer_tech.html)
9. [slides_network_connection.html](file:///e:/진짜배기/slm-landing-web/slides/slides_network_connection.html)

#### Updates per file:
- **Currency Clean-up**: Update `i18n` objects for `ko`, `ja`, and `en` to show single currency values.
- **Translation Polish**: Clean up mixed Korean sentences within `ja` blocks:
  - Translate `(個人정보보호 이중마스크 및 물리 복제방지 락 기본 무상 탑재)` to `(個人情報保護二重マスク及び物理コピー防止ロック基本無償搭載)`.
  - Translate `500만원의 특별셋트할인` / `500만월` / `500만` / `500만원` to `50万円の特別セット割引` / `50万円`.
  - Translate `300만원` / `300만` to `30万円`.
  - Translate `1200만`, `1000만`, `800만` etc. to corresponding JPY万円 inside Japanese block.
  - Fix any mixed strings in `tb_row1`, `tb_row2`, `tb_row3`.
- **Integrity Pipeline Alignment**: 
  - Change "8단계" to "10단계" across all occurrences.
- **Visual Enhancement**:
  - Add premium glowing border transition on hover to `.card-spec` and `.seal-stamp` elements.

---

## Verification Plan

### Manual Verification
- Run the local server via `run_server.bat` (or open files directly in a browser subagent).
- Verify toggling KO/JA/EN correctly updates the pricing table to single-currency values.
- Verify opening the slides shows single-currency prices matching the language configuration.
- Check hover states on cards and technical guarantee seal stamp to verify the glowing transition.
