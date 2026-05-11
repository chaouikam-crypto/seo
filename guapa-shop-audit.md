# SEO / GEO / AEO Full Audit — guapa-shop.com
**Date:** 2026-05-11  
**Auditor:** Claude (AI-assisted audit via web research)  
**Scope:** Full SEO + GEO (Generative Engine Optimization) + AEO (Answer Engine Optimization)

---

## Executive Summary

guapa-shop.com is a French clean-beauty e-commerce brand selling vegan body care products (brumes parfumées, huiles sèches, gommages, laits corps) across three fragrance collections: **BAILA CONMIGO** (Vanille Caramel), **AMOR SECRETO** (Thé Vert & Mandarine), and **BESO CALIENTE** (Musc Blanc). The brand has strong product differentiation (Grasse perfumers, vegan, made-in-France) but is significantly under-optimized across all three pillars—SEO, GEO, and AEO. The most critical issues are a dangerously thin Google index (only ~4 pages indexed), a dual-platform URL crisis likely caused by an incomplete migration from PrestaShop to Shopify, a generic one-word page title, and near-zero entity presence for AI-driven search engines.

**Priority Score:**  
- Technical SEO: 🔴 Critical  
- On-Page SEO: 🟠 Serious  
- Off-Page SEO: 🟠 Serious  
- GEO: 🔴 Critical  
- AEO: 🔴 Critical  

---

## 1. TECHNICAL SEO

### 1.1 Platform & URL Structure — 🔴 CRITICAL

**Issue: Dual-Platform URL Leak**

Google's index simultaneously contains:
- `https://guapa-shop.com/collections/all` → Shopify-style URL
- `http://guapa-shop.com/index.php` → PrestaShop root URL
- `https://guapa-shop.com/index.php?controller=manufacturer&id_manufacturer=24` → PrestaShop brand/manufacturer page

This is the signature of an **incomplete platform migration** (PrestaShop → Shopify) where:
1. Old PrestaShop URLs were never redirected (301) to their new Shopify equivalents.
2. Google still indexes and crawls the old PrestaShop URL tree, wasting crawl budget and splitting link equity.
3. The HTTP version of the old root URL (`http://guapa-shop.com/index.php`) is indexed without HTTPS—a ranking signal penalty.

**Actions Required:**
- Audit all PrestaShop URLs still in Google Search Console (GSC).
- Create 301 redirects for every old PrestaShop URL to its canonical Shopify equivalent.
- If PrestaShop is no longer live, return 410 (Gone) for orphaned pages with no Shopify equivalent.
- Submit updated sitemap after redirect implementation.
- Monitor via GSC's Coverage report until old URLs drop from index.

---

### 1.2 Index Coverage — 🔴 CRITICAL

**Finding:** Google indexes approximately **4 pages** for guapa-shop.com (homepage, /index.php, /collections/all, one manufacturer page). For a multi-collection beauty e-commerce site, this is catastrophically low.

**Root causes (likely):**
- Product and collection pages may be blocked by `robots.txt` (unverified — site returned 403 during audit).
- Individual product pages may have `noindex` set (common mistake during PrestaShop-to-Shopify migrations).
- `sitemap.xml` may be absent, malformed, or listing non-canonical URLs.
- Canonical tags may be mis-pointing, causing Google to defer to a preferred URL that it then doesn't index.

**Actions Required:**
- Verify `robots.txt`: ensure Googlebot is not blocked from `/collections/`, `/products/`, or other Shopify paths.
- Verify `sitemap.xml` exists at `guapa-shop.com/sitemap.xml` and is submitted to GSC.
- Audit canonical tags on all product and collection pages.
- Check for `noindex` directives on product pages (common in Shopify themes for variant pages).
- Set up Google Search Console if not already done; request indexing for key pages.

---

### 1.3 HTTPS & HTTP — 🟠 Serious

**Finding:** The old PrestaShop URL `http://guapa-shop.com/index.php` (HTTP, not HTTPS) is indexed by Google. If non-HTTPS URLs are accessible rather than redirecting, this hurts trust signals and rankings.

**Actions Required:**
- Ensure all HTTP requests redirect 301 to HTTPS.
- Add HSTS header if not already present.

---

### 1.4 robots.txt & sitemap.xml — 🔴 Unverifiable (site blocking crawlers)

