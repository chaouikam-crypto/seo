#!/usr/bin/env python3
import markdown
import weasyprint
import sys

md_path = "/home/user/seo/guapa-shop-audit.md"
pdf_path = "/home/user/seo/guapa-shop-audit.pdf"

with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

html_body = markdown.markdown(
    md_content,
    extensions=["tables", "fenced_code", "toc"]
)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>SEO / GEO / AEO Full Audit — guapa-shop.com</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.65;
    color: #1a1a2e;
    background: #ffffff;
    padding: 0;
  }}

  /* Cover page */
  .cover {{
    page-break-after: always;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    color: white;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: 80px 60px;
  }}
  .cover-tag {{
    background: #e94560;
    color: white;
    font-size: 9pt;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 6px 16px;
    border-radius: 3px;
    margin-bottom: 32px;
    display: inline-block;
  }}
  .cover h1 {{
    font-size: 36pt;
    font-weight: 700;
    line-height: 1.15;
    color: white;
    margin-bottom: 16px;
    border: none;
    padding: 0;
  }}
  .cover-subtitle {{
    font-size: 16pt;
    color: #a8b2d8;
    margin-bottom: 48px;
    font-weight: 400;
  }}
  .cover-meta {{
    display: flex;
    flex-direction: column;
    gap: 10px;
    font-size: 11pt;
    color: #ccd6f6;
    border-top: 1px solid rgba(255,255,255,0.15);
    padding-top: 32px;
    margin-top: 32px;
    width: 100%;
  }}
  .cover-meta span {{ color: #e94560; font-weight: 600; }}

  /* Page layout */
  @page {{
    size: A4;
    margin: 20mm 18mm 22mm 18mm;
    @bottom-center {{
      content: counter(page);
      font-family: 'Inter', Arial, sans-serif;
      font-size: 9pt;
      color: #999;
    }}
  }}
  @page:first {{ margin: 0; @bottom-center {{ content: none; }} }}

  .content {{
    padding: 0;
  }}

  /* Typography */
  h1 {{
    font-size: 22pt;
    font-weight: 700;
    color: #0f3460;
    border-bottom: 3px solid #e94560;
    padding-bottom: 10px;
    margin: 40px 0 20px;
    page-break-after: avoid;
    line-height: 1.2;
  }}
  h2 {{
    font-size: 15pt;
    font-weight: 700;
    color: #16213e;
    margin: 32px 0 12px;
    padding-left: 12px;
    border-left: 4px solid #e94560;
    page-break-after: avoid;
  }}
  h3 {{
    font-size: 12pt;
    font-weight: 700;
    color: #0f3460;
    margin: 24px 0 10px;
    page-break-after: avoid;
  }}
  h4 {{
    font-size: 11pt;
    font-weight: 600;
    color: #555;
    margin: 16px 0 8px;
    page-break-after: avoid;
  }}

  p {{
    margin: 0 0 12px;
  }}

  /* Executive summary box */
  .exec-summary {{
    background: #f0f4ff;
    border-left: 5px solid #0f3460;
    border-radius: 0 8px 8px 0;
    padding: 20px 24px;
    margin: 16px 0 24px;
  }}

  /* Tables */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0 24px;
    font-size: 10pt;
    page-break-inside: avoid;
  }}
  th {{
    background: #0f3460;
    color: white;
    font-weight: 700;
    padding: 10px 14px;
    text-align: left;
    font-size: 10pt;
  }}
  td {{
    padding: 9px 14px;
    border-bottom: 1px solid #e8ecf5;
    vertical-align: top;
  }}
  tr:nth-child(even) td {{
    background: #f8f9ff;
  }}
  tr:hover td {{
    background: #eef1fb;
  }}

  /* Code blocks */
  code {{
    background: #f4f4f8;
    border: 1px solid #e0e0e8;
    border-radius: 4px;
    padding: 2px 6px;
    font-family: 'Courier New', monospace;
    font-size: 9.5pt;
    color: #c62828;
  }}
  pre {{
    background: #1a1a2e;
    color: #a8b2d8;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 16px 0;
    overflow-x: auto;
    page-break-inside: avoid;
  }}
  pre code {{
    background: none;
    border: none;
    padding: 0;
    color: #ccd6f6;
    font-size: 9.5pt;
  }}

  /* Lists */
  ul, ol {{
    padding-left: 24px;
    margin: 8px 0 16px;
  }}
  li {{
    margin-bottom: 5px;
  }}
  li > ul, li > ol {{
    margin: 4px 0;
  }}

  /* Blockquotes (used for callouts) */
  blockquote {{
    background: #fff8e1;
    border-left: 4px solid #f5a623;
    padding: 14px 18px;
    margin: 16px 0;
    border-radius: 0 6px 6px 0;
    font-style: normal;
  }}

  /* Horizontal rule */
  hr {{
    border: none;
    border-top: 2px solid #e8ecf5;
    margin: 32px 0;
  }}

  /* Score badges inline */
  strong {{
    color: #0f3460;
    font-weight: 700;
  }}
  em {{
    color: #555;
  }}

  /* Priority callout sections */
  .priority-critical {{
    background: #fff0f0;
    border: 1px solid #ffcdd2;
    border-radius: 8px;
    padding: 12px 16px;
    margin: 8px 0;
  }}
  .priority-warning {{
    background: #fff8e1;
    border: 1px solid #ffe082;
    border-radius: 8px;
    padding: 12px 16px;
    margin: 8px 0;
  }}

  /* Page break utilities */
  .page-break {{ page-break-before: always; }}

  /* Footer note */
  .audit-note {{
    font-size: 8.5pt;
    color: #888;
    font-style: italic;
    margin-top: 40px;
    padding-top: 16px;
    border-top: 1px solid #e8ecf5;
  }}
</style>
</head>
<body>

<!-- Cover Page -->
<div class="cover">
  <div class="cover-tag">Confidential Audit Report</div>
  <h1>SEO · GEO · AEO<br>Full Audit Report</h1>
  <div class="cover-subtitle">guapa-shop.com</div>
  <div class="cover-meta">
    <div><span>Date:</span> 11 May 2026</div>
    <div><span>Domain:</span> guapa-shop.com</div>
    <div><span>Brand:</span> Guapa — Clean Vegan Beauty, Made in France</div>
    <div><span>Scope:</span> Technical SEO · On-Page SEO · Off-Page SEO · GEO · AEO</div>
    <div><span>Auditor:</span> AI-assisted research audit (Claude / Anthropic)</div>
  </div>
</div>

<!-- Main Content -->
<div class="content">
{html_body}
</div>

</body>
</html>"""

print("Converting to PDF...")
doc = weasyprint.HTML(string=html).write_pdf(
    pdf_path,
    presentational_hints=True,
)
print(f"PDF saved to: {pdf_path}")
