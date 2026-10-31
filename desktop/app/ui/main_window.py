from __future__ import annotations

import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal
from PySide6.QtWidgets import (
    QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMessageBox,
    QPushButton, QTabWidget, QTextEdit, QVBoxLayout, QWidget,
)

from app.core.group_engine import GroupEngine
from app.providers.gemini_provider import GeminiProvider


load_dotenv(Path(__file__).resolve().parents[2] / ".env")


class WorkerSignals(QObject):
    finished = Signal(str)
    failed = Signal(str)


class DiscussionWorker(QRunnable):
    def __init__(self, prompt: str) -> None:
        super().__init__()
        self.prompt = prompt
        self.signals = WorkerSignals()

    def run(self) -> None:
        try:
            # Current working provider: Gemini free tier. Other free cloud adapters are planned.
            turns = asyncio.run(GroupEngine([GeminiProvider()], max_rounds=2).discuss(self.prompt))
            rendered = "\\n\\n".join(f"### Gemini · {turn.provider}\n{turn.text}" for turn in turns)
            self.signals.finished.emit(rendered)
        except Exception as exc:
            self.signals.failed.emit(str(exc))


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("AI Workplace")
        self.resize(1280, 820)
        self.thread_pool = QThreadPool.globalInstance()
        self._build_ui()
        self._apply_theme()

    def _build_ui(self) -> None:
        root = QWidget()
        layout = QVBoxLayout(root)

        header = QHBoxLayout()
        title = QLabel("AI WORKPLACE")
        title.setObjectName("title")
        subtitle = QLabel("Cloud inference · free-tier only")
        subtitle.setObjectName("muted")
        header.addWidget(title)
        header.addWidget(subtitle)
        header.addStretch()
        self.status = QLabel("Gemini: configured" if os.getenv("GEMINI_API_KEY") else "Gemini: API key not set")
        self.status.setObjectName("status")
        header.addWidget(self.status)
        layout.addLayout(header)

        self.tabs = QTabWidget()
        self.group_output = QTextEdit()
        self.group_output.setReadOnly(True)
        self.group_output.setPlaceholderText("Responses from hosted AI providers will appear here.")
        group_page = QWidget()
        group_layout = QVBoxLayout(group_page)
        group_layout.addWidget(QLabel("GROUP ROOM · cloud AI discussion"))
        group_layout.addWidget(self.group_output)
        composer = QHBoxLayout()
        self.prompt = QLineEdit()
        self.prompt.setPlaceholderText("Write a message for the AI group…")
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self._send_group_message)
        self.prompt.returnPressed.connect(self._send_group_message)
        composer.addWidget(self.prompt, 1)
        composer.addWidget(self.send_button)
        group_layout.addLayout(composer)
        self.tabs.addTab(group_page, "Group Room")

        gemini_panel = QTextEdit()
        gemini_panel.setReadOnly(True)
        gemini_panel.setPlaceholderText("Gemini individual chat panel is planned for the next milestone.")
        self.tabs.addTab(gemini_panel, "Gemini")

        layout.addWidget(self.tabs)
        note = QLabel(
            "Only Gemini is wired into this prototype. Groq GPT-OSS, Mistral Free, Cloudflare Workers AI, "
            "and OpenRouter :free are researched candidates, not yet active. ChatGPT remains a separate "
            "reviewer through the shared GitHub handoff; no paid OpenAI API is used."
        )
        note.setObjectName("muted")
        note.setWordWrap(True)
        layout.addWidget(note)
        self.setCentralWidget(root)

    def _send_group_message(self) -> None:
        prompt = self.prompt.text().strip()
        if not prompt:
            return
        if not os.getenv("GEMINI_API_KEY"):
            QMessageBox.information(
                self, "Gemini API key required",
                "Add GEMINI_API_KEY to desktop/.env. No paid provider or fallback is available."
            )
            return
        self.prompt.clear()
        self.send_button.setEnabled(False)
        self.group_output.append(f"\n## YOU\n{prompt}\n\n*Gemini is responding…*")
        worker = DiscussionWorker(prompt)
        worker.signals.finished.connect(self._on_discussion_finished)
        worker.signals.failed.connect(self._on_discussion_failed)
        self.thread_pool.start(worker)

    def _on_discussion_finished(self, result: str) -> None:
        self.group_output.append(result)
        self.send_button.setEnabled(True)

    def _on_discussion_failed(self, error: str) -> None:
        self.group_output.append(f"\n**Request failed:** {error}")
        self.send_button.setEnabled(True)

    def _apply_theme(self) -> None:
        self.setStyleSheet("""
            QMainWindow, QWidget { background: #0A0F1B; color: #F2F5FF; }
            QLabel#title { color: #F2F5FF; font-size: 22px; font-weight: 700; }
            QLabel#muted { color: #98A4C4; }
            QLabel#status { color: #8FB8FF; padding: 6px 10px; }
            QTabWidget::pane { border: 1px solid #263150; border-radius: 10px; }
            QTabBar::tab { background: #141B2E; color: #98A4C4; padding: 10px 18px; }
            QTabBar::tab:selected { background: #1A2338; color: #F2F5FF; }
            QTextEdit, QLineEdit { background: #0E1422; border: 1px solid #263150;
                border-radius: 8px; padding: 10px; color: #F2F5FF; }
            QPushButton { background: #5685FF; color: white; border: 0;
                border-radius: 8px; padding: 10px 16px; font-weight: 600; }
            QPushButton:disabled { background: #2B3550; color: #98A4C4; }
        """)