**Finding:** The site returned HTTP 403 Forbidden for all direct fetch attempts during this audit—including `guapa-shop.com/robots.txt` and `guapa-shop.com/sitemap.xml`. This is either:
- A WAF/CDN blocking non-browser user agents (Cloudflare, etc.).
- An incorrectly configured access rule that may **also be blocking Googlebot**.

**Actions Required:**
- Check server/CDN access logs for Googlebot user-agent hits. If Googlebot is being 403'd, organic traffic will collapse.
- Whitelist Googlebot's IP ranges in WAF rules.
- Verify in GSC under Settings > Crawl Stats that Google is successfully crawling pages.
- Ensure `sitemap.xml` is accessible and submitted in GSC.

---

### 1.5 Core Web Vitals — 🟡 Unknown (manual check required)

**Note:** Direct performance measurement was not possible during this audit. The beauty e-commerce category is competitive for CWV (Google tightened LCP threshold to 2.0s in March 2026).

**Actions Required:**
- Run Google PageSpeed Insights on homepage and key product pages.
- Targets: LCP < 2.0s, INP < 200ms, CLS < 0.1.
- Common Shopify issues to check: unoptimized hero images (LCP), large JavaScript bundles (INP), image/layout shifts (CLS).
- Use lazy loading for below-fold images; compress hero images to WebP.

---

### 1.6 Structured Data / Schema Markup — 🔴 Critical (likely missing)

**Finding:** No structured data was confirmed on any indexed page. For an e-commerce site, absence of schema markup means:
- No Product rich results (star ratings, price, availability) in SERPs.
- No Breadcrumb trails in search results.
- No eligibility for Google Merchant Center free listings.

**Required Schema Types:**
| Page Type | Schema Required |
|-----------|----------------|
| Homepage | `Organization`, `WebSite` (with SearchAction) |
| Product pages | `Product` (with `offers`, `aggregateRating`, `brand`) |
| Collection pages | `CollectionPage`, `BreadcrumbList` |
| About/Story page | `AboutPage`, `Organization` |
| FAQ (if added) | `FAQPage` |

**Actions Required:**
- Add `Organization` schema to homepage with: `name`, `url`, `logo`, `sameAs` (Instagram, Trustpilot, Facebook).
- Add `Product` schema to every product page with `offers` (price, currency, availability), `brand`, `description`, and `aggregateRating` (fed from Trustpilot or on-site reviews).
- Add `BreadcrumbList` schema to collection and product pages.
- Validate with Google's Rich Results Test after implementation.

---

## 2. ON-PAGE SEO

### 2.1 Page Title — 🔴 Critical

**Current title:** `Guapa`

This is a single-word, generic title with zero SEO value. It:
- Contains no target keywords.
- Provides no context to search engines or users.
- Will rank for nothing except branded queries.

**Recommended title (homepage):**
```
Guapa | Soins Corps Vegan & Clean Beauty Made in France
```
Or (English-first alternative):
```
Guapa | Vegan Body Care & Clean Beauty — Made in France
```

**Title formula for key pages:**
- Collection: `[Collection Name] | Soins Corps [Scent] — Guapa`
- Product: `[Product Name] [Size] | [Collection] — Guapa`
- About: `Notre Histoire | Beauté Vegan & Rituels Sensoriels — Guapa`

**Actions Required:**
- Rewrite homepage title to include: brand name + product category + key differentiators (vegan, clean, France).
- Audit and rewrite titles for all product and collection pages using the formula above.
- Keep titles under 60 characters to avoid truncation in SERPs.

---

### 2.2 Meta Descriptions — 🟠 Serious (likely missing or auto-generated)

No custom meta description was confirmed. Search snippets showed auto-extracted body text ("reinvents beauty routine into a sunny sensory ritual"), which is good brand copy but not optimized for click-through rate.

**Recommended homepage meta description:**
```
Découvrez Guapa, la marque de soins corps vegan et clean, formulée avec des parfumeurs de Grasse. Rituels sensoriels en 3 collections : Vanille Caramel, Thé Vert & Musc Blanc. Livraison France & international.
```
(~160 characters)

**Actions Required:**
- Write custom meta descriptions for all pages: homepage, each collection, each product, about page.
- Include 1–2 keywords + a CTA (e.g., "Découvrez", "Commandez", "Livraison mondiale").
- Keep under 155–160 characters.

---

### 2.3 Heading Structure (H1–H6) — 🟡 Unknown (cannot verify due to 403)

