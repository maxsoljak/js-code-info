import re
from playwright.sync_api import Page, expect
import pytest

from pathlib import Path

file_url = Path("index.html").resolve().as_uri()

@pytest.fixture
def index(page: Page):
    page.goto(f"{file_url}")

    page.get_by_label("Input Code").fill(open('test.js').read())
    
    return page

def test_escape(index):
    expect(index.locator("code")).to_have_text(re.compile(r"<h1>"))

def test_line_count(index):
    expect(index.locator("[name=line-count]")).to_have_text("10")

def test_blank_line_count(index):
    expect(index.locator("[name=blank-line-count]")).to_have_text("2")

def test_char_count(index):
    expect(index.locator("[name=char-count]")).to_have_text("114")
