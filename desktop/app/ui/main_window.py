from __future__ import annotations

import asyncio
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Qt
from PySide6.QtWidgets import (
    QDialog, QDialogButtonBox, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMessageBox,
    QPushButton, QStackedWidget, QTextEdit, QVBoxLayout, QWidget,
)

from app.core.group_engine import GroupEngine
from app.providers.gemini_provider import GeminiProvider
from app.security.secret_store import is_configured


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
            turns = asyncio.run(GroupEngine([GeminiProvider()], max_rounds=2).discuss(self.prompt))
            rendered = "\n\n".join(f"### Gemini · {turn.provider}\n{turn.text}" for turn in turns)
            self.signals.finished.emit(rendered)
        except Exception:
            self.signals.failed.emit("The request could not be completed. Check the provider setup and try again.")


class MainWindow(QMainWindow):
    """Apple-inspired, dark glass-style AI Workplace desktop shell."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("AI Workplace")
        self.resize(1380, 880)
        self.setMinimumSize(980, 680)
        self.thread_pool = QThreadPool.globalInstance()
        self._build_ui()
        self._apply_theme()

    def _label(self, text: str, name: str = "") -> QLabel:
        label = QLabel(text)
        if name:
            label.setObjectName(name)
        return label

    def _card(self, layout: QVBoxLayout, title: str, detail: str = "") -> QFrame:
        card = QFrame()
        card.setObjectName("card")
        inner = QVBoxLayout(card)
        inner.setContentsMargins(20, 18, 20, 18)
        inner.setSpacing(8)
        inner.addWidget(self._label(title, "cardTitle"))
        if detail:
            inner.addWidget(self._label(detail, "muted"))
        layout.addWidget(card)
        return card

    def _build_ui(self) -> None:
        shell = QWidget()
        shell.setObjectName("shell")
        outer = QHBoxLayout(shell)
        outer.setContentsMargins(14, 14, 14, 14)
        outer.setSpacing(14)

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(226)
        side = QVBoxLayout(sidebar)
        side.setContentsMargins(16, 18, 16, 16)
        side.setSpacing(10)

        brand = QHBoxLayout()
        mark = self._label("✦", "brandMark")
        mark.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mark.setFixedSize(38, 38)
        brand.addWidget(mark)
        brand_text = QVBoxLayout()
        brand_text.setSpacing(1)
        brand_text.addWidget(self._label("AI Workplace", "brandTitle"))
        brand_text.addWidget(self._label("YOUR AI COMMAND CENTER", "eyebrow"))
        brand.addLayout(brand_text)
        brand.addStretch()
        side.addLayout(brand)
        side.addSpacing(22)
        side.addWidget(self._label("WORKSPACE", "eyebrow"))

        self.nav_buttons: list[QPushButton] = []
        for text, index in [("⌂   Overview", 0), ("◉   Group Room", 1), ("✧   Gemini", 2)]:
            button = QPushButton(text)
            button.setObjectName("navActive" if index == 0 else "navButton")
            button.setCheckable(True)
            button.clicked.connect(lambda checked=False, i=index: self._show_page(i))
            self.nav_buttons.append(button)
            side.addWidget(button)
        self.nav_buttons[0].setChecked(True)
        side.addStretch()

        side.addWidget(self._label("CONNECTION", "eyebrow"))
        self.connection_card = QFrame()
        self.connection_card.setObjectName("miniCard")
        connection_layout = QVBoxLayout(self.connection_card)
        connection_layout.setContentsMargins(12, 12, 12, 12)
        connection_layout.setSpacing(7)
        status_text = "Connected" if is_configured("Gemini") else "Not connected"
        self.sidebar_status = self._label("●  Gemini  ·  " + status_text, "connectionStatus")
        connection_layout.addWidget(self.sidebar_status)
        connection_layout.addWidget(self._label("Free-tier provider", "mutedSmall"))
        side.addWidget(self.connection_card)

        self.settings_button = QPushButton("⚙   API Security")
        self.settings_button.setObjectName("settingsButton")
        self.settings_button.clicked.connect(self._open_api_security)
        side.addWidget(self.settings_button)
        outer.addWidget(side)

        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(10, 8, 8, 8)
        content_layout.setSpacing(18)

        top = QHBoxLayout()
        top_text = QVBoxLayout()
        top_text.setSpacing(3)
        self.page_title = self._label("Overview", "pageTitle")
        self.page_subtitle = self._label("A calm space to think, build, and collaborate.", "muted")
        top_text.addWidget(self.page_title)
        top_text.addWidget(self.page_subtitle)
        top.addLayout(top_text)
        top.addStretch()
        self.status = self._label("●  " + status_text, "statusPill")
        top.addWidget(self.status)
        content_layout.addLayout(top)

        self.pages = QStackedWidget()
        self.pages.addWidget(self._overview_page())
        self.pages.addWidget(self._group_page())
        self.pages.addWidget(self._gemini_page())
        content_layout.addWidget(self.pages, 1)
        outer.addWidget(content, 1)
        self.setCentralWidget(shell)

    def _overview_page(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        hero = QFrame()
        hero.setObjectName("hero")
        hero_layout = QVBoxLayout(hero)
        hero_layout.setContentsMargins(26, 25, 26, 25)
        hero_layout.setSpacing(10)
        hero_layout.addWidget(self._label("YOUR WORKSPACE, AT A GLANCE", "eyebrow"))
        hero_layout.addWidget(self._label("Good ideas deserve\na beautiful place to grow.", "heroTitle"))
        hero_layout.addWidget(self._label(
            "Bring your projects and approved AI assistants into one focused workspace.",
            "heroBody"
        ))
        action_row = QHBoxLayout()
        start = QPushButton("Open Group Room  →")
        start.setObjectName("primaryButton")
        start.clicked.connect(lambda: self._show_page(1))
        action_row.addWidget(start)
        action_row.addStretch()
        hero_layout.addLayout(action_row)
        layout.addWidget(hero)

        stats = QHBoxLayout()
        stats.setSpacing(12)
        for title, value, caption in [
            ("AI PROVIDERS", "01", "Gemini connected"),
            ("WORK MODE", "Cloud", "Inference stays hosted"),
            ("BILLING POLICY", "Free-first", "No paid fallback"),
        ]:
            card = QFrame()
            card.setObjectName("card")
            c = QVBoxLayout(card)
            c.setContentsMargins(18, 16, 18, 16)
            c.setSpacing(6)
            c.addWidget(self._label(title, "eyebrow"))
            c.addWidget(self._label(value, "statValue"))
            c.addWidget(self._label(caption, "mutedSmall"))
            stats.addWidget(card, 1)
        layout.addLayout(stats)

        section = self._label("Your workspace", "sectionTitle")
        layout.addWidget(section)
        grid = QHBoxLayout()
        grid.setSpacing(12)
        for symbol, title, desc in [
            ("✧", "Group Room", "Discuss ideas with connected AI providers."),
            ("◈", "Shared Memory", "Keep approved project context organized."),
            ("⌘", "Secure settings", "Store provider keys in your OS vault."),
        ]:
            card = QFrame()
            card.setObjectName("card")
            c = QVBoxLayout(card)
            c.setContentsMargins(18, 17, 18, 17)
            c.addWidget(self._label(symbol, "tileIcon"))
            c.addWidget(self._label(title, "cardTitle"))
            c.addWidget(self._label(desc, "muted"))
            grid.addWidget(card, 1)
        layout.addLayout(grid)
        layout.addStretch()
        layout.addWidget(self._label(
            "Early preview · Gemini is the only provider currently wired into the group prototype.",
            "mutedSmall"
        ))
        return page

    def _group_page(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)

        intro = QFrame()
        intro.setObjectName("card")
        intro_layout = QVBoxLayout(intro)
        intro_layout.setContentsMargins(18, 15, 18, 15)
        intro_layout.addWidget(self._label("Group Room", "sectionTitle"))
        intro_layout.addWidget(self._label(
            "A shared space for independent answers and a bounded review round.",
            "muted"
        ))
        layout.addWidget(intro)

        self.group_output = QTextEdit()
        self.group_output.setObjectName("conversation")
        self.group_output.setReadOnly(True)
        self.group_output.setPlaceholderText(
            "Your conversation will appear here. Start with a question, an idea, or a task…"
        )
        layout.addWidget(self.group_output, 1)

        composer = QFrame()
        composer.setObjectName("composer")
        composer_layout = QHBoxLayout(composer)
        composer_layout.setContentsMargins(12, 10, 12, 10)
        self.prompt = QLineEdit()
        self.prompt.setObjectName("promptInput")
        self.prompt.setPlaceholderText("Message your AI group…")
        self.send_button = QPushButton("Send  ↑")
        self.send_button.setObjectName("primaryButton")
        self.send_button.clicked.connect(self._send_group_message)
        self.prompt.returnPressed.connect(self._send_group_message)
        composer_layout.addWidget(self.prompt, 1)
        composer_layout.addWidget(self.send_button)
        layout.addWidget(composer)
        return page

    def _gemini_page(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        card = QFrame()
        card.setObjectName("card")
        inner = QVBoxLayout(card)
        inner.setContentsMargins(22, 22, 22, 22)
        inner.addWidget(self._label("Gemini", "sectionTitle"))
        inner.addWidget(self._label("Provider status and connection settings", "muted"))
        inner.addSpacing(10)
        state = "Connected to the local credential vault" if is_configured("Gemini") else "API key not configured"
        inner.addWidget(self._label("●  " + state, "connectionStatus"))
        inner.addWidget(self._label(
            "Individual provider chat is planned for a later milestone. The current working flow is Group Room.",
            "muted"
        ))
        button = QPushButton("Manage API Security")
        button.setObjectName("secondaryButton")
        button.clicked.connect(self._open_api_security)
        inner.addWidget(button, 0, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(card)
        layout.addStretch()
        return page

    def _show_page(self, index: int) -> None:
        self.pages.setCurrentIndex(index)
        titles = [
            ("Overview", "A calm space to think, build, and collaborate."),
            ("Group Room", "One conversation, independent AI perspectives."),
            ("Gemini", "Manage your currently connected provider."),
        ]
        self.page_title.setText(titles[index][0])
        self.page_subtitle.setText(titles[index][1])
        for i, button in enumerate(self.nav_buttons):
            button.setObjectName("navActive" if i == index else "navButton")
            button.setChecked(i == index)
            button.style().unpolish(button)
            button.style().polish(button)

    def _open_api_security(self) -> None:
        from app.security.secret_store import save_api_key, delete_api_key
        dialog = QDialog(self)
        dialog.setWindowTitle("API Security — Local Vault")
        dialog.setMinimumWidth(420)
        form = QFormLayout(dialog)
        form.setContentsMargins(22, 22, 22, 18)
        form.setSpacing(12)
        provider = QComboBox()
        provider.addItems(["Gemini"])
        secret = QLineEdit()
        secret.setEchoMode(QLineEdit.EchoMode.Password)
        secret.setPlaceholderText("API key (hidden)")
        state = QLabel("Configured" if is_configured("Gemini") else "Not configured")
        form.addRow("Provider", provider)
        form.addRow("API key", secret)
        form.addRow("Local vault", state)
        buttons = QDialogButtonBox()
        save_btn = buttons.addButton("Save securely", QDialogButtonBox.ButtonRole.AcceptRole)
        delete_btn = buttons.addButton("Delete key", QDialogButtonBox.ButtonRole.DestructiveRole)
        buttons.addButton(QDialogButtonBox.StandardButton.Close)
        form.addRow(buttons)

        def save() -> None:
            try:
                save_api_key(provider.currentText(), secret.text())
                secret.clear()
                state.setText("Configured")
                QMessageBox.information(
                    dialog, "Saved",
                    "Stored in the OS credential vault. The key is not sent to GitHub."
                )
            except Exception:
                secret.clear()
                QMessageBox.critical(
                    dialog, "Secure vault unavailable",
                    "Could not save. Configure the OS credential manager. Plaintext fallback is disabled."
                )

        def remove() -> None:
            if QMessageBox.question(
                dialog, "Delete key", "Delete this key from the local vault?"
            ) == QMessageBox.StandardButton.Yes:
                try:
                    delete_api_key(provider.currentText())
                    secret.clear()
                    state.setText("Not configured")
                except Exception:
                    QMessageBox.critical(
                        dialog, "Delete failed",
                        "The OS credential vault could not delete this key."
                    )

        save_btn.clicked.connect(save)
        delete_btn.clicked.connect(remove)
        buttons.rejected.connect(dialog.reject)
        dialog.exec()
        self._refresh_status()

    def _refresh_status(self) -> None:
        configured = is_configured("Gemini")
        state = "Connected" if configured else "Not connected"
        self.status.setText("●  " + state)
        self.sidebar_status.setText("●  Gemini  ·  " + state)

    def _send_group_message(self) -> None:
        prompt = self.prompt.text().strip()
        if not prompt:
            return
        if not is_configured("Gemini"):
            QMessageBox.information(
                self, "Gemini API key required",
                "Add your key through API Security. It will be stored in your operating system credential vault."
            )
            return
        self.prompt.clear()
        self.send_button.setEnabled(False)
        self.group_output.append(f"\n<h3>You</h3><p>{prompt}</p><p><i>Gemini is responding…</i></p>")
        worker = DiscussionWorker(prompt)
        worker.signals.finished.connect(self._on_discussion_finished)
        worker.signals.failed.connect(self._on_discussion_failed)
        self.thread_pool.start(worker)

    def _on_discussion_finished(self, result: str) -> None:
        self.group_output.append(result)
        self.send_button.setEnabled(True)

    def _on_discussion_failed(self, error: str) -> None:
        self.group_output.append("\n<p><b>Request failed.</b> " + error + "</p>")
        self.send_button.setEnabled(True)

    def _apply_theme(self) -> None:
        self.setStyleSheet("""
            QMainWindow, QWidget#shell { background: #111216; color: #F5F5F7; }
            QWidget { color: #F5F5F7; font-family: 'SF Pro Display', 'Inter', 'Segoe UI'; font-size: 13px; }
            QFrame#sidebar { background: #1B1C21; border: 1px solid #2C2D33; border-radius: 20px; }
            QLabel#brandMark { color: #FFFFFF; background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 #8D9CFF, stop:1 #B58BFF); border-radius: 12px; font-size: 22px; font-weight: 700; }
            QLabel#brandTitle { font-size: 15px; font-weight: 700; }
            QLabel#eyebrow { color: #858791; font-size: 10px; font-weight: 700; letter-spacing: 1px; }
            QPushButton#navButton, QPushButton#navActive { text-align: left; border: 0; border-radius: 10px; padding: 11px 12px; color: #A5A6AF; background: transparent; font-weight: 600; }
            QPushButton#navButton:hover { background: #27282F; color: #F5F5F7; }
            QPushButton#navActive { background: #30313A; color: #FFFFFF; }
            QFrame#miniCard { background: #24252B; border: 1px solid #34353D; border-radius: 12px; }
            QLabel#connectionStatus { color: #A9D7B5; font-weight: 600; }
            QLabel#mutedSmall { color: #858791; font-size: 11px; }
            QPushButton#settingsButton { text-align: left; background: #292A31; color: #D9DAE0; border: 1px solid #393A43; border-radius: 10px; padding: 10px 12px; }
            QLabel#pageTitle { font-size: 27px; font-weight: 700; letter-spacing: -0.6px; }
            QLabel#muted, QLabel#pageSubtitle { color: #A0A1AA; }
            QLabel#statusPill { background: #202B24; color: #A9D7B5; border: 1px solid #304438; border-radius: 13px; padding: 7px 11px; font-size: 11px; font-weight: 600; }
            QFrame#hero { background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 #292B38, stop:0.55 #252632, stop:1 #30283A); border: 1px solid #41404F; border-radius: 20px; }
            QLabel#heroTitle { color: #FFFFFF; font-size: 31px; font-weight: 700; letter-spacing: -0.8px; }
            QLabel#heroBody { color: #B8B9C3; font-size: 14px; }
            QFrame#card { background: #1B1C21; border: 1px solid #303138; border-radius: 16px; }
            QLabel#cardTitle, QLabel#sectionTitle { color: #F5F5F7; font-size: 16px; font-weight: 650; }
            QLabel#statValue { color: #FFFFFF; font-size: 23px; font-weight: 700; }
            QLabel#tileIcon { color: #B8A6FF; font-size: 23px; }
            QPushButton#primaryButton { background: #F5F5F7; color: #17181C; border: 0; border-radius: 10px; padding: 11px 16px; font-weight: 700; }
            QPushButton#primaryButton:hover { background: #DCDDE2; }
            QPushButton#secondaryButton { background: #30313A; color: #F5F5F7; border: 1px solid #45464F; border-radius: 9px; padding: 10px 14px; }
            QTextEdit#conversation { background: #17181D; border: 1px solid #303138; border-radius: 16px; padding: 15px; selection-background-color: #6E72A8; }
            QFrame#composer { background: #202127; border: 1px solid #3A3B44; border-radius: 15px; }
            QLineEdit#promptInput { background: transparent; border: 0; color: #F5F5F7; padding: 9px; font-size: 14px; }
            QPushButton:disabled { background: #45464D; color: #8B8C94; }
            QDialog { background: #1B1C21; }
            QLineEdit, QComboBox { background: #25262D; border: 1px solid #41424B; border-radius: 8px; padding: 9px; color: #F5F5F7; }
        """)
