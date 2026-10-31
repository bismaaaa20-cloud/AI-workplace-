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
            providers = [GeminiProvider()]
            turns = asyncio.run(GroupEngine(providers, max_rounds=2).discuss(self.prompt))
            rendered = "\n\n".join(f"### {turn.provider}\n{turn.text}" for turn in turns)
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
        subtitle = QLabel("Multi-agent desktop workspace")
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
        self.group_output.setPlaceholderText("Group discussion responses will appear here.")
        group_page = QWidget()
        group_layout = QVBoxLayout(group_page)
        group_layout.addWidget(QLabel("GROUP ROOM · moderated discussion"))
        group_layout.addWidget(self.group_output)
        composer = QHBoxLayout()
        self.prompt = QLineEdit()
        self.prompt.setPlaceholderText("Write a message for the AI group…")
        self.send_button = QPushButton("Send to group")
        self.send_button.clicked.connect(self._send_group_message)
        self.prompt.returnPressed.connect(self._send_group_message)
        composer.addWidget(self.prompt, 1)
        composer.addWidget(self.send_button)
        group_layout.addLayout(composer)
        self.tabs.addTab(group_page, "Group Room")

        for name in ("ChatGPT", "Gemini", "Claude"):
            panel = QTextEdit()
            panel.setReadOnly(True)
            panel.setPlaceholderText(
                f"{name} individual session will be available when its provider is configured."
            )
            self.tabs.addTab(panel, name)

        layout.addWidget(self.tabs)
        note = QLabel(
            "Prototype: Group Room currently connects Gemini only. OpenAI and Claude adapters are optional "
            "and paid-gated. Individual panels are UI placeholders in this milestone."
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
                "Add GEMINI_API_KEY to desktop/.env. The application does not use a paid fallback."
            )
            return
        self.prompt.clear()
        self.send_button.setEnabled(False)
        self.group_output.append(f"\n## YOU\n{prompt}\n\n*AI agents are responding…*")
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
