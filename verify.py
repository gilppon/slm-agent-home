import os
import subprocess
import sys

def check_git_exists():
    if not os.path.exists(".git"):
        print("[ERROR] Error: .git directory not found.")
        sys.exit(1)
    print("[SUCCESS] Success: .git directory exists.")

def check_branch_name():
    try:
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
        if branch != "main":
            print(f"[ERROR] Error: Current branch is '{branch}', expected 'main'.")
            sys.exit(1)
        print("[SUCCESS] Success: Current branch is 'main'.")
    except Exception as e:
        print(f"[ERROR] Error while checking branch: {e}")
        sys.exit(1)

def check_remote_url():
    try:
        remote_url = subprocess.check_output(["git", "remote", "get-url", "origin"]).decode().strip()
        expected = "https://github.com/gilppon/slm-agent-home"
        if remote_url != expected:
            print(f"[ERROR] Error: Remote URL is '{remote_url}', expected '{expected}'.")
            sys.exit(1)
        print(f"[SUCCESS] Success: Remote URL matches '{expected}'.")
    except Exception as e:
        print(f"[ERROR] Error while checking remote URL: {e}")
        sys.exit(1)

def check_gitignore():
    try:
        result = subprocess.run(["git", "check-ignore", "relocation_report.txt"], capture_output=True)
        if result.returncode == 0:
            print("[SUCCESS] Success: 'relocation_report.txt' is correctly ignored by git.")
        else:
            print("[ERROR] Error: 'relocation_report.txt' is NOT ignored by git.")
            sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Error checking gitignore: {e}")
        sys.exit(1)

def check_sitemap():
    sitemap_path = "sitemap.xml"
    if not os.path.exists(sitemap_path):
        print(f"[ERROR] Error: '{sitemap_path}' not found.")
        sys.exit(1)
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()
    expected_domain = "https://rag.next-haru.com/"
    loc_count = content.count("<loc>")
    if expected_domain not in content:
        print(f"[ERROR] Error: '{expected_domain}' not found in '{sitemap_path}'.")
        sys.exit(1)
    if loc_count < 10:
        print(f"[ERROR] Error: Expected at least 10 URLs in sitemap, found {loc_count}.")
        sys.exit(1)
    print(f"[SUCCESS] Success: '{sitemap_path}' verified with {loc_count} valid URLs.")

def check_robots():
    robots_path = "robots.txt"
    if not os.path.exists(robots_path):
        print(f"[ERROR] Error: '{robots_path}' not found.")
        sys.exit(1)
    with open(robots_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "Sitemap: https://rag.next-haru.com/sitemap.xml" not in content:
        print(f"[ERROR] Error: Sitemap directive missing in '{robots_path}'.")
        sys.exit(1)
    if "User-agent: GPTBot" not in content:
        print(f"[ERROR] Error: GPTBot directive missing in '{robots_path}'.")
        sys.exit(1)
    print(f"[SUCCESS] Success: '{robots_path}' verified (AI Crawlers & Sitemap directive active).")

def check_og_image():
    og_path = "og-image.png"
    if not os.path.exists(og_path):
        print(f"[ERROR] Error: '{og_path}' not found.")
        sys.exit(1)
    size = os.path.getsize(og_path)
    if size < 1024:
        print(f"[ERROR] Error: '{og_path}' size too small ({size} bytes).")
        sys.exit(1)
    print(f"[SUCCESS] Success: '{og_path}' exists and verified (Size: {size:,} bytes).")

def check_seo_in_index():
    index_path = "index.html"
    if not os.path.exists(index_path):
        print(f"[ERROR] Error: '{index_path}' not found.")
        sys.exit(1)
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    required_keywords = [
        '<link rel="canonical" href="https://rag.next-haru.com/">',
        '<meta property="og:image" content="https://rag.next-haru.com/og-image.png">',
        'application/ld+json',
        'SoftwareApplication',
        'FAQPage'
    ]
    for kw in required_keywords:
        if kw not in content:
            print(f"[ERROR] Error: Required SEO/GEO tag missing in '{index_path}': '{kw}'")
            sys.exit(1)
    print(f"[SUCCESS] Success: '{index_path}' contains all required Canonical, OG, and 2026 GEO Schema.org tags.")

if __name__ == "__main__":
    print("[START] Running Global PMO Harness Gate verification...")
    check_git_exists()
    check_branch_name()
    check_remote_url()
    check_gitignore()
    check_sitemap()
    check_robots()
    check_og_image()
    check_seo_in_index()
    print("[OK] All local & SEO/GEO verification gates PASSED successfully!")
