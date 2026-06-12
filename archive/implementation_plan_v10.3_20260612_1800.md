# Localization & Content Alignment Plan (v10.4)

This plan outlines the changes required to localize currency representations across the landing page and all B2B pitch decks, resolve translation inconsistencies, correct version discrepancies (8-stage vs 10-stage), fix a pricing typo, and enhance the visual hover effects with premium glassmorphic/neon glow attributes.

## User Review Required

> [!IMPORTANT]
> **Currency Separation Strategy**: 
> - **Korean (ko)**: Displays ONLY Korean Won (KRW).
> - **Japanese (ja)**: Displays ONLY Japanese Yen (JPY).
> - **English (en)**: Displays ONLY US Dollars (USD).
>
> **Design Polish**:
> - We will enhance `.card-spec`, `.deck-card`, and `.seal-stamp` with dynamic transitions and glowing border effects to elevate B2B visual appeal.

## Open Questions
- None. All key decisions have been aligned during the `/grill-me` session.

## Proposed Changes

We will systematically update `index.html`, `pr_launch_copy.md`, and all HTML slide decks inside `slides/`.

---

### [Component: slm-landing-web]

#### [MODIFY] [index.html](file:///e:/진짜배기/slm-landing-web/index.html)
- Update dynamic JavaScript `tableBody.innerHTML` rendering under `switchLang(lang)`:
  - English (`en`): Change `JPY 2,500,000 / KRW 25,000,000` to `USD 25,000` (and `Enjoy USD 5,000 special bundle discount!`).
  - Korean (`ko`): Change `JPY 2,500,000 / KRW 2,500만 원` to `KRW 2,500만 원` (and `일괄 계약 시 500만 원 특별 결합 할인!`).
  - Update option pricing in tables to represent only their respective currencies.

#### [MODIFY] [pr_launch_copy.md](file:///e:/진짜배기/slm-landing-web/pr_launch_copy.md)
- Fix the Korean pricing typo for Healer OS: change `힐러 OS(80만 원)` to `힐러 OS(800만 원)` in line 26.
- Separate currency representations strictly (USD in section 3, KRW in section 1, JPY in section 2).

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
- **Currency Clean-up**: Update `i18n` objects for `ko`, `ja`, and `en` to show single currency values:
  - `ko`: Show Won (`KRW 1,200만 원`, `KRW 2,500만 원` etc.)
  - `ja`: Show Yen (`JPY 1,200,000 (120万円)`, `JPY 2,500,000 (250万円)` etc.)
  - `en`: Show Dollars (`USD 12,000`, `USD 25,000` etc.)
- **Translation Polish**: Clean up mixed Korean sentences within `ja` blocks:
  - Translate `(個人정보보호 이중마스크 및 물리 복제방지 락 기본 무상 탑재)` to `(個人情報保護二重マスク及び物理コピー防止ロック基本無償搭載)`.
  - Translate `500만ウォン` to `50万円`.
  - Translate `社내Wiki 자동 연동 노션 커넥터` to `社内Wiki自動連携ノーションコネクタ`.
- **Integrity Pipeline Alignment**: 
  - Change "8단계" to "10단계" in `slides_all_in_one.html` and `slides_all_in_one_tech.html`.
- **Visual Enhancement**:
  - Add premium glowing border transition on hover to `.card-spec` and `.seal-stamp` elements.

---

## Verification Plan

### Manual Verification
- Run the local server via `run_server.bat` (or open files directly in a browser subagent).
- Verify toggling KO/JA/EN correctly updates the pricing table to single-currency values.
- Verify opening the slides shows single-currency prices matching the language configuration.
- Check hover states on cards and technical guarantee seal stamp to verify the glowing transition.