**Best practices to verify:**
- Homepage should have exactly **one H1** clearly stating the brand proposition.
- Product pages: H1 = product name; H2 = section titles (Description, Ingredients, How to Use).
- Collection pages: H1 = collection name; H2 = product listing subheadings.

---

### 2.4 Content Depth & Keyword Targeting — 🟠 Serious

**Finding:** Product and collection content appears minimal based on search engine snippets. The beauty e-commerce category requires rich, keyword-rich content to compete organically.

**Missing content assets:**
- Ingredient glossaries (e.g., "Huile de Macadamia — bienfaits pour la peau").
- How-to-use / ritual guides per collection.
- "Why vegan?" / "Why clean?" educational pages.
- A blog (currently not detected in indexed pages).

**Target keywords to incorporate (French market):**
- `soins corps vegan france`
- `clean beauty france`
- `brume parfumée corps vegan`
- `lait corps vegan`
- `gommage corps naturel`
- `coffret beauté vegan cadeau`
- `parfumeurs grasse cosmétiques`

**Target keywords (English/international):**
- `vegan body care france`
- `clean beauty gifts french`
- `french vegan body mist`

---

### 2.5 Image Optimization — 🟡 Unknown

**Actions Required:**
- Verify all product images have descriptive `alt` attributes (e.g., `alt="Brume parfumée corps Amor Secreto thé vert mandarine 100ml — Guapa"`).
- Serve images in WebP format.
- Use descriptive file names (e.g., `amor-secreto-body-mist-guapa.webp`, not `IMG_1234.jpg`).

---

### 2.6 Internal Linking — 🟠 Serious

**Likely issues:**
- No blog = no internal link engine.
- Product cross-links within collections may be absent.

**Actions Required:**
- Add "Complete the Ritual" cross-link sections on product pages (linking scrub → body milk → mist in same collection).
- Add contextual links from homepage brand story to collection pages.
- Implement breadcrumbs on all product and collection pages.

---

## 3. OFF-PAGE SEO

### 3.1 Backlink Profile — 🟠 Serious (inferred)

**Finding:** The site has extremely limited press coverage and external mentions specific to guapa-shop.com. Only one external reference found (bibaconceptstore.pt selling Guapa products). No dedicated press articles, beauty blog features, or influencer mentions were found linking to the domain.

**Actions Required:**
- **PR Outreach:** Target French clean beauty blogs (Do It In Paris, Madame Figaro Beauté, Marie Claire Beauté, Glamour FR) for product reviews and brand features.
- **Influencer seeding:** Send press kits to micro-influencers (10K–100K followers) in the French and Portuguese clean beauty niches.
- **Wholesale/retailer partnerships:** Encourage retail stockists (like bibaconceptstore.pt) to link back to guapa-shop.com from their product pages.
- **Submit to clean beauty directories:** Officialveganshop.com, naturkosmetik.de, cosmos-organic directories.

### 3.2 Brand Mentions & Trustpilot — 🟢 Positive Signal

**Finding:** Trustpilot score is 4.7/5 from 29 reviews. This is a positive trust signal.

**Actions Required:**
- Add Trustpilot reviews widget or star badge to homepage and product pages.
- Add `aggregateRating` schema using Trustpilot data (or migrate to on-site reviews for richer schema control).
- Proactively ask customers for Trustpilot reviews post-purchase via email.

---

## 4. GEO — Generative Engine Optimization

GEO concerns how well a brand is represented in AI-generated answers from tools like ChatGPT, Claude, Gemini, Perplexity, and AI Overviews in Google Search.

### 4.1 Entity Recognition — 🔴 Critical

**Finding:** "Guapa" as a brand entity is extremely difficult for AI models to disambiguate. The query space contains:
- `guapa-shop.com` (this brand)
- `guapalab.it` (Italian natural cosmetics)
- `guapaskincare.com` (skincare brand)
- `guaapa.com` (Spanish beauty retailer)
- `gguapa.com` (Colombian makeup)
- `guapa.cosmetics` (Instagram account)
- The Spanish word "guapa" (meaning "beautiful/handsome")

Without strong entity signals, AI engines will conflate or ignore guapa-shop.com in generative answers.

**Actions Required:**
- **Create a Wikipedia/Wikidata entry** for the brand (if notable enough — build up press first).
- **Add a structured "About" page** with clear entity signals: founding year, country, founders, mission, brand differentiators.
- **Use `sameAs` in Organization schema** pointing to all official social profiles (Instagram, Trustpilot, Facebook, LinkedIn if applicable).
- **Secure and optimize Google Business Profile** (even for a purely online brand).
- **Register on open knowledge graphs:** Wikidata, Crunchbase, LinkedIn company page.

---

### 4.2 Brand Story & Factual Content — 🔴 Critical

**Finding:** AI models learn about brands from factual, structured, widely-cited content. guapa-shop.com currently has very little of this.

**Content assets needed for GEO:**
1. **About page with founder story** (who created Guapa, when, why, based where in France).
2. **Clear value proposition page:** Why vegan? Why Grasse perfumers? What makes Guapa different from Nécessaire, Typology, or Aroma-Zone?
3. **Ingredient transparency page** listing key ingredients per collection with sourcing details.
4. **Press page** aggregating all media mentions.

---

### 4.3 AI Overview Eligibility — 🟠 Serious

For Google's AI Overviews to cite guapa-shop.com, the site needs:
- Authoritative, factual content (E-E-A-T signals: Experience, Expertise, Authoritativeness, Trustworthiness).
- Schema markup (especially `Organization`, `Product`, `FAQPage`).
- Backlinks from authoritative domains in the beauty space.
- Mentions in knowledge bases AI models are trained on.

**Current status:** The brand is virtually invisible to AI engines. No AI-generated beauty round-ups or gift guides are likely citing Guapa.

---

### 4.4 Multilingual & International Signals — 🟠 Serious

**Finding:** Google-indexed titles appear in English ("Guapa | Vegan beauty brand...") while product descriptions use French. This inconsistency confuses both users and AI models about the brand's target market.

**Actions Required:**
- Decide on primary language strategy: French-first with English subpages, or bilingual.
- Implement `hreflang` tags if serving both French and English audiences.
- Ensure `<html lang="fr">` (or `lang="fr-FR"`) is set correctly in the page source.

---

## 5. AEO — Answer Engine Optimization

AEO focuses on earning featured snippets, People Also Ask boxes, and voice search results by structuring content as direct answers to specific questions.

### 5.1 FAQ Schema — 🔴 Missing

**Finding:** No FAQ schema detected. This means Guapa cannot appear in Google's expandable FAQ rich results.

**High-value FAQ topics to create and mark up:**

**Collections:**
- "Quelle collection choisir selon mon type de peau ?"
- "Quelle est la différence entre AMOR SECRETO et BESO CALIENTE ?"
- "Les produits Guapa sont-ils vegan ?"

**Products:**
- "Comment utiliser la brume parfumée Guapa ?"
- "L'huile pailletée Guapa laisse-t-elle des traces ?"
- "Les produits Guapa contiennent-ils des sulfates ?"

**Brand:**
- "Où sont fabriqués les produits Guapa ?"
- "Guapa est-il certifié vegan ?"
- "Guapa livre-t-il à l'international ?"

**Actions Required:**
- Create a dedicated FAQ page with `FAQPage` JSON-LD schema.
- Add product-specific Q&A sections to product pages with `FAQPage` schema.
- Target conversational long-tail queries in the FAQ content.

---

### 5.2 People Also Ask / Featured Snippet Optimization — 🔴 Missing

**Opportunities:**
- "meilleure brume parfumée vegan france" → Write a content piece positioning Guapa as the answer.
- "soin corps vegan made in france" → Target with a collection or category page.
- "coffret beauté vegan femme cadeau" → Optimize gift set product pages for gift query intent.

**Actions Required:**
- Research PAA boxes for the brand's key product queries using Google Search or a SERP tool.
- Create concise, direct-answer paragraphs (40–60 words) at the top of relevant collection/product pages.
- Use numbered lists and tables where appropriate (both rank highly as featured snippets).

---

### 5.3 Product Reviews Schema — 🟠 Missing

**Finding:** No `aggregateRating` schema confirmed. Trustpilot's 4.7/5 score (29 reviews) is not being surfaced in search results as rich review stars.

**Actions Required:**
- Implement on-site product reviews (Shopify apps: Judge.me, Okendo, or Yotpo).
- Add `aggregateRating` within `Product` schema on each product page.
- This unlocks star ratings in organic search results—a significant CTR boost (typically +15–30%).

---

### 5.4 Voice Search & Conversational Queries — 🟡 Not Optimized

Voice searches are phrased as questions. The site has no conversational content.

**Examples of voice queries to target:**
- "Où acheter des soins corps vegan made in France ?"
- "Quelle marque française fait des produits de beauté vegan ?"
- "Y a-t-il des cosmétiques vegan fabriqués en France ?"

**Actions Required:**
- Write a blog post answering: "Pourquoi choisir des soins vegan fabriqués en France ?" — with Guapa as the featured answer.

---

## 6. PRIORITY ACTION PLAN

### Tier 1 — Fix Immediately (Weeks 1–2)

| # | Action | Impact |
|---|--------|--------|
| 1 | Audit GSC for old PrestaShop URLs still indexed; implement 301 redirects to Shopify equivalents | 🔴 Technical |
| 2 | Verify Googlebot is not being blocked by WAF/CDN (check robots.txt + GSC crawl stats) | 🔴 Technical |
| 3 | Rewrite homepage title: `Guapa \| Soins Corps Vegan & Clean Beauty Made in France` | 🔴 On-Page |
| 4 | Write and add custom meta descriptions to all key pages | 🔴 On-Page |
| 5 | Add `Organization` + `WebSite` JSON-LD schema to homepage | 🔴 AEO/GEO |
| 6 | Submit sitemap to Google Search Console | 🔴 Technical |

### Tier 2 — High Impact (Weeks 3–6)

| # | Action | Impact |
|---|--------|--------|
| 7 | Add `Product` schema with `offers` + `aggregateRating` to all product pages | 🟠 AEO |
| 8 | Install on-site review app (Judge.me or Okendo) to collect + display product reviews | 🟠 AEO |
| 9 | Create FAQ page + `FAQPage` schema with 10–15 key questions | 🟠 AEO |
| 10 | Rewrite all product page titles and meta descriptions | 🟠 On-Page |
| 11 | Add `alt` text to all product images | 🟠 On-Page |
| 12 | Run PageSpeed Insights; fix LCP on homepage (target < 2.0s) | 🟠 Technical |

### Tier 3 — Strategic Growth (Months 2–4)

| # | Action | Impact |
|---|--------|--------|
| 13 | Launch brand blog: 2 posts/month on vegan beauty, rituals, ingredients | 🟡 Content/GEO |
| 14 | PR outreach to 10 French beauty publications for brand features + backlinks | 🟡 Off-Page/GEO |
| 15 | Create Wikidata entity for Guapa brand | 🟡 GEO |
| 16 | Build out a comprehensive About/Brand Story page | 🟡 GEO/E-E-A-T |
| 17 | Implement hreflang if targeting non-French markets | 🟡 International |
| 18 | Seed micro-influencers (clean beauty, vegan lifestyle niches) | 🟡 Off-Page |
| 19 | Add Trustpilot badge/widget to homepage and product pages | 🟡 Trust |
| 20 | Create "Complete the Ritual" internal cross-linking within each collection | 🟡 On-Page |

---

## 7. COMPETITIVE GAPS

Key competitors in the French vegan body care space include: **Nécessaire**, **Typology**, **Aroma-Zone**, **Merme Berlin**, **Nuxe** (semi-natural). These brands have:
- Hundreds of indexed pages vs. Guapa's ~4.
- Rich editorial blogs driving organic traffic.
- Strong backlink profiles from press features.
- Product schema with review stars in SERPs.

Guapa's defensible advantages that should be amplified in SEO content:
1. Grasse perfumers collaboration — a unique luxury signal.
2. All three pillars: clean + vegan + made in France (rare combination).
3. Sensory/ritual brand narrative — emotionally resonant and differentiated.

---

## 8. METRICS TO TRACK

Set up tracking for the following KPIs after implementing changes:

| Metric | Tool | Target |
|--------|------|--------|
| Google indexed pages | Google Search Console | 50+ pages within 90 days |
| Organic impressions | GSC | 10x increase in 90 days |
| Core Web Vitals (LCP) | PageSpeed Insights / GSC | < 2.0s |
| Rich result eligibility | Google Rich Results Test | Product + FAQ results |
| Trustpilot review count | Trustpilot | 100+ reviews within 6 months |
| Backlink count | Ahrefs / Semrush | 20+ referring domains within 6 months |

---

*Audit conducted via public web research. Direct page-source analysis was not possible due to the site returning HTTP 403 for all programmatic fetches. Findings are based on Google Search index data, search result snippets, Trustpilot data, and cross-referenced SEO best practices. A manual inspection of page source, GSC data, and sitemap by the site owner is strongly recommended to validate and extend these findings.*
